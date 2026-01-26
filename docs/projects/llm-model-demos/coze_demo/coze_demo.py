# 参考教程：https://juejin.cn/post/7444047947249385523

# 参考：
## https://juejin.cn/post/7444047947249385523
# 简介
# 本程序演示了如何通过 Coze API 创建、发布和与智能体进行对话。具体包括以下几个主要功能：
# 初始化 Coze 客户端：程序首先通过 initialize_coze_client() 函数初始化 Coze 客户端，使用从环境变量中获取的 API 令牌进行身份验证，连接到 Coze 的中国区 API 服务。
# 上传头像：在 upload_avatar() 函数中，程序支持上传用户指定的头像文件，并返回上传后的头像 ID。
# 创建智能体：通过 create_bot() 函数，程序在指定的工作空间中创建一个新的智能体，并为其指定头像、名称和提示信息（如翻译功能）。
# 发布智能体：使用 publish_bot() 函数，将创建的智能体发布为 API 服务，用户可以通过该智能体与系统进行交互。
# 启动对话流：在 start_conversation() 函数中，程序启动了一个对话流，并实时输出聊天消息。用户可以与智能体进行对话，智能体将根据提示信息进行相应的处理和回应。
# 主程序入口：main() 函数串联了上述各个功能，完成了客户端初始化、头像上传、智能体创建与发布、以及对话的启动。
# 运行流程
# 程序首先初始化 Coze 客户端，并上传头像。
# 然后创建一个智能体并发布为 API 服务。
# 最后，启动与智能体的对话流，实时输出用户和智能体之间的互动内容。


import os
from pathlib import Path
from cozepy import Coze, TokenAuth, BotPromptInfo, Message, ChatEventType, MessageContentType, COZE_CN_BASE_URL

def initialize_coze_client():
    """初始化 Coze 客户端"""
    coze_api_token = os.getenv("COZE_API_TOKEN")
    if not coze_api_token:
        raise ValueError("请设置环境变量 COZE_API_TOKEN")

    return Coze(auth=TokenAuth(token=coze_api_token), base_url=COZE_CN_BASE_URL)

def upload_avatar(coze, file_path: Path):
    """上传头像并返回头像ID"""
    avatar = coze.files.upload(file=file_path)
    return avatar.id

def create_bot(coze, avatar_id: str, space_id: str, bot_name: str, prompt: str):
    """创建智能体并返回"""
    bot = coze.bots.create(
        space_id=space_id,
        name=bot_name,
        icon_file_id=avatar_id,
        prompt_info=BotPromptInfo(prompt=prompt)
    )
    return bot

def publish_bot(coze, bot):
    """发布智能体为API服务"""
    coze.bots.publish(bot_id=bot.bot_id)

def start_conversation(coze, bot_id: str, user_id: str, user_message: str):
    """启动对话流并实时输出消息"""
    for event in coze.chat.stream(
        bot_id=bot_id,
        user_id=user_id,
        additional_messages=[Message.build_user_question_text(user_message)],
    ):
        if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
            if isinstance(event.message.content, str):
                print(event.message.content, end="", flush=True)
            elif hasattr(event.message.content, 'type') and event.message.content.type == MessageContentType.TEXT:
                print(event.message.content.text, end="", flush=True)

        if event.event == ChatEventType.CONVERSATION_CHAT_COMPLETED:
            print("\n对话结束。")
            print("token 使用情况:", event.chat.usage.token_count)

def main():
    """主程序入口"""
    # 初始化 Coze 客户端
    coze = initialize_coze_client()

    # 上传头像并获取头像ID
    avatar_id = upload_avatar(coze, Path("image.png"))

    # 创建智能体
    space_id = "xxxxxx"  # 替换为你的工作空间ID[必须]
    bot_name = "翻译机器人"  # 智能体名称[可不改]
    prompt = "你是一个翻译助手，翻译以下英文为中文"  # 智能体的提示内容[可不改]
    bot = create_bot(coze, avatar_id, space_id, bot_name, prompt)

    # 发布智能体为API服务
    publish_bot(coze, bot)

    # 启动对话流
    user_id = "unique_user_id"  # 替换为实际用户ID[可不改]
    user_message = "什么是jobleap.cn，它可以用来解决什么问题?"  # 用户输入的消息[可不改]
    start_conversation(coze, bot.bot_id, user_id, user_message)

if __name__ == "__main__":
    main()