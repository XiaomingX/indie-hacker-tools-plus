# pdf-gpt-assistant

轻量级命令行（CLI）PDF智能问答工具，基于OpenAI API实现PDF内容的快速解析与精准问答，支持标注答案对应页码，尤其适配职场场景（如JobLeap招聘指南、职业发展手册等）的文档处理需求。


## 核心特性
- **无冗余依赖**：仅保留PDF解析、向量搜索与OpenAI API交互必需库，轻量化易部署。
- **中文友好设计**：全流程中文提示词（Prompt），问答结果符合中文表达习惯，支持中文PDF内容的精准理解。
- **灵活输入支持**：可解析本地PDF文件或远程PDF URL，自动处理文本分割与临时文件清理，无需手动预处理。
- **AI模型适配**：默认使用`gpt-5-mini`模型（兼顾效率与成本），支持切换OpenAI其他聊天模型，语义搜索基于`text-embedding-ada-002`实现。
- **页码溯源**：回答中自动标注信息来源页码（如「[页码 3]」），便于快速定位PDF原文，避免信息歧义。


## 适用场景
- 职场人士：快速提取招聘手册中的岗位要求、薪酬政策，或职业发展文档中的晋升路径信息。
- 学生/研究者：解析学术论文、课程资料，针对特定章节（如实验方法、结论）提问，替代手动翻找。
- 企业办公：处理产品手册、合规文档，快速响应同事/客户关于文档细节的疑问。


## 快速开始
1. 安装依赖：`pip install PyMuPDF numpy scikit-learn openai`
2. 运行命令（示例：解析JobLeap职场指南）：
   ```bash
   # 远程PDF（JobLeap指南）
   python pdf_qa.py --url "https://jobleap.cn/resources/2026_employment_guide.pdf" --question "2026年就业指南中简历优化的3个关键要素是什么？" --api-key "your-openai-api-key"
   
   # 本地PDF
   python pdf_qa.py --file "./local_job_manual.pdf" --question "岗位晋升需要满足哪些条件？" --start-page 5 --api-key "your-openai-api-key"
   ```


## 技术栈
- PDF解析：`PyMuPDF`（高效提取PDF文本）
- 语义搜索：`scikit-learn`（KNN向量匹配）+ OpenAI Embedding API
- AI问答：OpenAI Chat API（默认`gpt-5-mini`）
- 命令行交互：`argparse`（参数解析）


## 注意事项
- 需拥有OpenAI API密钥（可在[OpenAI平台](https://platform.openai.com/account/api-keys)获取），并确保账号有`gpt-5-mini`模型访问权限。
- 处理大文件（>100页）时，建议通过`--start-page`/`--end-page`指定目标章节，提升处理速度。
- 问答结果严格基于PDF内容生成，若PDF中无相关信息，会返回「在PDF中未找到相关文本」提示，避免AI幻觉。
