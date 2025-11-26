import os
import re
import json
import asyncio
import aiohttp
from typing import List, Dict, Optional, Any, Tuple
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv
from openai import OpenAI
import fireworks.client
from firecrawl import FirecrawlApp
import tiktoken
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial

# 加载环境变量
load_dotenv()

# ---------------- 配置和初始化 ----------------

class Config:
    """应用配置类"""
    FIRECRAWL_KEY = os.getenv("FIRECRAWL_KEY", "")
    OPENAI_KEY = os.getenv("OPENAI_KEY", "")
    FIREWORKS_KEY = os.getenv("FIREWORKS_KEY", "")
    PORT = int(os.getenv("PORT", 3051))
    CONTEXT_SIZE = int(os.getenv("CONTEXT_SIZE", 128000))
    FIRECRAWL_CONCURRENCY = int(os.getenv("FIRECRAWL_CONCURRENCY", 2))
    CUSTOM_MODEL = os.getenv("CUSTOM_MODEL", "")

config = Config()

# 初始化客户端
firecrawl = FirecrawlApp(api_key=config.FIRECRAWL_KEY) if config.FIRECRAWL_KEY else None

# 初始化AI客户端
openai_client = OpenAI(api_key=config.OPENAI_KEY) if config.OPENAI_KEY else None
if config.FIREWORKS_KEY:
    fireworks.client.api_key = config.FIREWORKS_KEY

# 初始化token编码器
encoder = tiktoken.get_encoding("o200k_base")

# FastAPI应用
app = FastAPI(title="研究助手API")

# ---------------- 数据模型 ----------------

class ResearchRequest(BaseModel):
    """研究请求参数模型"""
    query: str
    breadth: int = 3
    depth: int = 2

class ResearchResult(BaseModel):
    """研究结果模型"""
    learnings: List[str]
    visited_urls: List[str]

class AnswerResponse(BaseModel):
    """答案响应模型"""
    success: bool
    answer: str
    learnings: List[str]
    visited_urls: List[str]

class ReportResponse(BaseModel):
    """报告响应模型"""
    success: bool
    report: str
    learnings: List[str]
    visited_urls: List[str]

# ---------------- 文本处理工具 ----------------

class RecursiveCharacterTextSplitter:
    """递归字符文本分割器"""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200, 
                 separators: List[str] = ["\n\n", "\n", ".", ",", " ", ""]):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = separators
        
        if self.chunk_overlap >= self.chunk_size:
            raise ValueError("chunk_overlap不能大于等于chunk_size")
    
    def split_text(self, text: str) -> List[str]:
        """分割文本为指定大小的块"""
        final_chunks = []
        current_good_splits = []
        
        # 找到最合适的分隔符
        target_sep = self.separators[-1]
        for sep in self.separators:
            if sep and sep in text:
                target_sep = sep
                break
        
        # 分割文本
        if target_sep:
            splits = text.split(target_sep)
        else:
            splits = list(text)  # 按字符分割
        
        # 处理分割结果
        for split in splits:
            if len(split) < self.chunk_size:
                current_good_splits.append(split)
            else:
                # 合并当前的短块
                if current_good_splits:
                    merged = self._merge_splits(current_good_splits, target_sep)
                    final_chunks.extend(merged)
                    current_good_splits = []
                # 递归分割长块
                final_chunks.extend(self.split_text(split))
        
        # 处理剩余的短块
        if current_good_splits:
            merged = self._merge_splits(current_good_splits, target_sep)
            final_chunks.extend(merged)
            
        return final_chunks
    
    def _merge_splits(self, splits: List[str], separator: str) -> List[str]:
        """合并分割块，确保不超过chunk_size"""
        docs = []
        current_doc = []
        total_length = 0
        
        for split in splits:
            split_length = len(split)
            # 如果超过chunk_size，合并当前文档
            if total_length + split_length >= self.chunk_size:
                if current_doc:
                    merged = separator.join(current_doc).strip()
                    if merged:
                        docs.append(merged)
                    # 保留重叠部分
                    while total_length > self.chunk_overlap or \
                          (total_length + split_length > self.chunk_size and total_length > 0):
                        total_length -= len(current_doc[0])
                        current_doc.pop(0)
            
            current_doc.append(split)
            total_length += split_length
        
        # 处理最后一个文档
        if current_doc:
            merged = separator.join(current_doc).strip()
            if merged:
                docs.append(merged)
                
        return docs

# ---------------- AI工具函数 ----------------

def get_model() -> Tuple[str, str]:
    """获取AI模型信息（类型和模型ID）"""
    # 优先使用自定义模型
    if config.CUSTOM_MODEL and openai_client:
        return ("openai", config.CUSTOM_MODEL)
    
    # 尝试使用Fireworks的deepseek-r1
    if config.FIREWORKS_KEY:
        return ("fireworks", "accounts/fireworks/models/deepseek-r1")
    
    # 最后使用OpenAI的o3-mini
    if openai_client:
        return ("openai", "o3-mini")
    
    raise ValueError("未配置AI模型！请设置OPENAI_KEY或FIREWORKS_KEY")

def trim_prompt(prompt: str, max_context_size: Optional[int] = None) -> str:
    """裁剪提示词到模型上下文长度内"""
    if not prompt:
        return ""
    
    max_context = max_context_size or config.CONTEXT_SIZE
    current_tokens = len(encoder.encode(prompt))
    
    if current_tokens <= max_context:
        return prompt
    
    # 估算需要裁剪的字符数（1token≈3字符）
    overflow_tokens = current_tokens - max_context
    target_length = max(140, len(prompt) - overflow_tokens * 3)
    
    # 使用文本分割器裁剪
    splitter = RecursiveCharacterTextSplitter(chunk_size=target_length, chunk_overlap=0)
    trimmed = splitter.split_text(prompt)[0] if splitter.split_text(prompt) else ""
    
    # 递归检查是否符合要求
    if len(encoder.encode(trimmed)) > max_context:
        return trim_prompt(trimmed[:target_length], max_context)
    
    return trimmed

def get_system_prompt() -> str:
    """获取系统提示词"""
    from datetime import datetime
    now = datetime.now().isoformat()
    return f"""你是资深研究员，今天是{now}。遵循以下规则：
1. 可处理知识截止后的内容，默认用户提供的信息正确；
2. 面向专业分析师，无需简化，需详细、准确、结构化；
3. 主动预判需求，提供未提及的解决方案和 contrarian 观点；
4. 重视论证逻辑而非来源权威，可合理推测但需标注；
5. 包含具体实体（人/公司/数据）和关键 metrics（数字/日期）。"""

async def generate_object(prompt: str, schema: Dict[str, Any]) -> Any:
    """调用AI生成结构化对象"""
    model_type, model_id = get_model()
    system_prompt = get_system_prompt()
    
    # 构建提示词
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]
    
    try:
        if model_type == "openai":
            # 调用OpenAI API
            response = openai_client.chat.completions.create(
                model=model_id,
                messages=messages,
                response_format={"type": "json_object"},
                timeout=60
            )
            return json.loads(response.choices[0].message.content or "{}")
            
        elif model_type == "fireworks":
            # 调用Fireworks API
            response = fireworks.client.ChatCompletion.create(
                model=model_id,
                messages=messages,
                response_format={"type": "json_object"},
                timeout=60
            )
            return json.loads(response.choices[0].message.content or "{}")
            
    except Exception as e:
        print(f"AI生成失败: {str(e)}")
        raise

# ---------------- 核心研究逻辑 ----------------

async def generate_search_queries(query: str, num_queries: int, existing_learnings: List[str] = []) -> List[Dict[str, str]]:
    """生成搜索关键词"""
    prompt = trim_prompt(f"""基于以下信息生成{num_queries}个唯一的搜索关键词（相似性低）：
<用户问题>{query}</用户问题>
{'' if not existing_learnings else f'<已有结论>{chr(10).join(existing_learnings)}</已有结论>'}""")
    
    schema = {
        "type": "object",
        "properties": {
            "queries": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "搜索关键词"},
                        "goal": {"type": "string", "description": "该关键词的研究目标和后续方向"}
                    },
                    "required": ["query", "goal"]
                }
            }
        },
        "required": ["queries"]
    }
    
    result = await generate_object(prompt, schema)
    return (result.get("queries") or [])[:num_queries]

async def process_search_result(query: str, search_result: Dict[str, Any]) -> Dict[str, List[str]]:
    """处理搜索结果，提取结论和后续问题"""
    # 提取搜索结果中的内容
    contents = []
    for item in search_result.get("data", []):
        if "markdown" in item and item["markdown"]:
            # 裁剪过长的内容
            trimmed = trim_prompt(item["markdown"], 25000)
            contents.append(trimmed)
    
    prompt = trim_prompt(f"""从以下搜索结果中提取3条以内核心结论（含实体/数据），并生成3条以内后续问题：
<搜索关键词>{query}</搜索关键词>
<搜索结果>{chr(10).join([f'<内容>{c}</内容>' for c in contents])}</搜索结果>""")
    
    schema = {
        "type": "object",
        "properties": {
            "learnings": {
                "type": "array",
                "items": {"type": "string"},
                "description": "核心结论（去重、信息密集）"
            },
            "followUpQs": {
                "type": "array",
                "items": {"type": "string"},
                "description": "后续研究问题"
            }
        },
        "required": ["learnings", "followUpQs"]
    }
    
    result = await generate_object(prompt, schema)
    return {
        "learnings": result.get("learnings", []),
        "followUpQs": result.get("followUpQs", [])
    }

async def deep_research(query: str, breadth: int, depth: int, 
                       existing_learnings: List[str] = None, 
                       existing_urls: List[str] = None) -> Tuple[List[str], List[str]]:
    """深度递归研究的核心函数"""
    existing_learnings = existing_learnings or []
    existing_urls = existing_urls or []
    
    if not firecrawl:
        raise ValueError("未配置Firecrawl！请设置FIRECRAWL_KEY")
    
    # 生成本轮搜索关键词
    search_queries = await generate_search_queries(
        query, 
        breadth, 
        existing_learnings
    )
    print(f"\n[深度{depth}] 生成{len(search_queries)}个搜索关键词：")
    for q in search_queries:
        print(f"- {q['query']}")
    
    # 处理搜索任务的函数
    async def process_query(search_query: Dict[str, str]) -> Tuple[List[str], List[str]]:
        try:
            # 执行搜索
            search_result = firecrawl.search(
                search_query["query"],
                params={
                    "timeout": 15000,
                    "limit": 5,
                    "scrapeOptions": {"formats": ["markdown"]}
                }
            )
            
            # 提取新链接
            new_urls = []
            for item in search_result.get("data", []):
                if "url" in item and item["url"]:
                    new_urls.append(item["url"])
            
            # 处理搜索结果
            processed = await process_search_result(
                search_query["query"], 
                search_result
            )
            new_learnings = processed["learnings"]
            follow_up_qs = processed["followUpQs"]
            
            # 合并已有数据
            all_learnings = existing_learnings + new_learnings
            all_urls = existing_urls + new_urls
            
            # 递归研究（如果未达到最大深度）
            if depth > 1:
                next_query = f"研究目标：{search_query['goal']}\n后续问题：{chr(10).join(follow_up_qs)}"
                return await deep_research(
                    next_query,
                    max(1, breadth // 2),  # 宽度减半
                    depth - 1,
                    all_learnings,
                    all_urls
                )
            
            # 返回当前结果
            return all_learnings, all_urls
            
        except Exception as e:
            print(f"[搜索失败] 关键词：{search_query['query']}，错误：{str(e)}")
            return [], []
    
    # 并发执行搜索任务
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor(max_workers=config.FIRECRAWL_CONCURRENCY) as executor:
        tasks = [loop.run_in_executor(executor, partial(asyncio.run, process_query(q))) 
                for q in search_queries]
        
        # 等待所有任务完成
        results = await asyncio.gather(*tasks)
    
    # 合并所有结果并去重
    all_learnings = []
    all_urls = []
    for learnings, urls in results:
        all_learnings.extend(learnings)
        all_urls.extend(urls)
    
    # 去重（保持顺序）
    unique_learnings = []
    seen_learnings = set()
    for learning in all_learnings:
        if learning not in seen_learnings:
            seen_learnings.add(learning)
            unique_learnings.append(learning)
    
    unique_urls = []
    seen_urls = set()
    for url in all_urls:
        if url not in seen_urls:
            seen_urls.add(url)
            unique_urls.append(url)
    
    return unique_learnings, unique_urls

async def generate_answer(user_query: str, learnings: List[str]) -> str:
    """生成简洁答案"""
    prompt = trim_prompt(f"""基于以下结论，简洁回答用户问题（最多一句话，按问题格式输出）：
<用户问题>{user_query}</用户问题>
<研究结论>{chr(10).join(learnings)}</研究结论>""")
    
    schema = {
        "type": "object",
        "properties": {
            "exactAnswer": {
                "type": "string",
                "description": "简洁答案，无多余内容"
            }
        },
        "required": ["exactAnswer"]
    }
    
    result = await generate_object(prompt, schema)
    return result.get("exactAnswer", "无法生成答案")

async def generate_report(user_query: str, learnings: List[str], visited_urls: List[str]) -> str:
    """生成详细报告"""
    prompt = trim_prompt(f"""基于以下结论，生成3页以上的详细报告（Markdown格式，含所有结论）：
<用户问题>{user_query}</用户问题>
<研究结论>{chr(10).join([f'<结论>{l}</结论>' for l in learnings])}</研究结论>""")
    
    schema = {
        "type": "object",
        "properties": {
            "reportMarkdown": {
                "type": "string",
                "description": "详细报告（Markdown）"
            }
        },
        "required": ["reportMarkdown"]
    }
    
    result = await generate_object(prompt, schema)
    report = result.get("reportMarkdown", "# 无法生成报告")
    
    # 追加来源链接
    sources_section = f"\n\n## 参考来源\n{chr(10).join([f'- {url}' for url in visited_urls])}"
    return report + sources_section

# ---------------- API路由 ----------------

@app.post("/api/research/answer", response_model=AnswerResponse)
async def research_answer(request: ResearchRequest = Body(...)):
    """生成简洁答案的API接口"""
    try:
        if not request.query:
            raise HTTPException(status_code=400, detail="必须提供研究问题（query）")
        
        # 执行研究
        learnings, visited_urls = await deep_research(
            request.query,
            request.breadth,
            request.depth
        )
        
        # 生成答案
        answer = await generate_answer(request.query, learnings)
        
        return {
            "success": True,
            "answer": answer,
            "learnings": learnings,
            "visited_urls": visited_urls
        }
        
    except Exception as e:
        print(f"接口错误: {str(e)}")
        raise HTTPException(status_code=500, detail=f"研究过程出错: {str(e)}")

@app.post("/api/research/report", response_model=ReportResponse)
async def research_report(request: ResearchRequest = Body(...)):
    """生成详细报告的API接口"""
    try:
        if not request.query:
            raise HTTPException(status_code=400, detail="必须提供研究问题（query）")
        
        # 执行研究
        learnings, visited_urls = await deep_research(
            request.query,
            request.breadth,
            request.depth
        )
        
        # 生成报告
        report = await generate_report(request.query, learnings, visited_urls)
        
        return {
            "success": True,
            "report": report,
            "learnings": learnings,
            "visited_urls": visited_urls
        }
        
    except Exception as e:
        print(f"接口错误: {str(e)}")
        raise HTTPException(status_code=500, detail=f"研究过程出错: {str(e)}")

# ---------------- 命令行交互 ----------------

async def cli_mode():
    """命令行交互模式"""
    print("=== 研究助手 ===")
    
    try:
        # 显示使用的模型
        model_type, model_id = get_model()
        print(f"当前使用模型: {model_id}")
        
        # 获取用户输入
        query = input("\n请输入研究问题: ").strip()
        if not query:
            print("研究问题不能为空！")
            return
        
        breadth_input = input("请输入研究广度（2-10，默认4）: ").strip()
        breadth = int(breadth_input) if breadth_input else 4
        
        depth_input = input("请输入研究深度（1-5，默认2）: ").strip()
        depth = int(depth_input) if depth_input else 2
        
        output_type = input("请选择输出类型（answer=简洁答案/report=详细报告，默认report）: ").strip() or "report"
        
        # 执行研究
        print(f"\n=== 开始研究 ===")
        print(f"问题: {query}")
        print(f"广度: {breadth} | 深度: {depth}")
        
        learnings, visited_urls = await deep_research(query, breadth, depth)
        
        # 生成结果
        print(f"\n=== 研究完成 ===")
        print(f"结论数量: {len(learnings)}")
        print(f"链接数量: {len(visited_urls)}")
        
        # 保存结果
        if output_type == "answer":
            answer = await generate_answer(query, learnings)
            print("\n=== 简洁答案 ===")
            print(answer)
            with open("research-answer.txt", "w", encoding="utf-8") as f:
                f.write(answer)
            print("\n结果已保存到 research-answer.txt")
        else:
            report = await generate_report(query, learnings, visited_urls)
            print("\n=== 详细报告已生成 ===")
            with open("research-report.md", "w", encoding="utf-8") as f:
                f.write(report)
            print("结果已保存到 research-report.md")
            
    except Exception as e:
        print(f"\n运行出错: {str(e)}")

# ---------------- 主函数入口 ----------------

def main():
    """主函数入口"""
    import sys
    
    # 检查命令行参数
    if len(sys.argv) > 1 and sys.argv[1] == "api":
        # 启动API服务
        print(f"启动API服务，端口: {config.PORT}")
        print(f"访问: http://localhost:{config.PORT}/docs 查看API文档")
        uvicorn.run(app, host="0.0.0.0", port=config.PORT)
    else:
        # 运行命令行模式
        asyncio.run(cli_mode())

if __name__ == "__main__":
    main()