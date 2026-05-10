# 2026 Mamba 与状态空间模型 (SSM) 研究指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Mamba 架构已成为 Transformer 的强力竞争者，特别是在长文本处理和端侧模型领域。
> - **长文本优势**：Mamba 具有线性缩放的推理时间，处理 100k+ token 的成本远低于传统 Transformer。
> - **端侧部署**：由于其常数级的内存占用（Constant State），Mamba 极度适合在手机、IoT 等内存受限设备上运行。
> - **研究趋势**：重点关注混合架构（如 Jamba），它结合了 Transformer 的注意力机制与 Mamba 的高效序列处理。

---

## 🏗️ 核心论文与理论 (Core Research)

- [ ] [**Mamba: Linear-Time Sequence Modeling with Selective State Spaces**](https://arxiv.org/abs/2312.00752) - **[必读]** 奠基性论文，提出了选择性状态空间机制。
- [ ] [**Efficiently Modeling Long Sequences with Structured State Spaces (S4)**](https://arxiv.org/abs/2111.00396) - 了解 Mamba 的前身——结构化状态空间模型。
- [ ] [**Jamba: A Hybrid Transformer-Mamba Language Model**](https://arxiv.org/abs/2403.19829) - 探索混合架构如何平衡表达能力与推理效率。
- [ ] [**MambaByte: Token-free Selective State Space Model**](https://arxiv.org/abs/2401.13660) - 针对字节级长序列建模的研究。

---

## 🛠️ 代码实现与模型 (Implementations & Models)

- [ ] [**Mamba 官方仓库 (CUDA 优化版)**](https://github.com/state-spaces/mamba) - 包含极速的 CUDA 核，生产环境必备。
- [ ] [**Zyphra/Zamba**](https://github.com/Zyphra/Zamba) - 预训练的 Mamba 7B 模型，在多项基准测试中优于 Llama 系列。
- [ ] [**AI21 Labs / Jamba-v0.1**](https://huggingface.co/ai21labs/Jamba-v0.1) - 首个大规模商用的混合架构模型。
- [ ] [**Mamba-minimal (PyTorch)**](https://github.com/johnma2006/mamba-minimal) - 适合初学者理解底层算法逻辑的极简实现。

---

## 🚀 实战与优化 (Optimization & Practice)

- [ ] [**Mamba 推理加速 (Flash-Mamba)**](https://github.com/state-spaces/mamba) - 利用 GPU 的 SRAM 缓存提升序列处理速度。
- [ ] [**端侧量化与蒸馏**](https://github.com/state-spaces/mamba/tree/main/benchmarks) - 学习如何将 Mamba 模型压缩至 1B 甚至更小，部署在边缘端。
- [ ] [**长文本 RAG 适配**](https://github.com/state-spaces/mamba) - 利用 Mamba 的线性注意力机制提升 RAG 系统的检索上下文长度。

---

## 💡 选型建议
1. **构建极长上下文的应用 (如分析整本书)**：优先考虑 **Mamba** 或 **Jamba** 架构。
2. **手机端实时语音/文字助理**：选 **Mamba 1B-3B** 系列模型。
3. **需要极高推理吞吐量的 SaaS**：切换至 **Mamba** 后端可大幅降低 H100 租用成本。
4. **科研探索**：重点研究 **Linear Attention** 与 **State Space Model** 的融合点。
