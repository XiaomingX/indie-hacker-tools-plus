# AI 智能代理工具汇总 (2026 Checklist)

以下是 2026 年主流的 AI 智能代理与框架，按照独立开发者最常用的场景进行了分类。

---

## 🏗️ 代理开发框架 (Agent Frameworks)

- [ ] [**AutoGen (Microsoft)**](https://microsoft.github.io/autogen/) - 2026 年最成熟的多代理协作框架，支持复杂的任务编排与工具调用。
- [ ] [**CrewAI**](https://www.crewai.io/) - 专注于“角色扮演”型代理，通过定义角色、任务和流程实现高度自动化的团队协作。
- [ ] [**LangGraph (LangChain)**](https://langchain-ai.github.io/langgraph/) - 提供循环图结构的代理开发框架，适合需要精细状态控制的复杂 Agent 逻辑。
- [ ] [**MetaGPT**](https://github.com/geekan/MetaGPT) - 将软件公司的标准作业程序 (SOP) 注入到 Agent 之中，可一键生成完整的软件开发产出。
- [ ] [**PydanticAI**](https://ai.pydantic.dev/) - 2026 年新锐框架，利用 Pydantic 的类型安全特性构建稳健的 Agent 应用。

---

## 💻 编程与代码助手 (Dev Agents)

- [ ] [**Cursor**](https://www.cursor.com) - 独立开发者的首选 AI IDE，支持 Composer 模式，可直接操作多文件进行重构。
- [ ] [**Cline (原 Devin)**](https://github.com/cline/cline) - 开源的高级编程助手，具备自主运行测试、读取文件和执行命令的能力，是目前最接近“AI 程序员”的项目。
- [ ] [**Aider**](https://aider.chat/) - 命令行中的编程核武器，擅长基于已有代码库进行快速修改。
- [ ] [**OpenClaw**](https://github.com/OpenClaw/OpenClaw) - 国内开发者发起的开源 Agent，针对中文语境和国内工具链进行了深度优化。
- [ ] [**Hermes Agent**](https://github.com/NousResearch/Hermes-Agent) - 基于 Nous Hermes 模型的自进化代理，具备极强的逻辑推理与任务拆解能力。
- [ ] [**Open Interpreter**](https://openinterpreter.com/) - 让大模型直接操作你的电脑桌面，执行 Python 代码、修改系统设置。

---

## 🔍 研究、数据与自动化 (Research & Data)

- [ ] [**GPT Researcher**](https://github.com/assafelovic/gpt-researcher) - 一键生成长篇、结构化研究报告的智能代理，支持引用 20+ 个信息源。
- [ ] [**Tavily**](https://tavily.com/) - 为 Agent 设计的搜索引擎 API，返回结构化、可直接喂给模型的数据。
- [ ] [**AskYourDatabase**](https://www.askyourdatabase.com/) - 通过自然语言直接与 SQL/NoSQL 数据库对话并生成可视化看板。
- [ ] [**Perplexity Pro**](https://www.perplexity.ai/) - 集成了深度研究模式的 AI 搜索代理，2026 年已支持多轮交互与文件上传分析。
- [ ] [**Taskade**](https://taskade.com/) - 任务管理与 Agent 自动化结合的典范，支持自定义 Agent 角色并执行周期性任务。

---

## 建议避开或已失效 (2026 状态)

- [x] **Adept AI**：核心团队已加入 Amazon，产品重心已转移，不再适合独立开发者。
- [x] **Airplane.dev**：已被收购并停止服务，请转向 **Retool** 或 **Railway**。
- [x] **AutoGPT / BabyAGI (原始版)**：作为实验性概念非常出色，但在 2026 年的实际生产中，已被 AutoGen 和 CrewAI 等更稳健的框架取代。

---

## 🔗 MCP 生态与高影响力 Skill (MCP & Skills)

> [!NOTE]
> **MCP (Model Context Protocol)** 是 Anthropic 发起的开放标准，旨在统一 AI 模型与工具、数据的连接方式。

- [ ] [**Supabase MCP**](https://supabase.com/docs/guides/ai/mcp) - **Supabase 开源**。赋予 Agent 管理数据库模式、执行迁移和查询数据的能力。
- [ ] [**Developer Knowledge MCP**](https://developers.googleblog.com/en/google-mcp-server-developer-docs/) - **Google 开源**。集成 Android、Firebase 等官方文档，解决模型过时信息问题。
- [ ] [**Chrome DevTools MCP**](https://github.com/google/mcp-servers) - **Google 开源**。允许 Agent 控制浏览器进行调试与网页测试。
- [ ] [**Filesystem & GitHub MCP**](https://github.com/modelcontextprotocol/servers) - **Anthropic 官方**。基础中的基础，支持文件读写与仓库协作。
- [ ] [**Context7**](https://context7.com/) - **高频刚需付费**。提供上百个技术框架的最新文档实时检索，开发者愿意为“无幻觉”付费。
- [ ] [**Firebase Genkit**](https://firebase.google.com/docs/genkit) - **Google 开源**。全栈 AI SDK，预置大量常用 Skill 与工具集成。

---

### 选型建议

1. **轻量级应用**：直接使用 **Cursor** 或 **Aider**。
2. **多代理协作**：首选 **CrewAI** (易上手) 或 **AutoGen** (可定制性强)。
3. **自主任务执行**：关注 **Cline** 和 **Open Interpreter**。
