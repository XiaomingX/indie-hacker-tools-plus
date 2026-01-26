# Awesome React: 现代 React 生态精选指南
一个整理了 React 生态中**实用、主流、高价值工具与资源**的合集，帮你快速找到开发所需的解决方案。


## 一、React 核心资源
### 1. 基础入门与社区
这部分是学习 React 和融入社区的起点，包含官方文档、交流渠道等核心入口。
- [React 官方网站](https://react.dev/) - 最新官方文档（React 18+），包含基础教程、API 参考和最佳实践，是学习的首选。
- [React GitHub](https://github.com/facebook/react) - React 源码仓库，可查看更新日志、提交记录和贡献指南。
- [Reactiflux Discord 社区](http://www.reactiflux.com/) - 全球最大的 React 开发者交流平台，可提问、分享经验和参与讨论。
- [React 社区页面](https://react.dev/community) - 官方整理的社区资源，包含会议、博客和贡献方式。
- [React CodeSandbox 在线编辑器](https://codesandbox.io/s/new) - 无需本地配置，可直接在线编写、运行 React 代码，适合快速验证想法。


### 2. 教程与实战指南
从基础入门到架构设计，覆盖不同阶段的学习需求。
- [React 官方教程](https://react.dev/learn) - 官方推出的交互式教程，从组件到 Hooks 逐步讲解，适合新手。
- [VS Code 中使用 React](https://code.visualstudio.com/docs/nodejs/reactjs-tutorial) - 微软官方教程，教你配置 VS Code 开发 React 项目。
- [React 面试题大全](https://github.com/sudheerj/reactjs-interview-questions) - 包含基础、进阶、性能优化等面试高频问题及答案。
- [React 设计模式](https://www.patterns.dev/) - 讲解 React 开发中常用的组件模式、状态管理模式等，提升代码质量。
- [Bulletproof React](https://github.com/alan2207/bulletproof-react) - 生产级 React 应用架构指南，涵盖项目结构、TypeScript、测试等。
- [React + TypeScript 速查表](https://github.com/typescript-cheatsheets/react-typescript-cheatsheet) - 帮有 React 基础的开发者快速上手 TypeScript 开发。
- [GraphQL 全栈教程](https://github.com/howtographql/howtographql) - 讲解 React 与 GraphQL 结合的开发流程（Apollo Client 为主）。


## 二、React 框架（完整开发方案）
框架封装了路由、构建、部署等底层能力，是开发中大型应用的首选，无需从零搭建项目。

| 框架名称 | 核心价值与适用场景 |
|----------|--------------------|
| [Next.js](https://github.com/vercel/next.js) | 目前最主流的 React 框架，支持 **SSR（服务端渲染）、SSG（静态站点生成）、App Router（React Server Components）**，适合博客、电商、官网等几乎所有场景，部署适配 Vercel 极方便。 |
| [Remix](https://github.com/remix-run/remix) | 全栈框架，强调“嵌套路由”和“数据加载与提交的一致性”，与后端集成紧密（支持 Node/Cloudflare 等），适合需要强后端交互的应用。 |
| [Gatsby](https://github.com/gatsbyjs/gatsby) | 专注 **静态站点生成（SSG）**，生态丰富（插件多），适合博客、文档、营销页等内容型站点。 |
| [React Admin](https://github.com/marmelab/react-admin) | 专为 **B2B 后台系统** 设计的框架，内置数据表格、表单、权限等组件，快速搭建管理后台。 |
| [Refine](https://github.com/refinedev/refine) | 无约束的 CRUD 应用框架，支持多种后端（REST/GraphQL）和 UI 库，灵活性高，适合定制化后台。 |


## 三、UI 组件库（快速搭建界面）
无需重复开发基础组件，直接使用成熟库加速开发，重点关注**可定制性、无障碍性、设计风格**。

| 组件库名称 | 核心特点 | 适用场景 |
|------------|----------|----------|
| [MUI (原 Material-UI)](https://github.com/mui/material-ui) | 基于 Material Design，组件丰富（按钮、卡片、表格等），生态成熟，可定制性强。 | 通用 Web 应用、企业级产品。 |
| [Ant Design](https://github.com/ant-design/ant-design) | 阿里出品的企业级 UI 库，组件全面（支持复杂表单、树形控件等），设计风格稳重。 | 后台系统、B 端产品。 |
| [shadcn-ui](https://github.com/shadcn-ui/ui) | 近年爆火的“拷贝式”组件库，基于 Radix UI（无障碍）和 Tailwind CSS，**无包体积负担**，可完全定制样式。 | 追求设计独特性、重视无障碍的应用。 |
| [Mantine](https://github.com/mantinedev/mantine) | 全功能组件库，内置表单、通知、模态框等，对 TypeScript 支持极佳，文档友好。 | 中大型应用，需要一站式组件解决方案。 |
| [Ariakit](https://github.com/ariakit/ariakit) | 轻量的**无障碍组件工具包**，只提供核心逻辑，样式完全自定义，适合需要深度定制 UI 的场景。 | 对无障碍（a11y）要求高、设计个性化的项目。 |
| [React Bootstrap](https://github.com/react-bootstrap/react-bootstrap) | Bootstrap 组件的 React 实现，适合熟悉 Bootstrap 风格的开发者。 | 快速搭建简单界面、原型。 |
| [Fluent UI](https://github.com/microsoft/fluentui) | 微软 Fluent Design 风格，组件贴合 Windows 生态，适合微软系产品。 | 企业级应用、与微软服务集成的项目。 |


## 四、状态管理与数据获取
解决“组件间数据共享”和“异步数据（接口请求）管理”问题，不同方案对应不同复杂度场景。

### 1. 状态管理（同步状态）
| 工具名称 | 核心价值 | 适用场景 |
|----------|----------|----------|
| [Redux Toolkit](https://redux-toolkit.js.org/) | Redux 的官方推荐工具集，简化 Redux 模板代码（如 createSlice），内置 immer 和 devTools。 | 中大型应用、需要严格状态追踪的场景（如电商购物车）。 |
| [Zustand](https://github.com/pmndrs/zustand) | 轻量无 Provider 的状态管理，API 简洁（直接用 hook 取状态），支持中间件。 | 中小型应用、追求简洁的项目。 |
| [Jotai](https://github.com/pmndrs/jotai) | 原子化状态管理，状态可拆分（类似 Recoil），无 Provider，支持 Suspense。 | 需要精细控制状态依赖、避免不必要重渲染的场景。 |
| [MobX](https://github.com/mobxjs/mobx) | 基于“响应式”的状态管理，修改状态直接赋值（无需 immutable），学习成本低。 | 快速开发、不喜欢 Redux 模板代码的项目。 |
| [XState](https://github.com/statelyai/xstate) | 基于“状态机”的管理工具，适合复杂业务逻辑（如表单步骤、支付流程），可可视化状态流转。 | 业务逻辑复杂、状态流转多的场景。 |

### 2. 数据获取（异步状态）
| 工具名称 | 核心价值 | 适用场景 |
|----------|----------|----------|
| [TanStack Query](https://tanstack.com/query/latest) | 专注异步数据管理（接口请求、缓存、刷新），支持缓存优化、自动重试、无限滚动。 | 所有需要请求接口的应用，替代传统的 useEffect + useState 写法。 |
| [SWR](https://github.com/vercel/swr) | Vercel 出品，与 TanStack Query 功能类似，API 更简洁，适合 Vercel 部署的项目。 | 中小型应用、需要快速集成异步数据管理的场景。 |
| [Apollo Client](https://github.com/apollographql/apollo-client) | 成熟的 GraphQL 客户端，支持缓存、查询合并、实时数据。 | 使用 GraphQL 作为 API 层的应用。 |

### 3.  Immutable 工具（辅助状态管理）
- [Immer](https://github.com/immerjs/immer) - 简化 immutable 数据操作，“直接修改”草稿数据即可生成新的 immutable 数据，无需手动深拷贝。
- [Immutable.js](https://github.com/immutable-js/immutable-js) - 早期流行的 immutable 库，提供 List/Map 等数据结构，现在更多被 Immer 替代（除非需要复杂 immutable 操作）。


## 五、样式解决方案
React 中常见的样式写法，各有优缺点，根据项目需求选择。

| 方案名称 | 核心特点 | 适用场景 |
|----------|----------|----------|
| [Tailwind CSS](https://tailwindcss.com/) | **Utility-First（工具类优先）** 样式库，通过类名组合快速实现样式，无需写 CSS 文件。 | 追求开发效率、设计系统统一的项目（常与 shadcn-ui 搭配）。 |
| [Styled Components](https://github.com/styled-components/styled-components) | CSS-in-JS 代表，样式与组件绑定，支持动态样式（通过 props 传值）。 | 组件样式独立、需要动态调整样式的场景。 |
| [Emotion](https://github.com/emotion-js/emotion) | 轻量的 CSS-in-JS 库，性能比 Styled Components 好，支持多种写法（字符串/对象）。 | 对性能有要求的 CSS-in-JS 项目。 |
| [Vanilla Extract](https://github.com/seek-oss/vanilla-extract) | 零运行时的 CSS-in-TypeScript，样式在构建时生成 CSS 文件，兼顾类型安全和性能。 | 大型项目、重视性能和类型安全的场景。 |


## 六、路由管理
控制页面跳转、URL 与组件的映射，是单页应用（SPA）的核心。

| 路由工具 | 核心价值 | 适用场景 |
|----------|----------|----------|
| [React Router](https://github.com/remix-run/react-router) | 官方推荐的路由库，支持嵌套路由、参数传递、懒加载，适配 Next.js/Remix 等框架。 | 绝大多数 React 应用（SPA/SSR 均可）。 |
| [TanStack Router](https://github.com/TanStack/router) | 新一代 TypeScript 路由，**类型安全**（自动推导参数类型），内置缓存和 URL 状态管理。 | 重视类型安全、使用 TypeScript 的大型项目。 |
| [Wouter](https://github.com/molefrog/wouter) | 轻量路由（仅 1KB），API 简洁，无需 Provider，适合小型应用。 | 原型、小型 SPA 项目。 |


## 七、开发工具（提升开发效率）
包含项目搭建、调试、编译等工具，直接影响开发体验。

| 工具名称 | 核心价值 | 适用场景 |
|----------|----------|----------|
| [Vite](https://github.com/vitejs/vite) | 新一代构建工具，**启动/热更新极快**，支持 TypeScript、React 等，零配置开箱即用。 | 目前首选的 React 项目搭建工具（替代 Create React App）。 |
| [Create React App](https://github.com/facebook/create-react-app) | 曾经的官方推荐工具，零配置搭建 React 项目，但现在因速度慢逐渐被 Vite 替代。 | 维护旧项目、不熟悉 Vite 的新手。 |
| [Million](https://github.com/aidenybai/million) | React 性能优化编译器，通过虚拟 DOM 优化提升渲染速度，可无缝集成到现有项目。 | 大型 React 应用，需要优化渲染性能的场景。 |
| [Reactotron](https://github.com/skellock/reactotron) | 桌面调试工具，可查看组件状态、API 请求、Redux 流转，支持 React/React Native。 | 中大型项目调试，需要追踪数据流转的场景。 |
| [ESLint + eslint-plugin-react](https://github.com/yannickcr/eslint-plugin-react) | 代码检查工具，检测 React 语法错误、规范代码风格（如 Hooks 使用规则）。 | 所有项目，保证代码质量和一致性。 |
| [Vitest](https://vitest.dev/) | 与 Vite 配套的测试工具，比 Jest 更快，支持 ESM，适合 Vite 项目的单元测试。 | Vite 项目的单元测试、组件测试。 |


## 八、表单处理与验证
解决表单状态管理、校验、提交等痛点，是业务应用的核心需求。

| 工具名称 | 核心价值 | 适用场景 |
|----------|----------|----------|
| [React Hook Form](https://github.com/react-hook-form/react-hook-form) | 性能优先的表单库，**减少重渲染**，API 简洁，支持原生表单校验。 | 所有表单场景，尤其重视性能的应用。 |
| [Zod](https://zod.dev/) | 类型安全的校验库，常与 React Hook Form 搭配，通过 TypeScript 推导校验规则和表单类型。 | 需要强类型校验的表单场景（如注册、提交数据）。 |
| [Formik](https://github.com/jaredpalmer/formik) | 易用的表单库，封装了表单状态（value/error/touched），学习成本低。 | 中小型表单、追求快速开发的场景。 |
| [Formily](https://github.com/alibaba/formily) | 阿里出品的复杂表单解决方案，支持动态表单、可视化设计，适合企业级场景。 | 大型后台系统、复杂动态表单（如流程配置）。 |


## 九、表格与数据网格
处理结构化数据展示，支持排序、筛选、分页等功能，是后台系统的核心组件。

| 工具名称 | 核心价值 | 适用场景 |
|----------|----------|----------|
| [TanStack Table](https://github.com/TanStack/table) | Headless（无 UI）表格工具，只提供逻辑（排序/筛选/分页），样式完全自定义。 | 需要深度定制表格 UI 的场景。 |
| [React Data Grid](https://github.com/adazzle/react-data-grid) | 功能丰富的表格组件，支持编辑、合并单元格、树形结构，适合企业级需求。 | 后台系统、需要编辑数据的表格场景。 |
| [AG Grid React](https://www.ag-grid.com/react-data-grid/) | 企业级表格解决方案，支持大数据量、自定义渲染、导出，功能极其强大（部分功能收费）。 | 大型企业应用、处理百万级数据的场景。 |
| [React Grid Layout](https://github.com/react-grid-layout/react-grid-layout) | 可拖拽、可调整大小的网格布局组件，适合仪表盘（Dashboard）场景。 | 数据可视化仪表盘、自定义布局页面。 |


## 十、测试工具
保障代码质量，包含单元测试、组件测试、E2E 测试。

| 测试类型 | 工具名称 | 核心价值 |
|----------|----------|----------|
| 单元/组件测试 | [@testing-library/react](https://testing-library.com/docs/react-testing-library/intro/) | 测试“用户行为”而非组件实现，贴近真实使用场景，React 官方推荐。 |
| 单元/组件测试 | [Vitest](https://vitest.dev/) | 与 Vite 无缝集成，启动快、支持 ESM，替代 Jest 用于 Vite 项目。 |
| E2E 测试 | [Cypress](https://github.com/cypress-io/cypress) | 浏览器端 E2E 测试，支持实时预览、截图录屏，易于调试。 | 模拟用户完整操作流程（如登录→下单）。 |
| 组件测试 | [Storybook](https://github.com/storybookjs/storybook) | 组件开发环境，可孤立开发/测试组件，生成组件文档（“组件沙箱”）。 | 组件库开发、团队共享组件规范。 |


## 十一、动画与交互
提升页面体验，实现过渡、手势、3D 等效果。

| 工具名称 | 核心价值 | 适用场景 |
|----------|----------|----------|
| [Framer Motion](https://github.com/framer/motion) | 最流行的 React 动画库，API 简洁，支持过渡动画、手势（拖拽/缩放）、滚动触发。 | 绝大多数前端动画场景（按钮反馈、页面过渡）。 |
| [React Spring](https://github.com/pmndrs/react-spring) | 基于物理弹簧的动画库，动画更自然（如弹性回弹），支持 3D 动画。 | 需要模拟真实物理效果的动画（如拖拽后的回弹）。 |
| [Auto Animate](https://github.com/formkit/auto-animate) | 零配置动画工具，只需一行代码即可为列表增删、组件显隐添加过渡效果。 | 快速实现简单过渡动画（如弹窗、列表更新）。 |
| [React Three Fiber](https://github.com/pmndrs/react-three-fiber) | Three.js 的 React 封装，可通过 React 组件编写 3D 场景。 | 3D 可视化、游戏、创意展示页面。 |


## 十二、React 渲染器（拓展 React 能力）
让 React 不仅能渲染网页，还能渲染到其他载体（3D、PDF、CLI 等）。
- [React Three Fiber](https://github.com/pmndrs/react-three-fiber) - 渲染 3D 场景（基于 Three.js）。
- [Remotion](https://github.com/remotion-dev/remotion) - 用 React 组件编写视频（支持动画、动态数据）。
- [React PDF](https://github.com/diegomura/react-pdf) - 用 React 组件生成 PDF 文件（支持文本、图片、表格）。
- [Ink](https://github.com/vadimdemedes/ink) - 用 React 编写交互式 CLI 应用（命令行界面）。


## 十三、国际化（i18n）
解决多语言适配问题，支持不同地区的文本、日期、货币格式。
- [React i18next](https://github.com/i18next/react-i18next) - 最流行的 React 国际化库，支持多语言切换、插值、复数，生态丰富（可集成翻译管理工具）。
- [Format.js](https://github.com/formatjs/formatjs) - 基于 ICU 语法的国际化工具，支持复杂的文本格式化（如性别、复数），适合企业级应用。


## 十四、React Native（跨平台开发）
用 React 编写 iOS/Android 原生应用，共享前端技术栈。

### 1. 基础资源
- [React Native 官网](https://reactnative.dev/) - 官方文档，学习基础语法和原生交互。
- [Expo](https://expo.dev/) - 简化 React Native 开发的工具链，无需配置原生环境，支持热更新。
- [Expo Snack](https://snack.expo.dev/) - 在线编写 React Native 代码，可实时在手机上预览。

### 2. 导航
- [React Navigation](https://github.com/react-navigation/react-navigation) - 最流行的 React Native 导航库，支持栈导航、标签导航、抽屉导航。
- [React Native Navigation](https://github.com/wix/react-native-navigation) - 基于原生导航组件，性能更好，适合需要原生体验的应用。

### 3. 组件与库
- [React Native Paper](https://callstack.github.io/react-native-paper/) - Material Design 风格的组件库，组件丰富，适配 iOS/Android。
- [React Native Vector Icons](https://github.com/oblador/react-native-vector-icons) - 支持多种图标库（FontAwesome、Material Icons），自定义性强。
- [React Native Gifted Chat](https://github.com/FaridSafi/react-native-gifted-chat) - 成熟的聊天 UI 组件，支持消息气泡、输入框、头像。
- [Realm JS](https://github.com/realm/realm-js) - 轻量的本地数据库，适合存储离线数据（替代 SQLite）。


## 十五、真实项目参考
通过开源项目学习最佳实践：
- [Mattermost](https://github.com/mattermost/mattermost-server) - 开源企业级聊天工具，用 React 开发前端。
- [Kibana](https://github.com/elastic/kibana) - Elastic Stack 的可视化平台，React 开发的复杂数据可视化应用。
- [Webamp](https://github.com/captbaritone/webamp) - 浏览器端的 Winamp 播放器复刻，展示 React 处理复杂交互的能力。
- [Remotion Examples](https://github.com/remotion-dev/examples) - Remotion 视频生成的示例项目（如数据可视化视频）。
