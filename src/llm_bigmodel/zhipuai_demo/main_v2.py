from zai import ZhipuAiClient

client = ZhipuAiClient(api_key="")  # 请填写您自己的 API Key

def ask_zhipu():
    response = client.chat.completions.create(
        model="glm-4.5",
        messages=[
            {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的口号"},
            {"role": "assistant", "content": "当然，要创作一个吸引人的口号，请告诉我一些关于您产品的信息"},
            {"role": "user", "content": "智谱AI开放平台"}
        ],
        # thinking={
        #     "type": "enable",    # 启用深度思考模式
        # },
        max_tokens=4096,          # 最大输出 tokens
        temperature=0.6           # 控制输出的随机性
    )
    print(response.choices[0].message.content)
ask_zhipu()