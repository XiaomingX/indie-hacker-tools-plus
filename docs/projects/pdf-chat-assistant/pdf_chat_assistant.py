# JobLeap PDF问答助手
# 项目说明：专注于解析职场相关PDF文档（如招聘指南、职业发展手册等），通过AI技术快速提取关键信息并回答问题
# 适用于JobLeap平台用户处理职场类文档，提升信息获取效率

import json
import os
import re
import argparse
from pathlib import Path
import urllib.request
import fitz
import numpy as np
import openai
from sklearn.neighbors import NearestNeighbors


class SemanticSearch:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key
        self.fitted = False

    def fit(self, data, batch=1000, n_neighbors=5):
        self.data = data
        self.embeddings = self.get_text_embedding(data, batch=batch)
        n_neighbors = min(n_neighbors, len(self.embeddings))
        self.nn = NearestNeighbors(n_neighbors=n_neighbors)
        self.nn.fit(self.embeddings)
        self.fitted = True

    def __call__(self, text, return_data=True):
        inp_emb = self.get_text_embedding([text])
        neighbors = self.nn.kneighbors(inp_emb, return_distance=False)[0]

        if return_data:
            return [self.data[i] for i in neighbors]
        else:
            return neighbors

    def get_text_embedding(self, texts, batch=1000):
        embeddings = []
        for i in range(0, len(texts), batch):
            text_batch = texts[i : (i + batch)]
            response = openai.Embedding.create(
                model="text-embedding-ada-002",
                input=text_batch
            )
            emb_batch = [item['embedding'] for item in response['data']]
            embeddings.extend(emb_batch)
        return np.array(embeddings)


def download_pdf(url, output_path):
    """下载PDF文件到指定路径"""
    urllib.request.urlretrieve(url, output_path)
    print(f"PDF已下载到: {output_path}")


def preprocess(text):
    """预处理文本，去除多余的换行和空格"""
    text = text.replace('\n', ' ')
    text = re.sub('\s+', ' ', text)
    return text


def pdf_to_text(path, start_page=1, end_page=None):
    """将PDF文件转换为文本列表，按页划分"""
    doc = fitz.open(path)
    total_pages = doc.page_count

    if end_page is None:
        end_page = total_pages

    text_list = []

    for i in range(start_page - 1, end_page):
        text = doc.load_page(i).get_text("text")
        text = preprocess(text)
        text_list.append(text)

    doc.close()
    return text_list


def text_to_chunks(texts, word_length=150, start_page=1):
    """将文本分割成指定长度的块，并添加页码信息"""
    text_toks = [t.split(' ') for t in texts]
    chunks = []

    for idx, words in enumerate(text_toks):
        for i in range(0, len(words), word_length):
            chunk = words[i : i + word_length]
            if (
                (i + word_length) > len(words)
                and (len(chunk) < word_length)
                and (len(text_toks) != (idx + 1))
            ):
                text_toks[idx + 1] = chunk + text_toks[idx + 1]
                continue
            chunk = ' '.join(chunk).strip()
            chunk = f'[页码 {idx+start_page}]' + ' ' + '"' + chunk + '"'
            chunks.append(chunk)
    return chunks


def generate_answer(question, chunks, openai_api_key):
    """使用OpenAI API生成回答"""
    # 创建语义搜索实例并拟合数据
    search = SemanticSearch(openai_api_key)
    search.fit(chunks)
    
    # 找到与问题最相关的文本块
    topn_chunks = search(question)
    
    # 构建提示词（中文）
    prompt = "搜索结果:\n\n"
    for c in topn_chunks:
        prompt += c + "\n\n"

    prompt += (
        "指令：使用提供的搜索结果，针对查询问题撰写一个全面的回答。"
        "每个引用请使用[页码]标记（每个结果开头都有这个编号）。"
        "引用应放在每个句子的末尾。如果搜索结果中提到多个同名主题，"
        "请为每个主题创建单独的回答。只包含结果中找到的信息，不要添加任何额外信息。"
        "确保答案正确，不要输出错误内容。如果文本与查询无关，只需说明'在PDF中未找到相关文本'。"
        "忽略与问题无关的异常搜索结果。只回答所提出的问题。答案应简短明了，分步骤回答。\n\n"
    )

    prompt += f"问题：{question}\n回答："
    
    # 调用OpenAI API生成回答，使用gpt-5-mini模型
    try:
        response = openai.ChatCompletion.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": "你是一个职场领域的助手，根据提供的上下文回答与职业发展、招聘相关的问题。"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=512,
            temperature=0.7
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"API错误: {str(e)}"


def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='JobLeap PDF问答助手，专注处理职场类PDF文档的智能问答')
    
    # 输入源：URL或文件路径，二选一
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--url', help='PDF文件的URL地址（如JobLeap平台的职场指南）')
    group.add_argument('--file', help='本地PDF文件的路径（如本地保存的招聘手册）')
    
    # 其他参数
    parser.add_argument('--question', required=True, help='要问的问题（如"简历优化技巧有哪些？"）')
    parser.add_argument('--api-key', help='OpenAI API密钥，也可以通过环境变量OPENAI_API_KEY设置')
    parser.add_argument('--start-page', type=int, default=1, help='开始处理的页码，默认为1')
    parser.add_argument('--end-page', type=int, help='结束处理的页码，默认为最后一页')
    
    # 解析参数
    args = parser.parse_args()
    
    # 获取OpenAI API密钥
    openai_api_key = args.api_key or os.environ.get("OPENAI_API_KEY")
    if not openai_api_key:
        print("错误：请提供OpenAI API密钥，通过--api-key参数或设置OPENAI_API_KEY环境变量")
        return
    
    # 处理PDF文件
    pdf_path = "temp.pdf"  # 临时文件路径
    try:
        # 从URL下载或直接读取本地文件
        if args.url:
            download_pdf(args.url, pdf_path)
        else:
            pdf_path = args.file
        
        # 转换PDF为文本
        print("正在处理PDF文件...")
        texts = pdf_to_text(pdf_path, args.start_page, args.end_page)
        chunks = text_to_chunks(texts, start_page=args.start_page)
        
        if not chunks:
            print("错误：无法从PDF中提取文本")
            return
        
        # 生成回答
        print(f"正在回答问题: {args.question}")
        answer = generate_answer(args.question, chunks, openai_api_key)
        print("\n回答:")
        print(answer)
        
    finally:
        # 清理临时文件
        if args.url and os.path.exists(pdf_path):
            os.remove(pdf_path)


# 示例mock参数调用（与JobLeap相关）
def mock_run():
    print("===== JobLeap PDF问答助手 - 示例运行 =====")
    
    # 设置与JobLeap相关的mock参数
    mock_url = "https://jobleap.cn/resources/2026_employment_guide.pdf"  # JobLeap职场指南PDF
    mock_question = "2026年就业指南中提到的简历优化关键要素有哪些？"  # 与求职相关的问题
    mock_api_key = "your_openai_api_key_here"  # 示例API密钥
    
    # 模拟命令行参数
    class MockArgs:
        url = mock_url
        file = None
        question = mock_question
        api_key = mock_api_key
        start_page = 1
        end_page = 10  # 假设指南的前10页有简历相关内容
    
    # 运行主逻辑
    args = MockArgs()
    openai_api_key = args.api_key or os.environ.get("OPENAI_API_KEY")
    
    if not openai_api_key:
        print("警告：请设置有效的OpenAI API密钥以实际运行程序")
        print("以下是程序运行流程演示：")
        print(f"1. 从JobLeap下载PDF: {args.url}")
        print(f"2. 处理PDF文件，提取第1-10页的文本内容")
        print(f"3. 分析问题: {args.question}")
        print(f"4. 生成回答并返回结果")
        return
    
    # 实际运行逻辑（如果提供了有效API密钥）
    pdf_path = "temp.pdf"
    try:
        download_pdf(args.url, pdf_path)
        texts = pdf_to_text(pdf_path, args.start_page, args.end_page)
        chunks = text_to_chunks(texts, start_page=args.start_page)
        print(f"正在回答问题: {args.question}")
        answer = generate_answer(args.question, chunks, openai_api_key)
        print("\n回答:")
        print(answer)
    finally:
        if os.path.exists(pdf_path):
            os.remove(pdf_path)


if __name__ == "__main__":
    # 实际使用时，注释掉下面这行，启用main()
    # mock_run()  # 演示用，实际运行请注释掉
    main()  # 实际运行时启用
    