import os
import time
import requests
import feedparser
from typing import List, Dict, Any
from pathlib import Path
from dotenv import load_dotenv
import markdown

# -------------------------- 常量配置 --------------------------
# RSS 源地址
RSS_FEED_URL = "https://mp.jobleap4u.com/rss"
# 内置基础 CSS 样式
BASIC_CSS = """
body { font-family: Arial, sans-serif; max-width: 1000px; margin: 0 auto; padding: 20px; line-height: 1.6; }
.container { border: 1px solid #eee; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
.header { background: #2c3e50; color: white; padding: 15px 20px; }
.content { padding: 20px; }
.footer { text-align: center; padding: 15px; background: #f8f9fa; border-top: 1px solid #eee; }
a { color: #3498db; text-decoration: none; }
a:hover { text-decoration: underline; }
code { background: #f0f0f0; padding: 2px 4px; border-radius: 4px; }
ul { margin: 10px 0; padding-left: 20px; }
.article-meta { color: #7f8c8d; font-size: 0.9em; margin-bottom: 10px; }
"""
# 最大文章数量限制
MAX_ARTICLE_LIMIT = 5
# 默认使用 GPT-4o-mini
DEFAULT_MODEL = "gpt-4o-mini"


# -------------------------- 核心工具函数 --------------------------
def get_rss_articles(limit: int = 5) -> List[Dict[str, Any]]:
    """从 RSS 源获取文章列表"""
    try:
        # 解析 RSS 源
        feed = feedparser.parse(RSS_FEED_URL)
        if feed.bozo:  # 检查解析错误
            print(f"⚠️ RSS 解析警告: {feed.bozo_exception}")
        
        articles = []
        # 提取需要的字段
        for entry in feed.entries[:limit]:
            article = {
                "title": entry.get("title", "无标题"),
                "link": entry.get("link", ""),
                "published": entry.get("published", "未知发布时间"),
                "summary": entry.get("summary", "无摘要内容"),
                "author": entry.get("author", "未知作者")
            }
            articles.append(article)
        
        print(f"✅ 成功获取 {len(articles)} 篇文章")
        return articles
    except Exception as e:
        print(f"❌ 获取 RSS 文章失败: {e}")
        return []


def get_article_content(url: str) -> str:
    """获取文章全文内容"""
    if not url:
        return "⚠️  该文章无链接"
    
    try:
        # 使用 Jina AI 接口解析网页内容
        resp = requests.get(f"https://r.jina.ai/{url}", timeout=10)
        resp.raise_for_status()
        return resp.text[:80000]  # 限制长度，避免 Token 超限
    except Exception as e:
        print(f"⚠️  获取文章 {url} 内容失败: {e}")
        return "⚠️  无法获取文章全文内容"


def call_llm(api_key: str, base_url: str, prompt: str) -> str:
    """调用 LLM 生成文章摘要"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": DEFAULT_MODEL,
        "messages": [
            {"role": "system", "content": "你是专业的内容摘要师，擅长提炼文章核心内容和要点"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }
    
    try:
        resp = requests.post(f"{base_url}/chat/completions", headers=headers, json=data, timeout=20)
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"❌ 调用 LLM 失败: {e}")
        return ""


def generate_article_summary(article: Dict, llm_config: Dict) -> str:
    """生成单篇文章的摘要"""
    # 获取文章全文内容
    full_content = get_article_content(article["link"])
    
    # 构造 LLM 提示词
    prompt = f"""
基于以下文章信息，生成专业摘要：
- 标题：{article['title']}
- 作者：{article['author']}
- 发布时间：{article['published']}
- 摘要：{article['summary']}
- 全文内容：{full_content}

请严格按以下格式输出（Markdown）：
### 核心要点
（300字内概括文章核心内容和主要观点）

### 关键信息
- 要点1（重要信息或数据）
- 要点2（核心观点或建议）
- 要点3（值得关注的细节）

### 总结评价
（简要评价文章价值或适用性）
"""
    
    # 调用 LLM 生成摘要
    summary = call_llm(
        api_key=llm_config["api_key"],
        base_url=llm_config["base_url"],
        prompt=prompt
    )
    
    # 格式化摘要
    return f"""
## [{article['title']}]({article['link']})
**作者**: {article['author']} | **发布时间**: {article['published']}

{summary}

---
"""


# -------------------------- 输出与邮件功能 --------------------------
def save_markdown(content: str, save_path: Path):
    """保存摘要为 Markdown 文件"""
    save_path.parent.mkdir(exist_ok=True)  # 确保文件夹存在
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Markdown 已保存至: {save_path}")


def md_to_html(md_path: Path, html_path: Path):
    """将 Markdown 转换为带样式的 HTML"""
    # 读取 Markdown 内容
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    # 转换为 HTML
    html_content = markdown.markdown(md_content, extensions=["extra", "toc"])
    
    # 嵌入样式模板
    full_html = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{md_path.stem}</title>
    <style>{BASIC_CSS}</style>
</head>
<body>
    <div class="container">
        <header class="header"><h1>{md_path.stem}</h1></header>
        <main class="content">{html_content}</main>
        <footer class="footer">JobLeap 文章摘要生成器</footer>
    </div>
</body>
</html>
    """
    
    # 保存 HTML
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"✅ HTML 已保存至: {html_path}")


def send_email(html_path: Path, subject: str):
    """发送 HTML 内容到指定邮箱"""
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    # 从环境变量获取邮件配置
    config = {
        "host": os.getenv("EMAIL_HOST"),
        "port": int(os.getenv("EMAIL_PORT", 465)),
        "user": os.getenv("EMAIL_USER"),
        "pass": os.getenv("EMAIL_PASS"),
        "sender": os.getenv("EMAIL_SENDER"),
        "receivers": os.getenv("EMAIL_RECEIVERS", "").split(",")
    }

    # 检查配置是否完整
    if not all(config.values()) or len(config["receivers"]) == 0 or "" in config["receivers"]:
        print("⚠️  邮件配置不完整，跳过发送（需设置 EMAIL_* 环境变量）")
        return

    # 读取 HTML 内容
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            mail_content = f.read()
    except Exception as e:
        print(f"❌ 读取 HTML 文件失败: {e}")
        return

    # 构造邮件
    msg = MIMEText(mail_content, "html", "utf-8")
    msg["From"] = Header(config["sender"], "utf-8")
    msg["To"] = Header(",".join(config["receivers"]), "utf-8")
    msg["Subject"] = Header(subject, "utf-8")

    # 发送邮件
    try:
        with smtplib.SMTP_SSL(config["host"], config["port"]) as smtp:
            smtp.login(config["user"], config["pass"])
            smtp.sendmail(config["sender"], config["receivers"], msg.as_string())
        print("✅ 邮件发送成功")
    except Exception as e:
        print(f"❌ 邮件发送失败: {e}")


# -------------------------- 主流程函数 --------------------------
def main():
    # 1. 加载环境变量
    load_dotenv()
    llm_config = {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "base_url": os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    }

    # 2. 检查核心配置
    if not llm_config["api_key"]:
        print("❌ 错误：未找到 OPENAI_API_KEY 环境变量，请在 .env 文件中配置")
        return

    # 3. 核心流程：生成摘要
    print("📰 开始生成 JobLeap 文章摘要...")
    date_str = time.strftime("%Y-%m-%d_%H%M%S")
    final_summary = f"# JobLeap 文章摘要 {date_str}\n> 生成时间：{time.strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n"

    # 4. 获取并处理每篇文章
    articles = get_rss_articles(limit=MAX_ARTICLE_LIMIT)
    if not articles:
        print("❌ 未获取到任何文章，流程终止")
        return

    for i, article in enumerate(articles, 1):
        print(f"\n🔍 处理第 {i}/{len(articles)} 篇文章：{article['title']}")
        # 生成单篇文章摘要
        article_summary = generate_article_summary(article, llm_config)
        if article_summary:
            final_summary += article_summary

    # 5. 保存输出文件
    md_path = Path(f"output/jobleap_summary_{date_str}.md")
    html_path = Path(f"output/jobleap_summary_{date_str}.html")
    save_markdown(final_summary, md_path)
    md_to_html(md_path, html_path)

    # 6. 发送邮件
    send_email(html_path, subject=f"JobLeap 文章摘要 {date_str}")

    print("\n🎉 流程结束！")


# -------------------------- 启动入口 --------------------------
if __name__ == "__main__":
    main()