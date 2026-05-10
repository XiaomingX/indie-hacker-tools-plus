# Unity3D 现代开发资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Unity 开发已全面进入 **"数据驱动"** 与 **"AI 增强"** 时代。
> - **高性能基石**：大型复杂场景强制使用 **DOTS (Entities)** 和 **Burst Compiler**。
> - **渲染管线**：优先选择 **URP**（通用渲染管线），它是目前跨平台（移动/Web/XR）的最佳平衡点。
> - **AI 辅助**：集成 **Sentis** (原 Barracuda) 在本地运行 AI 模型，实现实时的姿态识别或对话。

---

## 🏗️ 核心架构与高性能 (DOTS & Performance)

- [ ] [**Unity Entities (DOTS)**](https://unity.com/dots) - **[核心]** 数据导向型技术栈，实现海量实体的高效并行处理。
- [ ] [**Burst Compiler**](https://docs.unity3d.com/Packages/com.unity.burst@latest) - 将 C# 代码编译为高度优化的原生指令。
- [ ] [**VContainer**](https://github.com/hadashiA/VContainer) - **[推荐]** 极速、零 GC 消耗的依赖注入库，是 Zenject 的现代替代品。
- [ ] [**UniTask**](https://github.com/Cysharp/UniTask) - 为 Unity 优化的高效异步 (async/await) 库，彻底告别复杂的协程。

---

## 🎨 渲染、特效与着色器 (Rendering & VFX)

- [ ] [**Shader Graph**](https://unity.com/features/shader-graph) - 可视化编写着色器，支持 URP 和 HDRP。
- [ ] [**VFX Graph**](https://unity.com/features/vfx-graph) - 基于 GPU 的粒子系统，轻松实现百万级粒子的惊艳特效。
- [ ] [**Crest Ocean Render**](https://github.com/huwb/crest-oceanrender) - 目前最先进的海洋渲染系统，支持真实的流体动力学。
- [ ] [**Kino**](https://github.com/keijiro/Kino) - Keijiro 大神的视觉特效合集（Glitch, Bloom, Datamosh 等）。

---

## 🤖 AI、逻辑与交互 (AI & Interaction)

- [ ] [**Unity Sentis**](https://unity.com/products/sentis) - 在端侧实时运行 ONNX 模型，不消耗后端算力。
- [ ] [**Behavior Designer**](https://opsive.com/assets/behavior-designer/) - 业界标准的行为树编辑器（虽然是付费，但几乎是独立开发者必备）。
- [ ] [**NodeGraphProcessor**](https://github.com/alelievr/NodeGraphProcessor) - 现代化的节点编辑器框架，适合自定义技能树或对话系统。
- [ ] [**InControl**](http://www.tasharen.com/?page_id=230) - 跨平台手柄控制器的统一映射方案。

---

## 🛠️ 开发效率与工具 (Tooling)

- [ ] [**DOTween**](https://dotween.demigiant.com/) - 动画引擎事实标准，几行代码搞定 UI 和物体动效。
- [ ] [**NaughtyAttributes**](https://github.com/dbrizov/NaughtyAttributes) - 极大地扩展了 Inspector 的属性标签，减少自定义 Editor 代码。
- [ ] [**Mulligan Renamer**](https://github.com/redbluegames/unity-mulligan-renamer) - 强大的批量重命名工具，保持项目整洁的利器。
- [ ] [**Fast Script Reload**](https://github.com/handzlikchris/FastScriptReload) - **[提效]** 实现 C# 代码热重载，修改代码后无需等待漫长的编译重启。

---

## 💡 选型建议
1. **制作轻量级 2D 游戏**：选 **URP 2D** + **DOTween** + **Aseprite Importer**。
2. **构建海量实体（如战争模拟）**：强制选 **DOTS (Entities)** + **Hybrid Renderer**。
3. **开发移动端 AR 应用**：选 **AR Foundation** + **Sentis (AI 识别)**。
4. **追求极致开发效率**：必装 **UniTask** + **VContainer** + **Fast Script Reload**。
