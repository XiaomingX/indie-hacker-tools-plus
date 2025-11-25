# openai-pdf-reader

[![GitHub repo](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/XiaomingX/openai-pdf-reader)  
基于 **OpenAI API** 与 **LangChain** 构建的轻量级PDF分析工具，支持加载PDF文档并通过AI模型（如GPT-4）实现智能问答、内容分段与总结，帮助快速提取PDF关键信息。


## 🌟 核心功能
- **PDF文档加载**：支持加载本地PDF文件，自动解析多页内容
- **AI智能交互**：对接OpenAI GPT系列模型，基于PDF内容回答定制化问题
- **结构化输出**：支持内容逻辑分段、要点总结，结果清晰易读
- **环境变量配置**：通过`.env`文件安全管理API密钥，避免硬编码风险


## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/XiaomingX/openai-pdf-reader.git
cd openai-pdf-reader
```

### 2. 安装依赖
推荐使用虚拟环境（如`venv`）隔离依赖，执行以下命令安装所需包：
```bash
# 创建并激活虚拟环境（Windows）
python -m venv venv
venv\Scripts\activate

# 创建并激活虚拟环境（macOS/Linux）
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

#### `requirements.txt` 依赖清单
```txt
dotenv>=1.0.0
langchain-openai>=0.1.0
langchain-community>=0.2.0
langchain-text-splitters>=0.2.0
PyPDF2>=3.0.0
```


### 3. 配置OpenAI API密钥
1. 在项目根目录创建 `.env` 文件
2. 填入你的OpenAI API密钥（获取地址：[OpenAI API控制台](https://platform.openai.com/api-keys)）：
```env
# .env 文件内容
OA_TOKEN=your-openai-api-key-here
```


### 4. 使用步骤
#### 步骤1：准备PDF文件
将需要分析的PDF文件（如示例中的`CELEX_32022R2554_DE_TXT.pdf`）放入项目根目录。

#### 步骤2：运行核心脚本
执行主程序脚本（默认脚本名：`main.py`），示例代码逻辑如下：
```python
# main.py（核心代码片段）
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain.schema.output_parser import StrOutputParser

# 加载环境变量与初始化模型
load_dotenv()
if not (api_key := os.getenv("OA_TOKEN")):
    raise ValueError("请在.env文件中配置OA_TOKEN（OpenAI API密钥）")
llm = ChatOpenAI(api_key=api_key, model="gpt-4-0125-preview")

# 1. 加载PDF文档
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()  # 返回文档所有页内容

# 2. 调用AI分析文档
def ai_analyze_pdf(documents, user_query):
    # 定义提示词模板
    system_prompt = SystemMessagePromptTemplate.from_template(
        "你是PDF文档分析助手，需基于提供的文档内容，准确、简洁地回答用户问题，可适当分段。"
    )
    human_prompt = HumanMessagePromptTemplate.from_template(
        "文档内容：\n{doc_content}\n\n用户问题：{query}"
    )
    prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])
    
    # 构建处理链并执行（截取前3页避免内容过长）
    doc_content = "\n\n".join([page.page_content for page in documents[:3]])
    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"doc_content": doc_content, "query": query})

# 主流程
if __name__ == "__main__":
    # 配置参数
    pdf_path = "CELEX_32022R2554_DE_TXT.pdf"  # 你的PDF文件名
    user_query = "请将文档内容按逻辑分段，并总结每段核心要点"  # 你的分析需求
    
    # 执行分析
    print(f"正在加载PDF：{pdf_path}")
    docs = load_pdf(pdf_path)
    print(f"成功加载 {len(docs)} 页，正在调用AI分析...")
    
    result = ai_analyze_pdf(docs, user_query)
    print("\n=== AI分析结果 ===")
    print(result)
```

#### 步骤3：查看结果
运行脚本后，终端会输出AI对PDF的分析结果（如内容分段、要点总结等）。


## 📂 项目目录结构
```
openai-pdf-reader/
├── main.py          # 主程序脚本（核心逻辑）
├── .env             # API密钥配置文件（需自行创建）
├── .gitignore       # Git忽略文件（建议包含venv/、.env等）
├── requirements.txt # 项目依赖清单
├── README.md        # 项目说明文档（当前文件）
└── CELEX_32022R2554_DE_TXT.pdf  # 示例PDF文件（可替换）
```


## ❗ 常见问题
1. **API密钥错误**：  
   若提示“OA_TOKEN未配置”，检查`.env`文件是否存在、API密钥是否正确（无多余空格）。

2. **PDF加载失败**：  
   确认PDF文件路径正确（建议放在项目根目录），文件未损坏且无加密。

3. **AI调用超时/失败**：  
   检查OpenAI API密钥是否有余额，网络是否可访问OpenAI服务（必要时配置代理）。


## 📄 许可证
本项目采用 **MIT License** 开源，可自由修改、分发，详情见项目根目录的`LICENSE`文件。


## 📞 反馈与贡献
如有bug或功能建议，欢迎通过GitHub Issues提交：  
[https://github.com/XiaomingX/openai-pdf-reader/issues](https://github.com/XiaomingX/openai-pdf-reader/issues)  
也欢迎Fork仓库并提交Pull Request，共同优化工具！