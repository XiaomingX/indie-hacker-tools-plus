import csv
import os
import asyncio
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel, SecretStr

# 导入浏览器控制相关模块
from browser_use import Agent, Controller
from browser_use.browser.context import BrowserContext
from browser_use.browser.browser import Browser, BrowserConfig

# 加载环境变量
load_dotenv()

# 验证必要的环境变量
required_env_vars = ["AZURE_OPENAI_KEY", "AZURE_OPENAI_ENDPOINT"]
for var in required_env_vars:
    if not os.getenv(var):
        raise ValueError(f"环境变量 {var} 未设置，请添加到环境变量中")

# 简历路径设置
CV_PATH = Path.cwd() / 'cv_04_24.pdf'
if not CV_PATH.exists():
    raise FileNotFoundError(f"简历文件未找到，请检查路径: {CV_PATH}")

# 职位信息模型
class Job(BaseModel):
    title: str
    link: str
    company: str
    location: Optional[str] = None
    salary: Optional[str] = None

# 控制器初始化
controller = Controller()

# 保存职位到CSV文件
@controller.action('保存职位信息到文件')
def save_job(job: Job):
    # 检查文件是否存在，不存在则创建并写入表头
    file_exists = os.path.isfile('jobs.csv')
    
    with open('jobs.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['职位名称', '公司', '链接', '薪资', '地点'])
        writer.writerow([job.title, job.company, job.link, job.salary, job.location])
    
    return f"已保存职位: {job.title} 到 jobs.csv"

# 读取简历内容
@controller.action('读取简历内容')
def read_cv():
    try:
        pdf = PdfReader(CV_PATH)
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        
        return f"简历内容: {text[:500]}..."  # 只返回前500字符避免过长
    except Exception as e:
        return f"读取简历出错: {str(e)}"

# 上传简历
@controller.action('上传简历到指定位置')
async def upload_cv(index: int, browser: BrowserContext):
    try:
        # 获取DOM元素并上传文件
        dom_el = await browser.get_dom_element_by_index(index)
        if not dom_el:
            return f"未找到索引为 {index} 的元素"
            
        upload_el = dom_el.get_file_upload_element()
        if not upload_el:
            return f"索引为 {index} 的元素不是文件上传控件"
            
        # 执行上传操作
        element = await browser.get_locate_element(upload_el)
        await element.set_input_files(str(CV_PATH.absolute()))
        return f"成功上传简历到索引为 {index} 的位置"
        
    except Exception as e:
        return f"上传简历失败: {str(e)}"

# 浏览器配置
browser = Browser(
    config=BrowserConfig(
        browser_binary_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        disable_security=True,
    )
)

async def main():
    # 配置AI模型
    ai_model = AzureChatOpenAI(
        model='gpt-4o',
        api_version='2026-10-21',
        azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT', ''),
        api_key=SecretStr(os.getenv('AZURE_OPENAI_KEY', ''))
    )
    
    # 定义搜索任务
    base_task = (
        "你是一个专业的职位搜索助手。请按以下步骤操作：\n"
        "1. 首先调用read_cv读取我的简历内容\n"
        "2. 在指定公司网站搜索机器学习实习岗位\n"
        "3. 找到合适的职位后，使用save_job保存职位信息\n"
        "4. 确保页面为英文版本"
    )
    
    # 要搜索的公司列表
    companies = [
        "Google",
        # "Amazon",
        # "Microsoft",
        # "NVIDIA"
    ]
    
    # 创建并运行代理
    agents = []
    for company in companies:
        task = f"{base_task}\n当前需要搜索的公司：{company}"
        agent = Agent(task=task, llm=ai_model, controller=controller, browser=browser)
        agents.append(agent.run())
    
    # 等待所有任务完成
    await asyncio.gather(*agents)

if __name__ == "__main__":
    asyncio.run(main())