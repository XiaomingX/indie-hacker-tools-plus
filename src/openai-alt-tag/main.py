import os, json
from openai import OpenAI

together = OpenAI(api_key=os.environ.get('TOGETHER_API_KEY'),
                  base_url="https://api.together.xyz/v1")

response = together.chat.completions.create(
    model="meta-llama/Llama-Vision-Free",
    messages=[
        {"role": "user",
         "content": [
             {"type": "text",
              "text": "Describe the image"},
             {"type": "image_url",
              "image_url": { "url": "https://res.cloudinary.com/dlxdbsdqx/image/upload/e_enhance/e_sharpen/q_auto:best/eayorcxnwuzwyepktgns.png"}}
         ]}
    ])

print(response.choices[0].message.content)