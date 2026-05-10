# Three.js 开发者生态资源 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Web 3D 已不再是点缀，而是 **"沉浸式体验"** 的核心。
> - **引擎选择**：Three.js 依然是王者，但 **WebGPU** 渲染器已经正式可用，性能提升巨大。
> - **开发范式**：在 React 中使用 **React-Three-Fiber (R3F)** 是目前的行业标准，它让 3D 场景开发像写 HTML 一样自然。

---

## 🏗️ 核心框架与集成 (Core & Frameworks)

- [ ] [**Three.js**](https://threejs.org/) - **[必学]** 浏览器 3D 图形的绝对标准。优先关注 r170+ 版本对 WebGPU 的支持。
- [ ] [**React-Three-Fiber (R3F)**](https://github.com/pmndrs/react-three-fiber) - React 开发者必备，将 Three.js 逻辑组件化，极大提升开发效率。
- [ ] [**Drei**](https://github.com/pmndrs/drei) - R3F 的超强工具库，提供现成的控制器、天空盒、后期处理等组件。
- [ ] [**TresJS**](https://github.com/Tresjs/tres) - Vue 3 开发者的最佳选择，语法风格与 Vue 保持一致。
- [ ] [**Threlte**](https://github.com/grischaerbe/threlte) - Svelte 生态的高性能 3D 组件库。

---

## ⚡ 性能优化与工具 (Performance & Tools)

- [ ] [**Gltf-transform**](https://gltf-transform.dev/) - **[推荐]** 命令行模型优化神器，支持 Draco 压缩、纹理转 KTX2，体积减小 70%+。
- [ ] [**Three-mesh-bvh**](https://github.com/gkjohnson/three-mesh-bvh) - 使用包围盒层级加速射线检测与碰撞，复杂场景必备。
- [ ] [**Rapier.js**](https://github.com/dimforge/rapier) - 现代轻量级物理引擎，性能远超旧的 Cannon/Ammo。
- [ ] [**Lygia**](https://github.com/patriciogonzalezvivo/lygia) - Shader 库，提供 PBR、噪声等现成函数，像调包一样写 GLSL。

---

## 🎨 材质、模型与灵感 (Assets & Inspo)

- [ ] [**Poly Haven**](https://polyhaven.com/) - 免费 CC0 授权的高质量 PBR 纹理、HDRI 环境图与模型。
- [ ] [**Sketchfab**](https://sketchfab.com/) - 全球最大的 3D 模型市场，支持按 Three.js 兼容格式筛选。
- [ ] [**ShaderToy**](https://www.shadertoy.com/) - 获取顶级 Shader 灵感的最佳去处，代码通常可直接移植。
- [ ] [**Three.js Journey**](https://threejs-journey.com/) - Bruno Simon 出品的公认最好的实战课程。

---

## 🛠️ 设计与调试工具 (Design & Debug)

- [ ] [**Three.js Editor**](https://threejs.org/editor/) - 官方在线场景编辑器，调试材质与光照的最佳场所。
- [ ] [**Spline**](https://spline.design/) - 零代码 Web 3D 协作工具，支持直接导出可交互的 Three.js 场景。
- [ ] [**Blender**](https://www.blender.org/) - 开源建模软件，导出 GLTF/GLB 模型到 Web 的唯一首选。
- [ ] [**Graphtoy**](https://graphtoy.com/) - 可视化调试 GLSL 数学函数，写 Shader 时的好帮手。

---

## 💡 选型建议
1. **构建高性能商业站**：选 **React** + **R3F** + **Drei** + **GSAP** (动画)。
2. **需要物理模拟（如小游戏）**：必接 **Rapier.js**。
3. **模型过大导致加载慢**：强制使用 **gltf-transform** 进行 KTX2 纹理压缩。
4. **追求极速渲染（大场景）**：开启 **WebGPURenderer** 并配合 **InstancedMesh**。
