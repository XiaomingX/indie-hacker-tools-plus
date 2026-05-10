# PyTorch 核心资源 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年的 PyTorch 开发已进入 **"Compilation First"** 阶段。
> - **性能提升**：务必尝试 `torch.compile()`，在 2026 年它能为大多数模型带来 20%~50% 的原生加速。
> - **端侧部署**：利用 **ExecuTorch** 将模型运行在手机与嵌入式设备上。

---

## 📝 自然语言处理 (NLP)

- [ ] [**Transformers (HuggingFace)**](https://github.com/huggingface/transformers) - 2026 年依然是 NLP 领域的终极入口。
- [ ] [**Fairseq**](https://github.com/facebookresearch/fairseq) - 序列建模与机器翻译的研究级框架。
- [ ] [**NeuralCoref**](https://github.com/huggingface/neuralcoref) - 基于 spaCy 的指代消解工具。
- [ ] [**Tokenizers**](https://github.com/huggingface/tokenizers) - 极速的文本分词库。

---

## 📷 计算机视觉 (CV)

- [ ] [**Torchvision**](https://github.com/pytorch/vision) - 官方视觉库，包含基础模型与变换。
- [ ] [**Detectron2 (FAIR)**](https://github.com/facebookresearch/detectron2) - 目标检测与实例分割的标杆。
- [ ] [**Kornia**](https://github.com/kornia/kornia) - 可微分的计算机视觉算法库，适合神经网络集成。
- [ ] [**Albumentations**](https://github.com/albumentations-team/albumentations) - 性能最强的图像增强库。
- [ ] [**PyTorch3D**](https://github.com/facebookresearch/pytorch3d) - 3D 深度学习的研究利器。

---

## 🎙️ 语音与音频 (Speech & Audio)

- [ ] [**SpeechBrain**](https://github.com/speechbrain/speechbrain) - 一站式开源语音工具包。
- [ ] [**Torchaudio**](https://github.com/pytorch/audio) - 官方音频处理库。
- [ ] [**ESPnet**](https://github.com/espnet/espnet) - 端到端语音处理的强大框架。

---

## 🛠️ 训练框架与工具 (Training & Frameworks)

- [ ] [**PyTorch Lightning**](https://github.com/Lightning-AI/lightning) - 让你的 PyTorch 代码更规范、更强大。
- [ ] [**Fast.ai**](https://github.com/fastai/fastai) - 极简的高层封装，适合快速实验。
- [ ] [**TorchMetrics**](https://github.com/PyTorchLightning/metrics) - 统一的模型评估指标库。
- [ ] [**DeepSpeed**](https://github.com/microsoft/DeepSpeed) - 分布式训练与大规模模型优化的标配。

---

## 📈 图神经网络 (GNN)

- [ ] [**PyG (PyTorch Geometric)**](https://github.com/pyg-team/pytorch_geometric) - 图深度学习的事实标准。
- [ ] [**DGL (Deep Graph Library)**](https://github.com/dmlc/dgl) - 另一个高性能图神经网络框架。

---

## 📚 教程与进阶 (Learning)

- [x] **PyTorch Tutorials**: 官方从入门到精通的系列文档。
- [x] **Dive into Deep Learning (d2l.ai)**: 互动式深度学习教材。
- [x] **ExecuTorch Documentation**: 学习如何将模型部署到边缘端。

---

## 💡 选型建议
1. **追求极致开发效率**：选 **Fast.ai**。
2. **构建企业级生产管道**：选 **PyTorch Lightning**。
3. **处理海量多模态数据**：集成 **Transformers**。
4. **移动端 AI 应用**：重点研究 **ExecuTorch**。
