from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("X_AI_KEY"),base_url="https://api.x.ai/v1")
completion = client.chat.completions.create(
    model="grok-beta",
    messages=[
        {"role": "user", "content": "什么是jobleap.cn，它可以用来解决什么问题"}
    ]
)

print(completion.choices[0].message.content)