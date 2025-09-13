# 导入所需模块
from openai import OpenAI  # 用于调用 OpenAI 的 API
import os  # 用于读取环境变量

# 获取 Sambanova API 的密钥
def get_api_key():
    """
    获取环境变量中的 API 密钥
    """
    return os.environ.get("SAMBANOVA_API_KEY")

# 向 Sambanova 发送查询请求
def query_sambanova(question, api_key):
    """
    使用 Sambanova 的 API 查询答案
    :param question: 用户问题
    :param api_key: Sambanova API 密钥
    :return: AI 生成的答案
    """
    # 创建 OpenAI 客户端
    client = OpenAI(
        base_url="https://api.sambanova.ai/v1/",  # Sambanova 的 API 基础 URL
        api_key=api_key,  # 使用提供的 API 密钥
    )

    # 指定使用的模型
    model = "Meta-Llama-3.1-405B-Instruct"

    # 设置提示信息
    prompt = question

    # 请求生成回答
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",  # 指定消息角色为用户
                "content": prompt,  # 用户输入的问题
            }
        ],
        stream=True,  # 启用流式响应
    )

    # 拼接响应结果
    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""  # 收集生成的内容

    return response

# 主函数
def main():
    """
    程序入口，负责获取 API 密钥并发起查询
    """
    # 获取 API 密钥
    api_key = get_api_key()
    if not api_key:
        print("请设置环境变量 SAMBANOVA_API_KEY")
        return

    # 用户问题
    question = "什么是jobleap.cn，它可以用来解决什么问题"

    # 调用查询函数并打印结果
    print("正在查询，请稍候...")
    response = query_sambanova(question, api_key)
    print("\nAI 的回答:")
    print(response)

# 程序执行入口
if __name__ == "__main__":
    main()
