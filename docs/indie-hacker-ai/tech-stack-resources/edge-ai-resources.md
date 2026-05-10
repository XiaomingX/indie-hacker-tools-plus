# 边缘 AI (Edge AI) 核心资源 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年的边缘 AI 不再只是简单的视觉识别，**边缘侧大模型 (Edge LLM)** 已成为新战场。
> - **手机端推理**：利用 **MNN 2.0** 或 **CoreML** 在用户手机上运行千亿级参数模型的精简版。
> - **端云协同**：敏感数据在边缘侧处理（使用 **llama.cpp**），复杂逻辑请求云端。

---

## 🔌 核心硬件平台 (Hardware)

- [ ] [**NVIDIA Jetson Orin 系列**](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/) - 边缘计算的性能标杆，支持运行复杂的生成式 AI 模型。
- [ ] [**Google Coral (Edge TPU)**](https://coral.ai/) - 高效能、低功耗的 ASIC 加速器，适合快速视觉推理。
- [ ] [**Apple Neural Engine (M4/A18)**](https://developer.apple.com/machine-learning/) - 通过 CoreML 调动苹果芯片的强大 AI 算力。
- [ ] [**ESP32-S3/P4**](https://www.espressif.com/en/products/socs/esp32-s3) - 极低成本的入门级 AI 芯片，适合简单的语音唤醒与视觉触发。
- [ ] [**瑞芯微 RK3588**](https://www.rock-chips.com/) - 国产高性能 SoC，广泛应用于智能座舱与机器人控制。

---

## ⚙️ 边缘推理框架 (Inference Engines)

- [ ] [**MNN 2.0 (Alibaba)**](https://github.com/alibaba/MNN) - 2026 年移动端推理的首选，针对大模型（LLM）进行了深度优化。
- [ ] [**llama.cpp**](https://github.com/ggerganov/llama.cpp) - 边缘侧运行 LLM 的事实标准，支持多种量化格式与硬件加速。
- [ ] [**TensorFlow Lite**](https://www.tensorflow.org/lite) - 跨平台嵌入式推理的老牌劲旅，支持从手机到 MCU 的全场景。
- [ ] [**ONNX Runtime Edge**](https://onnxruntime.ai/) - 极佳的跨平台兼容性，支持所有主流模型格式。
- [ ] [**CoreML (Apple)**](https://developer.apple.com/documentation/coreml) - 苹果生态开发者的必选，极致利用硬件加速。

---

## 🛠️ 开发工具与平台 (Dev Tools)

- [ ] [**Edge Impulse**](https://www.edgeimpulse.com/) - 最成熟的 TinyML 开发平台，支持从数据采集到模型部署的全流程。
- [ ] [**uTVM**](https://tvm.apache.org/) - 深度优化的模型编译器，适合需要极致算力的定制化硬件。
- [ ] [**DeepView**](https://www.nxp.com/design/software/development-software/deepview-ai-tool-suite:DEEPVIEW-AI-TOOL-SUITE) - NXP 提供的专业边缘 AI 开发套件。

---

## 📚 学习与基准测试 (Learning & Bench)

- [x] **MLPerf Tiny**: 全球权威的边缘 AI 性能评测基准。
- [x] **TinyML Summit**: 关注低功耗边缘 AI 的顶级行业峰会。
- [x] **Awesome Edge AI**: 持续更新的 GitHub 资源合集。

---

## 💡 选型建议
1. **构建手机端 AI App**：首选 **MNN 2.0** 或 **CoreML**。
2. **开发智能硬件/机器人**：推荐 **NVIDIA Jetson** + **llama.cpp**。
3. **极低成本 IoT 设备**：使用 **ESP32-S3** + **TensorFlow Lite Micro**。
4. **需要快速落地生产线**：使用 **Edge Impulse** 缩短开发周期。
