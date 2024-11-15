# simplellm
A script for using various LLMs around the world

# 综述
 - 对于会员而言，每个人每个月能得到25美元的api使用额度。

这是如何申请和使用x.ai (Grok) API密钥的简化描述：

### 申请API密钥

#### 前提条件
你需要先订阅X平台的**Premium+会员**（每月费用约1,960日元）。

#### 步骤
1. 访问Grok的PromptIDE平台
   - 打开ide.x.ai网站并登录
   - 点击右上角个人资料图标，选择"API Keys"

2. 创建新的API密钥
   - 点击"Create API Key"
   - 设置权限（如聊天读取、写入权限等）

3. 保存API密钥
   - 设置完权限后点击"Save"并复制密钥，安全保存

### 使用API密钥
 - 可以复用openai的SDK.
```
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("X_AI_KEY"),base_url="https://api.x.ai/v1")
completion = client.chat.completions.create(
    model="grok-beta",
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)

print(completion.choices[0].message.content)
```