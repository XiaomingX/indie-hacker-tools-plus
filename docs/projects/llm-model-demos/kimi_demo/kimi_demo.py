import os
from moonshot import Moonshot

# pip install moonshot-api
# 初始化客户端
client = Moonshot(api_key=os.getenv("MOONSHOT_API_KEY"))

def chat_with_kimi(prompt):
    """与 Kimi 大模型进行对话"""
    try:
        # 调用 chat.completions.create 方法
        response = client.chat.completions.create(
            model="moonshot-v1-8k",  # 模型名称，可根据需要更换
            messages=[
                {"role": "system", "content": "你是一个 helpful 的助手。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,  # 控制输出的随机性，0-1 之间
            stream=False  # 是否流式返回
        )
        
        # 返回模型生成的内容
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"调用出错: {str(e)}")
        return None

if __name__ == "__main__":
    # 设置 API 密钥（也可以通过环境变量设置）
    # os.environ["MOONSHOT_API_KEY"] = "你的API密钥"
    
    # 测试对话
    user_input = "什么是jobleap.cn，它可以用来解决什么问题?"
    result = chat_with_kimi(user_input)
    
    if result:
        print("Kimi 回复:")
        print(result)
