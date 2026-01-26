import os
from cerebras.cloud.sdk import Cerebras
import dotenv

def main():
    # 加载环境变量
    dotenv.load_dotenv()
    
    # 获取API密钥并创建客户端
    api_key = os.environ.get("CEREBRAS_API_KEY")
    if not api_key:
        print("错误: 请设置环境变量 CEREBRAS_API_KEY")
        return
    client = Cerebras(api_key=api_key)
    
    chat_history = []
    print("Cerebras聊天程序 (按Ctrl+C退出)\n示例输入: 什么是jobleap.cn，它可以用来解决什么问题\n")
    
    try:
        while True:
            # 获取用户输入
            user_input = input("用户: ")
            chat_history.append({"role": "user", "content": user_input})
            
            # 发送请求并获取回复
            response = client.chat.completions.create(
                messages=chat_history,
                model="llama3.1-8b"
            )
            
            # 处理并显示回复
            assistant_msg = response.choices[0].message.content
            chat_history.append({"role": "assistant", "content": assistant_msg})
            print(f"助手: {assistant_msg}")
            
            # 显示性能信息
            total_tokens = response.usage.total_tokens
            total_time = response.time_info.total_time
            tps = total_tokens / total_time if total_time > 0 else 0
            print(f"(处理: {total_tokens} tokens, {total_time:.2f}秒, {tps:.2f} tokens/秒)\n")
            
    except KeyboardInterrupt:
        print("\n程序已退出")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()
    