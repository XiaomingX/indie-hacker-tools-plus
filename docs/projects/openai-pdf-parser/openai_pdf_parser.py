from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain_community.document_loaders import PyPDFLoader
from langchain.schema.output_parser import StrOutputParser

# 加载环境变量
load_dotenv()
api_key = os.getenv("OA_TOKEN")

# 确保API密钥已配置
if not api_key:
    raise ValueError("请在.env文件中配置OA_TOKEN")

# 初始化OpenAI模型
llm = ChatOpenAI(api_key=api_key, model="gpt-4-0125-preview")

def load_pdf_document(file_path):
    """加载PDF文档并返回内容"""
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents

def process_document_with_ai(documents, query):
    """使用AI处理文档并回答问题"""
    # 系统提示：定义AI的角色和行为
    system_prompt = SystemMessagePromptTemplate.from_template(
        "你是一个文档处理助手，擅长分析PDF文档内容并回答相关问题。"
    )
    
    # 人类提示：包含用户查询和文档内容
    human_prompt = HumanMessagePromptTemplate.from_template(
        "请根据以下文档内容回答问题：\n{document}\n\n问题：{query}"
    )
    
    # 创建聊天提示模板
    chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])
    
    # 创建处理链并执行
    chain = chat_prompt | llm | StrOutputParser()
    
    # 为了避免内容过长，这里只使用前3页文档
    relevant_docs = "\n\n".join([doc.page_content for doc in documents[:3]])
    
    return chain.invoke({"document": relevant_docs, "query": query})

# 主流程
if __name__ == "__main__":
    # 1. 加载PDF文档
    pdf_path = "CELEX_32022R2554_DE_TXT.pdf"
    print(f"正在加载文档: {pdf_path}")
    documents = load_pdf_document(pdf_path)
    print(f"成功加载 {len(documents)} 页文档")
    
    # 2. 定义用户查询
    user_query = "请将文档内容逻辑分段，并总结每段的主要内容"
    
    # 3. 使用AI处理文档
    print("\n正在处理查询，请稍候...")
    result = process_document_with_ai(documents, user_query)
    
    # 4. 输出结果
    print("\n处理结果：")
    print(result)