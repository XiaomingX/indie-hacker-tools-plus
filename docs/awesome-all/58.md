# 优秀的 Gaussian Splatting 资源

一个精选的 Gaussian Splatting 资源列表，受到 awesome-computer-vision 的启发。

## 简介

Gaussian Splatting 是一种创新的技术，它结合了显式 3D 场景表示（如网格和点）和连续表示（如神经辐射场，NeRF）的优势。通过引入 3D 高斯，这种方法实现了灵活且具有表现力的场景表示，支持 1080p 分辨率下的高质量实时渲染。此外，该方法还优化了训练速度，非常适合从多张照片生成复杂场景的实时渲染。

## 快速链接

- **必读论文**：[3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)
- **精彩视频**：[3D Gaussian Splatting 简介](https://youtu.be/T_kXY43VZnk?si=DrkbDFxQAv5scQNT)
- **实现代码**：[C++ 和 CUDA 实现的 3D Gaussian Splatting](https://github.com/MrNeRF/gaussian-splatting-cuda)
- **入门介绍**：[博客：3D Gaussian Splatting 介绍](https://huggingface.co/blog/gaussian-splatting)
- **两分钟入门视频**：[3D Gaussian Splatting - 改变图像技术的未来](https://www.youtube.com/watch?v=HVv_IQKlafQ)

## 最新更新

- **2023年11月1日**：增加了入门友好的 GS 内容
- **2023年10月31日**：新增论文：4D Gaussian Splatting 用于实时动态场景渲染
- **2023年10月30日**：新增常见问题解答部分

## 相关论文

### 开创性的 3D Gaussian Splatting 论文
- [3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)  
  作者：Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis  
  描述：该论文提出了一种使用 3D 高斯的快速渲染方法，实现了 1080p 分辨率下的高质量实时视图合成。  
  [📄 低分辨率论文](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_low.pdf)  
  [📄 高分辨率论文](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/3d_gaussian_splatting_high.pdf)  
  [🌐 项目页面](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)  
  [💻 代码](https://github.com/graphdeco-inria/gaussian-splatting)  
  [🎥 简短介绍视频](https://youtu.be/T_kXY43VZnk?si=DrkbDFxQAv5scQNT)

### 动态 3D Gaussian Splatting
- [Dynamic 3D Gaussians: Tracking by Persistent Dynamic View Synthesis](https://dynamic3dgaussians.github.io/paper.pdf)  
  作者：Jonathon Luiten, Georgios Kopanas 等  
  描述：此论文提出了一种同时实现动态场景视图合成和场景元素跟踪的方法。  
  [📄 论文](https://dynamic3dgaussians.github.io/paper.pdf)  
  [🌐 项目页面](https://dynamic3dgaussians.github.io/)  
  [💻 代码](https://github.com/JonathonLuiten/Dynamic3DGaussians)  
  [🎥 解释视频](https://www.youtube.com/live/hDuy1TgD8I4?si=6oGN0IYnPRxOibpg)

### 4D Gaussian Splatting
- [4D Gaussian Splatting for Real-Time Dynamic Scene Rendering](https://arxiv.org/pdf/2310.08528.pdf)  
  作者：Guanjun Wu, Taoran Yi 等  
  描述：该论文介绍了一种 4D Gaussian Splatting 方法，用于实时渲染动态场景，具有效率和高分辨率（800*800 下达到 70 FPS）。  
  [📄 论文](https://arxiv.org/pdf/2310.08528.pdf)  
  [🌐 项目页面](https://guanjunwu.github.io/4dgs/)  
  [💻 代码](https://github.com/hustvl/4DGaussians)

## 实现

- [实时辐射场渲染的 3D Gaussian Splatting](https://github.com/graphdeco-inria/gaussian-splatting)
- [使用 Gaussian Splatting 的文本到 3D 转换](https://github.com/gsgen3d/gsgen)
- [DreamGaussian: 高效 3D 内容创建](https://github.com/dreamgaussian/dreamgaussian)

## 常见问题

### 什么是 3D Gaussian Splatting？
- **答**：3D Gaussian Splatting 是一种新技术，用于实现 3D 场景的高质量实时渲染。它通过使用 3D 高斯来实现灵活且高效的场景表示。

### 3D Gaussian Splatting 与传统的 3D 场景表示有何不同？
- **答**：传统的 3D 场景表示（如网格和点）适合快速的 GPU 渲染，但缺乏连续性。而 3D Gaussian Splatting 结合了显式表示的效率和连续表示的优点，提供了更好的视觉效果。

以上是对 Gaussian Splatting 技术和资源的简化描述，希望对您理解这个前沿技术有所帮助。
