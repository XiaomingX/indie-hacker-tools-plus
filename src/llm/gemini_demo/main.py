###
#!pip install google-cloud-aiplatform
#!pip install google-generativeai
#!pip install python-dotenv

import os
import google.generativeai as genai

# 使用API密钥进行身份验证
genai.configure(api_key="")

# 创建一个Gemini Pro模型实例
model = genai.GenerativeModel('gemini-pro')

# 定义你的问题
prompt_parts = ["你是谁"]

response = model.generate_content('What is AI?')
print(response.text)
