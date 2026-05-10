# Awesome DeepSeek & 独立开发实战 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: DeepSeek V3/R1 是 2026 年独立开发者的**性价比之王**。
> - **API 替代**: 在绝大多数非创意写作场景（如数据清洗、分类、代码重构）中，DeepSeek V3 可完美替代 GPT-4o，成本仅为其 1/10。
> - **本地部署**: 配合 Ollama 运行 DeepSeek-Coder-V2，是目前保护隐私且免费的最强 Copilot 方案。

---

## 🛠️ 桌面与移动端客户端 (Clients)

- [ ] [**Chatbox**](https://chatboxai.app/) - 全平台桌面客户端，独立开发者调试 API 的标杆工具。
- [ ] [**Cherry Studio**](https://cherrystudio.ai/) - 针对内容创作者优化的桌面 AI 助手，支持多模型并发。
- [ ] [**LibreChat**](https://www.librechat.ai/) - 极致自定义的开源聊天站，支持私有化部署。
- [ ] [**Pal - AI Chat (iOS)**](https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/pal/README.md) - 精美的 iOS 客户端，适配移动端 DeepSeek 体验。
- [ ] [**Liubai (微信)**](https://liubai.ai/) - 将微信变为你的个人 AI 助理，处理任务与日程。

---

## 💻 编程开发与 IDE (Coding)

- [ ] [**Cursor**](https://www.cursor.com/) - 2026 年最强 AI IDE，深度支持 DeepSeek V3/R1。
- [ ] [**Continue**](https://www.continue.dev/) - 开源的 IDE 助手，支持本地部署 DeepSeek 模型。
- [ ] [**Cline (原 Devin)**](https://github.com/cline/cline) - 高级编程 Agent，配合 DeepSeek API 可低成本执行复杂代码任务。
- [ ] [**Aider**](https://aider.chat/) - 命令行重构神器，完美适配 DeepSeek 极速模式。
- [ ] [**AutoDev (JetBrains)**](https://ide.unitmesh.cc/) - 专注于 Java/Kotlin 等生态的开源 AI 助手。

---

## 🌐 浏览器扩展与翻译 (Browser & Trans)

- [ ] [**沉浸式翻译 (Immersive Translate)**](https://immersivetranslate.com/) - 网页双语阅读标配，DeepSeek API 是其最推荐的翻译源。
- [ ] [**ChatGPT Box**](https://github.com/josStorer/chatgpt-box) - 在搜索结果侧边栏集成 DeepSeek，支持多平台一键切换。
- [ ] [**划词翻译 (hcfy)**](https://hcfy.app/) - 轻量级网页翻译插件，支持 API 自定义。

---

## 🏗️ 工作流与 RAG 框架 (Workflows & RAG)

- [ ] [**Dify**](https://dify.ai/) - 最流行的可视化 LLM 应用开发平台，内置 DeepSeek 全套支持。
- [ ] [**RAGFlow**](https://ragflow.io/) - 工业级 RAG 引擎，擅长处理复杂文档理解。
- [ ] [**n8n**](https://n8n.io/) - 自动化流程引擎，支持 DeepSeek 节点进行逻辑编排。
- [ ] [**Mem0**](https://mem0.ai/) - 为 AI 助手提供长期个性化记忆，支持 DeepSeek 存储。

---

## 📦 开发库与 SDK (SDKs)

- [ ] [**LiteLLM**](https://github.com/BerriAI/litellm) - 统一上百个模型 API，带成本跟踪。
- [ ] [**DeepSeek-PHP**](https://github.com/deepseek-php/deepseek-php-client) - 社区驱动的 PHP 客户端。
- [ ] [**promptfoo**](https://github.com/promptfoo/promptfoo) - 提示词测试与评估工具，帮助优化 DeepSeek 输出。

---

## 💡 实践建议
1. **优先使用 R1 进行推理**：在需要复杂逻辑推理的任务中，R1 的表现已逼近 OpenAI o1。
2. **长上下文管理**：DeepSeek 2026 版本已支持 128k+ 上下文，适合分析大型代码库。
3. **缓存命中**：合理利用 DeepSeek 的 Context Caching 功能，可进一步降低 50% 以上的 API 成本。
