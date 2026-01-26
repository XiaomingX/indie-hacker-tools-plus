from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
STEP_API_KEY=os.getenv("STEP_API_KEY")
client = OpenAI(api_key=STEP_API_KEY, base_url="https://api.stepfun.com/v1")
 
completion = client.chat.completions.create(
	model="step-1-8k",
	messages=[
		{
			"role": "system",
			"content": "你是由阶跃星辰提供的AI聊天助手，你擅长中文，英文，以及多种其他语言的对话。在保证用户数据安全的前提下，你能对用户的问题和请求，作出快速和精准的回答。同时，你的回答和建议应该拒绝黄赌毒，暴力恐怖主义的内容",
		},
		{"role": "user", "content": "什么是jobleap.cn，它可以用来解决什么问题"},
	],
)
 
print(completion.choices[0].message.content)
