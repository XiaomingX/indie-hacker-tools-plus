# WebGPU 高性能前端开发资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，WebGPU 已彻底取代 WebGL，成为浏览器端高性能渲染与 **"端侧 AI 推理"** 的核心引擎。
> - **超越渲染**：不要只把 WebGPU 当作 3D 引擎，它的 **Compute Shader** 才是真正的杀手锏，能让你的浏览器应用直接调用本地 GPU 进行复杂的矩阵运算。
> - **跨平台统一**：通过 **wgpu (Rust)**，你可以编写一套代码，同时在 Web、桌面和移动原生端以近乎原生的性能运行。
> - **端侧 AI**：配合 **WebLLM** 或 **Transformers.js**，可以在不依赖后端算力的情况下，在用户浏览器中本地运行 LLM。

---

## 🏗️ 官方标准与核心文档 (Core & Standards)

- [ ] [**WebGPU 官方说明 (Explainer)**](https://gpuweb.github.io/gpuweb/explainer/) - 快速理解 WebGPU 的设计理念与核心概念。
- [ ] [**WebGPU API 参考 (MDN)**](https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API) - **[必备]** 详细的接口定义与参数说明。
- [ ] [**WGSL 着色语言规范**](https://gpuweb.github.io/gpuweb/wgsl/) - 学习 WebGPU 专用的着色语言，语法现代且类型安全。

---

## ⚡ 框架、引擎与 AI 集成 (Engines & AI)

- [ ] [**Babylon.js**](https://www.babylonjs.com/) - 对 WebGPU 支持最完善的商业级 3D 引擎，开箱即用。
- [ ] [**Three.js (WebGPURenderer)**](https://threejs.org/examples/?q=webgpu) - 轻量级 Web 3D 事实标准，现已全面转向 WebGPU 渲染器。
- [ ] [**wgpu (Rust)**](https://github.com/gfx-rs/wgpu) - 跨平台的 WebGPU 原生实现，支持 Rust 开发者构建高性能游戏与工具。
- [ ] [**WebLLM**](https://github.com/mlc-ai/web-llm) - 利用 WebGPU 在浏览器中本地运行像 Llama 3 或 Mistral 这样的大模型。

---

## 🛠️ 效率工具与学习资源 (Tooling & Learning)

- [ ] [**WebGPU Samples**](https://webgpu.github.io/webgpu-samples/) - **[必看]** 官方示例集，涵盖从基础渲染到复杂计算的所有核心场景。
- [ ] [**Tour of WGSL**](https://google.github.io/tour-of-wgsl/) - 交互式的 WGSL 学习路径，非常适合初学者。
- [ ] [**Online WGSL Editor**](https://takahirox.github.io/online-wgsl-editor/) - 浏览器中的着色器实验沙箱，实时预览效果。
- [ ] [**WebGPU Inspector**](https://github.com/brendan-duncan/webgpu-inspector) - 浏览器扩展插件，深度调试 WebGPU 资源、管线与命令流。

---

## 🔬 实验性案例 (Experiments)

- [ ] [**WebGPU Fluid Simulation**](https://kishimisu.github.io/WebGPU-Fluid-Simulation/) - 展示超高性能的实时物理流体仿真。
- [ ] [**WebGPU Particles**](https://hsimpson.github.io/webgpu-particles/) - 演示如何利用 Compute Shader 处理百万级粒子的实时渲染。

---

## 💡 选型建议
1. **构建高性能 3D Web 应用**：选 **Babylon.js** 或 **Three.js**。
2. **构建浏览器端 AI 推理工具**：选 **WebLLM** 或 **Transformers.js (v3+)**。
3. **开发高性能跨端桌面工具**：选 **Rust** + **wgpu**。
4. **从 WebGL 迁移**：参考 **Chrome 官方迁移指南**。
