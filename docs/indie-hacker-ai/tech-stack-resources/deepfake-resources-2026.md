# Deepfake 核心资源 (2026 Checklist)

> [!WARNING]
> **道德与法律声明**：
> - **严禁恶意用途**：禁止利用此类技术进行诈骗、诽谤或制作未经许可的成人内容。
> - **合规标注**：2026 年多数平台要求 AI 生成内容必须附带显式水印或标注。
> - **隐私保护**：在使用他人面部/声音数据前，必须获得书面授权。

---

## 🛠️ 开源工具与项目 (Projects)

- [ ] [**Faceswap**](https://github.com/deepfakes/faceswap) - 经典的人脸替换框架，GUI 友好，适合新手。
- [ ] [**DeepFaceLab**](https://github.com/iperov/DeepFaceLab) - 行业标杆，支持高精度的模型训练与自定义遮罩。
- [ ] [**DeepFaceLive**](https://github.com/iperov/DeepFaceLive) - 针对直播与视频通话优化的实时换脸工具。
- [ ] [**SimSwap**](https://github.com/neuralchen/SimSwap) - 专注于高效、高保真的身份嵌入交换机制。
- [ ] [**Easy-Wav2Lip**](https://github.com/Rudrabha/Wav2Lip) - 极致的音唇同步（Lip Sync）工具，让图片或视频开口说话。
- [ ] [**Facerender (SadTalker)**](https://github.com/OpenTalker/SadTalker) - 通过单张图片和音频生成逼真的头部动画。

---

## 🛡️ 检测与防御 (Detection & Defense)

- [ ] [**Reality Defender**](https://www.realitydefender.com/) - 2026 年企业级全模态（文、图、音、视）伪造检测首选。
- [ ] [**Sentinel**](https://www.sentinel-ai.io/) - 针对虚假信息与深度伪造的实时监测平台。
- [ ] [**Disrupting Deepfakes**](https://github.com/natanielruiz/disrupting-deepfakes) - 研究如何通过添加“扰动”来防止自己的照片被 AI 伪造。
- [ ] [**FaceForensics++**](https://github.com/ondyari/FaceForensics++) - 权威的伪造检测基准数据集与模型。

---

## 🔬 核心研究论文 (Papers)

- [x] **2021 SimSwap**: 实现了高保真的实时人脸交换。
- [x] **2023 ViT for Detection**: 利用 Vision Transformer 提升检测的泛化能力。
- [x] **2025 Neural Radiance Fields (NeRF) in Deepfakes**: 利用神经辐射场技术提升伪造的 3D 一致性。

---

## 💡 独立开发者建议
1. **影视后期/创意制作**：选 **DeepFaceLab** 或 **SadTalker**。
2. **实时互动/直播特效**：选 **DeepFaceLive**。
3. **内容安全校验**：集成 **Sentinel** 或 **Reality Defender** 的 API。
4. **快速制作 AI 播报视频**：使用 **Wav2Lip**。
