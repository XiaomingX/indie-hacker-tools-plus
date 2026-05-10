# 神经渲染 (NeRF & 3DGS) 资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，3D 建模的范式已从“手动雕刻”转向“AI 重建”。
> - **技术路线**：NeRF (Neural Radiance Fields) 擅长隐式表达和照片级渲染，而 **3DGS (3D Gaussian Splatting)** 则是目前的实时渲染王者。
> - **商业机会**：利用手机拍摄一段视频，通过 **Luma AI** 或 **Instant-NGP** 快速生成可交互的 3D 资产，是电商、房产展示的降本利器。

---

## 🏗️ 核心框架与实时引擎 (Core Engines)

- [ ] [**3D Gaussian Splatting (3DGS)**](https://github.com/graphdeco-inria/gaussian-splatting) - **2026 标配**。目前最高效的神经渲染技术，支持 144FPS+ 的实时交互。
- [ ] [**Instant-NGP**](https://github.com/NVlabs/instant-ngp) - NVIDIA 出品，通过多分辨率哈希编码将 NeRF 训练时间从数小时缩短至数秒。
- [ ] [**NerfStudio**](https://github.com/nerfstudio-project/nerfstudio) - 最适合开发者的框架，模块化设计，支持多种 NeRF 变体的一键训练与可视化。
- [ ] [**TensoRF**](https://github.com/apchenstu/TensoRF) - 利用张量分解极大压缩了模型体积，适合在移动端部署。

---

## 🧠 关键研究方向 (Research Frontiers)

- [ ] [**4D-NeRF / Dynamic Scenes**](https://github.com/facebookresearch/4D-NeRF) - 解决运动物体（如人体、流水）的 3D 重建难题。
- [ ] [**Few-shot NeRF**](https://github.com/ajayjain/DietNeRF) - 研究如何仅通过 3-5 张照片就能还原高保真场景（DietNeRF）。
- [ ] [**NeRF-Art**](https://github.com/bytedance/NeRF-Art) - 字节跳动出品，实现文本驱动的 3D 场景风格化修改。
- [ ] [**Mip-NeRF 360**](https://jonbarron.info/mipnerf360/) - 专门针对大范围、无边界真实场景优化的渲染技术。

---

## 📂 数据集与工具 (Datasets & Tools)

- [ ] [**Luma AI**](https://lumalabs.ai/) - 目前最好用的消费级 App，手机拍摄即可生成高质量 NeRF/3DGS 模型。
- [ ] [**COLMAP**](https://colmap.github.io/) - **[必选]** 通用的运动恢复结构 (SfM) 工具，用于获取照片的位姿信息，是所有神经渲染的前置步骤。
- [ ] [**NeRF Official Datasets**](https://www.matthewtancik.com/nerf) - 包含合成场景 (Blender) 与真实场景 (LLFF) 的标准入门数据。
- [ ] [**Postman for 3D**](https://github.com/postman-open-source) - 辅助调试 3D API 的工具集。

---

## 🎥 入门与进阶课程 (Learning)

- [ ] [**李沐：NeRF 论文精读**](https://www.bilibili.com/video/BV1hM4y1F7hC/) - **[中文首选]** 深入浅出讲解 NeRF 与 3DGS 的数学原理与代码实现。
- [ ] [**CVPR Tutorial on Neural Rendering**](https://neuralrenderingsurvey.github.io/) - 计算机视觉顶会出品的权威教程。
- [ ] [**Awesome-NeRF Repo**](https://github.com/vsitzmann/awesome-implicit-representations) - 汇集了该领域几乎所有重要论文的清单。

---

## 💡 选型建议
1. **追求极致渲染速度**：选 **3D Gaussian Splatting**。
2. **需要精确的几何提取 (Mesh)**：结合 **VolSDF** 或 **NeuS** 方案。
3. **快速开发原型**：使用 **NerfStudio** 提供的命令行工具。
4. **移动端落地**：优先研究 **MobileNeRF** 或 **TensoRF** 压缩方案。
