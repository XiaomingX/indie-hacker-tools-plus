# 导入必要模块
import os
from cerebras.cloud.sdk import Cerebras
import dotenv

def load_env_variables():
    """
    加载环境变量。
    """
    dotenv.load_dotenv()

def create_cerebras_client():
    """
    创建 Cerebras 客户端实例。
    """
    api_key = os.environ.get("CEREBRAS_API_KEY")
    if not api_key:
        raise ValueError("环境变量 CEREBRAS_API_KEY 未设置")
    return Cerebras(api_key=api_key)

def process_chat(client, chat_history):
    """
    与用户进行聊天交互，并处理对话逻辑。
    """
    while True:
        # 获取用户输入
        user_input = input("用户: ")
        user_message = {"role": "user", "content": user_input}
        
        # 将用户输入添加到对话历史记录中
        chat_history.append(user_message)
        
        # 向 Cerebras 发送请求
        response = client.chat.completions.create(
            messages=chat_history,  # 使用完整的历史记录来生成回复
            model="llama3.1-8b",
        )
        
        # 获取助手回复并更新对话历史记录
        assistant_message = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": assistant_message})
        
        # 打印助手回复
        print("助手:", assistant_message)
        
        # 显示性能统计信息
        display_performance_stats(response)

def display_performance_stats(response):
    """
    显示性能统计信息：处理的总标记数、耗时以及每秒处理的标记数。
    """
    total_tokens = response.usage.total_tokens
    total_time = response.time_info.total_time
    tokens_per_second = total_tokens / total_time if total_time > 0 else 0
    print(f"(每秒处理的标记数: {tokens_per_second:.2f})\n")

def main():
    """
    主函数，用于启动程序。
    """
    try:
        # 加载环境变量
        load_env_variables()
        client = create_cerebras_client()
        chat_history = []
        process_chat(client, chat_history)
    except KeyboardInterrupt:
        print("\n程序已退出。")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()
