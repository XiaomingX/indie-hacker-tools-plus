# agent_discord_bot

`agent_discord_bot` 是一款基于 **Discord API** 与 **OpenAI 大模型** 开发的智能对话机器人，旨在为 Discord 服务器提供「上下文感知的连续交互」能力。机器人以「对话线程」为交互单元，支持多模型切换、内容安全审核、线程自动管理等核心功能，可作为服务器内的智能助手，满足问答、咨询、闲聊等多样化需求。


## 核心功能

| 功能模块                | 说明                                                                 |
|-------------------------|----------------------------------------------------------------------|
| 命令式对话线程创建      | 通过 `/chat` 指令快速创建专属对话线程，支持自定义模型、随机性、最大输出长度 |
| 多 OpenAI 模型支持      | 兼容 `gpt-5-mini`/`gpt-4o-mini` 等模型，可根据需求灵活切换               |
| 上下文连续交互          | 线程内自动保留历史对话记录，支持多轮连续交互，理解上下文逻辑           |
| 全链路内容安全审核      | 基于 OpenAI Moderation API 拦截违规内容、标记风险消息，支持审核日志归档 |
| 线程自动生命周期管理    | 消息数达上限时自动关闭线程（归档+锁定），避免上下文过长导致性能问题     |
| 友好的交互反馈          | 支持长文本拆分发送、「正在输入」状态提示、错误信息可视化（嵌入消息）    |


## 前置准备

在部署机器人前，需完成以下两项核心准备工作：

### 1. Discord 机器人配置
1. 访问 [Discord 开发者平台](https://discord.com/developers/applications)，创建新应用（Application），命名为 `agent_discord_bot`。
2. 进入「Bot」标签页，点击「Add Bot」创建机器人账号，复制 `Token`（后续配置用，切勿泄露）。
3. 开启机器人「Privileged Gateway Intents」中的 **Message Content Intent**（必须开启，否则无法读取消息内容）。
4. 进入「OAuth2 → URL Generator」，勾选以下权限：
   - **Scopes**：`bot` + `applications.commands`
   - **Bot Permissions**：`Send Messages`、`View Channels`、`Manage Threads`、`Delete Messages`（可选，用于删除违规消息）
5. 复制生成的 URL，在浏览器中打开并邀请机器人进入目标 Discord 服务器。


### 2. OpenAI API 准备
1. 访问 [OpenAI 平台](https://platform.openai.com/api-keys)，登录账号后创建新的 API Key，复制密钥（后续配置用）。
2. 确保账号已充值（OpenAI API 需付费使用，免费额度到期后需自行续费）。


## 快速部署

### 1. 环境要求
- Python 3.8+
- 依赖库：`discord.py`、`openai`


### 2. 安装步骤
1. 克隆/下载项目代码到本地：
   ```bash
   git clone <你的项目仓库地址>
   cd agent_discord_bot
   ```
2. 安装依赖库：
   ```bash
   pip install -r requirements.txt
   ```
   （若未创建 `requirements.txt`，可直接执行：`pip install discord.py openai`）


### 3. 配置机器人
修改项目根目录下的 `main.py` 文件，找到「配置变量」部分，填写关键参数：
```python
# -------------------------- 配置变量（必须修改） --------------------------
DISCORD_BOT_TOKEN = "你的 Discord 机器人 Token"  # 步骤1中复制的 Token
OPENAI_API_KEY = "你的 OpenAI API Key"            # 步骤2中复制的 API Key

# -------------------------- 可选配置（根据需求调整） --------------------------
ALLOWED_SERVER_IDS = [1234567890]  # 限制仅指定服务器可用（空列表表示不限制）
BOT_NAME = "AgentBot"              # 机器人在对话中显示的名称
DEFAULT_MODEL = "gpt-3.5-turbo"    # 默认使用的模型（可选 gpt-4）
MAX_THREAD_MESSAGES = 20           # 每个线程的最大消息数（防止上下文过长）
```


### 4. 启动机器人
在项目根目录执行以下命令，启动机器人：
```bash
python main.py
```
- 启动成功后，日志会输出机器人登录信息及邀请链接（若未提前邀请，可通过此链接邀请）。
- 若出现 `We have logged in as AgentBot` 提示，说明机器人已正常在线。


## 使用指南

### 1. 创建对话线程
在 Discord 服务器的文本频道中，使用 `/chat` 指令创建对话：
- 指令格式：`/chat 你的问题 [模型] [随机性] [最大输出长度]`
- 示例：
  - 基础用法：`/chat 什么是 Python？`（使用默认配置：gpt-3.5-turbo、随机性1.0、最大输出512 tokens）
  - 自定义配置：`/chat 写一段关于人工智能的短文 模型:gpt-4 随机性:0.7 最大输出:1024`

执行指令后，机器人会自动创建一个以 `💬 对话` 为前缀的线程，并在 thread 内返回第一个响应。


### 2. 继续对话
在创建的对话线程内，直接发送消息即可继续与机器人交互（无需重复使用 `/chat` 指令）。例如：
- 用户：`Python 适合初学者吗？`
- 机器人会基于历史对话（“什么是 Python？”+ 当前问题）生成连续响应。


### 3. 线程关闭
当线程内消息数达到 `MAX_THREAD_MESSAGES`（默认20条）时，机器人会自动：
1. 将线程名称改为 `🔒 已关闭` 前缀
2. 发送关闭提示
3. 归档并锁定线程（无法继续发送消息）

若需继续对话，需重新使用 `/chat` 指令创建新线程。


## 配置说明（进阶）

`main.py` 中的关键配置项可根据需求调整，以下是核心配置的详细说明：

| 配置项                  | 用途                                                                 | 默认值/示例                  |
|-------------------------|----------------------------------------------------------------------|------------------------------|
| `ALLOWED_SERVER_IDS`    | 限制机器人仅在指定服务器可用（服务器ID可通过 Discord 开发者模式查看）   | `[]`（不限制）/ `[1234567890]`|
| `BOT_INSTRUCTIONS`      | 定义机器人的角色和行为（引导 OpenAI 模型的回复风格）                   | "你是友好的 Discord 智能助手..." |
| `EXAMPLE_CONVOS`        | 示例对话（用于优化模型回复逻辑，格式为用户-机器人对话对）              | 见代码内默认示例              |
| `MODERATION_VALUES_FOR_BLOCKED` | 内容审核拦截阈值（超过该分数的消息会被删除）                        | `{"hate":0.7, "violence":0.7}`|
| `SERVER_TO_MODERATION_CHANNEL` | 审核日志频道（key:服务器ID，value:频道ID，用于接收违规消息日志）      | `{1234567890: 0987654321}`   |


## 注意事项

1. **权限要求**：确保机器人在 Discord 服务器中拥有 `Send Messages`、`View Channels`、`Manage Threads` 权限，否则无法创建线程或发送消息。
2. **API 成本**：OpenAI API 按 tokens 计费，`gpt-4` 成本高于 `gpt-3.5-turbo`，建议通过 `MAX_THREAD_MESSAGES` 和 `max_tokens` 控制成本。
3. **私信禁用**：机器人默认禁用私信交互，仅支持在服务器内的文本频道使用。
4. **日志查看**：启动后日志会输出关键操作（如线程创建、消息审核、错误信息），可通过日志排查问题。
5. **安全提示**：`DISCORD_BOT_TOKEN` 和 `OPENAI_API_KEY` 切勿泄露到公开仓库或分享给他人，否则可能导致账号被盗用或产生额外费用。


## 问题排查

1. **机器人不响应 `/chat` 指令**：
   - 检查 `main.py` 中的 `DISCORD_BOT_TOKEN` 是否正确。
   - 确认机器人已邀请到服务器，且拥有 `View Channels` 和 `Send Messages` 权限。
   - 执行 `python main.py` 后，查看日志是否有 `We have logged in` 提示（未登录则无法响应）。

2. **OpenAI 响应失败**：
   - 检查 `OPENAI_API_KEY` 是否正确，且账号是否有可用余额。
   - 查看日志中的错误信息，若提示“maximum context length”，需减少 `MAX_THREAD_MESSAGES` 或 `max_tokens`。

3. **无法删除违规消息**：
   - 确保机器人拥有 `Delete Messages` 权限，且在目标频道中未被限制该权限。


## 许可证

[MIT License](LICENSE)（可根据项目实际情况替换为对应的许可证）