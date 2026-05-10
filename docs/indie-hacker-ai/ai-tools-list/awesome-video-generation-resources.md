# Awesome Video Generation 研究资源汇总 (2026 Checklist)

> [!IMPORTANT]
> **2026 视频生成趋势**：
> 1. **物理引擎化**：视频不再是“逐帧生成”，而是具备基础物理规律的“模拟”。
> 2. **长视频突破**：支持 2-5 分钟的连贯叙事，且角色一致性极佳。
> 3. **4D 生成**：从视频直接生成可交互的 4D 动态资产。

---

## 🎬 核心产品与工具 (Products & Tools)

- [ ] [**Sora (OpenAI)**](https://openai.com/sora) - 2026 年视频生成的旗舰，支持高度一致的长视频生成与多模态理解。
- [ ] [**Kling (可灵)**](https://klingai.com/) - 凭借卓越的运动控制与写实画质，成为全球视频生成赛道的顶级玩家。
- [ ] [**Luma Dream Machine**](https://lumalabs.ai/dream-machine) - 2026 年独立开发者最常用的工具，生成的物理动态极佳且 API 稳定。
- [ ] [**Runway Gen-3 Alpha / Gen-4**](https://runwayml.com/) - 提供了最细粒度的摄影机控制（Camera Control）与画质调节。
- [ ] [**Pika 2.0**](https://pika.art/) - 擅长动画风格与特殊物理效果（如膨胀、破碎、融化）的趣味视频生成。
- [ ] [**Adobe Firefly Video**](https://www.adobe.com/products/firefly.html) - 深度集成在 Premiere Pro 中，支持 AI 扩视频与一键转场特效。

---

## 🔬 核心论文与技术里程碑 (Key Milestones)

- [x] **2024-02 Sora Architecture** (OpenAI) - 引入 DiT (Diffusion Transformer) 架构，奠定大模型视频生成的基础。
- [x] **2025-06 DiS (Diffusion with Symmetry)** - 解决了长视频生成中的循环抖动问题。
- [x] **2026-01 WorldSim-V1** (Google) - 将视频生成与物理模拟引擎结合，实现符合重力与碰撞规律的画面。
- [x] **2026-05 SkyReels-V2** (Kunlun) - 全球首个支持无限时长电影生成的开源模型。

---

## 📊 评估指标与数据集 (Benchmarks & Datasets)

- [ ] [**VMBench**](https://arxiv.org/pdf/2503.10076v2) - 首个感知对齐的视频运动评估基准。
- [ ] [**MJ-Bench-Video**](https://arxiv.org/pdf/2502.01719v3) - 从对齐性、安全性、连贯性等五大维度评估视频生成。
- [ ] [**WebVid-10M**](https://maxbain.com/webvid-dataset/) - 大规模视频-文本对齐数据集。
- [ ] [**UCF101**](https://www.crcv.ucf.edu/data/UCF101.php) - 经典动作识别数据集。

---

## 💡 独立开发者建议
- [x] **快速原型**：使用 **Luma Dream Machine** 或 **Kling**。
- [x] **专业剪辑**：配合 **Adobe Firefly** 的内联功能。
- [x] **趣味短视频**：使用 **Pika 2.0** 的特效功能。
- [x] **长期研发**：关注 **Sora** 和 **SkyReels** 的开源动态。
