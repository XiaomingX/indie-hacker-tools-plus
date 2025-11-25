# 导入模块（按「标准库→第三方库」分组，去重整理）
import json
import os
import re
import time
import pickle
from typing import List
from datetime import date, timedelta, datetime
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import markdown
from openai import OpenAI
from scholarly import scholarly
import arxiv
from metapub import PubMedFetcher
from Bio import Entrez
from cozepy import Coze, TokenAuth, Message, ChatEventType, COZE_CN_BASE_URL


class ScholarDaily:
    def __init__(self, json_path='scholar_daily_config.json'):
        """初始化：加载配置、设置默认日期、初始化存储变量"""
        self.json_path = json_path
        self.configs = {}  # 存储配置（关键词、数据源、API密钥等）
        self.date = date.today() - timedelta(days=1)  # 默认查询「昨天」的文献
        self.source_results = {}  # 按数据源存储原始结果（如{'Arxiv': [...]}）
        self.All_result = []  # 所有数据源的合并结果
        self.All_result_dict = {}  # 按标题分组的文献（去重后用）
        self.topic_dict = {}  # LLM聚类后的主题-文献映射
        self.News = ""  # 存储获取的AI新闻

        # 【修正拼写错误】数据源与搜索函数的映射（关键：确保函数名与数据源匹配）
        self.function_mapping = {
            'bioRxiv': self.search_bioRxiv,
            'Arxiv': self.search_Arxiv,
            'PubMed': self.search_PubMed,
            'GoogleScholar': self.search_GoogleScholar
        }

        # 自动加载配置（避免用户忘记调用）
        self.load_configs()
        # 检查必要配置项（防止后续报错）
        self._check_essential_configs()

    # ------------------------------
    # 1. 配置相关方法（加载、保存、检查）
    # ------------------------------
    def load_configs(self):
        """加载配置文件，若不存在则创建默认配置"""
        if os.path.exists(self.json_path):
            with open(self.json_path, 'r', encoding='utf-8') as f:
                self.configs = json.load(f)
        else:
            # 生成默认配置（方便用户直接使用）
            default_config = {
                "Keywords": ["artificial intelligence", "machine learning"],  # 默认关键词
                "Sources": ["Arxiv", "PubMed"],  # 默认数据源（避免Google Scholar代理问题）
                "max_num_per_source": 5,  # 每个数据源最多获取5篇
                "DASHSCOPE_API_KEY": "your_dashscope_key_here",  # 通义千问API密钥（需用户替换）
                "log_path": "./scholar_logs"  # 日志存储路径
            }
            # 创建配置文件
            with open(self.json_path, 'w', encoding='utf-8') as f:
                json.dump(default_config, f, ensure_ascii=False, indent=4)
            self.configs = default_config
            print(f"配置文件不存在，已创建默认配置：{self.json_path}")
            print("提示：请修改配置文件中的 DASHSCOPE_API_KEY 和关键词（Keywords）")

    def _check_essential_configs(self):
        """检查必要配置项是否存在，缺失则提示"""
        essential_items = ["Keywords", "Sources", "max_num_per_source", "DASHSCOPE_API_KEY"]
        missing = [item for item in essential_items if item not in self.configs]
        if missing:
            raise ValueError(f"配置文件缺失必要项：{', '.join(missing)}，请补充 {self.json_path}")

    def set_keywords(self, keywords: List[str]):
        """更新关键词并保存到配置文件"""
        self.configs["Keywords"] = keywords
        self._save_configs()
        print(f"已更新关键词：{keywords}")

    def set_sources(self, sources: List[str]):
        """更新数据源并保存到配置文件（需在function_mapping中存在）"""
        valid_sources = list(self.function_mapping.keys())
        invalid = [s for s in sources if s not in valid_sources]
        if invalid:
            print(f"无效数据源：{invalid}，可选数据源：{valid_sources}")
            return
        self.configs["Sources"] = sources
        self._save_configs()
        print(f"已更新数据源：{sources}")

    def _save_configs(self):
        """内部方法：保存配置（避免重复代码）"""
        with open(self.json_path, 'w', encoding='utf-8') as f:
            json.dump(self.configs, f, ensure_ascii=False, indent=4)

    # ------------------------------
    # 2. 文献搜索方法（按数据源分别实现）
    # ------------------------------
    def search_GoogleScholar(self):
        """搜索Google Scholar（国内需代理，注意反爬）"""
        print("⚠️  提示：Google Scholar国内需代理，且易触发反爬（建议最后使用）")
        keywords = self.configs["Keywords"]
        max_num = self.configs["max_num_per_source"]
        query = " OR ".join([f'"{key}"' for key in keywords])
        filtered = []

        try:
            # 按日期排序搜索（修正原代码无效参数 include_last_year）
            results = scholarly.search_pubs(query, sort_by="date")
            for res in results:
                # 提取「几天前」的发布时间（原代码逻辑保留）
                abstract = res.get("bib", {}).get("abstract", "")
                match = re.search(r'(\d+)\s+days\s+ago', abstract)
                if not match:
                    continue

                days_ago = int(match.group(1))
                if days_ago <= (date.today() - self.date).days:
                    # 补全文献详情（需休眠避免反爬）
                    time.sleep(2)
                    pub = scholarly.search_single_pub(res["bib"]["title"], filled=True)
                    filtered.append({
                        "Title": pub["bib"].get("title", "Unknown"),
                        "Authors": pub["bib"].get("author", ["Unknown"]),
                        "Link": pub.get("pub_url", "No Link"),
                        "Summary": pub["bib"].get("abstract", "No Abstract"),
                        "Source": pub["bib"].get("journal", "Google Scholar")
                    })

                # 达到最大数量则停止
                if len(filtered) >= max_num:
                    break

        except Exception as e:
            print(f"Google Scholar搜索失败：{str(e)}")

        print(f"Google Scholar 找到 {len(filtered)} 篇文献")
        self.source_results["GoogleScholar"] = filtered
        self.All_result.extend(filtered)

    def search_Arxiv(self):
        """搜索Arxiv（按提交日期筛选）"""
        keywords = self.configs["Keywords"]
        max_num = self.configs["max_num_per_source"]
        query = " OR ".join([f"all:{key}" for key in keywords])
        filtered = []

        try:
            # 初始化Arxiv客户端，按提交日期排序
            client = arxiv.Client()
            search = arxiv.Search(
                query=query,
                max_results=max_num,
                sort_by=arxiv.SortCriterion.SubmittedDate
            )

            # 筛选目标日期的文献（原代码逻辑保留）
            for res in tqdm(client.results(search), desc="Arxiv搜索中"):
                if res.updated.date() == self.date:
                    filtered.append({
                        "Title": res.title,
                        "Summary": res.summary,
                        "Authors": [str(auth) for auth in res.authors],
                        "Link": str(res.links[0]),
                        "Source": "Arxiv"
                    })
                else:
                    break  # 按日期排序，早于目标日期则后续无需处理

        except Exception as e:
            print(f"Arxiv搜索失败：{str(e)}")

        print(f"Arxiv 找到 {len(filtered)} 篇文献")
        self.source_results["Arxiv"] = filtered
        self.All_result.extend(filtered)

    def search_bioRxiv(self):
        """搜索bioRxiv（预印本平台，需解析HTML和API）"""
        keywords = self.configs["Keywords"]
        max_num = self.configs["max_num_per_source"]
        query = quote(f"abstract_title:{' OR '.join([f'"{key}"' for key in keywords])}")
        filtered = []

        # 构建搜索URL
        base_url = "https://www.biorxiv.org/search/"
        search_url = f"{base_url}{query}%20abstract_title_flags%3Amatch-phrase%20numresults%3A{max_num}%20sort%3Apublication-date%20direction%3Adescending"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0"}

        try:
            # 第一步：获取文献DOI链接
            response = requests.get(search_url, headers=headers)
            response.raise_for_status()  # 触发HTTP错误（如404、500）
            soup = BeautifulSoup(response.text, "html.parser")
            results = soup.find_all("li", class_="search-result", limit=max_num)
            dois = []
            for res in results:
                doi_span = res.find("span", class_="highwire-cite-metadata-doi")
                if doi_span:
                    dois.append(doi_span.get_text().split("doi:")[-1].strip())

            # 第二步：通过API获取文献详情和日期
            for doi in tqdm(dois, desc="bioRxiv详情获取"):
                time.sleep(2)  # 避免API限流
                api_url = f"https://api.biorxiv.org/details/biorxiv/{doi.replace('https://doi.org/', '')}"
                resp = requests.get(api_url, headers=headers)
                resp_json = resp.json()["collection"][0]

                # 筛选日期
                pub_date = datetime.strptime(resp_json["date"], "%Y-%m-%d").date()
                if pub_date >= self.date:
                    filtered.append({
                        "Title": resp_json["title"],
                        "Summary": resp_json["abstract"],
                        "Authors": resp_json["authors"].split("; "),
                        "Author_corresponding": resp_json.get("author_corresponding", "Unknown"),
                        "Author_corresponding_institution": resp_json.get("author_corresponding_institution", "Unknown"),
                        "Link": f"https://doi.org/{doi}",
                        "Source": "bioRxiv"
                    })

        except Exception as e:
            print(f"bioRxiv搜索失败：{str(e)}")

        print(f"bioRxiv 找到 {len(filtered)} 篇文献")
        self.source_results["bioRxiv"] = filtered
        self.All_result.extend(filtered)

    def search_PubMed(self):
        """搜索PubMed（需填写Entrez.email避免报错）"""
        # 关键：PubMed要求填写邮箱（否则会警告/报错）
        Entrez.email = self.configs.get("Entrez_email", "your_email@example.com")
        if Entrez.email == "your_email@example.com":
            print("⚠️  提示：请在配置文件中设置 Entrez_email（你的邮箱），否则PubMed可能拒绝访问")

        keywords = self.configs["Keywords"]
        max_num = self.configs["max_num_per_source"]
        query = f"({' OR '.join([f'"{key}"' for key in keywords])})"
        # 日期范围：目标日期 到 明天（确保包含当天）
        date_range = f'"{self.date.strftime("%Y/%m/%d")}"[Date - Publication] : "{(self.date + timedelta(days=1)).strftime("%Y/%m/%d")}"[Date - Publication]'
        full_query = f"{query} AND {date_range}"
        filtered = []

        try:
            # 第一步：搜索获取PMID（文献唯一标识）
            handle = Entrez.esearch(
                db="pubmed",
                term=full_query,
                sort="pub date",
                retmax=max_num,
                retmode="xml"
            )
            pmids = Entrez.read(handle)["IdList"]
            handle.close()

            # 第二步：通过PMID获取文献详情
            fetcher = PubMedFetcher()
            for pmid in tqdm(pmids, desc="PubMed详情获取"):
                info = fetcher.article_by_pmid(pmid)
                filtered.append({
                    "Title": info.title,
                    "Summary": info.abstract if info.abstract else "No Abstract",
                    "Authors": [str(auth) for auth in info.authors],
                    "Link": info.url,
                    "Source": info.journal
                })

        except Exception as e:
            print(f"PubMed搜索失败：{str(e)}")

        print(f"PubMed 找到 {len(filtered)} 篇文献")
        self.source_results["PubMed"] = filtered
        self.All_result.extend(filtered)

    # ------------------------------
    # 3. 文献处理方法（去重、聚类、总结）
    # ------------------------------
    def _remove_duplicates(self):
        """按标题去重（不同数据源可能抓取同一篇文献）"""
        seen_titles = set()
        unique_papers = []
        for paper in self.All_result:
            title = paper["Title"]
            if title not in seen_titles:
                seen_titles.add(title)
                unique_papers.append(paper)
        self.All_result = unique_papers
        print(f"去重后剩余 {len(unique_papers)} 篇文献")

    def _categorize_by_title(self):
        """按标题分组（便于后续LLM聚类和总结）"""
        self.All_result_dict = {}
        for paper in self.All_result:
            title = paper["Title"]
            if title not in self.All_result_dict:
                self.All_result_dict[title] = [paper]
            else:
                self.All_result_dict[title].append(paper)

    def _cluster_by_topic(self):
        """用通义千问（qwen-plus）按标题聚类，生成主题"""
        if not self.All_result_dict:
            print("无文献可聚类")
            return

        api_key = self.configs["DASHSCOPE_API_KEY"]
        titles = list(self.All_result_dict.keys())
        keywords = self.configs["Keywords"]

        try:
            # 初始化OpenAI兼容客户端（通义千问）
            client = OpenAI(
                api_key=api_key,
                base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
            )

            # LLM提示词（明确任务，减少歧义）
            prompt = f"""
            请按以下规则处理文献标题列表：
            1. 仅保留与关键词 {keywords} 相关的标题，排除无关文献；
            2. 将相关标题按主题聚类，每个主题取一个简洁名称（不要用关键词直接命名）；
            3. 控制主题数量（避免1篇1类），返回格式为Python字典：{{"主题1": ["标题1", "标题2"], ...}}；
            4. 标题必须与输入完全一致（包括标点符号），不要修改。
            
            文献标题列表：{titles}
            """

            # 调用LLM
            response = client.chat.completions.create(
                model="qwen-plus",
                messages=[
                    {"role": "system", "content": "你是专业的学术文献分类助手，仅输出指定格式的字典，不附加其他内容"},
                    {"role": "user", "content": prompt}
                ]
            )

            # 解析LLM输出（去除代码块标记，转为字典）
            content = response.choices[0].message.content.strip()
            content = content.replace("```python", "").replace("```", "").strip()
            self.topic_dict = eval(content)  # 注意：仅信任LLM的格式化输出时使用eval

            total = sum(len(titles) for titles in self.topic_dict.values())
            print(f"成功聚类：{total} 篇文献 → {len(self.topic_dict)} 个主题")

        except Exception as e:
            raise RuntimeError(f"LLM聚类失败：{str(e)}") from e

    def _summarize_papers(self):
        """用通义千问提取每篇文献的关键词和创新点"""
        if not self.All_result_dict:
            print("无文献可总结")
            return

        api_key = self.configs["DASHSCOPE_API_KEY"]
        client = OpenAI(
            api_key=api_key,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )

        for title, papers in tqdm(self.All_result_dict.items(), desc="文献总结中"):
            paper = papers[0]  # 同一标题取第一篇（去重后实际只有一篇）
            abstract = paper["Summary"]
            if abstract in ["No Abstract", "Unknown"]:
                paper["Keywords"] = ["No Abstract"]
                paper["Novelty"] = "无法提取创新点（无摘要）"
                continue

            try:
                # LLM提示词（明确输出格式）
                prompt = f"""
                请分析以下文献摘要：
                标题：{title}
                摘要：{abstract}
                
                输出要求：
                1. 提取3-5个核心关键词（按相关性排序）；
                2. 总结1段创新点（100字以内，突出该文献的独特贡献）；
                3. 仅返回Python字典：{{"Keywords": ["关键词1",...], "Novelty": "创新点总结"}}，不附加其他内容。
                """

                response = client.chat.completions.create(
                    model="qwen-plus",
                    messages=[
                        {"role": "system", "content": "你是专业的学术文献分析助手，严格按要求格式输出"},
                        {"role": "user", "content": prompt}
                    ]
                )

                # 解析结果
                content = response.choices[0].message.content.strip()
                content = content.replace("```python", "").replace("```", "").strip()
                result = eval(content)

                # 更新文献信息
                paper["Keywords"] = result["Keywords"]
                paper["Novelty"] = result["Novelty"]

            except Exception as e:
                print(f"文献 {title} 总结失败：{str(e)}")
                paper["Keywords"] = ["Summary Failed"]
                paper["Novelty"] = "总结失败"

    def process_collected_papers(self):
        """统一调用文献处理流程（去重→分组→聚类→总结）"""
        print("\n=== 开始处理文献 ===")
        self._remove_duplicates()
        self._categorize_by_title()
        self._cluster_by_topic()
        self._summarize_papers()
        print("=== 文献处理完成 ===")

    # ------------------------------
    # 4. 新闻获取方法（基于Coze API）
    # ------------------------------
    def get_news(self):
        """通过Coze API获取最新10条AI新闻（需设置COZE_API_TOKEN环境变量）"""
        coze_token = os.getenv("COZE_API_TOKEN")
        if not coze_token:
            self.News = "⚠️  未设置 COZE_API_TOKEN 环境变量，无法获取AI新闻"
            print(self.News)
            return

        try:
            # 初始化Coze客户端（国内Base URL）
            coze = Coze(auth=TokenAuth(token=coze_token), base_url=COZE_CN_BASE_URL)
            bot_id = "7446278637571670025"  # 原代码中的Bot ID（需确保有效）
            user_id = "ScholarDaily_User"
            full_news = ""

            # 流式获取新闻
            for event in coze.chat.stream(
                bot_id=bot_id,
                user_id=user_id,
                additional_messages=[Message.build_user_question_text("输出最新10条AI新闻，每条占1行，开头标序号")]
            ):
                if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA and event.message.content:
                    full_news += event.message.content

            self.News = full_news if full_news else "未获取到AI新闻"
            print("=== AI新闻获取完成 ===")

        except Exception as e:
            self.News = f"⚠️  AI新闻获取失败：{str(e)}"
            print(self.News)

    # ------------------------------
    # 5. 报告生成与日志保存
    # ------------------------------
    def construct_html_report(self):
        """生成HTML格式的文献+新闻报告"""
        # 1. 构建Markdown内容（便于转换为HTML）
        md_content = f"""
<p align="center"><span style="font-size: 18px; font-weight: bold;">ScholarDaily 文献报告</span> | {self.date.strftime("%Y年%m月%d日")}</p>
---

## 一、文献汇总（共 {len(self.All_result)} 篇）
"""

        # 添加聚类后的文献
        for topic, titles in self.topic_dict.items():
            md_content += f"\n### {topic}（{len(titles)} 篇）\n"
            for idx, title in enumerate(titles, 1):
                paper = self.All_result_dict[title][0]
                md_content += f"""
#### {idx}. [{title}]({paper['Link']})
- **期刊/来源**: {paper['Source']}
- **作者**: {', '.join(paper['Authors'])}
- **关键词**: {', '.join(paper['Keywords'])}
- **摘要**: {paper['Summary'][:500]}...（全文见链接）
- **创新点**: {paper['Novelty']}
"""

        # 添加AI新闻
        md_content += f"""
---

## 二、最新AI新闻
{self.News}

---
<p align="center" style="color: #666;">Stay ahead, stay inspired. | 生成时间：{datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
"""

        # 2. 转换Markdown为HTML
        html_content = markdown.markdown(md_content, extensions=['extra', 'toc', 'tables'])
        full_html = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ScholarDaily_{self.date.strftime("%Y%m%d")}</title>
    <style>
        body {{ font-family: "Microsoft YaHei", Arial, sans-serif; line-height: 1.8; margin: 20px; max-width: 1200px; margin-left: auto; margin-right: auto; }}
        h1, h2, h3, h4 {{ color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 5px; }}
        a {{ color: #3498db; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .toc {{ margin: 20px 0; padding: 10px; border: 1px solid #eee; border-radius: 5px; }}
        .warning {{ color: #e74c3c; }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""

        # 3. 保存HTML文件
        report_path = f"ScholarDaily_{self.date.strftime("%Y%m%d")}.html"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"\n报告已保存：{os.path.abspath(report_path)}")

    def save_log(self):
        """保存运行日志（用pickle存储实例状态，便于后续分析）"""
        log_path = self.configs["log_path"]
        # 确保日志目录存在
        os.makedirs(log_path, exist_ok=True)
        log_file = f"{log_path}/ScholarDaily_{self.date.strftime("%Y%m%d")}.pkl"
        with open(log_file, "wb") as f:
            pickle.dump(self, f)
        print(f"日志已保存：{os.path.abspath(log_file)}")

    # ------------------------------
    # 6. 主流程（一键执行所有步骤）
    # ------------------------------
    def run(self):
        """端到端主流程：搜索→处理→新闻→报告→日志"""
        print(f"=== ScholarDaily 开始运行（目标日期：{self.date.strftime("%Y-%m-%d")}）===")
        
        # 1. 按数据源搜索文献
        print("\n=== 开始搜索文献 ===")
        for source in self.configs["Sources"]:
            print(f"\n--- 正在搜索 {source} ---")
            self.function_mapping[source]()

        # 2. 处理文献（去重、聚类、总结）
        self.process_collected_papers()

        # 3. 获取AI新闻
        print("\n=== 开始获取AI新闻 ===")
        self.get_news()

        # 4. 生成HTML报告
        print("\n=== 开始生成报告 ===")
        self.construct_html_report()

        # 5. 保存日志
        self.save_log()

        print("\n=== ScholarDaily 运行完成 ===")


# ------------------------------
# 端到端示例调用（新手直接运行此文件即可）
# ------------------------------
if __name__ == "__main__":
    # 1. 初始化实例（会自动创建/加载配置文件）
    scholar = ScholarDaily()

    # 2. （可选）自定义关键词和数据源（也可直接修改配置文件）
    # scholar.set_keywords(["large language model", "LLM fine-tuning"])  # 自定义关键词
    # scholar.set_sources(["Arxiv", "PubMed"])  # 自定义数据源（可选：Arxiv, PubMed, bioRxiv, GoogleScholar）

    # 3. （可选）自定义目标日期（格式：YYYYMMDD，默认昨天）
    # scholar.date = datetime.strptime("20240520", "%Y%m%d").date()

    # 4. 运行完整流程
    scholar.run()