# AI Agent 业务自动化与提效 (2026 Checklist)

> [!IMPORTANT]
> **Indie Hacker Insight**: 2026 年，独立开发者的竞争优势不再是“写代码”，而是“编排 Agent”。
> - **一人公司 (Solopreneur)**：通过 Agent 自动化处理 80% 的运营、客服与销售工作。
> - **核心标准**：优先选择支持 **MCP (Model Context Protocol)** 的工具，确保 Agent 能顺畅访问你的数据库与业务系统。

---

## 🛠️ Agent 编排与工作流 (Orchestration)

- [ ] [**Dify**](https://dify.ai/) - 开源 LLM 应用开发平台，可视化编排工作流、知识库 (RAG) 与 Agent 的首选。
- [ ] [**Coze (扣子)**](https://www.coze.cn/) - 字节跳动出品，极其丰富的插件生态，适合快速搭建与分发 Agent。
- [ ] [**LangGraph**](https://www.langchain.com/langgraph) - 适合构建复杂的、有状态的多 Agent 协作系统，支持循环逻辑。
- [ ] [**Flowise**](https://flowiseai.com/) - 拖拽式 UI 构建 LLM 流程，适合非代码人员或快速原型验证。

---

## 📞 客服与销售自动化 (Support & Sales)

- [ ] [**Intercom Fin**](https://www.intercom.com/ai) - 2026 年企业级 AI 客服标标杆，能基于文档库自动解决 50% 以上的问题。
- [ ] [**Chatbase**](https://www.chatbase.co/) - 几分钟内通过网站 URL 训练出一个专属 AI 聊天机器人，独立开发者最爱。
- [ ] [**Clay**](https://www.clay.com/) - AI 驱动的销售线索获取与个性化外拓 (Outreach)，极大提升销售效率。
- [ ] [**Relevance AI**](https://relevanceai.com/) - 构建“AI 员工”集群，处理从调研到归档的完整业务链。

---

## 📂 知识管理与内部搜索 (RAG & Knowledge)

- [ ] [**Glean**](https://www.glean.com/) - 企业级 AI 搜索，连接 Slack, Drive, GitHub 等所有碎片化知识。
- [ ] [**Dust**](https://dust.tt/) - 针对初创团队的自定义 Agent 平台，强调与内部数据的深度集成。
- [ ] [**Mendable**](https://www.mendable.ai/) - 专注于为开发者文档提供 AI 问答服务。

---

## 📈 运维与质量监控 (Observability)

- [ ] [**Langfuse**](https://langfuse.com/) - 开源 LLM 观测平台，监控 Token 消耗、延迟及 Agent 的推理路径。
- [ ] [**Arize Phoenix**](https://phoenix.arize.com/) - 专注于 RAG 评估与嵌入空间可视化的开源工具。
- [ ] [**Helicone**](https://www.helicone.ai/) - 轻量级的 LLM 请求网关与可观测性面板。

---

## 💡 落地建议
1. **先从“小事”开始**：先用 Agent 自动化你的**客户常见问题 (FAQ)**。
2. **重视数据质量**：RAG 的效果 80% 取决于你的知识库清洗程度。
3. **安全与权限**：在给 Agent 开启“写权限”（如自动发推、自动退款）前，务必加入 **Human-in-the-loop** 审核环节。
4. **统一协议**：尽可能集成 **MCP Server**，让你的 Agent 具备读写本地文件或调用 API 的“手脚”。
