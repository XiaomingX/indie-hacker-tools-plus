# -*- encoding: utf-8 -*-

"""
rss_robot.py

检查指定RSS源更新并通过钉钉机器人推送新文章
"""
import os
import feedparser
from dingtalkchatbot.chatbot import DingtalkChatbot, CardItem

class RSSUpdater:
    def __init__(self):
        # RSS源地址
        self.rss_url = "https://mp.jobleap4u.com/rss"
        
        # 存储已发送文章URL的文件
        self.history_file = "sent_articles.txt"
        
        # 初始化钉钉机器人
        self.robot = DingtalkChatbot(
            os.environ.get("DD_WEBHOOK"),
            pc_slide=True, 
            secret=os.environ.get("DD_SECRET")
        )
        
        # 加载已发送的文章URL
        self.load_sent_urls()
    
    def load_sent_urls(self):
        """从文件加载已发送的文章URL"""
        try:
            with open(self.history_file, "r", encoding="utf-8") as f:
                self.sent_urls = set(line.strip() for line in f.readlines())
        except FileNotFoundError:
            self.sent_urls = set()
    
    def save_sent_urls(self):
        """将已发送的文章URL保存到文件"""
        with open(self.history_file, "w", encoding="utf-8") as f:
            for url in self.sent_urls:
                f.write(f"{url}\n")
    
    def get_new_articles(self):
        """获取RSS源中的新文章"""
        feed = feedparser.parse(self.rss_url)
        new_articles = []
        
        # 遍历文章条目，筛选出新文章
        for entry in feed.entries:
            if entry.link not in self.sent_urls:
                new_articles.append(entry)
        
        return new_articles
    
    def send_to_dingtalk(self, articles):
        """将新文章通过钉钉机器人发送"""
        if not articles:
            print("没有新文章需要发送")
            return
        
        # 创建卡片列表
        card_items = []
        for article in articles:
            card = CardItem(
                title=article.title,
                url=article.link,
                pic_url="https://picsum.photos/200/300?random=1"  # 替换为合适的图片
            )
            card_items.append(card)
        
        # 发送卡片消息
        self.robot.send_feed_card(card_items)
        
        # 更新已发送记录
        for article in articles:
            self.sent_urls.add(article.link)
        self.save_sent_urls()
        
        print(f"成功发送 {len(articles)} 篇新文章到钉钉")

def check_and_send():
    updater = RSSUpdater()
    new_articles = updater.get_new_articles()
    updater.send_to_dingtalk(new_articles)

if __name__ == '__main__':
    check_and_send()