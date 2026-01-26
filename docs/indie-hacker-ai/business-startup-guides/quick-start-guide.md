高价值：否

标题：
《Together AI API快速入门：注册、安装、运行一步到位》

### 一起AI API快速入门指南

#### 开篇：主题与背景
主题是快速掌握Together AI的API使用方法，背景是Together AI能让用户用几行代码轻松运行领先开源模型，目的是帮助用户快速上手其API。

#### 1. 注册账号
何时何地：首先，用户需要进行账号注册，无特定地点限制。相关人物是用户自己。
注册后，用户要将API密钥设置为名为`TOGETHER_API_KEY`的环境变量。Shell命令为：`export TOGETHER_API_KEY=xxxxx`，新账户注册完成后可免费获得1美元初始额度用于试用。

#### 2. 安装开发库
何时何地：在注册账号并获取API密钥后，进行开发库安装。无特定地点限制。相关人物是用户自己。
Together官方提供了Python和TypeScript的库，也能通过HTTP API用任意编程语言调用。安装命令如下：
 - Python：`pip install together`
 - TypeScript：查看TypeScript安装指南。

#### 3. 运行第一个模型查询
何时何地：在完成账号注册和开发库安装后，可进行模型查询，无特定地点限制。相关人物是用户自己。
选择一个模型进行查询，以Llama 3.1 8B为例进行聊天补全并开启流式传输。Python示例代码如下：
```python
from together import Together

client = Together()

stream = client.chat.completions.create(
  model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
  messages=[{"role": "user", "content": "What are the top 3 things to do in New York?"}],
  stream=True,
)

for chunk in stream:
  print(chunk.choices[0].delta.content or "", end="", flush=True)
```
这里可以把模型查询比作去餐厅点菜，选好要吃的菜品（这里是选好模型），然后按照流程下单（运行代码查询）。

#### 总结
本文先点明主题是快速掌握Together AI API使用方法，然后按注册账号、安装开发库、运行第一个模型查询的顺序展开。注册账号是获取API密钥的前提，安装开发库是为了能调用API，运行第一个模型查询则是实际应用API的示例。通过这样的步骤，用户能快速上手Together AI的API，完成首次查询就像完成了一个简单的小任务，让用户有成就感并能继续深入学习使用该API。