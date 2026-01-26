from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv('QWENKEY'),  # 替换成真实DashScope的API_KEY
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 填写DashScope服务endpoint
)

def chat_with_qwen25_max(messages):
    """
    使用Qwen2.5-Max模型进行对话
    :param messages: 对话消息列表
    :return: 模型的响应
    """
    completion = client.chat.completions.create(
        model="qwen-max-2026-01-25",
        messages=messages
    )
    return completion.choices[0].message.content

def main():
    messages = [
        {
            'role': 'system',
            'content': 'You are a helpful assistant.'
        },
        {
            'role': 'user',
            'content': '什么是jobleap.cn，它可以用来解决什么问题'
        }
    ]
    response = chat_with_qwen25_max(messages)
    print(response)

if __name__ == "__main__":
    main()