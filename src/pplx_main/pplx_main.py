from openai import OpenAI
import os

def main():
    client = OpenAI(
        base_url="https://api.perplexity.ai",
        api_key="pplx-",
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You serve as an assistant that helps me play Minecraft. I will give you my goal in the game, please break it down as a tree-structure plan to achieve this goal. The requirements of the tree-structure plan are: 1. The plan tree should be exactly of depth 2. 2. Describe each step in one line. 3. You should index the two levels like ’1.’, ’1.1.’, ’1.2.’, ’2.’, ’2.1.’, etc. 4. The sub-goals at the bottom level should be basic actions so that I can easily execute them in the game."
            ),
        },
        {
            "role": "user",
            "content": (
                "I want to build a house in Minecraft. Please break it down as a tree-structure plan to achieve this goal."
            ),
        },
    ]

    # demo chat completion without streaming
    response = client.chat.completions.create(
        # model="pplx-70b-online",
        model="mixtral-8x7b-instruct",
        messages=messages,
    )
    answer = response.choices[0].message.content
    print(answer)

if __name__ == "__main__":
  main()