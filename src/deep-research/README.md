# Deep Research
一个基于 AI 与网页搜索的自动化研究助手，支持通过命令行（CLI）或 API 快速生成针对性研究结论与详细报告，无需手动检索和整理信息。


## 📋 项目介绍
Deep Research 是一款轻量级自动化研究工具，核心功能是将 **AI 推理** 与 **网页深度搜索** 结合：
1. 根据用户问题自动生成多层级搜索关键词
2. 递归爬取网页内容并提取核心结论（支持自定义研究广度与深度）
3. 基于研究结论生成 **简洁答案** 或 **结构化报告**
4. 支持命令行直接交互和 API 服务两种使用方式

适合学生、研究者、分析师快速完成课题调研、行业分析等任务。


## ✨ 核心功能
| 功能特性                | 说明                                                                 |
|-------------------------|----------------------------------------------------------------------|
| 双交互模式              | 命令行（CLI）快速使用 + FastAPI 服务供其他系统调用                   |
| 深度递归研究            | 自定义 `breadth`（每轮搜索关键词数）和 `depth`（递归研究层数）       |
| 双输出类型              | 简洁答案（适合具体问题） + Markdown 详细报告（适合深度调研）         |
| 多 AI 模型支持          | 支持 OpenAI（o3-mini 等）、Fireworks（deepseek-r1 等）模型切换       |
| 自动文本处理            | 智能裁剪长文本到模型上下文限制内，保留语义完整性                     |
| 结果自动保存            | 输出内容自动保存为文件（`research-answer.txt` / `research-report.md`）|


## 🚀 快速开始

### 1. 环境准备
#### 1.1 依赖环境
- Python 3.8+（推荐 3.10+）
- 网络连接（需访问 AI 模型 API 和 Firecrawl 服务）

#### 1.2 必要 API 密钥
需注册获取以下密钥（至少满足 1 个 AI 密钥 + Firecrawl 密钥）：
| 密钥名称         | 用途                  | 获取地址                                  |
|------------------|-----------------------|-------------------------------------------|
| `FIRECRAWL_KEY`  | 网页搜索与内容爬取    | [Firecrawl 官网](https://www.firecrawl.dev/) |
| `OPENAI_KEY`     | AI 推理（优先推荐）   | [OpenAI 平台](https://platform.openai.com/)  |
| `FIREWORKS_KEY`  | AI 推理（替代方案）   | [Fireworks 官网](https://fireworks.ai/)     |


### 2. 安装步骤
#### 2.1 克隆仓库（或下载源码）
```bash
git clone https://github.com/your-username/deep-research.git
cd deep-research
```

#### 2.2 创建虚拟环境（推荐）
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 2.3 安装依赖
```bash
pip install -r requirements.txt
```

#### 2.4 配置环境变量
1. 在项目根目录创建 `.env` 文件
2. 填入密钥和配置（参考下方「配置说明」）：
```env
# 必要密钥
FIRECRAWL_KEY=your_firecrawl_api_key
OPENAI_KEY=your_openai_api_key
# FIREWORKS_KEY=your_fireworks_api_key  # 可选，替代 OpenAI

# 可选配置
PORT=3051
CONTEXT_SIZE=128000
FIRECRAWL_CONCURRENCY=2
```


### 3. 使用方法
提供两种使用方式，根据需求选择：

#### 方式一：命令行交互（适合快速使用）
直接运行主程序，按提示输入参数：
```bash
python main.py
```

**交互流程示例**：
```
=== 研究助手 ===
当前使用模型: o3-mini

请输入研究问题: 2024年AI大模型发展趋势
请输入研究广度（2-10，默认4）: 3
请输入研究深度（1-5，默认2）: 2
请选择输出类型（answer=简洁答案/report=详细报告，默认report）: report

=== 开始研究 ===
问题: 2024年AI大模型发展趋势
广度: 3 | 深度: 2

[深度2] 生成3个搜索关键词：
- 2024 AI大模型技术突破
- 2024 主流AI大模型厂商动态
- 2024 AI大模型行业应用案例

=== 研究完成 ===
结论数量: 8
链接数量: 12

=== 详细报告已生成 ===
结果已保存到 research-report.md
```


#### 方式二：API 服务（适合集成到其他系统）
1. 启动 API 服务：
```bash
python main.py api
```

2. 服务启动后，可通过以下方式调用：
   - 访问 [http://localhost:3051/docs](http://localhost:3051/docs) 查看自动生成的 API 文档（支持在线测试）
   - 使用 curl/Postman 调用接口


##### API 接口说明
| 接口地址                | 方法 | 功能                | 请求体参数                          | 响应示例                                                                 |
|-------------------------|------|---------------------|-------------------------------------|--------------------------------------------------------------------------|
| `/api/research/answer`  | POST | 生成简洁答案        | `{"query": "问题", "breadth": 3, "depth": 2}` | `{"success": true, "answer": "...", "learnings": [...], "visited_urls": [...]}` |
| `/api/research/report`  | POST | 生成详细报告        | 同上                                | `{"success": true, "report": "# 报告标题...", "learnings": [...], "visited_urls": [...]}` |


##### curl 调用示例（生成答案）
```bash
curl -X POST http://localhost:3051/api/research/answer \
-H "Content-Type: application/json" \
-d '{
  "query": "2024年AI大模型发展趋势",
  "breadth": 3,
  "depth": 2
}'
```


## ⚙️ 配置说明
`.env` 文件中所有可配置参数：

| 参数名称               | 类型   | 默认值       | 说明                                                                 |
|------------------------|--------|--------------|----------------------------------------------------------------------|
| `FIRECRAWL_KEY`        | 字符串 | 空           | 必需，Firecrawl 服务密钥，用于网页搜索                               |
| `OPENAI_KEY`           | 字符串 | 空           | 可选（二选一），OpenAI 密钥，用于 AI 推理                            |
| `FIREWORKS_KEY`        | 字符串 | 空           | 可选（二选一），Fireworks 密钥，用于 AI 推理                          |
| `PORT`                 | 整数   | 3051         | API 服务端口号                                                       |
| `CONTEXT_SIZE`         | 整数   | 128000       | AI 模型最大上下文长度（token），超过会自动裁剪                        |
| `FIRECRAWL_CONCURRENCY`| 整数   | 2            | 网页搜索并发数，过高可能触发限流，建议 2-5                            |
| `CUSTOM_MODEL`         | 字符串 | 空           | 自定义 AI 模型（如 "gpt-4o"），需配合 `OPENAI_KEY` 使用               |


## 📂 代码结构（单文件模块化设计）
`main.py` 内部按功能划分模块，便于理解和维护：
```
main.py
├── 配置模块（Config）          # 环境变量读取与管理
├── 数据模型（Pydantic）        # 请求/响应数据结构验证
├── 文本处理（TextSplitter）    # 长文本分割与裁剪
├── AI 工具函数                # 模型选择、Prompt 处理、AI 调用
├── 核心研究逻辑               # 关键词生成、搜索、递归研究
├── 结果生成函数               # 简洁答案、详细报告生成
├── API 路由                  # FastAPI 接口定义
├── 命令行交互                # CLI 模式逻辑
└── 主入口函数                # 程序启动与模式切换
```


## ❗ 常见问题
1. **「未配置AI模型」错误**：  
   确保 `.env` 中填入 `OPENAI_KEY` 或 `FIREWORKS_KEY`，二者至少选一个。

2. **搜索超时/失败**：  
   - 检查网络连接，确保能访问 Firecrawl 服务
   - 降低 `FIRECRAWL_CONCURRENCY` 并发数（建议 2）
   - 延长超时时间（修改代码中 `firecrawl.search` 的 `timeout` 参数）

3. **AI 生成结果为空**：  
   检查 Prompt 长度是否过长（可减小 `CONTEXT_SIZE`），或更换 AI 模型。


## 🤝 贡献指南
1. Fork 本仓库
2. 创建特性分支（`git checkout -b feature/amazing-feature`）
3. 提交修改（`git commit -m 'Add some amazing feature'`）
4. 推送到分支（`git push origin feature/amazing-feature`）
5. 打开 Pull Request


## 📄 许可证
本项目采用 [MIT 许可证](LICENSE) - 详见 LICENSE 文件。
