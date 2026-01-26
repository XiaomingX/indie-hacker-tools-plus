import os
import asyncio
import requests
from enum import Enum
from dataclasses import dataclass, fields
from typing import Any, Optional, Dict, List, Literal, TypedDict, Annotated
from pydantic import BaseModel, Field
import operator

# 第三方库导入（需提前安装：pip install langchain-core langgraph tavily exa-py linkup-python langchain-community）
from langchain_core.runnables import RunnableConfig
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.constants import Send
from langgraph.graph import START, END, StateGraph
from langgraph.types import interrupt, Command
from langchain_community.retrievers import ArxivRetriever
from langchain_community.utilities.pubmed import PubMedAPIWrapper
from exa_py import Exa
from linkup import LinkupClient
from tavily import AsyncTavilyClient


# ============================== 1. 基础常量与枚举定义 ==============================
# 默认报告结构
DEFAULT_REPORT_STRUCTURE = """Use this structure to create a report on the user-provided topic:
1. Introduction (no research needed)
   - Brief overview of the topic area
2. Main Body Sections:
   - Each section focuses on a sub-topic of the user-provided topic
3. Conclusion
   - Include 1 structural element (list/table) to distill main sections
   - Concise summary of the report"""

# 搜索API枚举
class SearchAPI(Enum):
    PERPLEXITY = "perplexity"
    TAVILY = "tavily"
    EXA = "exa"
    ARXIV = "arxiv"
    PUBMED = "pubmed"
    LINKUP = "linkup"

# LLM提供商枚举（规划器/写入器通用）
class LLMProvider(Enum):
    ANTHROPIC = "anthropic"
    OPENAI = "openai"
    GROQ = "groq"


# ============================== 2. 数据模型定义（整合外部依赖） ==============================
# 报告章节模型
class Section(BaseModel):
    name: str = Field(description="章节名称")
    description: str = Field(description="章节内容概述")
    research: bool = Field(description="是否需要网页搜索")
    content: str = Field(description="章节内容（初始为空）")

# 章节列表模型
class Sections(BaseModel):
    sections: List[Section] = Field(description="报告章节列表")

# 搜索查询模型
class SearchQuery(BaseModel):
    search_query: str = Field(description="网页搜索关键词")

# 搜索查询列表模型
class Queries(BaseModel):
    queries: List[SearchQuery] = Field(description="搜索关键词列表")

# 章节质量反馈模型
class Feedback(BaseModel):
    grade: Literal["pass", "fail"] = Field(description="章节质量评级")
    follow_up_queries: List[SearchQuery] = Field(description="补充搜索关键词（fail时需填）")

# 图输入/输出状态模型
class ReportStateInput(TypedDict):
    topic: str  # 报告主题

class ReportStateOutput(TypedDict):
    final_report: str  # 最终报告

# 报告全局状态（图运行时状态）
class ReportState(TypedDict):
    topic: str
    feedback_on_report_plan: Optional[str] = None  # 章节规划的反馈
    sections: List[Section] = []  # 所有章节列表
    completed_sections: Annotated[List[Section], operator.add] = []  # 已完成的章节
    report_sections_from_research: str = ""  # 已完成章节的文本汇总（用于无搜索章节）
    final_report: str = ""  # 最终报告

# 单章节处理状态（子图状态）
class SectionState(TypedDict):
    topic: str
    section: Section  # 当前处理的章节
    search_iterations: int = 0  # 搜索迭代次数
    search_queries: List[SearchQuery] = []  # 搜索关键词列表
    source_str: str = ""  # 搜索结果文本
    report_sections_from_research: str = ""  # 已完成章节汇总（用于无搜索章节）
    completed_sections: List[Section] = []  # 已完成章节

class SectionOutputState(TypedDict):
    completed_sections: List[Section]  # 子图输出：已完成的章节


# ============================== 3. 配置类（简化逻辑） ==============================
@dataclass(kw_only=True)
class Configuration:
    """报告生成配置类"""
    report_structure: str = DEFAULT_REPORT_STRUCTURE
    number_of_queries: int = 2  # 每次迭代生成的搜索关键词数量
    max_search_depth: int = 2  # 最大搜索迭代次数
    planner_provider: LLMProvider = LLMProvider.ANTHROPIC  # 规划器LLM提供商
    planner_model: str = "claude-3-7-sonnet-latest"  # 规划器模型
    writer_provider: LLMProvider = LLMProvider.ANTHROPIC  # 写入器LLM提供商
    writer_model: str = "claude-3-5-sonnet-latest"  # 写入器模型
    search_api: SearchAPI = SearchAPI.TAVILY  # 默认搜索API
    search_api_config: Optional[Dict[str, Any]] = None  # 搜索API额外配置

    @classmethod
    def from_runnable_config(cls, config: Optional[RunnableConfig] = None) -> "Configuration":
        """从RunnableConfig生成配置（优先环境变量→配置参数）"""
        config = config or {}
        configurable = config.get("configurable", {})
        
        # 读取所有字段的配置值
        values = {}
        for field in fields(cls):
            # 优先环境变量（全大写字段名），其次是configurable参数
            env_value = os.environ.get(field.name.upper())
            config_value = configurable.get(field.name, env_value)
            if config_value is not None:
                # 处理枚举类型（如LLMProvider、SearchAPI）
                field_type = field.type
                if issubclass(field_type, Enum):
                    config_value = field_type(config_value)
                values[field.name] = config_value
        
        # 用默认值填充未配置的字段
        return cls(**values)


# ============================== 4. 工具函数（简化冗余） ==============================
def get_config_value(value: Any) -> str:
    """将枚举值转换为字符串（兼容枚举/字符串输入）"""
    return value.value if isinstance(value, Enum) else value

def get_search_params(search_api: str, search_api_config: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """过滤搜索API的有效参数（避免无效参数报错）"""
    # 各API支持的参数列表
    API_PARAMS = {
        "exa": ["max_characters", "num_results", "include_domains", "exclude_domains", "subpages"],
        "arxiv": ["load_max_docs", "get_full_documents", "load_all_available_meta"],
        "pubmed": ["top_k_results", "email", "api_key", "doc_content_chars_max"],
        "linkup": ["depth"],
        "tavily": [], "perplexity": []  # 这两个API暂不支持额外参数
    }
    if not search_api_config:
        return {}
    # 只保留当前API支持的参数
    return {k: v for k, v in search_api_config.items() if k in API_PARAMS.get(search_api, [])}

def deduplicate_and_format_sources(search_results: List[Dict], max_tokens_per_source: int = 4000) -> str:
    """去重并格式化搜索结果（统一不同API的输出格式）"""
    unique_sources = {}
    # 去重（按URL）
    for result in search_results:
        for item in result.get("results", []):
            if "url" in item and item["url"] not in unique_sources:
                unique_sources[item["url"]] = item
    
    # 格式化文本
    formatted = "搜索结果汇总：\n"
    for idx, (url, source) in enumerate(unique_sources.items(), 1):
        formatted += f"\n{'='*50}\n"
        formatted += f"来源{idx}：{source.get('title', '无标题')}\n"
        formatted += f"链接：{url}\n"
        formatted += f"内容：{source.get('content', '无内容')[:max_tokens_per_source]}...\n"
    return formatted

def format_sections(sections: List[Section]) -> str:
    """将章节列表格式化为文本（用于无搜索章节的上下文）"""
    formatted = ""
    for idx, sec in enumerate(sections, 1):
        formatted += f"\n章节{idx}：{sec.name}\n"
        formatted += f"内容：{sec.content}\n"
    return formatted


# ============================== 5. 搜索函数（整合不同API） ==============================
async def tavily_search_async(queries: List[str]) -> List[Dict]:
    """Tavily搜索（异步）"""
    client = AsyncTavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    tasks = [client.search(q, max_results=5, include_raw_content=True) for q in queries]
    return await asyncio.gather(*tasks)

def perplexity_search(queries: List[str]) -> List[Dict]:
    """Perplexity搜索（同步）"""
    headers = {
        "Authorization": f"Bearer {os.getenv('PERPLEXITY_API_KEY')}",
        "Content-Type": "application/json"
    }
    results = []
    for q in queries:
        payload = {
            "model": "sonar-pro",
            "messages": [{"role": "user", "content": q}]
        }
        resp = requests.post("https://api.perplexity.ai/chat/completions", json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()
        # 格式化输出（对齐Tavily格式）
        results.append({
            "query": q,
            "results": [{"title": "Perplexity结果", "url": "https://perplexity.ai", "content": data["choices"][0]["message"]["content"]}]
        })
    return results

async def exa_search(queries: List[str], **params) -> List[Dict]:
    """Exa搜索（异步）"""
    client = Exa(api_key=os.getenv("EXA_API_KEY"))
    results = []
    for q in queries:
        resp = await asyncio.get_event_loop().run_in_executor(
            None, lambda: client.search_and_contents(q, **params)
        )
        # 格式化输出
        results.append({
            "query": q,
            "results": [{"title": r.title, "url": r.url, "content": r.summary} for r in resp.results]
        })
    return results

async def arxiv_search_async(queries: List[str], **params) -> List[Dict]:
    """ArXiv搜索（异步）"""
    results = []
    for q in queries:
        retriever = ArxivRetriever(**params)
        docs = await asyncio.get_event_loop().run_in_executor(None, lambda: retriever.invoke(q))
        # 格式化输出
        results.append({
            "query": q,
            "results": [{"title": d.metadata["Title"], "url": d.metadata["entry_id"], "content": d.page_content} for d in docs]
        })
    return results

async def pubmed_search_async(queries: List[str], **params) -> List[Dict]:
    """PubMed搜索（异步）"""
    results = []
    for q in queries:
        wrapper = PubMedAPIWrapper(**params)
        docs = await asyncio.get_event_loop().run_in_executor(None, lambda: list(wrapper.lazy_load(q)))
        # 格式化输出
        results.append({
            "query": q,
            "results": [{"title": d["Title"], "url": f"https://pubmed.ncbi.nlm.nih.gov/{d['uid']}/", "content": d["Summary"]} for d in docs]
        })
    return results

async def linkup_search(queries: List[str], **params) -> List[Dict]:
    """Linkup搜索（异步）"""
    client = LinkupClient(api_key=os.getenv("LINKUP_API_KEY"))
    tasks = [client.async_search(q, **params) for q in queries]
    resp_list = await asyncio.gather(*tasks)
    # 格式化输出
    results = []
    for q, resp in zip(queries, resp_list):
        results.append({
            "query": q,
            "results": [{"title": r.name, "url": r.url, "content": r.content} for r in resp.results]
        })
    return results

async def select_and_execute_search(search_api: str, queries: List[str], params: Dict) -> str:
    """根据配置选择并执行搜索，返回格式化结果"""
    search_api = search_api.lower()
    # 映射API与搜索函数
    API_FUNC = {
        "tavily": tavily_search_async,
        "perplexity": perplexity_search,
        "exa": exa_search,
        "arxiv": arxiv_search_async,
        "pubmed": pubmed_search_async,
        "linkup": linkup_search
    }
    if search_api not in API_FUNC:
        raise ValueError(f"不支持的搜索API：{search_api}")
    
    # 执行搜索并格式化结果
    search_results = await API_FUNC[search_api](queries, **params)
    return deduplicate_and_format_sources(search_results)


# ============================== 6. 核心提示词（整合外部依赖） ==============================
class Prompts:
    """提示词统一管理（避免分散）"""
    # 规划器-生成搜索关键词
    report_planner_query = """基于报告主题和结构，生成{number_of_queries}个搜索关键词，用于规划章节。
    报告主题：{topic}
    报告结构：{report_organization}
    要求：关键词需覆盖章节规划所需的核心信息，避免重复。"""

    # 规划器-生成章节列表
    report_planner = """基于主题、结构和搜索结果，生成报告章节列表。
    报告主题：{topic}
    报告结构：{report_organization}
    搜索结果：{context}
    反馈（可选）：{feedback}
    要求：每个章节需包含name（名称）、description（概述）、research（是否需搜索）、content（留空）。"""

    # 写入器-生成章节搜索关键词
    query_writer = """为章节生成{number_of_queries}个搜索关键词，用于补充章节内容。
    报告主题：{topic}
    章节概述：{section_topic}
    要求：关键词需聚焦章节核心内容，覆盖信息缺口。"""

    # 写入器-有搜索的章节内容
    section_writer = """基于搜索结果撰写章节，严格遵循以下要求：
    1. 字数150-200字，用## 章节名 作为标题
    2. 每段2-3句，所有观点需来自搜索结果
    3. 结尾用### 来源 列出引用的URL（按顺序编号）
    报告主题：{topic}
    章节名：{section_name}
    章节概述：{section_topic}
    已有内容（可选）：{section_content}
    搜索结果：{context}"""

    # 写入器-无搜索的章节内容（如引言、结论）
    final_section_writer = """基于已完成章节撰写无搜索章节，严格遵循要求：
    引言要求：# 报告标题，50-100字，无结构元素，无来源
    结论要求：## 结论，100-150字，1个结构元素（列表/表格），无来源
    报告主题：{topic}
    章节名：{section_name}
    章节概述：{section_topic}
    已完成章节：{context}"""

    # 评估器-章节质量评分
    section_grader = """评估章节是否满足需求，输出评分和补充关键词。
    报告主题：{topic}
    章节概述：{section_topic}
    章节内容：{section}
    要求：评分pass/fail；fail时需生成{number_of_queries}个补充搜索关键词。"""


# ============================== 7. 图节点函数（简化逻辑） ==============================
async def generate_report_plan(state: ReportState, config: RunnableConfig) -> Dict:
    """节点1：生成报告章节规划（含搜索辅助）"""
    # 1. 读取配置和状态
    cfg = Configuration.from_runnable_config(config)
    topic = state["topic"]
    feedback = state.get("feedback_on_report_plan", "")
    search_api = get_config_value(cfg.search_api)
    search_params = get_search_params(search_api, cfg.search_api_config)

    # 2. 生成规划用的搜索关键词
    writer_llm = init_chat_model(
        model=cfg.writer_model,
        model_provider=get_config_value(cfg.writer_provider),
        temperature=0
    ).with_structured_output(Queries)
    query_prompt = Prompts.report_planner_query.format(
        number_of_queries=cfg.number_of_queries,
        topic=topic,
        report_organization=cfg.report_structure
    )
    queries = await writer_llm.ainvoke([SystemMessage(content=query_prompt), HumanMessage(content="生成搜索关键词")])
    query_list = [q.search_query for q in queries.queries]

    # 3. 执行搜索获取规划上下文
    source_str = await select_and_execute_search(search_api, query_list, search_params)

    # 4. 生成章节规划
    planner_llm = init_chat_model(
        model=cfg.planner_model,
        model_provider=get_config_value(cfg.planner_provider),
        max_tokens=20000,
        thinking={"type": "enabled", "budget_tokens": 16000} if cfg.planner_model == "claude-3-7-sonnet-latest" else {}
    ).with_structured_output(Sections)
    plan_prompt = Prompts.report_planner.format(
        topic=topic,
        report_organization=cfg.report_structure,
        context=source_str,
        feedback=feedback
    )
    sections = await planner_llm.ainvoke([SystemMessage(content=plan_prompt), HumanMessage(content="生成章节列表")])

    return {"sections": sections.sections}

def human_feedback(state: ReportState, config: RunnableConfig) -> Command:
    """节点2：人工反馈（中断图运行，获取用户对章节规划的确认）"""
    # 1. 格式化当前章节规划
    sections = state["sections"]
    sections_str = "\n".join([f"- {s.name}（需搜索：{s.research}）\n  概述：{s.description}" for s in sections])
    prompt = f"报告主题：{state['topic']}\n当前章节规划：\n{sections_str}\n\n请确认：输入'true'批准规划，或输入反馈内容重新生成"

    # 2. 中断获取反馈
    feedback = interrupt(prompt)

    # 3. 路由逻辑：批准→开始写章节；反馈→重新规划
    if feedback is True:
        # 对需要搜索的章节，并行启动子图
        return Command(goto=[
            Send("build_section_with_web_research", {"topic": state["topic"], "section": s, "search_iterations": 0}) 
            for s in sections if s.research
        ])
    elif isinstance(feedback, str):
        return Command(goto="generate_report_plan", update={"feedback_on_report_plan": feedback})
    else:
        raise TypeError(f"不支持的反馈类型：{type(feedback)}")

async def generate_queries(state: SectionState, config: RunnableConfig) -> Dict:
    """子图节点1：为单章节生成搜索关键词"""
    cfg = Configuration.from_runnable_config(config)
    # 生成关键词
    writer_llm = init_chat_model(
        model=cfg.writer_model,
        model_provider=get_config_value(cfg.writer_provider),
        temperature=0
    ).with_structured_output(Queries)
    prompt = Prompts.query_writer.format(
        number_of_queries=cfg.number_of_queries,
        topic=state["topic"],
        section_topic=state["section"].description
    )
    queries = await writer_llm.ainvoke([SystemMessage(content=prompt), HumanMessage(content="生成章节搜索关键词")])
    return {"search_queries": queries.queries}

async def search_web(state: SectionState, config: RunnableConfig) -> Dict:
    """子图节点2：执行单章节的搜索"""
    cfg = Configuration.from_runnable_config(config)
    # 执行搜索
    search_api = get_config_value(cfg.search_api)
    search_params = get_search_params(search_api, cfg.search_api_config)
    query_list = [q.search_query for q in state["search_queries"]]
    source_str = await select_and_execute_search(search_api, query_list, search_params)
    # 更新搜索迭代次数
    return {"source_str": source_str, "search_iterations": state["search_iterations"] + 1}

async def write_section(state: SectionState, config: RunnableConfig) -> Command:
    """子图节点3：撰写单章节+质量评估（决定是否继续搜索）"""
    cfg = Configuration.from_runnable_config(config)
    section = state["section"]
    topic = state["topic"]

    # 1. 撰写章节内容
    writer_llm = init_chat_model(
        model=cfg.writer_model,
        model_provider=get_config_value(cfg.writer_provider),
        temperature=0
    )
    write_prompt = Prompts.section_writer.format(
        topic=topic,
        section_name=section.name,
        section_topic=section.description,
        section_content=section.content,
        context=state["source_str"]
    )
    content = await writer_llm.ainvoke([SystemMessage(content=write_prompt), HumanMessage(content="撰写章节内容")])
    section.content = content.content

    # 2. 评估章节质量
    grader_llm = init_chat_model(
        model=cfg.planner_model,
        model_provider=get_config_value(cfg.planner_provider),
        max_tokens=20000,
        thinking={"type": "enabled", "budget_tokens": 16000} if cfg.planner_model == "claude-3-7-sonnet-latest" else {}
    ).with_structured_output(Feedback)
    grade_prompt = Prompts.section_grader.format(
        topic=topic,
        section_topic=section.description,
        section=section.content,
        number_of_queries=cfg.number_of_queries
    )
    feedback = await grader_llm.ainvoke([SystemMessage(content=grade_prompt), HumanMessage(content="评估章节质量")])

    # 3. 路由逻辑：pass/达到最大深度→完成；fail→继续搜索
    if feedback.grade == "pass" or state["search_iterations"] >= cfg.max_search_depth:
        return Command(update={"completed_sections": [section]}, goto=END)
    else:
        return Command(update={"search_queries": feedback.follow_up_queries, "section": section}, goto="search_web")

async def write_final_sections(state: SectionState, config: RunnableConfig) -> Dict:
    """节点3：撰写无搜索章节（引言/结论）"""
    cfg = Configuration.from_runnable_config(config)
    section = state["section"]
    # 撰写内容
    writer_llm = init_chat_model(
        model=cfg.writer_model,
        model_provider=get_config_value(cfg.writer_provider),
        temperature=0
    )
    prompt = Prompts.final_section_writer.format(
        topic=state["topic"],
        section_name=section.name,
        section_topic=section.description,
        context=state["report_sections_from_research"]
    )
    content = await writer_llm.ainvoke([SystemMessage(content=prompt), HumanMessage(content="撰写无搜索章节")])
    section.content = content.content
    return {"completed_sections": [section]}

def gather_completed_sections(state: ReportState) -> Dict:
    """节点4：汇总已完成的有搜索章节（用于无搜索章节的上下文）"""
    return {"report_sections_from_research": format_sections(state["completed_sections"])}

def initiate_final_section_writing(state: ReportState) -> List[Send]:
    """节点5：触发无搜索章节的并行撰写"""
    # 筛选无需搜索的章节
    no_research_sections = [s for s in state["sections"] if not s.research]
    # 并行启动撰写
    return [
        Send("write_final_sections", {
            "topic": state["topic"],
            "section": s,
            "report_sections_from_research": state["report_sections_from_research"]
        }) for s in no_research_sections
    ]

def compile_final_report(state: ReportState) -> Dict:
    """节点6：整合所有章节为最终报告"""
    # 按原规划顺序整合内容
    completed = {s.name: s.content for s in state["completed_sections"]}
    final_content = "\n\n".join([completed[s.name] for s in state["sections"]])
    return {"final_report": final_content}


# ============================== 8. 图构建与端到端运行 ==============================
def build_report_graph():
    """构建报告生成的状态图（含子图）"""
    # 1. 构建子图：单章节处理（搜索→撰写→评估）
    section_subgraph = StateGraph(SectionState, output=SectionOutputState)
    section_subgraph.add_node("generate_queries", generate_queries)
    section_subgraph.add_node("search_web", search_web)
    section_subgraph.add_node("write_section", write_section)
    # 子图 edges
    section_subgraph.add_edge(START, "generate_queries")
    section_subgraph.add_edge("generate_queries", "search_web")
    section_subgraph.add_edge("search_web", "write_section")

    # 2. 构建主图：全局报告流程
    main_graph = StateGraph(ReportState, input=ReportStateInput, output=ReportStateOutput)
    # 添加主图节点
    main_graph.add_node("generate_report_plan", generate_report_plan)
    main_graph.add_node("human_feedback", human_feedback)
    main_graph.add_node("build_section_with_web_research", section_subgraph.compile())
    main_graph.add_node("gather_completed_sections", gather_completed_sections)
    main_graph.add_node("write_final_sections", write_final_sections)
    main_graph.add_node("compile_final_report", compile_final_report)
    # 主图 edges
    main_graph.add_edge(START, "generate_report_plan")
    main_graph.add_edge("generate_report_plan", "human_feedback")
    main_graph.add_edge("build_section_with_web_research", "gather_completed_sections")
    main_graph.add_conditional_edges("gather_completed_sections", initiate_final_section_writing, ["write_final_sections"])
    main_graph.add_edge("write_final_sections", "compile_final_report")
    main_graph.add_edge("compile_final_report", END)

    return main_graph.compile()

async def run_report_generator(topic: str, config: Optional[Configuration] = None):
    """端到端运行报告生成器"""
    # 1. 初始化配置
    config = config or Configuration()
    run_config = {"configurable": config.__dict__}

    # 2. 构建图
    graph = build_report_graph()

    # 3. 运行图（输入报告主题，等待人工反馈后自动完成）
    print(f"开始生成报告：{topic}\n")
    result = await graph.ainvoke(
        input={"topic": topic},
        config=run_config
    )

    # 4. 输出结果
    print("\n" + "="*60)
    print("最终报告：")
    print("="*60)
    print(result["final_report"])
    return result["final_report"]


# ============================== 9. 运行示例（需配置环境变量） ==============================
if __name__ == "__main__":
    # 1. 配置环境变量（需替换为自己的API密钥）
    os.environ["TAVILY_API_KEY"] = "your_tavily_api_key"  # 默认用TAVILY搜索
    os.environ["ANTHROPIC_API_KEY"] = "your_anthropic_api_key"  # 默认用Anthropic LLM

    # 2. 定义报告主题
    report_topic = "大语言模型在教育领域的应用现状与挑战"

    # 3. 运行报告生成器
    asyncio.run(run_report_generator(report_topic))