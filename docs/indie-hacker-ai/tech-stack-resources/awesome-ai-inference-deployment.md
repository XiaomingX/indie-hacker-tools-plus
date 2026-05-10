# Awesome AI 模型推理部署框架精选 (2026 Checklist)

> [!IMPORTANT]
> **2026 部署核心**：推理不仅是运行，更是**极致压缩与异构加速**。独立开发者应优先关注 **vLLM** (大模型) 和 **SGLang** (高吞吐)，移动端则首选 **MNN 2.0** 或 **NCNN**。

---

## 🏗️ 主流推理框架选型 (Inference Frameworks)

- [ ] [**vLLM**](https://github.com/vllm-project/vllm) - 2026 年大模型推理的工业标准，支持 PagedAttention 和 FP8 量化，吞吐量极高。
- [ ] [**SGLang**](https://github.com/sgl-project/sglang) - 针对复杂 Prompt 和结构化输出优化的推理引擎，比 vLLM 在特定场景下更快。
- [ ] [**TensorRT / TensorRT-LLM (NVIDIA)**](https://developer.nvidia.com/tensorrt) - NVIDIA 硬件上的性能天花板，支持 Blackwell 架构的极致加速。
- [ ] [**OpenVINO (Intel)**](https://docs.openvino.ai/) - Intel CPU/GPU/NPU 的部署首选，特别适合边缘计算和工业质检。
- [ ] [**ONNX Runtime (Microsoft)**](https://onnxruntime.ai) - 跨平台、跨硬件的“万能钥匙”，支持从 Web 到移动端的所有场景。
- [ ] [**MNN (Alibaba)**](https://github.com/alibaba/MNN) - 移动端推理的佼佼者，2026 年已进化到 2.0 版本，支持极其强大的异构计算调度。
- [ ] [**NCNN (Tencent)**](https://github.com/Tencent/ncnn) - 极致精简，无第三方依赖，是嵌入式与微型设备部署的最佳选择。

---

## 🛠️ 模型转换与压缩工具 (Conversion & Compression)

- [ ] [**ONNX Simplifier**](https://github.com/daquexian/onnx-simplifier) - 去除模型冗余节点，减小体积并提升推理稳定性。
- [ ] [**Netron**](https://netron.app/) - 模型结构可视化神器，支持 2026 年所有主流模型格式。
- [ ] [**AutoGPTQ / AutoAWQ**](https://github.com/AutoGPTQ/AutoGPTQ) - 大模型 4-bit 量化的标准工具，在不损失精度的前提下大幅降低显存占用。
- [ ] [**Unsloth**](https://unsloth.ai/) - 2026 年微调与导出大模型的最快路径，支持一键导出各种量化格式。

---

## 💡 独立开发者实践建议

- [x] **如果是开发大模型应用**：首选 **vLLM** 部署在 Linux GPU 服务器上。
- [x] **如果是开发端侧 AI (iOS/Android)**：首选 **MNN** 或 **CoreML/TFLite**。
- [x] **如果是开发跨平台桌面应用**：首选 **ONNX Runtime**。
- [x] **如果是追求极致性能 (NVIDIA)**：必须学习 **TensorRT** 算子优化。

---

## 📂 关键概念：ONNX (开放神经网络交换)

- [x] **中立性**：由微软/Meta 发起，打破了训练框架与硬件之间的壁垒。
- [x] **互操作性**：PyTorch 训练 -> 转 ONNX -> 部署到各种推理引擎。
- [x] **生态完备**：2026 年几乎所有 AI 芯片都有对应的 ONNX 执行提供者 (EP)。
