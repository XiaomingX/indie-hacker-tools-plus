# 机器学习核心资源 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年的机器学习已进入 **"AI Engineering"** 时代。
> - **不必从头开始**：利用 **Hugging Face** 的预训练模型进行微调，而非从零训练。
> - **端侧优先**：利用 **Apple MLX** 或 **Mojo** 在本地硬件上实现极速推理。

---

## 🐍 Python 核心生态 (Python Ecosystem)

- [ ] [**PyTorch**](https://github.com/pytorch/pytorch) - 2026 年科研与工业界的事实标准，生态最完整。
- [ ] [**Scikit-Learn**](https://scikit-learn.org/) - 传统机器学习（回归、聚类、SVM）的不可替代方案。
- [ ] [**Hugging Face Transformers**](https://github.com/huggingface/transformers) - 访问所有主流大模型（LLM, Vision, Audio）的统一入口。
- [ ] [**JAX**](https://github.com/google/jax) - Google 出品的高性能数值计算库，适合前沿算法开发。
- [ ] [**PyTorch Lightning**](https://github.com/PyTorchLightning/pytorch-lightning) - 极简的 PyTorch 封装，让训练代码更整洁、可移植。
- [ ] [**XGBoost / LightGBM**](https://github.com/dmlc/xgboost) - 处理表格数据的王者，依然是 Kaggle 竞赛的首选。

---

## 🏎️ 推理加速与部署 (Inference & Deployment)

- [ ] [**vLLM**](https://github.com/vllm-project/vllm) - 极高吞吐量的 LLM 服务引擎。
- [ ] [**TensorRT (NVIDIA)**](https://developer.nvidia.com/tensorrt) - 针对 NVIDIA GPU 的终极加速方案。
- [ ] [**MLX (Apple)**](https://github.com/ml-explore/mlx) - 专门为 Apple Silicon 优化的机器学习框架。
- [ ] [**Triton Inference Server**](https://github.com/triton-inference-server/server) - 支持多种后端、多模型的企业级部署平台。

---

## 🛠️ 计算机视觉与 NLP (CV & NLP)

- [ ] [**OpenCV**](https://opencv.org/) - 计算机视觉领域的基石。
- [ ] [**Detectron2 (FAIR)**](https://github.com/facebookresearch/detectron2) - 目标检测与分割的顶级框架。
- [ ] [**spaCy**](https://github.com/explosion/spaCy) - 工业级的自然语言处理库，速度极快。
- [ ] [**NLTK**](https://www.nltk.org/) - 经典的自然语言处理教学与研究平台。

---

## 🍎 移动端与边缘计算 (Mobile & Edge)

- [ ] [**CoreML (Apple)**](https://developer.apple.com/machine-learning/core-ml/) - 苹果全家桶设备的 AI 动力源。
- [ ] [**TensorFlow Lite**](https://www.tensorflow.org/lite) - 跨平台移动端推理。
- [ ] [**MNN (Alibaba)**](https://github.com/alibaba/MNN) - 针对移动端优化的轻量级推理引擎。

---

## 📚 学习资源与实战 (Learning)

- [x] **Fast.ai**: 依然是最好的“自上而下”机器学习课程。
- [x] **Machine Learning Mastery**: 充满实战代码的博客与电子书。
- [x] **Kaggle**: 通过竞赛实战提升数据处理与模型调优能力。

---

## 💡 选型建议
1. **深度学习研究**：首选 **PyTorch**。
2. **处理表格类业务数据**：**Scikit-Learn** + **XGBoost**。
3. **在 iPhone 上运行模型**：**CoreML**。
4. **极致性能的数值模拟**：**JAX**。
