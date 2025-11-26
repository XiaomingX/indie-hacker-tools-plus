# main.py - Discord OpenAI 对话机器人
# 功能：通过 /chat 命令创建对话线程，在线程内与 OpenAI 模型交互，包含内容审核机制

# -------------------------- 必要依赖导入 --------------------------
import discord
from discord import app_commands, Message as DiscordMessage
from discord.ext import commands
import logging
import asyncio
from dataclasses import dataclass
from typing import Optional, List, Tuple, Dict, DefaultDict
from collections import defaultdict
from enum import Enum
from openai import AsyncOpenAI

# -------------------------- 配置变量（用户需根据自身情况修改） --------------------------
# Discord 机器人令牌（从 Discord 开发者平台获取）
DISCORD_BOT_TOKEN = "YOUR_DISCORD_BOT_TOKEN"
# OpenAI API 密钥（从 OpenAI 平台获取）
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

# 允许使用机器人的服务器 ID 列表（仅允许列表内服务器使用，空列表表示不限制）
ALLOWED_SERVER_IDS: List[int] = []
# 机器人名称（会显示在对话中）
BOT_NAME = "GPT-Bot"
# 机器人指令（告诉 OpenAI 机器人的角色和行为）
BOT_INSTRUCTIONS = """你是一个友好的 Discord 对话机器人，负责回答用户的问题，语气自然、简洁明了，帮助用户解决问题。"""

# 示例对话（用于引导 OpenAI 理解对话格式，可根据需要修改）
EXAMPLE_CONVOS: List[Dict[str, List[Dict[str, str]]]] = [
    {
        "messages": [
            {"user": "用户", "text": "你好！"},
            {"user": "GPT-Bot", "text": "你好呀！有什么我可以帮你的吗？"}
        ]
    },
    {
        "messages": [
            {"user": "用户", "text": "什么是 Python？"},
            {"user": "GPT-Bot", "text": "Python 是一种简洁、易读的编程语言，广泛用于数据分析、人工智能、Web 开发等领域。"}
        ]
    }
]

# 线程相关配置
ACTIVATE_THREAD_PREFIX = "💬 对话"  # 活跃对话线程的前缀
INACTIVATE_THREAD_PREFIX = "🔒 已关闭"  # 关闭对话线程的前缀
MAX_THREAD_MESSAGES = 20  # 每个线程的最大消息数（防止上下文过长）
SECONDS_DELAY_RECEIVING_MSG = 1  # 接收消息后的延迟（防止用户连续发送消息导致重复响应）

# 模型相关配置
AVAILABLE_MODELS = ["gpt-5-mini", "gpt-4o-mini"]  # 支持的 OpenAI 模型
DEFAULT_MODEL = "gpt-5-mini"  # 默认使用的模型
MAX_CHARS_PER_REPLY_MSG = 2000  # Discord 单条消息最大字符数（拆分长回复用）

# 内容审核配置（OpenAI Moderation API）
MODERATION_VALUES_FOR_BLOCKED = {  # 超过该分数则拦截消息
    "hate": 0.7,
    "hate/threatening": 0.5,
    "self-harm": 0.5,
    "sexual": 0.7,
    "sexual/minors": 0.5,
    "violence": 0.7,
    "violence/graphic": 0.5
}
MODERATION_VALUES_FOR_FLAGGED = {  # 超过该分数则标记消息（不拦截，仅提示）
    "hate": 0.4,
    "hate/threatening": 0.2,
    "self-harm": 0.2,
    "sexual": 0.4,
    "sexual/minors": 0.2,
    "violence": 0.4,
    "violence/graphic": 0.2
}

# 审核频道配置（key: 服务器ID，value: 审核频道ID，用于发送审核日志）
SERVER_TO_MODERATION_CHANNEL: Dict[int, int] = {
    # 示例：1234567890: 0987654321
}

# -------------------------- 日志配置 --------------------------
logging.basicConfig(
    format="[%(asctime)s] [%(filename)s:%(lineno)d] %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# -------------------------- OpenAI 客户端初始化 --------------------------
openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

# -------------------------- 数据类定义（存储对话和配置信息） --------------------------
@dataclass
class Message:
    """存储单条消息的结构"""
    user: str  # 发送者名称
    text: Optional[str] = None  # 消息内容（可选，防止空消息）

    def render(self) -> str:
        """将消息格式化为字符串（用于构建 Prompt）"""
        result = f"{self.user}:"
        if self.text:
            result += f" {self.text}"
        return result


@dataclass
class Conversation:
    """存储一组对话的结构"""
    messages: List[Message]  # 对话中的消息列表

    def render(self) -> str:
        """将整个对话格式化为字符串（用于构建 Prompt）"""
        return "\n<|endoftext|>".join([msg.render() for msg in self.messages])


@dataclass(frozen=True)
class ThreadConfig:
    """存储每个对话线程的模型配置（冻结不可修改）"""
    model: str  # 使用的模型名称
    max_tokens: int  # 模型最大输出 tokens
    temperature: float  # 随机性（0-1，越高越随机）


@dataclass
class Prompt:
    """构建 OpenAI API 所需的 Prompt 结构"""
    header: Message  # 系统指令（告诉模型角色）
    examples: List[Conversation]  # 示例对话
    convo: Conversation  # 当前实际对话

    def full_render(self, bot_name: str) -> List[Dict[str, str]]:
        """生成 OpenAI API 所需的 messages 格式（包含系统指令、示例、当前对话）"""
        # 1. 构建系统指令
        system_prompt = "\n<|endoftext|>".join([
            self.header.render(),
            Message("System", "示例对话：").render(),
            *[conv.render() for conv in self.examples],
            Message("System", "现在开始处理当前实际对话。").render()
        ])

        # 2. 构建消息列表
        messages = [{"role": "system", "content": system_prompt}]
        # 添加当前对话的消息（区分用户和机器人角色）
        for msg in self.convo.messages:
            if bot_name in msg.user:
                messages.append({"role": "assistant", "name": bot_name, "content": msg.text})
            else:
                messages.append({"role": "user", "name": msg.user, "content": msg.text})
        
        return messages


class CompletionResult(Enum):
    """OpenAI 响应的状态枚举"""
    OK = 0  # 正常响应
    TOO_LONG = 1  # 上下文过长
    INVALID_REQUEST = 2  # 请求参数错误
    OTHER_ERROR = 3  # 其他错误
    MODERATION_FLAGGED = 4  # 内容被标记（不拦截）
    MODERATION_BLOCKED = 5  # 内容被拦截


@dataclass
class CompletionData:
    """存储 OpenAI 响应的结果数据"""
    status: CompletionResult  # 响应状态
    reply_text: Optional[str]  # 回复内容（正常时非空）
    status_text: Optional[str]  # 状态描述（错误时非空）

# -------------------------- 工具函数（辅助功能） --------------------------
def should_block(guild: Optional[discord.Guild]) -> bool:
    """检查是否需要阻止当前服务器使用机器人"""
    # 1. 不支持私信（仅服务器内使用）
    if not guild:
        logger.info("拒绝私信请求：机器人仅支持服务器内使用")
        return True
    
    # 2. 检查服务器是否在允许列表内（空列表表示不限制）
    if ALLOWED_SERVER_IDS and guild.id not in ALLOWED_SERVER_IDS:
        logger.info(f"拒绝服务器 {guild.name}（ID: {guild.id}）的请求：不在允许列表内")
        return True
    
    return False


def discord_message_to_message(discord_msg: DiscordMessage) -> Optional[Message]:
    """将 Discord 消息转换为自定义 Message 格式"""
    # 处理线程启动消息（提取初始请求）
    if (discord_msg.type == discord.MessageType.thread_starter_message 
        and discord_msg.reference 
        and discord_msg.reference.cached_message):
        
        cached_msg = discord_msg.reference.cached_message
        if cached_msg.embeds and cached_msg.embeds[0].fields:
            field = cached_msg.embeds[0].fields[-1]  # 最后一个字段是用户的初始消息
            if field.value:
                return Message(user=field.name, text=field.value)
    
    # 处理普通消息
    elif discord_msg.content:
        return Message(user=discord_msg.author.name, text=discord_msg.content)
    
    # 不支持的消息类型（如纯图片、文件）
    return None


def split_into_shorter_messages(text: str) -> List[str]:
    """将长文本拆分为 Discord 支持的短消息（单条最大 2000 字符）"""
    return [text[i:i+MAX_CHARS_PER_REPLY_MSG] for i in range(0, len(text), MAX_CHARS_PER_REPLY_MSG)]


def is_last_message_stale(
    interaction_msg: DiscordMessage, 
    last_msg: Optional[DiscordMessage], 
    bot_id: int
) -> bool:
    """检查当前消息是否已过时（用户发送了新消息，无需处理当前消息）"""
    if not last_msg:
        return False
    # 条件：最后一条消息不是当前交互消息，且不是机器人发送的
    return last_msg.id != interaction_msg.id and last_msg.author.id != bot_id


async def close_thread(thread: discord.Thread):
    """关闭对话线程（修改名称、发送关闭提示、归档并锁定）"""
    await thread.edit(name=f"{INACTIVATE_THREAD_PREFIX} {thread.name[len(ACTIVATE_THREAD_PREFIX)+1:]}")
    await thread.send(
        embed=discord.Embed(
            description="🔒 对话已关闭：已达到最大消息数，防止上下文过长。",
            color=discord.Color.blue()
        )
    )
    await thread.edit(archived=True, locked=True)
    logger.info(f"关闭线程：{thread.name}（ID: {thread.id}）")


async def fetch_moderation_channel(guild: Optional[discord.Guild]) -> Optional[discord.TextChannel]:
    """获取当前服务器的审核频道（用于发送审核日志）"""
    if not guild or guild.id not in SERVER_TO_MODERATION_CHANNEL:
        return None
    
    channel_id = SERVER_TO_MODERATION_CHANNEL[guild.id]
    try:
        return await guild.fetch_channel(channel_id)
    except discord.NotFound:
        logger.error(f"审核频道不存在：服务器 {guild.name} 的频道 ID {channel_id}")
        return None
    except Exception as e:
        logger.error(f"获取审核频道失败：{str(e)}")
        return None


async def moderate_message(message: str, user: discord.User) -> Tuple[str, str]:
    """使用 OpenAI Moderation API 审核消息（返回：[标记原因, 拦截原因]）"""
    try:
        response = await openai_client.moderations.create(
            input=message,
            model="text-moderation-latest"
        )
        category_scores = response.results[0].category_scores
        
        flagged_str = ""  # 标记原因（不拦截）
        blocked_str = ""  # 拦截原因（拦截消息）
        
        # 检查每个分类的分数
        for category, score in category_scores.items():
            # 先检查是否需要拦截
            if score > MODERATION_VALUES_FOR_BLOCKED.get(category, 1.0):
                blocked_str = f"{category}（分数：{round(score, 3)}）"
                logger.warning(f"拦截用户 {user.name}（ID: {user.id}）的消息：{blocked_str}")
                break  # 只要有一个分类触发拦截，直接返回
            
            # 再检查是否需要标记
            if score > MODERATION_VALUES_FOR_FLAGGED.get(category, 1.0):
                flagged_str += f"{category}（分数：{round(score, 3)}）、"
                logger.warning(f"标记用户 {user.name}（ID: {user.id}）的消息：{flagged_str[:-1]}")
        
        # 去除标记原因末尾的逗号
        if flagged_str.endswith("、"):
            flagged_str = flagged_str[:-1]
        
        return (flagged_str, blocked_str)
    
    except Exception as e:
        logger.error(f"内容审核失败：{str(e)}")
        return ("", "")  # 审核失败时不拦截、不标记


async def send_moderation_flagged_message(
    guild: Optional[discord.Guild],
    user: discord.User,
    flagged_str: str,
    message: str,
    url: Optional[str]
):
    """发送消息被标记的审核日志到审核频道"""
    if not guild or not flagged_str:
        return
    
    mod_channel = await fetch_moderation_channel(guild)
    if not mod_channel:
        return
    
    # 截取消息前 100 字符（避免日志过长）
    message_preview = message[:100] + "..." if len(message) > 100 else message
    await mod_channel.send(
        f"⚠️ 消息被标记 - 用户：{user.name}（ID: {user.id}）\n"
        f"原因：{flagged_str}\n"
        f"消息预览：{message_preview}\n"
        f"链接：{url or '无'}"
    )


async def send_moderation_blocked_message(
    guild: Optional[discord.Guild],
    user: discord.User,
    blocked_str: str,
    message: str
):
    """发送消息被拦截的审核日志到审核频道"""
    if not guild or not blocked_str:
        return
    
    mod_channel = await fetch_moderation_channel(guild)
    if not mod_channel:
        return
    
    # 截取消息前 500 字符（保留更多上下文）
    message_preview = message[:500] + "..." if len(message) > 500 else message
    await mod_channel.send(
        f"❌ 消息被拦截 - 用户：{user.name}（ID: {user.id}）\n"
        f"原因：{blocked_str}\n"
        f"消息内容：{message_preview}"
    )

# -------------------------- OpenAI 交互函数（核心功能） --------------------------
async def generate_completion_response(
    messages: List[Message],
    user: discord.User,
    thread_config: ThreadConfig
) -> CompletionData:
    """调用 OpenAI API 生成响应"""
    try:
        # 1. 构建 Prompt
        prompt = Prompt(
            header=Message("system", f"{BOT_NAME} 的指令：{BOT_INSTRUCTIONS}"),
            examples=[Conversation(msg_list) for msg_list in [
                [Message(m["user"], m["text"]) for m in conv["messages"]] 
                for conv in EXAMPLE_CONVOS
            ]],
            convo=Conversation(messages)
        )
        openai_messages = prompt.full_render(BOT_NAME)

        # 2. 调用 OpenAI API
        response = await openai_client.chat.completions.create(
            model=thread_config.model,
            messages=openai_messages,
            temperature=thread_config.temperature,
            max_tokens=thread_config.max_tokens,
            stop=["<|endoftext|>"]  # 停止符（与 Prompt 格式对应）
        )

        # 3. 处理 API 响应
        reply_text = response.choices[0].message.content.strip()
        if not reply_text:
            return CompletionData(
                status=CompletionResult.OTHER_ERROR,
                reply_text=None,
                status_text="OpenAI 返回空响应"
            )

        # 4. 审核响应内容
        # 截取最后 500 字符（避免审核内容过长，聚焦最新回复）
        content_to_moderate = (openai_messages[-1]["content"] + reply_text)[-500:]
        flagged_str, blocked_str = await moderate_message(content_to_moderate, user)
        
        if blocked_str:
            return CompletionData(
                status=CompletionResult.MODERATION_BLOCKED,
                reply_text=reply_text,
                status_text=f"响应被拦截：{blocked_str}"
            )
        if flagged_str:
            return CompletionData(
                status=CompletionResult.MODERATION_FLAGGED,
                reply_text=reply_text,
                status_text=f"响应被标记：{flagged_str}"
            )

        # 5. 正常响应
        return CompletionData(
            status=CompletionResult.OK,
            reply_text=reply_text,
            status_text=None
        )

    # 处理 API 错误
    except openai.BadRequestError as e:
        # 上下文过长错误
        if "maximum context length" in str(e).lower():
            return CompletionData(
                status=CompletionResult.TOO_LONG,
                reply_text=None,
                status_text="上下文过长：请关闭当前线程并创建新对话"
            )
        # 其他请求错误（如模型不存在、API 密钥错误）
        else:
            logger.error(f"OpenAI 请求错误：{str(e)}")
            return CompletionData(
                status=CompletionResult.INVALID_REQUEST,
                reply_text=None,
                status_text=f"请求错误：{str(e)[:100]}"  # 截取前 100 字符避免过长
            )
    except Exception as e:
        # 其他未知错误
        logger.error(f"OpenAI 调用失败：{str(e)}")
        return CompletionData(
            status=CompletionResult.OTHER_ERROR,
            reply_text=None,
            status_text=f"未知错误：{str(e)[:100]}"
        )


async def process_response(
    user: discord.User,
    thread: discord.Thread,
    response_data: CompletionData
):
    """处理 OpenAI 响应并发送到 Discord 线程"""
    status = response_data.status
    reply_text = response_data.reply_text
    status_text = response_data.status_text

    # 1. 正常响应或被标记的响应（发送回复）
    if status in [CompletionResult.OK, CompletionResult.MODERATION_FLAGGED]:
        if not reply_text:
            await thread.send(
                embed=discord.Embed(
                    description="❓ 未获取到有效回复，请稍后再试。",
                    color=discord.Color.yellow()
                )
            )
            return
        
        # 拆分长回复并发送
        for short_reply in split_into_shorter_messages(reply_text):
            sent_msg = await thread.send(short_reply)
        
        # 发送标记提示（如果被标记）
        if status == CompletionResult.MODERATION_FLAGGED:
            await thread.send(
                embed=discord.Embed(
                    description="⚠️ 该回复内容已被系统标记，请注意内容安全。",
                    color=discord.Color.yellow()
                )
            )
            # 发送审核日志
            await send_moderation_flagged_message(
                guild=thread.guild,
                user=user,
                flagged_str=status_text.split("：")[-1] if status_text else "",
                message=reply_text,
                url=sent_msg.jump_url if "sent_msg" in locals() else None
            )

    # 2. 被拦截的响应（不发送回复，提示拦截）
    elif status == CompletionResult.MODERATION_BLOCKED:
        await thread.send(
            embed=discord.Embed(
                description="❌ 响应内容违反安全规则，已被拦截。",
                color=discord.Color.red()
            )
        )
        await send_moderation_blocked_message(
            guild=thread.guild,
            user=user,
            blocked_str=status_text.split("：")[-1] if status_text else "",
            message=reply_text or "无内容"
        )

    # 3. 上下文过长（关闭线程）
    elif status == CompletionResult.TOO_LONG:
        await thread.send(
            embed=discord.Embed(
                description=f"⚠️ {status_text}",
                color=discord.Color.orange()
            )
        )
        await close_thread(thread)

    # 4. 其他错误（提示错误信息）
    else:
        error_msg = f"❌ 处理失败：{status_text or '未知错误'}"
        await thread.send(embed=discord.Embed(description=error_msg, color=discord.Color.red()))

# -------------------------- Discord 机器人初始化 --------------------------
# 启用必要的意图（消息内容、服务器成员等）
intents = discord.Intents.default()
intents.message_content = True  # 必须启用，否则无法读取消息内容
intents.guilds = True  # 启用服务器相关功能

# 初始化客户端和命令树
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# 存储线程配置（key: 线程ID，value: ThreadConfig）
thread_data: DefaultDict[int, ThreadConfig] = defaultdict(ThreadConfig)

# -------------------------- Discord 事件和命令 --------------------------
@client.event
async def on_ready():
    """机器人就绪事件（启动后触发）"""
    # 同步命令树（确保 /chat 命令在服务器中可用）
    await tree.sync()
    # 打印就绪日志
    invite_url = f"https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=268435456&scope=bot%20applications.commands"
    logger.info(f"机器人已登录：{client.user}（ID: {client.user.id}）")
    logger.info(f"邀请链接：{invite_url}")


@tree.command(name="chat", description="创建一个新的对话线程，与 AI 聊天")
@app_commands.checks.has_permissions(send_messages=True, view_channel=True)
@app_commands.checks.bot_has_permissions(
    send_messages=True, 
    view_channel=True, 
    manage_threads=True  # 必须有管理线程权限，否则无法创建线程
)
@app_commands.describe(
    message="你的初始问题或对话内容",
    model="使用的 AI 模型（默认：gpt-5-mini）",
    temperature="随机性（0-1，越高越灵活，默认：1.0）",
    max_tokens="AI 最大输出字符数（1-4096，默认：512）"
)
async def chat_command(
    interaction: discord.Interaction,
    message: str,
    model: str = DEFAULT_MODEL,
    temperature: float = 1.0,
    max_tokens: int = 512
):
    """/chat 命令：创建新的对话线程"""
    # 1. 基础检查（仅允许在文本频道使用）
    if not isinstance(interaction.channel, discord.TextChannel):
        await interaction.response.send_message(
            "❌ 仅支持在文本频道使用此命令", ephemeral=True
        )
        return
    
    # 2. 检查服务器是否被阻止
    if should_block(interaction.guild):
        await interaction.response.send_message(
            "❌ 你无权使用此机器人", ephemeral=True
        )
        return

    # 3. 验证参数有效性
    # 验证温度（0-1）
    if not (0.0 <= temperature <= 1.0):
        await interaction.response.send_message(
            f"❌ 无效的温度值：{temperature}（必须在 0.0-1.0 之间）",
            ephemeral=True
        )
        return
    # 验证最大 tokens（1-4096）
    if not (1 <= max_tokens <= 4096):
        await interaction.response.send_message(
            f"❌ 无效的最大输出字符数：{max_tokens}（必须在 1-4096 之间）",
            ephemeral=True
        )
        return
    # 验证模型是否支持
    if model not in AVAILABLE_MODELS:
        await interaction.response.send_message(
            f"❌ 不支持的模型：{model}（支持的模型：{', '.join(AVAILABLE_MODELS)}）",
            ephemeral=True
        )
        return

    # 4. 审核用户的初始消息
    flagged_str, blocked_str = await moderate_message(message, interaction.user)
    # 拦截被禁止的消息
    if blocked_str:
        await send_moderation_blocked_message(
            guild=interaction.guild,
            user=interaction.user,
            blocked_str=blocked_str,
            message=message
        )
        await interaction.response.send_message(
            "❌ 你的消息违反安全规则，已被拦截",
            ephemeral=True
        )
        return

    try:
        # 5. 发送初始响应（创建线程前的提示）
        # 构建嵌入消息（显示用户请求和配置）
        embed = discord.Embed(
            title="🤖 新对话已创建",
            description=f"<@{interaction.user.id}> 的初始问题：\n{message}",
            color=discord.Color.green()
        )
        embed.add_field(name="模型", value=model, inline=True)
        embed.add_field(name="随机性", value=f"{temperature:.1f}", inline=True)
        embed.add_field(name="最大输出", value=f"{max_tokens} tokens", inline=True)
        
        # 如果消息被标记，修改嵌入颜色和标题
        if flagged_str:
            embed.color = discord.Color.yellow()
            embed.title += " ⚠️ （内容已标记）"
        
        # 发送嵌入消息
        await interaction.response.send_message(embed=embed)
        initial_msg = await interaction.original_response()

        # 6. 发送标记日志（如果被标记）
        if flagged_str:
            await send_moderation_flagged_message(
                guild=interaction.guild,
                user=interaction.user,
                flagged_str=flagged_str,
                message=message,
                url=initial_msg.jump_url
            )

        # 7. 创建对话线程
        # 线程名称格式：前缀 + 用户名 + 初始消息前 30 字符
        thread_name = f"{ACTIVATE_THREAD_PREFIX} {interaction.user.name[:20]} - {message[:30]}"
        # 截断过长的线程名称（Discord 线程名称最大 100 字符）
        if len(thread_name) > 100:
            thread_name = thread_name[:97] + "..."
        
        thread = await initial_msg.create_thread(
            name=thread_name,
            slowmode_delay=1,  # 慢速模式（防止刷屏）
            auto_archive_duration=60,  # 60 分钟无活动自动归档
            reason=f"用户 {interaction.user.name} 创建的 AI 对话"
        )

        # 8. 存储线程配置
        thread_data[thread.id] = ThreadConfig(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature
        )
        logger.info(f"创建线程：{thread.name}（ID: {thread.id}）- 用户：{interaction.user.name}")

        # 9. 生成初始响应
        async with thread.typing():  # 显示"正在输入"状态
            # 构建初始对话消息
            initial_messages = [Message(user=interaction.user.name, text=message)]
            # 调用 OpenAI 生成响应
            response_data = await generate_completion_response(
                messages=initial_messages,
                user=interaction.user,
                thread_config=thread_data[thread.id]
            )
            # 处理并发送响应
            await process_response(
                user=interaction.user,
                thread=thread,
                response_data=response_data
            )

    except Exception as e:
        # 捕获创建线程过程中的错误
        logger.error(f"创建对话失败：{str(e)}")
        await interaction.response.send_message(
            f"❌ 创建对话失败：{str(e)[:50]}",  # 截取前 50 字符避免过长
            ephemeral=True
        )


@client.event
async def on_message(message: DiscordMessage):
    """消息事件（监测线程内的消息，生成响应）"""
    # 1. 过滤不需要处理的消息
    # 忽略机器人自身的消息
    if message.author == client.user:
        return
    # 忽略非线程内的消息
    if not isinstance(message.channel, discord.Thread):
        return
    
    thread = message.channel
    # 忽略非机器人创建的线程
    if thread.owner_id != client.user.id:
        return
    # 忽略已归档/锁定/非对话前缀的线程
    if thread.archived or thread.locked or not thread.name.startswith(ACTIVATE_THREAD_PREFIX):
        return
    # 忽略被阻止的服务器
    if should_block(thread.guild):
        return

    # 2. 检查线程消息数是否超过上限
    if thread.message_count > MAX_THREAD_MESSAGES:
        await close_thread(thread)
        return

    # 3. 审核用户消息
    flagged_str, blocked_str = await moderate_message(message.content, message.author)
    # 拦截被禁止的消息
    if blocked_str:
        # 尝试删除被拦截的消息
        try:
            await message.delete()
            await thread.send(
                embed=discord.Embed(
                    description=f"❌ <@{message.author.id}> 的消息违反安全规则，已删除。",
                    color=discord.Color.red()
                )
            )
        except discord.Forbidden:
            # 没有删除权限时提示
            await thread.send(
                embed=discord.Embed(
                    description=f"❌ <@{message.author.id}> 的消息违反安全规则，但无法删除（缺少「管理消息」权限）。",
                    color=discord.Color.red()
                )
            )
        await send_moderation_blocked_message(
            guild=thread.guild,
            user=message.author,
            blocked_str=blocked_str,
            message=message.content
        )
        return

    # 4. 标记消息（不拦截，仅提示）
    if flagged_str:
        await thread.send(
            embed=discord.Embed(
                description=f"⚠️ <@{message.author.id}> 的消息已被标记，请注意内容安全。",
                color=discord.Color.yellow()
            )
        )
        await send_moderation_flagged_message(
            guild=thread.guild,
            user=message.author,
            flagged_str=flagged_str,
            message=message.content,
            url=message.jump_url
        )

    # 5. 延迟处理（防止用户连续发送消息导致重复响应）
    if SECONDS_DELAY_RECEIVING_MSG > 0:
        await asyncio.sleep(SECONDS_DELAY_RECEIVING_MSG)
        # 检查是否有新消息（如果有，忽略当前消息）
        if is_last_message_stale(
            interaction_msg=message,
            last_msg=thread.last_message,
            bot_id=client.user.id
        ):
            logger.info(f"忽略过时消息：用户 {message.author.name} 在 thread {thread.id}")
            return

    logger.info(f"处理线程消息：{thread.name} - {message.author.name}: {message.content[:50]}")

    try:
        # 6. 获取线程内的历史消息（构建上下文）
        # 反转消息顺序（从旧到新）
        history_messages = [
            discord_message_to_message(msg)
            async for msg in thread.history(limit=MAX_THREAD_MESSAGES)
        ]
        # 过滤空消息，按时间正序排列
        valid_messages = [msg for msg in history_messages if msg]
        valid_messages.reverse()

        # 7. 生成响应
        async with thread.typing():
            # 检查线程配置是否存在（防止异常）
            if thread.id not in thread_data:
                thread_data[thread.id] = ThreadConfig(
                    model=DEFAULT_MODEL,
                    max_tokens=512,
                    temperature=1.0
                )
            # 调用 OpenAI 生成响应
            response_data = await generate_completion_response(
                messages=valid_messages,
                user=message.author,
                thread_config=thread_data[thread.id]
            )

        # 8. 检查响应是否过时（处理延迟期间的新消息）
        if is_last_message_stale(
            interaction_msg=message,
            last_msg=thread.last_message,
            bot_id=client.user.id
        ):
            logger.info(f"忽略过时响应：thread {thread.id}")
            return

        # 9. 处理并发送响应
        await process_response(
            user=message.author,
            thread=thread,
            response_data=response_data
        )

    except Exception as e:
        logger.error(f"处理线程消息失败：{str(e)}")
        await thread.send(
            embed=discord.Embed(
                description=f"❌ 处理消息失败：{str(e)[:50]}",
                color=discord.Color.red()
            )
        )

# -------------------------- 启动机器人 --------------------------
if __name__ == "__main__":
    # 检查必要配置是否填写
    if not DISCORD_BOT_TOKEN or DISCORD_BOT_TOKEN == "YOUR_DISCORD_BOT_TOKEN":
        logger.error("请先填写 DISCORD_BOT_TOKEN（在配置变量部分）")
        exit(1)
    if not OPENAI_API_KEY or OPENAI_API_KEY == "YOUR_OPENAI_API_KEY":
        logger.error("请先填写 OPENAI_API_KEY（在配置变量部分）")
        exit(1)
    
    # 启动机器人
    client.run(DISCORD_BOT_TOKEN)