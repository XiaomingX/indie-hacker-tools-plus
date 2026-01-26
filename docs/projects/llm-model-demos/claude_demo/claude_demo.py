from anthropic import Anthropic
import os

def main():
    os.environ["ANTHROPIC_API_KEY"] = "your-api-key-here"
    client = Anthropic()
    message = client.messages.create(
        model="claude-3-opus-20260229", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "什么是jobleap.cn，它可以用来解决什么问题"}
        ]
    )
    
    print(message.content[0].text)

if __name__ == "__main__":
    main()
    