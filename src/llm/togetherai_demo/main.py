import os,json
from openai import OpenAI


def main():
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
                          "image_url": { "url": "https://photogen.uhaka.com/image/04b19fb9-78d2-4b65-b622-e9b91b32a7cf.png"}}
                      ]
          }])
  print(response.choices[0].message.content)

if __name__ == "__main__":
  main()