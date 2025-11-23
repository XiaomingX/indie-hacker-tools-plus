# awesome-captcha-plus：验证码资源精选


## 常用验证码库  
这些是各编程语言/框架中主流的验证码工具，方便开发者快速集成到项目中。

- [mewebstudio/captcha](https://github.com/mewebstudio/captcha)  
  Laravel 框架专用验证码库，支持生成数字、字母混合的图形验证码，配置简单，适合快速集成到 PHP 项目中。

- [google/recaptcha](https://github.com/google/recaptcha)  
  谷歌推出的经典验证码服务，目前主流版本为 v2（点击验证）和 v3（无交互，通过用户行为打分），广泛用于防止垃圾注册、评论刷屏等场景。

- [mojocn/base64Captcha](https://github.com/mojocn/base64Captcha)  
  Golang 语言的验证码库，支持数字、字母、算术题等多种类型，生成的验证码以 Base64 格式输出，无需保存图片文件，特别适合前后端分离项目。

- [ArgoZhang/SliderCaptcha](https://github.com/ArgoZhang/SliderCaptcha)  
  支持移动端的滑块验证码实现，用户通过滑动拼图完成验证，兼顾安全性和用户体验，适合 App 或移动端网页。

- [hCaptcha](https://www.hcaptcha.com)  
  可替代 reCAPTCHA 的隐私友好型验证码服务，不追踪用户数据，同时支持文字识别、图像分类等验证方式，适合注重隐私的网站。

- [Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/)  
  Cloudflare 推出的「无感知验证码」，用户完全无需任何操作（无点击、无滑动），通过后台分析判断是否为机器人，对用户体验影响极小。

- [FriendlyCaptcha](https://github.com/FriendlyCaptcha/friendly-challenge)  
  开源的无交互验证码方案，用户无需任何操作，仅通过前端运行轻量任务验证，强调开源透明和隐私保护，适合自建服务。

- [django-simple-captcha](https://github.com/mbi/django-simple-captcha)  
  Python/Django 框架专用验证码库，支持动态生成图形验证码，可自定义样式和验证逻辑，集成简单。


## 验证码生成工具  
专注于生成各类验证码的库，支持不同格式和场景需求。

- [dchest/captcha](https://github.com/dchest/captcha)  
  Go 语言实现的验证码库，不仅支持生成图形验证码，还能生成音频验证码（帮助视障用户），安全性较高。

- [lepture/captcha](https://github.com/lepture/captcha)  
  Python 验证码库，支持生成图形和音频验证码，可自定义字符集、干扰线等参数，适合 Flask、Django 等框架。

- [lemonce/svg-captcha](https://github.com/lemonce/svg-captcha)  
  Node.js 环境下的 SVG 验证码生成工具，生成的验证码是矢量图（放大不失真），无需依赖图片处理库，轻量高效。

- [Captcha.NET](https://github.com/VahidN/Captcha)  
  基于 ASP.NET Core 的验证码库，支持生成图形验证码和数学计算题验证码，自带验证逻辑，适合 .NET 开发者。

- [Android-SlideVerify](https://github.com/mcxtzhang/SwipeCaptcha)  
  Android 平台的滑动验证码组件，提供现成的滑动验证 UI 和验证逻辑，可直接集成到 App 中。


## 商业解决方案  
功能更全面、支持更完善的付费验证码服务，适合企业级应用。

- [BotDetect CAPTCHA](https://captcha.com/)  
  高度定制化的商业验证码服务，支持图像、音频、数学题等多种验证类型，提供多语言 SDK，适合对安全性和定制化要求高的场景。

- [Geetest CAPTCHA](https://www.geetest.com/en)  
  国内流行的行为验证服务，以滑块、拼图、点选文字等交互形式为主，通过分析用户操作行为判断是否为机器人，用户体验流畅，适合中文场景。


## 验证码破解与识别  
用于研究验证码安全性的技术和工具（注：请遵守法律法规，仅用于合法研究）。

- [zakizhou/CAPTCHA](https://github.com/zakizhou/CAPTCHA)  
  基于 TensorFlow 的验证码识别工具，通过训练模型对简单图形验证码进行分类识别，适合学习深度学习在验证码识别中的应用。

- [ypwhs/captcha_break](https://github.com/ypwhs/captcha_break)  
  使用 Keras 搭建的 CNN（卷积神经网络）模型，用于破解数字、字母混合的图形验证码，附带有训练数据和示例。

- [chxj1992/slide_captcha_cracker](https://github.com/chxj1992/slide_captcha_cracker)  
  基于 Canny 边缘检测算法的滑块验证码破解工具，通过识别滑块和目标位置，自动计算滑动路径。

- [Anti-Captcha](https://anti-captcha.com/)  
  在线验证码破解服务，支持自动识别 reCAPTCHA、hCaptcha 等主流验证码，常用于爬虫或自动化测试场景（需注意合规性）。

### 中文验证码相关  
- [taosir/cnn_handwritten_chinese_recognition](https://github.com/taosir/cnn_handwritten_chinese_recognition)  
  基于 CNN 的手写汉字识别模型，可用于研究中文验证码（如汉字点选、手写输入类）的识别方法。


## 辅助工具  
- [Tesseract](https://github.com/tesseract-ocr/tesseract)  
  开源 OCR（光学字符识别）引擎，可辅助识别简单的图形验证码文字内容，常与图像处理库（如 OpenCV）配合使用。


### 补充说明  
验证码的核心是平衡「安全性」和「用户体验」：  
- 简单的图形验证码易被破解，复杂的又会影响用户体验；  
- 现代趋势更倾向于「无交互验证码」（如 Cloudflare Turnstile），通过分析用户行为、设备指纹等后台数据判断是否为机器人，既安全又友好。  

选择时需根据自身场景（如网站流量、安全等级、用户群体）决定合适的方案。
