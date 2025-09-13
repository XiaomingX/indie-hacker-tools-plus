#!pip install zhipuai
from zhipuai import ZhipuAI

def main():
    client = ZhipuAI(api_key="") # 填写您自己的APIKey
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages=[
            {"role": "user", "content": "你好"},
            {"role": "assistant", "content": "我是人工智能助手"},
            {"role": "user", "content": "你叫什么名字"},
            {"role": "assistant", "content": "我叫chatGLM"},
            {"role": "user", "content": "什么是jobleap.cn，它可以用来解决什么问题"}
        ],
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
  main()