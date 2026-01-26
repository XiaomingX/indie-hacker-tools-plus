# coding=utf-8
import os
import argparse
from pathlib import Path
from loguru import logger
import pdfplumber  # 更活跃的PDF解析库
import openai  # OpenAI API库


def extract_pdf_text(pdf_path):
    """使用pdfplumber提取PDF文本内容"""
    if not Path(pdf_path).exists():
        logger.error(f"PDF文件不存在: {pdf_path}")
        return None

    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = []
            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text()
                if text:
                    full_text.append(f"=== 第{page_num}页 ===\n{text}")
            return "\n\n".join(full_text)
    except Exception as e:
        logger.error(f"PDF解析失败: {str(e)}")
        return None


def get_llm_summary(paper_text):
    """使用GPT-4o-mini生成论文归纳总结"""
    # 验证API密钥
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        logger.error("请设置环境变量 OPENAI_API_KEY")
        return None

    # 优化后的科研论文归纳提示词
    prompt = """
    请作为科研助手，帮我归纳以下论文的核心内容。请按照以下结构组织回答：
    1. 研究背景与动机：简述研究领域现状及为什么需要这项研究
    2. 核心问题：研究要解决的关键科学问题或技术挑战
    3. 研究方法：采用的主要方法、模型、实验设计或理论框架
    4. 关键结果：最重要的实验发现或研究结论（列举2-3个核心结果）
    5. 意义与局限：研究的科学价值、应用前景及存在的局限性

    请用简洁专业的中文回答，避免冗余。如果内容涉及公式或图表，简要描述其核心含义即可。

    论文内容：
    {paper_text}
    """.strip()

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "你是专业的科研论文分析助手，擅长提炼学术文献的核心信息。"},
                {"role": "user", "content": prompt.format(paper_text=paper_text)}
            ],
            temperature=0.3,  # 降低随机性，保证结果稳定性
            max_tokens=1500   # 足够覆盖科研论文核心归纳
        )
        return response.choices[0].message["content"]
    except Exception as e:
        logger.error(f"LLM调用失败: {str(e)}")
        return None


def main():
    # 简化命令行参数
    parser = argparse.ArgumentParser(description="科研论文阅读助手 - 基于GPT-4o-mini的论文归纳工具")
    parser.add_argument("--file", type=str, required=True, help="PDF论文文件路径")
    args = parser.parse_args()

    # 1. 提取PDF文本
    logger.info(f"开始解析PDF: {args.file}")
    paper_text = extract_pdf_text(args.file)
    if not paper_text:
        logger.error("无法继续处理，退出程序")
        return

    # 2. 调用LLM生成归纳
    logger.info("开始生成论文归纳...")
    summary = get_llm_summary(paper_text)
    if not summary:
        logger.error("归纳生成失败")
        return

    # 3. 保存结果
    output_path = Path(args.file).with_suffix(".summary.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary)
    logger.success(f"论文归纳已保存至: {output_path}")


if __name__ == "__main__":
    # 配置日志
    logger.add("paper_assistant.log", rotation="10 MB", level="INFO")
    main()