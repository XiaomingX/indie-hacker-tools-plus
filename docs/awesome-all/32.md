# Awesome Electron 开源精选指南
（基于 Electron 框架的优质开源工具与资源汇总，帮你快速找到实用应用和开发利器）


## 一、什么是 Electron？
先用一句话说清核心：**Electron 是用 JavaScript、HTML、CSS 开发跨平台桌面应用的框架**。它让前端开发者不用学 C++/Qt 也能做 Windows、macOS、Linux 桌面软件，比如 VS Code、Discord 都是用它做的。


## 二、精选 Electron 应用
按使用场景分类，每款都标注「核心优势」和「适用人群」，方便你按需选择。

### 1. 代码编辑与终端
| 应用名称 | 核心优势 | 适用场景 |
|----------|----------|----------|
| [Visual Studio Code](https://github.com/microsoft/vscode) | 插件生态无敌（支持 100+ 语言）、内置 Git 与调试器、跨平台体验一致 | 所有开发者的主力代码编辑器 |
| [Hyper](https://github.com/vercel/hyper) | 用 CSS/JS 完全自定义主题/功能、支持分屏与插件扩展、轻量流畅 | 喜欢个性化终端的开发者 |
| [WezTerm](https://github.com/wez/wezterm)（补充推荐） |  GPU 加速、原生支持 Unicode 与表情、跨平台性能优于 Hyper | 对终端响应速度有要求的用户 |

### 2. 文档与笔记
| 应用名称 | 核心优势 | 适用场景 |
|----------|----------|----------|
| [Mark Text](https://github.com/marktext/marktext) | 实时预览 Markdown、支持 MathJax 公式与图表、极简无干扰界面 | 写技术文档、博客草稿的用户 |
| [Logseq](https://github.com/logseq/logseq)（替代 Notable） | 开源免费、双向链接（知识关联）、本地优先存储、支持白板 | 做知识管理、读书笔记、思维导图的用户 |
| [Simplenote](https://github.com/Automattic/simplenote-electron) | 多端实时同步、纯文本无格式干扰、数据开源可导出 | 喜欢轻量笔记、怕数据丢失的用户 |

### 3. 开发与测试工具
| 应用名称 | 核心优势 | 适用场景 |
|----------|----------|----------|
| [Insomnia](https://github.com/getinsomnia/insomnia) | 开源免费、支持 REST/GraphQL/gRPC、团队协作功能 | API 测试与管理（比 Postman 轻量） |
| [Postman（Electron 版）](https://www.postman.com) | 功能全面（API 设计/调试/监控）、支持复杂场景（如 OAuth2.0） | 企业级或复杂 API 项目测试 |
| [Beekeeper Studio](https://github.com/beekeeper-studio/beekeeper-studio) | 可视化数据库管理、支持 MySQL/PostgreSQL/SQLite、界面友好 | 非专业 DBA 的开发者（写 SQL 更高效） |
| [MQTTX](https://github.com/emqx/MQTTX) | 支持 MQTT 5.0、可视化消息收发、SSL/TLS 加密 | IoT 开发者调试设备通信 |

### 4. 系统与实用工具
| 应用名称 | 核心优势 | 适用场景 |
|----------|----------|----------|
| [Motrix](https://github.com/agalwood/Motrix) | 多协议支持（HTTP/BT/磁力/FTP）、多线程下载、无广告 | 替代迅雷的开源下载管理器 |
| [Etcher](https://github.com/balena-io/etcher) | 一键写入镜像、自动校验文件（防烧录失败）、支持 SD 卡/U盘 | 装系统、刷树莓派镜像的用户 |
| [LosslessCut](https://github.com/mifi/lossless-cut) | 视频无损裁剪（无需重新编码）、提取音频/字幕、快如复制 | 剪辑短视频、截取电影片段的用户 |
| [Pomotroid](https://github.com/Splode/pomotroid) | 极简界面、自定义工作/休息时长、专注统计 | 用番茄工作法提升效率的用户 |
| [Ferdi](https://github.com/getferdi/ferdi)（替代 Franz） | 开源免费、整合 WhatsApp/Slack/Discord 等、自定义服务 | 多社交/办公软件用户（减少桌面图标杂乱） |

### 5. 娱乐与社交
| 应用名称 | 核心优势 | 适用场景 |
|----------|----------|----------|
| [Museeks](https://github.com/KeitIG/museeks) | 本地音乐库管理、标签编辑、轻量无广告 | 听本地音乐的极简主义者 |
| [Heroic Games Launcher](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher) | 支持 Epic/GOG/Amazon 游戏、自动更新、Linux 兼容（Proton） | 不想装 Epic 客户端的玩家（尤其 Linux/macOS 用户） |


## 三、开发者必备工具
如果你用 Electron 做开发，这些工具能解决 90% 的常见问题。

### 1. 构建与打包
- **[electron-builder](https://github.com/electron-userland/electron-builder)**  
  ✅ 推荐首选！支持生成 Windows（exe/msi）、macOS（dmg/pkg）、Linux（deb/rpm）安装包，自动处理图标、代码签名、应用更新，新手也能快速打包。  
- **[electron-packager](https://github.com/electron-userland/electron-packager)**  
  仅生成「可执行文件」（无安装流程），适合快速测试或需要自定义打包逻辑的场景。  
- **[electron-rebuild](https://github.com/electron/electron-rebuild)**  
  解决「原生模块适配问题」：当你用了 `sqlite3`、`serialport` 等 Node 原生模块，Electron 版本升级后模块会失效，用它重建就能适配。  
- **[electron-vite](https://github.com/alex8088/electron-vite)**  
  基于 Vite 的构建工具，比 Webpack 快 10 倍+，支持热更新、TypeScript，兼容 Vue/React/Svelte 等框架，现代 Electron 开发必备。

### 2. 开发调试辅助
- **[electron-debug](https://github.com/sindresorhus/electron-debug)**  
  一键开启调试（快捷键 `Ctrl+Shift+I`），支持刷新页面（`F5`），自动安装 React/Vue 开发者工具。  
- **[electron-is-dev](https://github.com/sindresorhus/electron-is-dev)**  
  一行代码判断环境：`isDev && console.log('调试日志')`，避免生产环境泄露调试信息。  
- **[electron-reloader](https://github.com/sindresorhus/electron-reloader)**  
  代码修改后自动刷新应用，不用手动重启，开发效率翻倍。  
- **[electron-log](https://github.com/megahertz/electron-log)**  
  记录应用日志（支持文件/控制台/远程服务器），自动切割大日志文件，方便排查生产环境问题。

### 3. 数据存储
- **[electron-store](https://github.com/sindresorhus/electron-store)**  
  轻量级键值对存储，基于 JSON，不用配置数据库，适合存用户偏好（如窗口大小、主题）。  
- **[RxDB](https://github.com/pubkey/rxdb)**  
  客户端 NoSQL 数据库，支持实时同步、离线优先、加密，适合笔记/待办等需要本地复杂数据管理的应用。

### 4. 网络与文件处理
- **[electron-dl](https://github.com/sindresorhus/electron-dl)**  
  简化文件下载：自带进度条、暂停/继续功能，自动处理保存路径弹窗。  
- **[got](https://github.com/sindresorhus/got)**  
  主进程 HTTP 请求库，支持拦截器、重试、超时控制，比原生 `fetch` 更强大。


## 四、快速构建应用的工具
不用写复杂代码，就能用 Electron 做工具：
1.  **[nativefier](https://github.com/jiahaog/nativefier)**  
   输入任意网址（如 Notion、GitHub），一键生成桌面应用，支持自定义图标和快捷键。比如把网页版微信转成桌面 app，避免浏览器标签杂乱。  
2.  **[html-pdf-electron](https://github.com/fraserxu/electron-pdf)（更新替代）**  
   把 HTML、Markdown 转成 PDF，支持自定义页眉页脚、分页，适合生成报告或电子书。  
3.  **[jest-electron](https://github.com/hustcc/jest-electron)**  
   在 Electron 环境中运行 Jest 测试，解决「浏览器 API 与桌面环境差异」问题，测试结果更贴近真实用户场景。


## 五、UI 组件与框架
帮你快速做出「原生风格」的桌面界面：
- **[menubar](https://github.com/maxogden/menubar)**  
  快速构建「菜单栏应用」（如 macOS 顶部状态栏工具、Windows 托盘工具），简化托盘图标、菜单交互开发。  
- **[@mui/x-electron](https://mui.com/)（补充推荐）**  
  Material-UI 的 Electron 适配组件，提供原生风格的按钮、窗口控件，支持 React 开发者快速搭界面。  
- **[electron-vue-template](https://github.com/electron-vite/electron-vue-template)**  
  开箱即用的 Vue 3 + Vite 模板，集成路由、状态管理、打包配置，新手直接上手开发。


## 六、官方资源与学习渠道
### 1. 核心官方资源
- **最新官方文档**：[https://www.electronjs.org/docs/latest](https://www.electronjs.org/docs/latest)（旧文档已废弃，优先看这个）  
- **快速入门教程**：[https://www.electronjs.org/docs/latest/tutorial/quick-start](https://www.electronjs.org/docs/latest/tutorial/quick-start)（30 分钟做一个 Hello World 应用）  
- **官方 GitHub**：[https://github.com/electron/electron](https://github.com/electron/electron)（获取源码、提交 Issue、看更新日志）  
- **官方 Discord**：[https://discord.com/invite/electron](https://discord.com/invite/electron)（提问交流、找开发者协作）

### 2. 优质进阶资源
- 文章：《Electron 29 新特性与性能优化实践》（2024，Medium）  
  讲解最新 API 用法、内存优化、启动速度提升技巧，解决「Electron 应用臃肿」问题。  
- 文章：《Electron 应用签名与公证指南（2024 版）》（Electron 官方博客）  
  适配 macOS Sonoma 和 Windows 11 的签名流程，避免应用被系统拦截为「恶意软件」。  
- 视频：《Electron for Beginners 2024》（YouTube：Traversy Media）  
  案例驱动教学，从搭建环境到打包发布，适合零基础入门。


## 七、补充：替代方案与常见问题
### 1. 轻量级替代：Tauri
如果觉得 Electron 应用体积大、内存高，可以试试 **[Tauri](https://tauri.app/)**：基于 Rust 开发，应用体积比 Electron 小 80%+，但生态不如 Electron 成熟，适合对性能有高要求的场景。

### 2. 常见问题解决
- **Q：应用体积太大？**  
  A：用 `electron-vite` 开启 tree-shaking（移除无用代码）；用 `asar` 压缩资源；拆分主进程和渲染进程代码。  
- **Q：启动速度慢？**  
  A：减少主进程初始化任务；用懒加载渲染进程；替换重依赖（如用 `lodash-es` 替代 `lodash`）。  
- **Q：出现白屏？**  
  A：检查 HTML 路径是否正确；生产环境禁用 `devtools`；确保资源加载完成后再显示窗口（监听 `ready-to-show` 事件）。
