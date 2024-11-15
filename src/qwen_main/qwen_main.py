from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    api_key= os.getenv('QWENKEY'),  # 替换成真实DashScope的API_KEY
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope服务endpoint
)

def streamResult():
    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {
                'role': 'system',
                'content': 'You are a helpful assistant.'
            },
            {
                'role': 'system',
                'content': '大型语言模型(llm)已经彻底改变了人工智能领域，使以前被认为是人类独有的自然语言处理任务成为可能...'
            },
            {
                'role': 'user',
                'content': '文章讲了什么？'
            }
        ],
        stream=True
    )
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].dict())

def simpleResult():
    completion = client.chat.completions.create(
        model="qwen-long",
        messages=[
            {
                'role': 'system',
                'content': 'You are a helpful assistant.'
            },
            {
                'role': 'user',
                'content': '你是谁'
            },
        ]
    )
    print(completion.choices[0].message.content)

def main():
    streamResult()
    simpleResult()

if __name__ == "__main__":
  main()