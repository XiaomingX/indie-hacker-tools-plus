import os
import random
import tweepy
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime

# 加载环境变量
load_dotenv()

# 初始化API客户端
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
twitter_client = tweepy.Client(
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

def generate_prompt():
    """生成随机的推文提示词"""
    categories = ['tech', 'life_wisdom']
    category = random.choice(categories)
    
    if category == 'tech':
        return "生成一条第一人称的科技类推文，分享编程、技术学习中的经验或思考，语气轻松亲切，能引发讨论"
    else:  # life_wisdom
        return "生成一条关于生活感悟的推文，针对日常关系或个人成长，语气直接坦率，不使用话题标签，引发共鸣"

def generate_tweet(prompt):
    """根据提示词调用OpenAI生成推文内容"""
    try:
        response = openai_client.chat.completions.create(
            messages=[
                {"role": "system", "content": "你是一个擅长写推文的助手，内容简洁有力"},
                {"role": "user", "content": prompt}
            ],
            model="gpt-4o-mini",
            max_tokens=280,
            temperature=0.2
        )
        
        # 去除可能的首尾引号
        tweet = response.choices[0].message.content.strip()
        if tweet.startswith('"') and tweet.endswith('"'):
            tweet = tweet[1:-1]
        return tweet
    except Exception as e:
        print(f"生成推文出错: {e}")
        return None

def post_tweet(content):
    """发布推文到Twitter"""
    if not content:
        print("推文内容为空，不发布")
        return
        
    try:
        twitter_client.create_tweet(text=content)
        print("推文发布成功!")
    except tweepy.errors.TooManyRequests as e:
        if hasattr(e, 'response') and 'x-rate-limit-reset' in e.response.headers:
            reset_time = datetime.fromtimestamp(int(e.response.headers['x-rate-limit-reset']))
            wait_time = (reset_time - datetime.now()).total_seconds()
            print(f"触发限流，将在 {wait_time:.0f} 秒后重试")
        else:
            print("触发限流，具体重试时间未知")
    except Exception as e:
        print(f"发布推文出错: {e}")

if __name__ == "__main__":
    # 完整流程：生成提示词 -> 生成推文 -> 发布推文
    prompt = generate_prompt()
    print(f"使用提示词: {prompt}")
    
    tweet_content = generate_tweet(prompt)
    if tweet_content:
        print(f"生成的推文: {tweet_content}")
        post_tweet(tweet_content)
    else:
        print("未能生成有效的推文内容")