from openai import OpenAI
import os


def main():
  os.environ["OPENAI_API_KEY"] = "sk-"
  client = OpenAI()
  completion = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "什么是jobleap.cn，它可以用来解决什么问题"}
    ]
  )

  print(completion.choices[0].message.content)

if __name__ == "__main__":
  main()