# Godot 游戏引擎与开源项目精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Godot 4.x 已成为独立游戏开发者对抗 Unity 订阅制风险的 **"避风港"**。
> - **C# 崛起**：虽然 GDScript 很好用，但 C# 在 2026 年的性能优势和生态库支持已让其成为商业项目的首选。
> - **渲染进化**：利用 **Vulkan** 后端，Godot 4 的 3D 渲染表现已能满足绝大多数独立游戏的需求。
> - **开源力量**：所有的插件和扩展都是透明的，无需担心底层 API 被突然锁定。

---

## 🏗️ 核心框架与入门 (Core & Getting Started)

- [ ] [**Godot 官方文档**](https://docs.godotengine.org/) - **[权威]** 包含从 GDScript 到 C# 的所有 API 文档与入门指南。
- [ ] [**Godot Asset Library**](https://godotengine.org/asset-library/asset) - 官方资源商店，所有资源均为免费且开源。
- [ ] [**GDQuest**](https://www.gdquest.com/) - 最专业的 Godot 学习平台，提供大量开源演示项目。
- [ ] [**Godot Shaders**](https://godotshaders.com/) - **[必备]** 专门收集 Godot Shader 的社区，一键复制炫酷的 2D/3D 特效。

---

## 🎮 优秀开源游戏项目 (Open Source Games)

- [ ] [**LibreAim (Godot 4)**](https://github.com/Nokorpo/LibreAim) - 学习 3D FPS 开发架构、瞄准逻辑和 UI 交互的典范。
- [ ] [**Poder Solar (Godot 4)**](https://github.com/antimundo/poder-solar) - 2D 资源管理与模拟经营类游戏的绝佳参考。
- [ ] [**Super Tux Party**](https://gitlab.com/SuperTuxParty/SuperTuxParty) - 学习多人在线派对游戏（类似马里奥派对）同步逻辑的最佳案例。
- [ ] [**Thrive**](https://github.com/Revolutionary-Games/Thrive/) - 大型开放世界生物进化模拟游戏，展示了 Godot 承载复杂系统的能力。

---

## 🛠️ 必装插件与扩展 (Essential Plugins)

- [ ] [**Dialogic**](https://github.com/coppolaemilio/dialogic) - 极其强大的对话系统，支持分支剧情、角色表情和变量注入。
- [ ] [**HTerrain**](https://github.com/Zylann/godot_heightmap_plugin) - 为 Godot 4 提供专业级的地形编辑支持（LOD, 纹理混合）。
- [ ] [**GodotSteam**](https://github.com/Gramps/GodotSteam) - 快速集成 Steam SDK，支持成就、大厅和工作坊。
- [ ] [**Phantom Camera**](https://github.com/Marcus-Xv/PhantomCamera) - 类似 Unity Cinemachine 的摄像机控制工具，轻松实现复杂的镜头跟随。

---

## 🔧 工具与生产力 (Utility Tools)

- [ ] [**Pixelorama**](https://github.com/Orama-Interactive/Pixelorama) - **[用 Godot 开发的工具]** 优秀的像素画编辑器。
- [ ] [**Material Maker**](https://github.com/RodZill4/material-maker) - 基于节点的 PBR 材质生成工具，类似开源版的 Substance Designer。
- [ ] [**Godot CI**](https://github.com/aBARICHELLO/godot-ci) - 基于 Docker 的工具，帮助你通过 GitHub Actions 自动导出全平台安装包。

---

## 💡 选型建议
1. **构建中型 3D 游戏**：选 **Godot 4 (Vulkan)** + **C#** + **Phantom Camera**。
2. **构建极简 2D 独立游戏**：选 **GDScript** + **Pixelorama** + **Dialogic**。
3. **商业分发**：务必在项目初期集成 **GodotSteam** 并配置 **Godot CI**。
4. **追求视觉效果**：到 **Godot Shaders** 寻找现成的材质球。
