# Please install OpenAI SDK first: `pip3 install openai`
## 文档地址：
### https://api-docs.deepseek.com/

from openai import OpenAI

from dotenv import load_dotenv
import os
load_dotenv()

def main():
    deepseek_key = os.getenv("DEEPSEEK_KEY")

    client = OpenAI(api_key=os.getenv("DEEPSEEK_KEY"), base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello"},
        ],
        stream=False
    )

    print(response.choices[0].message.content)

main()