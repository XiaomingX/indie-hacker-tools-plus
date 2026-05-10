# 微信小程序开发资源精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，小程序开发已进入 **"跨端与云原生"** 时代。
> - **跨端首选**：如果你需要同时发布 H5 和 App，**uni-app (Vue)** 或 **Taro (React)** 是工业级标准。
> - **全栈加速**：优先使用 **微信云开发 (CloudBase)**，无需购买服务器和域名备案，即可实现数据库、文件存储和云函数能力。

---

## 🏗️ 核心框架与工具 (Frameworks & Tools)

- [ ] [**uni-app**](https://github.com/dcloudio/uni-app) - **[首选]** 使用 Vue 语法，一套代码发布到微信、支付宝、抖音、H5 和 App。
- [ ] [**Taro**](https://github.com/NervJS/taro) - 京东出品，使用 React/Vue/Nerv 语法开发多端应用，适合 React 开发者。
- [ ] [**Mpx**](https://github.com/didi/mpx) - 滴滴出品，专注于极致性能增强的原生小程序框架，适合大型复杂项目。
- [ ] [**Weconsole**](https://github.com/weimobGroup/WeConsole) - 强大的移动端调试面板，在手机上也能拥有 Chrome DevTools 的体验。

---

## 🎨 UI 组件库 (UI Kits)

- [ ] [**Vant Weapp**](https://github.com/youzan/vant-weapp) - 有赞出品，移动端组件库标杆，样式精美且文档完备。
- [ ] [**Lin UI**](https://github.com/TaleLin/lin-ui) - 设计优良、基于原生小程序语法的 UI 组件库。
- [ ] [**WeUI-WXSS**](https://github.com/Tencent/weui-wxss) - 腾讯官方出品，完美适配微信原生视觉风格。
- [ ] [**Wux Weapp**](https://github.com/wux-weapp/wux-weapp) - 组件化程度高、可复用性强的 UI 库。

---

## 🧩 实用功能组件 (Utilities)

- [ ] [**mp-html**](https://github.com/jin-yufeng/mp-html) - **2026 推荐**。目前最好用的小程序富文本组件，完美支持 HTML 渲染与编辑。
- [ ] [**Weapp-QRCode**](https://github.com/tomfriwel/weapp-qrcode) - 纯 JS 实现的小程序二维码生成工具。
- [ ] [**Image-Cropper**](https://github.com/1977474741/image-cropper) - 丝滑的图片裁剪组件，适合头像上传等场景。
- [ ] [**Weapp-Cookie**](https://github.com/charleslo1/weapp-cookie) - 一行代码让小程序支持传统的 Cookie 机制。

---

## 🚀 最佳实践与 Demo (Best Practices)

- [ ] [**微信云开发 (CloudBase)**](https://developers.weixin.qq.com/miniprogram/dev/wxcloud/basis/getting-started.html) - 独立开发者必学，大幅降低后端运维成本。
- [ ] [**Gitter**](https://github.com/huangjianke/Gitter) - 颜值极高的 GitHub 小程序客户端示例（Taro 实现）。
- [ ] [**Focus-clock**](https://github.com/realyao/WXminiprogram-Focus-clock) - 简洁的时间管理/番茄钟小程序示例。

---

## 💡 选型建议
1. **追求开发效率与生态**：选 **uni-app** + **Vant Weapp**。
2. **需要极致性能与原生控制**：选 **原生开发** + **Mpx**。
3. **独立开发者 MVP**：必选 **微信云开发**，省去备案、HTTPS 证书和服务器运维。
4. **复杂数据展示**：使用 **echarts-for-weixin** 进行图表可视化。
