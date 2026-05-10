# 2026 Electron 跨平台桌面应用开发指南 (Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，Electron 依然是构建跨平台桌面应用的首选，但其资源占用问题需要通过更精细的架构设计来优化。
> - **Rust 协同**：对于计算密集型任务，强烈建议使用 **Native Modules (N-API)** 或 **Tauri** 思想，将逻辑下沉到 Rust。
> - **安全性**：默认启用 `contextIsolation` 和 `sandbox`，严禁在渲染进程中直接使用 Node.js API。
> - **分发**：利用 **Electron Forge** 或 **Electron Builder** 实现自动更新与多平台分发。

---

## 🏗️ 核心框架与基础 (Core Framework)

- [ ] [**Electron 官方文档**](https://www.electronjs.org/docs/latest/) - 了解主进程 (Main) 与渲染进程 (Renderer) 的进程架构。
- [ ] [**IPC 通信 (Inter-Process Communication)**](https://www.electronjs.org/docs/latest/tutorial/ipc) - 掌握 `ipcMain` 与 `ipcRenderer` 之间的数据交互规范。
- [ ] [**Preload Scripts**](https://www.electronjs.org/docs/latest/tutorial/sandbox) - 学习如何通过预加载脚本安全地将 API 暴露给渲染进程。
- [ ] [**Vite + Electron Starter**](https://github.com/electron-vite/electron-vite-vue) - **[推荐]** 现代化的开发工作流，极速热重载。

---

## 🛠️ 生态工具与分发 (Tools & Distribution)

- [ ] [**Electron Forge**](https://www.electronforge.io/) - 官方推荐的一站式打包、分发工具链。
- [ ] [**Electron Builder**](https://www.electron.build/) - 极其强大的打包工具，支持高度自定义的安装包配置。
- [ ] [**Update.rocks**](https://update.rocks/) - 轻量级的自动更新服务。
- [ ] [**Electron Store**](https://github.com/sindresorhus/electron-store) - 简单持久化的配置存储方案。
- [ ] [**Electron Log**](https://github.com/megahertz/electron-log) - 专业的日志记录与上报。

---

## 🚀 性能优化与进阶 (Optimization & Advanced)

- [ ] [**BrowserWindow 管理**](https://www.electronjs.org/docs/latest/api/browser-window) - 掌握窗口池化技术，减少冷启动时间。
- [ ] [**Native Node Modules**](https://www.electronjs.org/docs/latest/tutorial/using-native-node-modules) - 接入 C++/Rust 原生库，提升核心计算性能。
- [ ] [**Deep Linking**](https://www.electronjs.org/docs/latest/tutorial/launch-app-from-url-in-another-app) - 允许外部 URL 直接唤起并传参给应用。
- [ ] [**Tray & Menu**](https://www.electronjs.org/docs/latest/api/tray) - 打造专业的系统托盘与原生菜单体验。

---

## 💡 选型建议
1. **追求开发效率**：选 **Electron + React/Vue + Vite**，利用前端生态快速构建。
2. **追求极小安装包与低内存**：考虑 **Tauri (Rust)** 作为 Electron 的替代方案。
3. **复杂媒体处理应用**：必须集成 **FFmpeg** 原生二进制文件。
4. **企业级安全性**：强制开启 **ASAR 加密** 并实施严格的 **CSP (Content Security Policy)**。
