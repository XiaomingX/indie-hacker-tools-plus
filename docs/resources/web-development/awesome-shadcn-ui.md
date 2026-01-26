# awesome-shadcn-ui
shadcn/ui 是基于 Radix UI 和 Tailwind CSS 构建的轻量、可定制 UI 组件库，以下是经过筛选、分类优化的优质生态工具与资源，聚焦实用性与活跃度，帮你快速找到适配需求的工具。


## 一、核心组件与扩展库
该分类整合了基于 shadcn/ui 扩展的**高复用组件**，按功能场景划分，方便按需挑选。

### 1. 基础组件增强
- [aceternity-ui](https://ui.aceternity.com/) - 热门 React 组件集合，自带现成样式与动画，复制粘贴即可使用，无需手动调样式。
- [enhanced-button](https://github.com/jakobhoeg/enhanced-button) - 增强版 shadcn 按钮，支持加载状态、进度显示等进阶交互。
- [fancy-switch](https://github.com/Aslam97/react-fancy-switch) - 高颜值开关组件，样式比原生 shadcn 开关更精致，支持自定义颜色。
- [shadcn-spinner](https://github.com/allipiopereira/shadcn-spinner) - 扩展加载动画组件，提供多种旋转效果，适配不同加载场景。

### 2. 表单与输入组件
| 组件名称 | 核心功能 | 优势 |
|----------|----------|------|
| [auto-form](https://github.com/vantezzen/auto-form) | 基于 Zod  schema 自动生成表单 | 无需手写表单结构，自带校验逻辑，TypeScript 友好 |
| [autocomplete-select-shadcn-ui](https://www.armand-salle.fr/post/autocomplete-select-shadcn-ui) | 自动完成下拉框 | 结合 shadcn/ui 与 Fancy Multi Select，支持搜索与多选 |
| [downshift-shadcn-combobox](https://github.com/TheOmer77/downshift-shadcn-combobox) | 高级组合框/自动完成 | 基于 Downshift 实现，交互流畅，支持键盘导航 |
| [fancy-area](https://craft.mxkaske.dev/post/fancy-area) | 富文本输入框 | 仿 GitHub PR 评论区，支持 @提及与悬浮卡片预览，无需依赖大型编辑器库 |
| [fancy-multi-select](https://craft.mxkaske.dev/post/fancy-multi-select) | 多选组件 | 仿 cal.com 设置表单样式，支持标签化展示已选项 |
| [phone-input-shadcn-ui](https://www.armand-salle.fr/post/phone-input-shadcn-ui) | 手机号输入框 | 自动格式化号码，支持国家代码切换，适配不同地区号码规则 |
| [password-input](https://gist.github.com/mjbalcueva/b21f39a8787e558d4c536bf68e267398) | 密码输入框 | 自带强度检测、显示/隐藏密码功能，样式与 shadcn 原生组件统一 |

### 3. 日期与时间组件
- [date-range-picker-for-shadcn](https://github.com/johnpolacek/date-range-picker-for-shadcn) - 日期范围选择器，支持多月份视图、预设范围（如“近7天”）、日期对比功能。
- [datetime-picker](https://shadcn-datetime-picker-xi.vercel.app) - 全能日期时间选择器，支持时区切换、最小/最大日期限制、年月快速选择。
- [lingua-time](https://github.com/nainglinnkhant/lingua-time) - 智能日期选择器，可识别自然语言输入（如“明天下午3点”），降低用户操作成本。
- [shadcn-calendar-heatmap](https://shadcn-calendar-heatmap.vercel.app/) - 日历热力图组件，仿 GitHub 贡献热力图，直观展示数据分布。

### 4. 媒体与编辑器
- [capture-photo](https://github.com/UretzkyZvi/capture-photo) - 浏览器端拍照组件，快速集成摄像头功能，支持照片裁剪与预览。
- [echo-editor](https://github.com/Seedsa/echo-editor) - 现代 WYSIWYG 富文本编辑器，基于 tiptap 构建，样式与 shadcn 无缝融合。
- [file-uploader](https://github.com/sadmann7/file-uploader) - 文件上传组件，结合 react-dropzone 实现拖拽上传，支持进度显示、文件预览。
- [image-upload-shadcn](https://github.com/kushagrasarathe/image-upload-shadcn) - 图片专用上传组件，支持压缩、裁剪，上传后自动生成预览图。
- [shadcn-image-cropper](https://github.com/sujjeee/shadcn-image-cropper) - 轻量图片裁剪器，基于 react-image-crop 实现，操作流畅。

### 5. 数据展示组件
- [shadcn-table-v2](https://github.com/sadmann7/shadcn-table) - 高级表格组件，支持服务端排序、筛选、分页，适配大数据量展示。
- [shadcn-tree-view](https://github.com/mrlightful/shadcn-tree-view) - 层级树组件，支持节点展开/折叠、勾选、拖拽排序，适配分类数据展示。
- [crypto-charts](https://github.com/jstnw10/crypto-charts) - 加密货币图表组件，基于 PythNetwork 数据源，支持实时价格波动展示。
- [zoom-charts](https://github.com/shelwinsunga/zoom-chart-demo) - 可缩放图表，支持滚轮放大/缩小、区域选择，适配详细数据查看场景。

### 6. 布局与交互组件
- [drag-to-resize-sidebar](https://github.com/lumpinif/drag-to-resize-sidebar) - 可拖拽调整宽度的侧边栏，支持状态持久化（刷新后保留宽度），适配 Next.js。
- [dnd-dashboard](https://github.com/olliethedev/dnd-dashboard) - 拖拽排序仪表盘，支持区块互换位置，基于 swapy 实现，性能流畅。
- [react-dnd-kit-tailwind-shadcn-ui](https://github.com/Georgegriff/react-dnd-kit-tailwind-shadcn-ui) - 可拖拽看板组件，支持卡片拖拽排序，符合 A11y 可访问性标准。
- [shadcn-timeline](https://github.com/timDeHof/shadcn-timeline) - 时间线组件，支持自定义节点样式、内容布局，适配履历、流程展示场景。
- [vaul](https://vaul.emilkowal.ski/) - 底部抽屉组件，仿原生 App 抽屉交互，支持手势滑动关闭，适配移动端。

### 7. AI 与集成组件
- [assistant-ui](https://github.com/Yonom/assistant-ui) - AI 聊天组件，支持多轮对话、消息流式加载，可对接 OpenAI、Anthropic 等模型。
- [druid/ui](https://druidui.com/) - 含 Intercom 风格 AI 聊天机器人组件，支持自定义头像、话术，可直接集成到现有项目。
- [shadcn-chat](https://github.com/jakobhoeg/shadcn-chat) - 通用聊天组件，支持消息气泡、头像、时间戳，样式可高度定制。


## 二、实用工具与辅助资源
### 1. 开发插件与扩展
这些工具可直接集成到 IDE 或浏览器，提升 shadcn/ui 开发效率。
- [shadcn-ui (VS Code)](https://marketplace.visualstudio.com/items?itemName=SuhelMakkad.shadcn-ui) - VS Code 插件，可直接在编辑器中添加 shadcn 组件，无需手动复制代码。
- [shadcn/ui Components Manager (JetBrains)](https://plugins.jetbrains.com/plugin/23479-shadcn-ui-components-manager) - 适用于 WebStorm 等 JetBrains IDE，支持管理多框架（React/Vue/Svelte）的 shadcn 组件。
- [raycast-shadcn](https://www.raycast.com/luisFilipePT/shadcn-ui) - Raycast 扩展，快速查阅 shadcn 文档、组件示例，无需打开浏览器。
- [shadcn-hsl-preview (VS Code)](https://marketplace.visualstudio.com/items?itemName=dexxiez.shadcn-color-preview) - 实时预览 shadcn 颜色变量，鼠标悬停即可查看 HSL/HEX 值。

### 2. 主题与样式定制
- [ewgenius/ui](https://ui.ewgenius.me/shadcn-radix-colors) - 基于 Radix Colors 生成 shadcn 主题，支持实时调整色调、饱和度，直接复制 CSS 变量。
- [zippy starter's shadcn/ui theme generator](https://zippystarter.com/tools/shadcn-ui-theme-generator) - 单颜色生成完整主题，输入主色即可自动生成配套的中性色、功能色，适配不同场景。
- [shadcn-theme-editor](https://shadcnthemeeditor.vercel.app) - 可视化主题编辑器，支持调整颜色、圆角、阴影，实时预览组件效果。
- [gradient-picker](https://github.com/Illyism/gradient-picker) - 渐变色选择器，支持复制 shadcn 兼容的渐变代码，适配按钮、卡片等组件。

### 3. 动画与交互工具
- [animata](https://animata.design) - 手搓交互动画库，含 hover、点击、加载等动画效果，可直接复制到 shadcn 组件中。
- [motionvariants](https://github.com/chrisabdo/motionvariants) - Framer Motion 动画预设，与 shadcn 组件无缝配合，支持入场、退场动画。
- [tailwindcss-motion](https://rombo.co/tailwind/) - Tailwind 动画扩展，用简单语法实现复杂动画（如弹簧效果、延迟动画），适配 shadcn 样式体系。

### 4. 高效开发工具
- [v0](https://v0.dev/) - Vercel 生成式 UI 工具，输入文本/图片描述即可生成 shadcn 风格的 React 代码，支持 CLI 集成。
- [shadcn-form-builder](https://shadcn-form-build.vercel.app/) - 表单可视化生成器，拖拽组件即可创建表单，自动生成 react-hook-form + Zod 校验代码。
- [shadcn-zod-form](https://github.com/ilyichv/shadcn-zod-form) - CLI 工具，通过 Zod schema 一键生成 shadcn 表单组件，节省手写代码时间。
- [ui-fonts](https://www.uifonts.app/) - 字体预览工具，可实时测试字体在 shadcn 组件中的显示效果，快速选择适配字体。


## 三、项目灵感与示例
### 1. 网站与作品集参考
- [godly](https://godly.website/) - 顶级 web 设计灵感库，含大量 shadcn 风格的优秀案例，聚焦视觉与交互设计。
- [andrewsam.xyz](https://www.andrewsam.xyz/) - 开发者作品集模板，整合了 shadcn 时间线、简历卡片组件，风格简洁专业。
- [shubhporwal.me](https://www.shubhporwal.me/) - 视觉系作品集，用 GSAP 动画配合 shadcn 组件，适合展示设计类作品。
- [Nathan's AI](https://chat.brodin.dev) - AI 聊天机器人作品集，将 shadcn 聊天组件作为核心展示，突出技术能力。

### 2. 完整平台示例
- [grade-calculator](https://grades.nstr.dev/) - 学生成绩管理平台，用 shadcn 表格、表单组件实现成绩录入与分析，交互直观。
- [infinitunes](https://github.com/rajput-hemant/infinitunes) - 音乐播放器 web 应用，整合了 shadcn 弹窗、滑块、列表组件，适配音乐播放场景。
- [plotwist](https://plotwist.app/en-US) - 影视管理平台，用 shadcn 卡片、筛选组件实现影视收藏与评分，支持多设备适配。
- [memfree](https://github.com/memfreeme/memfree) - 开源 AI 搜索引擎，用 shadcn 输入框、结果列表组件构建核心交互，支持本地部署。


## 四、跨框架与设计支持
### 1. 跨框架移植（Ports）
shadcn/ui 原生基于 React，以下是官方/社区维护的其他框架移植版本：
- [Vue](https://github.com/radix-vue/shadcn-vue) - 由 radix-vue 团队维护，功能与 React 版对齐，支持 Vue 3。
- [Svelte](https://github.com/huntabyte/shadcn-svelte) - 官方推荐 Svelte 移植，适配 Svelte 3/4，支持 SSR。
- [Solid](https://github.com/hngngn/shadcn-solid) - SolidJS 版本，保留原组件的可定制性与性能优势。
- [React Native](https://github.com/mrzachnugent/react-native-reusables) - 推荐的 React Native 移植，适配移动端交互。
- [Angular](https://github.com/goetzrobin/spartan) - Angular 版本，支持 Angular 14+，样式与 web 版统一。

### 2. 设计系统资源
- [shadcn-ui-components (Figma)](https://www.figma.com/community/file/1342715840824755935/shadcn-ui-components) - 官方 Figma 组件库，1:1 还原 shadcn 组件，设计师可直接复用原型。
- [shadcn-ui-storybook](https://65711ecf32bae758b457ae34-uryqbzvojc.chromatic.com/) - 组件文档 Storybook，支持查看组件变体、交互逻辑，方便前后端协作。


## 五、项目模板与脚手架
按使用场景分类，可直接克隆启动项目，省去基础配置。

### 1. 通用 Next.js 模板
- [chadnext](https://github.com/moinulmoin/chadnext) - Next.js 14 全能模板，集成 shadcn/ui、LuciaAuth、Prisma、Stripe，适合快速启动 SaaS 项目。
- [kirimase](https://kirimase.dev/) - 轻量启动模板，含 shadcn/ui、Tailwind、Next.js 路由配置，适合小型项目。
- [taxonomy](https://github.com/shadcn/taxonomy) - 官方示例模板，展示 shadcn 与 Next.js 新特性（如服务器组件）的结合用法。

### 2. Admin/仪表盘模板
- [shadcn-admin](https://github.com/satnaing/shadcn-admin) - 轻量 Admin 模板，含侧边栏、表格、图表组件，基于 Vite 构建。
- [horizon-ai-nextjs-shadcn-boilerplate](https://horizon-ui.com/boilerplate-shadcn) - 高级 AI 仪表盘模板，集成 Stripe 支付、Supabase 认证，适合商业项目。
- [next-shadcn-dashboard-starter](https://github.com/Kiranism/next-shadcn-dashboard-starter) - Next.js 14 仪表盘，含数据卡片、筛选组件，样式简洁现代。

### 3. 跨平台模板
- [electron-shadcn](https://github.com/LuanRoger/electron-shadcn) - Electron 桌面应用模板，集成 shadcn/ui 与 Node.js 能力，支持 Windows/macOS。
- [create-tauri-core](https://github.com/mrlightful/create-tauri-core) - Tauri 模板，用 Rust 构建后端，React + shadcn 构建前端，体积更小、性能更好。

### 4. Monorepo 模板
- [turborepo-shadcn-ui-tailwindcss](https://github.com/henriqpohl/turborepo-shadcn-ui-tailwindcss) - Turborepo 基础模板，预配置 shadcn 共享组件，适合多包项目。
- [turborepo-launchpad](https://github.com/JadRizk/turborepo-launchpad) - 复杂 Monorepo 模板，含组件库、文档站、示例项目，适合团队协作开发。