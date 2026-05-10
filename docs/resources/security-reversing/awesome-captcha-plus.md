# 验证码解决方案精选 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年，验证码的趋势是 **"Invisible (无感)"**。
> - **优先选型**：首选 **Cloudflare Turnstile**，它对真实用户完全透明（无需点击），且防御能力极强。
> - **隐私保护**：如果你需要替代 Google reCAPTCHA 且注重隐私，**hCaptcha** 是最佳平衡点。
> - **安全性 vs 体验**：复杂的图形验证码已无法阻挡现代 AI (CNN/Transformers) 的识别，反而会驱逐你的真实用户。

---

## 🛡️ 无感与隐私友好型方案 (Invisible & Privacy)

- [ ] [**Cloudflare Turnstile**](https://www.cloudflare.com/products/turnstile/) - **[首选]** 真正的无感验证，基于用户行为分析，完全免费且隐私保护极佳。
- [ ] [**hCaptcha**](https://www.hcaptcha.com/) - 隐私友好的 reCAPTCHA 替代品，支持通过完成简单任务（如图片分类）来赚取奖励。
- [ ] [**FriendlyCaptcha**](https://github.com/FriendlyCaptcha/friendly-challenge) - 开源的 Proof-of-Work (PoW) 方案，让用户设备后台运行轻量计算完成验证，对用户透明。

---

## 🏗️ 编程语言专用库 (Framework Specific)

- [ ] [**base64Captcha (Golang)**](https://github.com/mojocn/base64Captcha) - 支持多种图形、算术题类型，Base64 输出，完美适配前后端分离架构。
- [ ] [**svg-captcha (Node.js)**](https://github.com/lemonce/svg-captcha) - 生成矢量图形验证码，无需 C++ 依赖（如 canvas），轻量高性能。
- [ ] [**django-simple-captcha (Python)**](https://github.com/mbi/django-simple-captcha) - Django 框架集成最简单的验证码方案。
- [ ] [**mewebstudio/captcha (PHP/Laravel)**](https://github.com/mewebstudio/captcha) - Laravel 社区最常用的验证码工具包。

---

## 📱 交互式与滑块验证 (Interactive)

- [ ] [**SliderCaptcha**](https://github.com/ArgoZhang/SliderCaptcha) - 经典的滑块拼图验证，适合移动端与 App 登录场景。
- [ ] [**SwipeCaptcha (Android)**](https://github.com/mcxtzhang/SwipeCaptcha) - 专门为 Android 原生应用优化的滑动验证组件。
- [ ] [**Geetest (极验)**](https://www.geetest.com/) - 国内行为验证的标杆，提供极其流畅的点选、拼图交互。

---

## 🔬 验证码识别与安全研究 (Research & Tools)

- [ ] [**Tesseract OCR**](https://github.com/tesseract-ocr/tesseract) - 用于识别简单文本验证码的开源引擎。
- [ ] [**captcha_break (Keras/CNN)**](https://github.com/ypwhs/captcha_break) - 学习如何利用卷积神经网络识别混合图形验证码。
- [ ] [**Anti-Captcha**](https://anti-captcha.com/) - 商业化的验证码代过服务，常用于爬虫测试（注意合规性）。

---

## 💡 选型建议
1. **追求极致用户转化**：无脑选 **Cloudflare Turnstile**，用户甚至不知道验证码的存在。
2. **需要强力对抗高级爬虫**：使用 **hCaptcha Enterprise** 或 **Geetest v4**。
3. **轻量级、不依赖外部服务**：选 **svg-captcha** (Node) 或 **base64Captcha** (Go)。
4. **辅助功能支持**：确保你的验证码方案提供 **音频验证 (Audio Captcha)** 以支持视障用户。
