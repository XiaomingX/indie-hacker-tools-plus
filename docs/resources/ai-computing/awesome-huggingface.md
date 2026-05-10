# Hugging Face 生态实战手册 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Hugging Face 已成为 AI 界的 **"GitHub + Docker Hub"**。
> - **不要重新发明轮子**：在开始训练前，先在 [HF Models](https://huggingface.co/models) 寻找是否已有经过微调的 SOTA 模型。
> - **Serverless 优先**：利用 [HF Inference Endpoints](https://huggingface.co/inference-endpoints) 实现秒级部署，按量计费。

---

## 🛠️ 核心官方库 (Core Libraries)

- [ ] [**Transformers**](https://github.com/huggingface/transformers) - 2026 年依然是 AI 开发的核心，支持 Jax, PyTorch 和 TensorFlow 的统一接口。
- [ ] [**Datasets**](https://github.com/huggingface/datasets) - 极速加载海量数据，支持流式读取（Streaming），解决硬盘不足问题。
- [ ] [**Tokenizers**](https://github.com/huggingface/tokenizers) - Rust 编写的高性能分词器，支持现代 LLM 的所有编码需求。
- [ ] [**Accelerate**](https://github.com/huggingface/accelerate) - 仅需数行代码即可让代码在多 GPU、TPU 或混合精度下运行。
- [ ] [**PEFT**](https://github.com/huggingface/peft) - **必选**。参数高效微调（LoRA, QLoRA），让消费级显卡也能微调百亿参数模型。
- [ ] [**TRL (Transformer Reinforcement Learning)**](https://github.com/huggingface/trl) - 训练 DPO, PPO 等对齐任务的标准库。

---

## 🚀 推理与部署优化 (Inference & Deployment)

- [ ] [**TGI (Text Generation Inference)**](https://github.com/huggingface/text-generation-inference) - 官方高性能推理后端，支持流式输出与连续批处理。
- [ ] [**Sentence Transformers**](https://github.com/UKPLab/sentence-transformers) - RAG 应用的基石，生成高质量的语义向量。
- [ ] [**vLLM**](https://github.com/vllm-project/vllm) - 兼容 HF 格式的最强推理引擎，极致的吞吐量优化。
- [ ] [**Optimum**](https://github.com/huggingface/optimum) - 针对 ONNX, OpenVINO, TensorRT 等特定硬件的加速接口。

---

## 🏗️ 应用与架构 (Application Frameworks)

- [ ] [**Gradio**](https://github.com/gradio-app/gradio) - 几行代码生成 AI 演示 Web UI，并可一键部署至 HF Spaces。
- [ ] [**Haystack**](https://github.com/deepset-ai/haystack) - 构建企业级问答系统与 Agent 的成熟框架。
- [ ] [**LangChain / LlamaIndex**](https://huggingface.co/docs/transformers/index) - 虽然是外部项目，但与 HF 深度集成，是构建 RAG 的首选。

---

## 🎓 学习与社区 (Community)

- [ ] [**Hugging Face Course**](https://huggingface.co/course) - 官方免费课程，从基础到进阶的最佳路径。
- [ ] [**HF Hub**](https://huggingface.co/hub) - 掌握模型版本管理、数据集托管及 Space 应用预览。
- [ ] [**Daily Papers**](https://huggingface.co/papers) - 每日必看，追踪 AI 领域最新的学术动态。

---

## 💡 选型建议
1. **构建 RAG 系统**：选 **Sentence Transformers (Embedding)** + **vLLM (Inference)**。
2. **在 4090 上微调 70B 模型**：选 **Accelerate** + **PEFT (QLoRA)**。
3. **快速展示 Demo**：选 **Gradio** + **HF Spaces**。
4. **边缘设备部署**：使用 **Optimum** 转化为 **ONNX** 格式。
