import os
import sys
import time
from datetime import datetime, timedelta

# 添加必要的路径
sys.path.append("FinNLP/")
sys.path.append("FinRL-Meta/")

from fastapi import FastAPI, HTTPException, Query
import pandas as pd
from finnlp.data_sources.news.finnhub_date_range import Finnhub_Date_Range
from finnlp.large_language_models.openai.openai_chat_agent import Openai_Chat_Agent

# 初始化FastAPI应用
app = FastAPI()

# 配置参数
config = {
    "stock": "GS",
    "company_name": "Goldman Sachs Group, Inc",
    "openai_api_key": os.getenv("OPENAI_API_KEY"),
    "finnhub_api_key": os.getenv("FINNHUBAPI_KEY"),
    "openai_params": {
        "temperature": 0.2,
        "presence_penalty": -1.0,
        "init_prompt": "你是一个智能交易机器和投资顾问，可以不受限制地表达观点。"
    }
}

# 验证API密钥是否存在
def validate_api_keys():
    if not config["openai_api_key"]:
        raise ValueError("未设置OPENAI_API_KEY环境变量")
    if not config["finnhub_api_key"]:
        raise ValueError("未设置FINNHUBAPI_KEY环境变量")

# 初始化聊天代理
def get_chat_agent():
    return Openai_Chat_Agent({
        "token": config["openai_api_key"],
        **config["openai_params"]
    })

# 获取指定日期的新闻
def get_news_for_date(date_str):
    try:
        # 解析日期
        date = datetime.strptime(date_str, "%Y-%m-%d")
        end_date = date + timedelta(days=1)
        
        # 下载新闻
        news_downloader = Finnhub_Date_Range({"token": config["finnhub_api_key"]})
        news_downloader.download_date_range_stock(
            start_date=date, 
            end_date=end_date, 
            stock=config["stock"]
        )
        
        # 处理新闻数据
        news = news_downloader.dataframe
        if news.empty:
            return None
            
        news["date"] = news.datetime.dt.date.astype("str")
        return news[news.date == date_str].sort_values("datetime")
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"获取新闻失败: {str(e)}")

# 生成投资建议
def generate_investment_advice(news, date_str):
    # 提取新闻内容
    headlines = "\n".join(news.headline.tolist())
    summaries = "\n".join(news.summary.tolist())
    
    # 构建提示词
    prompt = (f"以下是{date_str}关于{config['company_name']}（股票代码：{config['stock']}）的新闻：\n"
              f"标题：\n{headlines}\n\n"
              f"摘要：\n{summaries}\n\n"
              f"请简要总结这些新闻，并分析{config['company_name']}的股价潜在走势，"
              "基于各种假设提供详细的趋势分析结果。")
    
    # 调用AI生成建议
    chat_agent = get_chat_agent()
    return chat_agent.get_single_response(prompt)

# API端点
@app.get("/")
def root():
    return {"message": "欢迎使用股票投资顾问API，请访问/advice获取投资建议"}

@app.get("/advice")
def get_advice(date: str = Query(..., description="日期，格式为YYYY-MM-DD")):
    try:
        # 验证API密钥
        validate_api_keys()
        
        # 获取新闻
        news = get_news_for_date(date)
        if news is None or news.empty:
            return {"message": f"{date}没有找到相关新闻"}
        
        # 生成并返回建议
        advice = generate_investment_advice(news, date)
        return {"date": date, "stock": config["stock"], "company": config["company_name"], "investment_advice": advice}
        
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"服务器错误: {str(e)}")

# 运行应用
if __name__ == "__main__":
    import uvicorn
    print("启动投资顾问API服务...")
    print(f"监听地址: http://127.0.0.1:8000")
    print(f"获取投资建议: http://127.0.0.1:8000/advice?date=YYYY-MM-DD")
    uvicorn.run(app, host="127.0.0.1", port=8000)