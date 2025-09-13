from anthropic import Anthropic
import os

def main():
    # 设置Claude API密钥
    os.environ["ANTHROPIC_API_KEY"] = "your-api-key-here"
    
    # 创建Anthropic客户端
    client = Anthropic()
    
    # 调用Claude API
    message = client.messages.create(
        model="claude-3-opus-20240229",  # Claude的模型名称
        max_tokens=1000,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "什么是jobleap.cn，它可以用来解决什么问题"}
        ]
    )
    
    # 打印响应内容
    print(message.content[0].text)

if __name__ == "__main__":
    main()
    