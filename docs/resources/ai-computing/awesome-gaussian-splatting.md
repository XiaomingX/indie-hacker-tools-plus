# 3D Gaussian Splatting (3DGS) 技术与实战资源 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，3DGS 已成为**“实景 3D 重建”**的首选方案。
> - **实时性**：相比 NeRF，3DGS 的核心优势在于渲染极快（可在手机端达到 60FPS）。
> - **显存管理**：虽然渲染快，但高精度的高斯点云文件可能很大，务必使用 **Compressed 3DGS** 方案。
> - **物理引擎**：如果需要 3DGS 资产在游戏里产生物理碰撞，请关注 **PhysGaussian**。

---

## 🏗️ 核心论文与基石 (Foundational Papers)

- [ ] [**3D Gaussian Splatting (Original)**](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/) - 2023 年发布的开创性论文，定义了实时辐射场渲染的新范式。
- [ ] [**2D Gaussian Splatting**](https://surfacemesh.github.io/2dgs/) - 改进了物体表面的平滑度，特别适合生成具有准确法线的 3D 网格。
- [ ] [**SuGaR**](https://github.com/Antwo7/SuGaR) - **[网格化工具]** 实现了从 3D 高斯点云到高质量三角形网格 (Mesh) 的快速转换。
- [ ] [**4D Gaussian Splatting**](https://guanjunwu.github.io/4dgs/) - 针对动态场景（带时间维度）的实时渲染方案。

---

## 🛠️ 开源工具与实现 (Open Source Implementations)

- [ ] [**Post-process-3d-gaussian-splatting**](https://github.com/mkkellogg/GaussianSplats3D) - **[Web 端首选]** 基于 Three.js 的高性能 Web 渲染器，支持在大规模点云下保持流畅。
- [ ] [**NerfStudio**](https://github.com/nerfstudio-project/nerfstudio) - **[全能平台]** 虽然名字叫 NerfStudio，但它现在是训练、预览和对比 3DGS 模型最成熟的框架。
- [ ] [**GaussianSplatting-Unity**](https://github.com/aras-p/UnityGaussianSplatting) - 独立开发者将 3DGS 导入 Unity 游戏引擎的最佳插件。
- [ ] [**DreamGaussian**](https://github.com/dreamgaussian/dreamgaussian) - **[生成式 AI]** 结合扩散模型，实现从一张图在 2 分钟内生成高质量 3DGS 资产。

---

## 📂 扫描、处理与托管 (Scanning & Hosting)

- [ ] [**Luma AI**](https://lumalabs.ai/) - 手机端最成熟的 3DGS 采集 App，支持云端训练并导出 `.splat` 格式。
- [ ] [**Polycam**](https://poly.cam/) - 广泛用于建筑和房产扫描，支持最新的 3DGS 导出。
- [ ] [**PlayCanvas Viewer**](https://playcanvas.com/viewer) - 优秀的 Web 端 3DGS 预览器，支持实时调整视觉参数。

---

## 💡 选型建议
1. **构建网页端 3D 展厅**：选 **Luma AI 采集** + **Three.js (mkkellogg)** 渲染。
2. **需要模型参与游戏物理互动**：选 **SuGaR** 将高斯点云转化为 Mesh。
3. **追求极致的渲染质量**：使用 **Gaussian-Pro** 或 **Mip-Splatting**。
4. **节省带宽/首屏体积**：强制使用 **Compressed-3DGS** 插件。
