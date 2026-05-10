# 合成数据 (Synthetic Data) 核心资源 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，合成数据已成为**解决冷启动问题**的关键。
> - **LLM 蒸馏**：利用 GPT-5 或 Claude 4 生成高质量的垂直领域问答对，用于训练更小、更快的本地模型。
> - **合规避风港**：在涉及医疗、金融数据时，使用合成数据可以彻底规避隐私泄露风险。

---

## 🏗️ 文本、表格与时序数据 (Structured Data)

- [ ] [**Gretel Synthetics**](https://github.com/gretelai/gretel-synthetics) - 支持差分隐私的高级合成数据框架，适合金融与医疗。
- [ ] [**SDV (Synthetic Data Vault)**](https://github.com/sdv-dev/SDV) - 专注于关系型数据库与复杂表格数据的生成。
- [ ] [**YData Synthetic**](https://github.com/ydataai/ydata-synthetic) - 集成了多种 GAN 与扩散模型，适合小样本扩充。
- [ ] [**Synthea**](https://synthea.mitre.org/) - 专门用于生成符合隐私规范的虚拟患者健康记录。

---

## 🎨 图像与多模态合成 (Vision & Multimodal)

- [ ] [**Hugging Face Diffusers**](https://github.com/huggingface/diffusers) - 工业级扩散模型库，图像合成的首选。
- [ ] [**ControlNet**](https://github.com/lllyasviel/ControlNet) - 实现对生成图像布局、姿态、边缘的精确控制。
- [ ] [**NVIDIA Isaac Sim**](https://developer.nvidia.com/isaac-sim) - 高精度的物理仿真环境，用于生成机器人与自动驾驶训练数据。
- [ ] [**Unity Perception**](https://github.com/Unity-Technologies/com.unity.perception) - 基于 Unity 引擎的感知数据合成工具。

---

## 🎙️ 语音与音频合成 (Audio)

- [ ] [**ElevenLabs**](https://elevenlabs.io/) - 2026 年拟人化语音生成的巅峰工具。
- [ ] [**MusicGen (Meta)**](https://github.com/facebookresearch/audiocraft) - 通过文本直接生成高保真音乐与环境音效。
- [ ] [**VITS**](https://github.com/jaywalnut310/vits) - 优秀的开源语音合成模型。

---

## 📚 学习与评估 (Learning & Evaluation)

- [x] **Annotated Diffusion**: 逐行拆解扩散模型原理的硬核教程。
- [x] **Gretel AI Blog**: 了解合成数据在企业级隐私保护中的最佳实践。
- [x] **Hugging Face Datasets**: 查找开源的合成数据集（如 `synthetic_finance`）。

---

## 💡 选型建议
1. **训练垂直领域小模型**：利用大模型生成合成语料进行蒸馏。
2. **测试数据库性能**：使用 **SDV** 生成千万级仿真数据。
3. **开发计算机视觉算法**：使用 **Unity Perception** 或 **Isaac Sim**。
4. **提升推荐系统准确度**：使用 **ydata-synthetic** 扩充长尾用户行为数据。
