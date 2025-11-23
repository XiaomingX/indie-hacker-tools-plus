# awesome-threejs
Three.js 是一款基于 WebGL（并逐步支持 WebGPU）的 JavaScript 3D 图形库，**让开发者无需深入底层图形接口**，就能在浏览器中快速构建交互式 3D 场景、动画和应用。它抽象了 WebGL 的复杂细节，提供了开箱即用的 3D 核心组件（如场景、相机、光照、几何体），同时支持模型加载、粒子效果、物理模拟等高级功能。

如今 Three.js 已更新至 r160+ 版本，新增了 WebGPU 渲染器、体积云渲染、更高效的模型压缩等特性，广泛用于游戏开发、数据可视化、虚拟展厅、VR/AR 网页应用等场景。


# 一、入门与进阶书籍
书籍是系统学习的核心，以下均为行业公认的经典资源，标注了核心价值和适用场景。

## 1. 3D 基础理论
- **《3D Math Primer for Graphics and Game Development》**  
  👉 核心价值：3D 开发的「数学圣经」，从向量、矩阵到透视投影，用通俗的语言讲解 3D 图形必备的数学知识。  
  👉 适合人群：零基础补数学，搞懂「为什么顶点坐标有 4 个值（w 分量）」「矩阵如何实现相机移动」等核心问题。  
  作者：[@ZPostFacto](https://twitter.com/ZPostFacto) & [@Ian-Parberry](https://github.com/Ian-Parberry)  
  链接：[gamemath.com/book/intro.html](https://gamemath.com/book/intro.html)

- **《Physically Based Rendering - From Theory to Implementation》**  
  👉 核心价值：PBR（基于物理的渲染）领域的权威指南，从理论到代码实现全解析，让你的 3D 材质（金属、塑料等）看起来更真实。  
  👉 适合人群：想深入光照、材质原理，脱离「卡通感」3D 效果的开发者。  
  作者：[@mmp](https://github.com/mmp)、[@wjakob](https://github.com/wjakob) 等  
  链接：[pbr-book.org](https://pbr-book.org/)

## 2. 创意编程
- **《The Nature of Code》**  
  👉 核心价值：用「自然规律」讲编程，从物理运动（重力、碰撞）到生成艺术（分形、粒子系统），提供大量可直接迁移到 Three.js 的思路。  
  👉 特点：作者风格幽默，配套代码有 Processing 和 JavaScript 版本，适合培养 3D 创意思维。  
  作者：[@shiffman](https://github.com/shiffman)  
  链接：[natureofcode.com](https://natureofcode.com/)

## 3. Three.js 实战
- **《Discover three.js》**  
  👉 核心价值：官方推荐的入门读物，从基础场景搭建到高级特效（阴影、后期处理），示例代码同步最新 Three.js 版本。  
  链接：[discoverthreejs.com](https://discoverthreejs.com/)

- **《Learn Three.js - Fourth Edition》**  
  👉 核心价值：覆盖 Three.js 160+ 新特性（如 WebGPU 渲染器、GLTF 2.0 优化），包含游戏、数据可视化等实战项目。  
  链接：[packtpub.com/product/learn-three-js-fourth-edition/9781837637396](https://www.packtpub.com/product/learn-three-js-fourth-edition/9781837637396)


# 二、高效学习课程
课程适合「边做边学」，以下均为近年更新、社区认可度高的资源。

## 1. Three.js 核心
- **ThreeJS Journey**  
  👉 核心价值：最适合零基础的实战课程，从「Hello World 场景」到「3D 游戏+虚拟展厅」，每节配可编辑代码示例。  
  👉 优势：作者 Bruno Simon 是 Three.js 社区核心成员，课程持续更新，配套 Discord 社区可直接提问。  
  作者：[@bruno_simon](https://x.com/bruno_simon)  
  链接：[threejs-journey.com](https://threejs-journey.com/)

## 2. Shader 开发
- **《The Easiest Way to Learn GLSL》**  
  👉 核心价值：用「可视化案例」讲 GLSL（着色器语言），从基础语法到纹理、动画，避开纯理论的枯燥。  
  👉 适合人群：想给 3D 模型加特殊效果（渐变、波纹、溶解）但不懂 Shader 的开发者。  
  作者：[@iced_coffee_dev](https://x.com/iced_coffee_dev)  
  链接：[simondev.teachable.com/p/glsl-shaders-from-scratch](https://simondev.teachable.com/p/glsl-shaders-from-scratch)

- **《The Book of Shaders》**  
  👉 核心价值：免费开源的 Shader 圣经，从「像素级控制」到「生成艺术」，每节可在线编辑运行代码。  
  👉 特点：支持中文翻译，适合进阶 Shader 开发者。  
  作者：[@patriciogv](https://x.com/patriciogv)  
  链接：[thebookofshaders.com](https://thebookofshaders.com/)


# 三、实用文章与教程
按「基础理论→实战技巧→专项领域」分类，聚焦「能直接复用的知识」。

## 1. 官方文档与核心指南
- **Three.js Fundamentals**  
  👉 官方基础教程，从「场景、相机、渲染器三要素」到「纹理加载优化」，是新手必看的权威内容。  
  链接：[threejs.org/manual/#en/fundamentals](https://threejs.org/manual/#en/fundamentals)

- **MDN WebGL/GLSL 指南**  
  👉 比旧的「Shaderific」更权威，覆盖 GLSL 语法、变量类型、常用函数，配套浏览器兼容性说明。  
  链接：[developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Reference/GLSL_ES_Specification](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Reference/GLSL_ES_Specification)

## 2. 3D 理论精讲
- **《Explaining Homogeneous Coordinates & Projective Geometry》**  
  👉 通俗解释「齐次坐标（w 分量）」的作用——解决 3D 场景到 2D 屏幕的「透视投影」问题，看懂后再也不懵相机矩阵。  
  链接：[tomdalling.com/blog/modern-opengl/explaining-homogenous-coordinates-and-projective-geometry/](https://www.tomdalling.com/blog/modern-opengl/explaining-homogenous-coordinates-and-projective-geometry/)

## 3. 实战教程
- **《Surface Sampling in Three.js》**  
  👉 详解 `MeshSurfaceSampler` 的用法（在 3D 模型表面随机生成粒子、纹理），可用于「雨滴落在地面」「花瓣散落在模型上」等效果。  
  链接：[tympanus.net/codrops/2021/08/31/surface-sampling-in-three-js/](https://tympanus.net/codrops/2021/08/31/surface-sampling-in-three-js/)

- **《Three.js 160+ WebGPU 渲染器实战》**  
  👉 讲解如何启用 WebGPU 渲染器，对比 WebGL 提升的性能（如复杂场景帧率翻倍），附完整代码示例。  
  链接：[r3f.docs.pmnd.rs/advanced/webgpu](https://r3f.docs.pmnd.rs/advanced/webgpu)

- **《Rapier.js + Three.js 物理碰撞实战》**  
  👉 用现代物理引擎 Rapier 实现「物体碰撞、重力下落」，比旧的 Ammo.js 更轻量、API 更简洁。  
  链接：[dimforge.com/blog/2023/03/01/rapier-threejs-tutorial/](https://dimforge.com/blog/2023/03/01/rapier-threejs-tutorial/)

## 4. 专项领域
### 水面与流体
- **《Real-time rendering of water caustics》**  
  👉 用「纹理扰动」实现水面折射的「焦散效果」（阳光透过水面在水底形成的光斑），代码可直接复用。  
  链接：[medium.com/@martinRenou/real-time-rendering-of-water-caustics-59cda1d74aa](https://medium.com/@martinRenou/real-time-rendering-of-water-caustics-59cda1d74aa)

### 生成艺术
- **《Generative Artistry Tutorials》**  
  👉 从「分形几何」到「粒子系统」，教你用 Three.js 做可交互的生成艺术，示例代码简洁易懂。  
  作者：[@rumyra](https://github.com/rumyra) & [@tholman](https://github.com/tholman)  
  链接：[generativeartistry.com/tutorials/](https://generativeartistry.com/tutorials/)

### 碰撞检测
- **《Bounding Volume Collision Detection with Three.js》**  
  👉 讲解「包围盒（AABB）」「包围球」等简化碰撞检测的方法，避免直接计算复杂模型顶点的性能问题。  
  链接：[developer.mozilla.org/en-US/docs/Games/Techniques/3D_collision_detection/Bounding_volume_collision_detection_with_THREE.js](https://developer.mozilla.org/en-US/docs/Games/Techniques/3D_collision_detection/Bounding_volume_collision_detection_with_THREE.js)


# 四、灵感与参考案例
找创意、看效果的最佳渠道，直接看「别人做了什么」。

## 1. 视觉灵感
- **Three.js 官方示例库**  
  👉 官方维护的「效果图鉴」，从基础几何体到 VR 场景、体积云，每例可在线编辑代码。  
  链接：[threejs.org/examples/](https://threejs.org/examples/)

- **ShaderToy**  
  👉 全球最大的 Shader 分享平台，输入「water」「fire」等关键词，能找到可直接复用的 3D 特效 Shader 代码。  
  链接：[shadertoy.com](https://www.shadertoy.com/)

- **same.energy**  
  👉 视觉搜索引擎，上传一张 3D 效果图，能找到风格相似的作品，适合找设计灵感。  
  链接：[same.energy](https://same.energy/)

## 2. 实战项目参考
- **Three.js 社区案例合集**  
  👉 收录了「虚拟展厅」「3D 数据可视化」「Web 游戏」等真实项目，附技术栈和源码链接。  
  链接：[threejs.org/showcase/](https://threejs.org/showcase/)


# 五、必备资源库
涵盖「模型、纹理、Shader 代码」等可直接复用的素材。

## 1. 3D 资产（模型/材质）
| 资源名称       | 核心优势                                  | 授权类型       | 链接                          |
|----------------|-------------------------------------------|----------------|-------------------------------|
| Poly Haven     | 免费 CC0 授权，含 PBR 纹理、HDRI、3D 模型 | 完全免费商用   | [polyhaven.com](https://polyhaven.com/) |
| ambientCG      | 专注 PBR 纹理，支持 4K 下载，分类清晰     | CC0 免费商用   | [ambientcg.com](https://ambientcg.com/) |
| Poliigon       | 高质量付费纹理/模型，适合专业项目         | 付费（有免费样例） | [poliigon.com](https://www.poliigon.com/) |
| Sketchfab      | 海量用户上传模型，支持筛选 Three.js 兼容格式 | 免费/付费混合 | [sketchfab.com](https://sketchfab.com/) |

## 2. 纹理资源
- **3dtextures.me**  
  👉 免费 PBR 纹理库，每款纹理包含「漫反射、法线、置换、粗糙度」等完整贴图，直接适配 Three.js 材质。  
  链接：[3dtextures.me](https://3dtextures.me/)

## 3. Shader 代码片段
- **GLSL 噪声函数合集**  
  👉 包含 Perlin、Simplex 等常用噪声函数，可直接复制到 Shader 中，实现地形、流体、云等自然效果。  
  作者：[@patriciogv](https://x.com/patriciogv)  
  链接：[gist.github.com/patriciogonzalezvivo/670c22f3966e662d2f83](https://gist.github.com/patriciogv/670c22f3966e662d2f83)

- **PixelSpirit Elements Deck**  
  👉 「Shader 塔罗牌」，从基础形状到复杂特效，每一张「牌」都对应可复用的 GLSL 代码，循序渐进学 Shader。  
  作者：[@patriciogv](https://x.com/patriciogv)  
  链接：[pixelspiritdeck.com](https://pixelspiritdeck.com/)

- **信号塑形函数库**  
  👉 解决「如何让动画更自然」的问题，如缓动、脉冲、波纹等效果的数学实现，支持 GLSL 直接调用。  
  作者：[@iquilezles](https://x.com/iquilezles)  
  链接：[iquilezles.org/articles/functions/](https://iquilezles.org/articles/functions/)


# 六、效率工具
从「模型优化」到「Shader 调试」，提升开发效率的必备工具。

## 1. 模型调试与优化
- **GLTF Report**  
  👉 在线检查 GLTF 模型问题（如冗余顶点、纹理格式不兼容），支持预览模型在 Three.js 中的效果，还能优化 BASIS/KTX2 纹理。  
  作者：[@donmccurdy](https://github.com/donmccurdy)  
  链接：[gltf.report](https://gltf.report)

- **gltf-transform**  
  👉 命令行工具，批量优化 GLTF 模型（如合并顶点、Draco 压缩、纹理转 KTX2 格式），压缩后模型大小可减少 70%+。  
  作者：[@donmccurdy](https://github.com/donmccurdy)  
  链接：[gltf-transform.dev](https://gltf-transform.dev/)

## 2. 场景与材质编辑
- **Three.js Editor**  
  👉 官方可视化编辑器，拖拽即可添加相机、光照、模型，支持导入 GLTF 模型并调试材质，改完直接导出代码。  
  链接：[threejs.org/editor/](https://threejs.org/editor/)

- **Polygonjs**  
  👉 节点式 WebGL 工具，无需写代码就能生成「程序化几何体、粒子效果」，支持导出 Three.js 场景。  
  链接：[polygonjs.com](https://polygonjs.com)

## 3. Shader 开发工具
| 工具名称         | 核心优势                                  | 类型       | 链接                          |
|------------------|-------------------------------------------|------------|-------------------------------|
| GraphToy         | 可视化调试 GLSL 函数，实时看曲线变化      | 在线工具   | [graphtoy.com](https://graphtoy.com/) |
| NodeToy          | 节点式 Shader 编辑器，支持导出 Three.js 可用代码，兼容 React-Three-Fiber | 在线工具   | [app.nodetoy.co](https://app.nodetoy.co/) |
| glslViewer       | 命令行 Shader 沙盒，快速预览 2D/3D Shader 效果，适合快速迭代创意 | 本地工具   | [github.com/patriciogonzalezvivo/glslViewer](https://github.com/patriciogonzalezvivo/glslViewer) |

## 4. 3D 建模工具
- **Blender**  
  👉 免费开源的全功能建模软件，支持导出 GLTF 格式，Three.js 社区大部分自定义模型都用它制作。  
  链接：[blender.org](https://www.blender.org/)

- **Spline**  
  👉 轻量化 Web 建模工具，支持「实时协作」和「直接导出 Three.js 场景」，适合快速制作简单 3D 资产。  
  链接：[spline.design](https://spline.design/)


# 七、核心库与框架
Three.js 生态的「增强插件」，覆盖「框架集成、物理、动画」等场景。

## 1. 框架集成（按前端框架分）
### React
- **react-three-fiber（r3f）**  
  👉 用 React 语法写 Three.js，支持组件化开发（如 `<Mesh />` `<Camera />`），是 React 生态的主流方案。  
  维护者：[@pmndrs](https://github.com/pmndrs)  
  链接：[github.com/pmndrs/react-three-fiber](https://github.com/pmndrs/react-three-fiber)

- **drei**  
  👉 r3f 的「工具库」，提供现成的组件（如 `<OrbitControls />` `<GLTFModel />`），省去重复造轮子。  
  维护者：[@pmndrs](https://github.com/pmndrs)  
  链接：[github.com/pmndrs/drei](https://github.com/pmndrs/drei)

### Vue
- **TresJS**  
  👉 Vue 3 专属的 Three.js 封装，支持 `<TresScene />` `<TresMesh />` 等 Vue 组件，生态完善。  
  维护者：[@tresjs_dev](https://github.com/Tresjs)  
  链接：[github.com/Tresjs/tres](https://github.com/Tresjs/tres)

- **Cientos**  
  👉 TresJS 的工具集，提供碰撞检测、后期处理等现成功能，类似 React 的 drei。  
  链接：[github.com/Tresjs/cientos](https://github.com/Tresjs/cientos)

### Svelte
- **threlte**  
  👉 Svelte 生态的 Three.js 组件库，支持响应式数据绑定，性能接近原生 Three.js。  
  链接：[github.com/grischaerbe/threlte](https://github.com/grischaerbe/threlte)

## 2. 物理模拟
- **Rapier.js**  
  👉 现代轻量物理引擎，支持「碰撞检测、关节约束、重力模拟」，API 简洁，性能优于 Ammo.js。  
  维护者：[@dimforge](https://github.com/dimforge/)  
  链接：[github.com/dimforge/rapier](https://github.com/dimforge/rapier)

- **cannon-es**  
  👉 pmndrs 维护的物理引擎，适配 react-three-fiber，适合中小型项目。  
  维护者：[@pmndrs](https://github.com/pmndrs/)  
  链接：[github.com/pmndrs/cannon-es](https://github.com/pmndrs/cannon-es)

## 3. 动画
- **GSAP**  
  👉 全能动画库，支持 Three.js 物体的「位置、旋转、缩放」动画，还能结合 ScrollTrigger 做滚动触发动画。  
  链接：[greensock.com/gsap/](https://greensock.com/gsap/)

## 4. 高级功能插件
- **three-mesh-bvh**  
  👉 用「包围盒层级（BVH）」加速碰撞检测和射线投射，复杂场景下性能提升 10 倍以上，必备工具。  
  作者：[@gkjohnson](https://github.com/gkjohnson)  
  链接：[github.com/gkjohnson/three-mesh-bvh](https://github.com/gkjohnson/three-mesh-bvh)

- **three-bvh-csg**  
  👉 基于 three-mesh-bvh 实现「布尔运算」（如两个模型的交集、差集），可制作复杂的自定义几何体。  
  作者：[@gkjohnson](https://github.com/gkjohnson)  
  链接：[github.com/gkjohnson/three-bvh-csg](https://github.com/gkjohnson/three-bvh-csg)

- **lygia**  
  👉 跨语言 Shader 库，提供 PBR、噪声、后期处理等现成函数，支持 GLSL/HLSL，可直接集成到 Three.js Shader 中。  
  作者：[@patriciogv](https://x.com/patriciogv)  
  链接：[github.com/patriciogonzalezvivo/lygia](https://github.com/patriciogonzalezvivo/lygia)


# 八、社区与支持
遇到问题时的「求助渠道」，按响应速度排序。

1. **Three.js 官方 Discord**  
   👉 社区最活跃的地方，有核心开发者常驻，提问前附上代码片段，通常 1-2 小时内有回复。  
   链接：[discord.com/invite/56GBJwAnUS](https://discord.com/invite/56GBJwAnUS)

2. **Three.js 官方论坛**  
   👉 适合复杂问题（如性能优化、兼容性问题），回复更系统，可搜索历史解决方案。  
   链接：[discourse.threejs.org](https://discourse.threejs.org/)

3. **Stack Overflow（three.js 标签）**  
   👉 老牌问答社区，90% 的基础问题（如「模型加载失败」「光照不生效」）已有答案，提问前先搜索。  
   链接：[stackoverflow.com/questions/tagged/three.js](https://stackoverflow.com/questions/tagged/three.js)

4. **X（原 Twitter）@threejs**  
   👉 官方账号会推送新版本特性、社区案例，可直接私信提问（适合简单问题）。  
   链接：[x.com/threejs](https://x.com/threejs)
