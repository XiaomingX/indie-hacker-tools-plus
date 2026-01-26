import openai
import pandas as pd
from tqdm import tqdm
import sys

# 设置OpenAI API密钥 - 请替换为您自己的密钥
openai.api_key = "YOUR_OPENAI_API_KEY"  # 替换成您的API密钥

def ask_openai(question, model="gpt-3.5-turbo"):
    """调用OpenAI API获取回答"""
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "你是一个专业的招聘分析师，擅长从简历中提取关键信息并评估与职位的匹配度。"},
                {"role": "user", "content": question}
            ],
            temperature=0.3,
            max_tokens=500
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"API调用出错: {str(e)}")
        return "获取信息失败"

def analyze_resume(jd, resume, options):
    """分析简历并生成匹配度报告"""
    # 从简历中提取信息
    print("正在从简历中提取信息...")
    df_data = []
    
    for option in tqdm(options, desc="信息提取中", unit="项"):
        question = f"""
        请从以下简历中提取"{option}"信息：
        简历内容：{resume}
        要求：精简返回答案，最多不超过250字，如果查找不到，则返回'未提供'
        """
        response = ask_openai(question)
        df_data.append({'option': option, 'value': response})
    
    df = pd.DataFrame(df_data)
    df_string = df.applymap(lambda x: ', '.join(x) if isinstance(x, list) else x).to_string(index=False)
    
    # 生成综合匹配度概要
    print("\n正在生成综合匹配度分析...")
    summary_question = f"""
    职位要求：{jd}
    简历概要：{df_string}
    请基于以上信息，返回该候选人与应聘岗位的匹配度概要（控制在200字以内）。
    """
    summary = ask_openai(summary_question)
    df.loc[len(df)] = ['综合概要', summary]
    
    # 生成匹配分数
    print("正在计算匹配得分...")
    score_question = f"""
    职位要求：{jd}
    简历概要：{df.to_string(index=False)}
    打分要求：国内top10大学+3分，985大学+2分，211大学+1分，头部企业经历+2分，知名企业+1分，海外背景+3分，外企背景+1分。
    请基于以上信息和打分要求，返回该候选人的匹配分数（0-100），只需返回数字分数，不需要其他内容，以便与其他候选人对比排序。
    """
    score = ask_openai(score_question)
    df.loc[len(df)] = ['匹配得分', score]
    
    return df

def read_file_content(file_path):
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"读取文件 {file_path} 时出错：{str(e)}")
        sys.exit(1)

def main():
    print("===== 简历匹配度分析工具 =====")
    
    # 获取用户输入的文件路径
    jd_path = input("请输入职位描述(JD)文件路径: ").strip()
    resume_path = input("请输入简历文件路径: ").strip()
    
    # 读取文件内容
    jd_text = read_file_content(jd_path)
    resume_text = read_file_content(resume_path)
    
    # 定义需要提取的信息项
    options = [
        "姓名", "联系号码", "性别", "年龄", "工作年数（数字）", 
        "最高学历", "本科学校名称", "硕士学校名称", "是否在职", 
        "当前职务", "历史任职公司列表", "技术能力", "经验程度", "管理能力"
    ]
    
    # 执行分析
    result_df = analyze_resume(jd_text, resume_text, options)
    
    # 显示结果
    print("\n===== 分析结果 =====")
    print(f"综合匹配得分：{result_df.loc[result_df['option'] == '匹配得分', 'value'].values[0]}")
    print("\n详细信息：")
    print(result_df.to_string(index=False))
    
    # 保存结果到CSV
    output_file = "resume_analysis_result.csv"
    result_df.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"\n分析结果已保存到 {output_file}")

if __name__ == "__main__":
    main()