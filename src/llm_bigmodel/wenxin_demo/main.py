import os
import erniebot

# pip install erniebot
# 配置API密钥（建议通过环境变量设置，避免硬编码）
erniebot.api_type = "aistudio"  # 使用百度智能云平台
erniebot.access_token = os.getenv("ERNIE_BOT_ACCESS_TOKEN")

# 如果没有提前获取access_token，可以通过API Key和Secret Key获取
# from erniebot.auth import AuthService
# auth = AuthService(access_key="你的API Key", secret_key="你的Secret Key")
# erniebot.access_token = auth.get_access_token()

def chat_with_ernie(prompt):
    """使用文心一言进行对话"""
    try:
        # 调用对话接口
        response = erniebot.ChatCompletion.create(
            model="ernie-bot",  # 模型名称，可根据需要更换
            messages=[
                {"role": "system", "content": "你是一个乐于助人的智能助手。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,  # 控制生成内容的随机性
            top_p=0.9,        # 控制候选词的多样性
            stream=False      # 是否流式返回
        )
        
        # 返回生成的结果
        return response.get_result()
    
    except Exception as e:
        print(f"调用出错: {str(e)}")
        return None

if __name__ == "__main__":
    # 示例：询问文心一言的特点
    user_input = "请介绍一下文心一言的主要特点"
    result = chat_with_ernie(user_input)
    
    if result:
        print("文心一言回复:")
        print(result)
    