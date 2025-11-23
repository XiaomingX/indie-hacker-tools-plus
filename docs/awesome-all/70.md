# awesome-cloudflare  
⛅️ 精选的 Cloudflare 工具、开源项目、指南、博客和其他资源列表。

## 图床

| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| [cf-image-hosting](https://github.com/ifyour/cf-image-hosting) | 在 Telegraph 上免费无限制地托管图像，部署在 Cloudflare 上。 |  | 维护中 |
| [img-mom](https://github.com/beilunyang/img-mom) | 基于 Cloudflare Workers 运行时构建，轻量使用完全免费，支持多种图床（Telegram/Cloudflare R2/Backblaze B2等），快速部署。使用 Wrangler 可快速实现自部署 | | 维护中 |
| [workers-image-hosting](https://github.com/iiop123/workers-image-hosting) | 基于 Cloudflare Workers，数据存储于 KV 的图床 | | 维护中 |
| [Telegraph-Image](https://github.com/cf-pages/Telegraph-Image) | 免费图片托管解决方案，Flickr/imgur 替代品。使用 Cloudflare Pages 和 Telegraph。 |  | 维护中 |
| [cloudflare-worker-image](https://github.com/ccbikai/cloudflare-worker-image) | 使用 Cloudflare Worker 处理图片，依赖 Photon，支持缩放、剪裁、水印、滤镜等功能。 | | 维护中 |
| [tgState](https://github.com/csznet/tgState) | 使用 Telegram 作为存储的文件外链系统，不限制文件大小和格式。 |  | 维护中 |
| [telegraph-Image](https://github.com/x-dr/telegraph-Image) | 一个图床。 |  | 维护中 |
| [roim-picx](https://github.com/roimdev/roim-picx) | 基于 Cloudflare Pages 和 R2 实现的免费图床。 | | 维护中 |
| [CloudFlare-ImgBed](https://github.com/MarSeventh/CloudFlare-ImgBed) | 基于 Cloudflare 和 Telegraph 的免费图床，本仓库基于  ，是原项目前端页面的重制版。开源、清晰、美观、动画丝滑、玩法多样！ |  | 维护中 |

## 网站分析
| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| counterscale | 简单的 Web 分析跟踪器和仪表板，类似 umami，可自行托管，低成本。 | https://github.com/benvinegar/counterscale | 维护中 |

## 邮箱

| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| [vmail](https://github.com/oiov/vmail) | 开源临时邮箱工具，支持收发邮件。 |  | 维护中 |
| [smail](https://github.com/akazwz/smail) | 临时邮箱服务 |  | 维护中 |
| [Email.ML](https://email.ml/) | 运行在 Cloudflare 网络中的临时邮箱 | | 未开源 |
| [cloudflare_temp_email](https://github.com/dreamhunter2333/cloudflare_temp_email) | 使用 Cloudflare 免费服务搭建临时邮箱，D1 作为数据库，支持多国语言及自动回复功能，支持附件 IMAP SMTP |  | 维护中 |
| [mail2telegram](https://github.com/TBXark/mail2telegram) | 基于 Cloudflare Email Routing Worker 的 Telegram Bot，将邮件转换为 Telegram 消息，支持无限临时邮箱地址。 | | 维护中 |
| [AuthInbox](https://github.com/TooonyChen/AuthInbox) | 自建开源多邮箱验证码接码平台，基于 Cloudflare 免费服务，自动处理邮件验证码，支持 Bark 实时通知。 | | 维护中 |

## 博客

| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| [cloudflare-workers-blog](https://github.com/gdtool/cloudflare-workers-blog) | 运行在 Cloudflare Workers 上的博客程序，使用 Cloudflare KV 作为数据库，无其他依赖，兼顾静态和动态博客。 |  | 维护中 |
| [microfeed](https://github.com/microfeed/microfeed) | 在 Cloudflare 上自托管的轻量级内容管理系统 (CMS)，支持多种内容发布格式。 |  | 维护中 |
| [emaction.frontend](https://github.com/emaction/emaction.frontend) | 基于 Cloudflare D1 实现的 GitHub 风格 Reactions 点赞功能（前端）。 |  | 维护中 |
| [emaction.backend](https://github.com/emaction/emaction.backend) | 基于 Cloudflare D1 实现的 GitHub 风格 Reactions 点赞功能（后端）。 |  | 维护中 |
| [serverless-cloud-notepad](https://github.com/s0urcelab/serverless-cloud-notepad) | 基于 Cloudflare Worker 实现的 Serverless 云笔记。 |  | 维护中 |

## 脚手架

| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| [nextflare](https://github.com/ccbikai/nextflare) | Next.js App 运行于 Cloudflare，集成 Lemon Squeezy。 |  | 维护中 |

## 短链

| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| [short](https://github.com/igengdu/short/) | 使用 Cloudflare Pages 创建的 URL 缩短器。 |  | 维护中 |
| [short](https://github.com/x-dr/short) | 使用 Cloudflare Pages 创建的 URL 缩短器。 |  | 维护中 |
| [linklet](https://github.com/harrisonwang/linklet) | 基于 API 模式的 URL 缩短器，使用场景更多。 |  | 维护中 |
| [Url-Shorten-Worker](https://github.com/crazypeace/Url-Shorten-Worker) | 支持自定义短链，秘密路径访问，集成多功能（短链、网络记事本、图床）。 |  | 维护中 |
| [Url-Shorten-Worker](https://github.com/horsemail/Url-Shorten-Worker) | crazypeace 分支的 fork，增加管理员用户、正则匹配、环境变量配置等。 |  | 维护中 |
| [CloudFlare-Pages-UrlShorten](https://github.com/Jiaocz/CloudFlare-Pages-UrlShorten) | 多功能 URL 短链工具。 | | 维护中 |
| [Url-Shorten-Worker](https://github.com/Monopink/Url-Shorten-Worker/) | 优化页面，增加管理员用户和访客身份，支持正则表达式匹配和环境变量配置。 |  | 维护中 |
| [CloudflareWorker-KV-UrlShort](https://github.com/Ai-Yolo/CloudflareWorker-KV-UrlShort) | 支持自定义首页、菜单短链、文本和网页分享 URL。 | | 维护中 |
| [Sink](https://github.com/ccbikai/Sink) | 完全运行于 Cloudflare 的简单快速安全链接缩短器，具备分析功能和控制台面板。 |  | 维护中 |
| [short](https://github.com/molikai-work/short) | 基于 x-dr/short，新增短链密码、管理、Turnstile 验证、黑名单域名、多域名配置等。 |  | 维护中 |

## 网站分析

| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| [analytics_with_cloudflare](https://github.com/yestool/analytics_with_cloudflare) | 免费开源网页访客计数器，基于 Cloudflare Worker 和 D1 数据库，实现功能与“不蒜子”类似。 |  | 维护中 |
| [counterscale](https://github.com/benvinegar/counterscale) | 简单的 Web 分析跟踪器和仪表板，类似 umami，可自行托管，低成本。 |  | 维护中 |
| [HanAnalytics](https://github.com/uxiaohan/HanAnalytics) | 部署在 Cloudflare Pages 上的简易网络分析跟踪器，支持设备、来源、国家等数据查看，支持密码访问和域名白名单。 | | 维护中 |

## 隧道

| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| [Cloudflared-web](https://github.com/WisdomSky/Cloudflared-web) | Docker 镜像，集成 cloudflared CLI 和简单 Web UI，方便启动/停止 Cloudflare 隧道。 | | 维护中 |

## 加速

| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| [gh-proxy](https://github.com/hunshcn/gh-proxy) | github release、archive 及项目文件加速，支持 clone，含 Cloudflare Workers 无服务器版本和 Python 版本。 |  | 维护中 |
| [gh-proxy](https://github.com/crazypeace/gh-proxy) | github release、archive 及项目文件加速，支持 api.github.com, git.io。 |  | 维护中 |
| [cf-proxy-ex](https://github.com/1234567Yang/cf-proxy-ex) | Cloudflare 超级代理，支持 Duckduckgo 代理、OpenAI/ChatGPT 代理、Github 加速等。 |  | 维护中 |
| [cloudflare-docker-proxy](https://github.com/ciiiii/cloudflare-docker-proxy) | 在 Cloudflare Worker 上运行的 Docker Hub 注册代理。 | | 维护中 |
| [CF-Workers-docker.io](https://github.com/cmliu/CF-Workers-docker.io) | 基于 Cloudflare Workers 的 Docker 镜像代理工具，解决访问限制和加速访问问题。 |  | 维护中 |

## 文件分享

| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| [pastebin-worker](https://github.com/SharzyL/pastebin-worker) | 部署在 Cloudflare Workers 上的开源 Pastebin，支持文本/文件分享，支持密码和删除时间设置。 |  | 维护中 |
| [FileWorker](https://github.com/yllhwa/FileWorker) | 运行在 Cloudflare Worker 上的在线剪贴板/文件共享。 | | 维护中 |
| [cf-files-sharing](https://github.com/joyance-professional/cf-files-sharing) | 利用 Cloudflare Workers 全球加速优势，实现支持密码保护的文件分享，集成 D1 数据库和 R2 存储。 | | 维护中 |

## 测速

| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| [CloudflareSpeedTest](https://github.com/XIU2/CloudflareSpeedTest) | 帮助选择适合中国内地的 Cloudflare IP，降低延迟和丢包。 | | 维护中 |
| [SpeedTest](https://speed.cloudflare.com/) | 官方 SpeedTest 工具。 | | 运行中 |

## 监控

| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| [UptimeFlare](https://github.com/lyc8503/UptimeFlare) | 基于 Cloudflare Worker 的无服务器站点监控工具，支持多协议端口监控，全球多城市地理位置特定检查，自定义请求和响应校验。 | | 维护中 |
| [cf-workers-status-page](https://github.com/eidam/cf-workers-status-page) | 监控网站状态，展示历史记录，状态变化时通过 Slack 通知，基于 Cloudflare Workers、CRON 和 KV。 |  | 维护中 |

## 文章

| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| [workers](https://igdux.com/workers) | Cloudflare Workers 优秀项目收集。 | | 有效中 |
| [accelerate-and-secure-with-cloudflared](https://nova.moe/accelerate-and-secure-with-cloudflared/) | 教你使用 Cloudflare Argo Tunnel(cloudflared) 加速和保护网站。 | | 有效中 |
| [jsonbin](https://www.owenyoung.com/blog/jsonbin/) | 在 Cloudflare Workers 部署 JSON as a Storage 服务。 | | 有效中 |
| [cronbin](https://www.owenyoung.com/blog/cronbin/) | 在 Cloudflare Workers 部署带 Dashboard 的 Cron 服务。 | | 有效中 |
| [using-cloudflare-worker-proxy-google](https://xiaowangye.org/posts/using-cloudflare-worker-proxy-google/) | 使用 Cloudflare Worker 代理 Google 站点。 | | 有效中 |
| [Use-Cloudflare-Zero-Trust-protect-your-web-applications](https://jiapan.me/2023/Use-Cloudflare-Zero-Trust-protect-your-web-applications/) | 使用 Cloudflare Zero Trust 保护 Web 应用。 | | 有效中 |
| [Nextjs-app-router-with-cloudflare-r2](https://juejin.cn/post/7306723921717166131) | 如何在 Next.js 13 的 app/ 目录中使用 Cloudflare R2 存储。 | | 有效中 |
| [cloudflare-webssh-zerotrust](https://josephcz.xyz/technology/network/cloudflare-webssh-zerotrust/) | 使用 Cloudflare ZeroTrust 搭建 WebSSH。 | | 有效中 |
| [免费的 CAPTCHA 替代品](https://www.cloudflare.com/zh-cn/products/turnstile/) | 官方出品，免费的 CAPTCHA 替代品。 | | 有效中 |
| [通过 Cloudflare 页面函数向 Telegram 发消息](https://liujiacai.net/blog/2024/05/07/telegram-bot-functions/) | 利用页面函数作为 GitHub Webhook 地址，将事件转发到 Telegram 频道。 | | 有效中 |
| [使用Cloudflare Workers制作博客AI摘要](https://mabbs.github.io/2024/07/03/ai-summary.html) | 使用 Cloudflare Workers + Workers AI + D1 数据库实现博客 AI 摘要。 | | 有效中 |

## 其他

| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| [silk-privacy-pass-client](https://chrome.google.com/webstore/detail/silk-privacy-pass-client/ajhmfdgkijocedmfjonnpjfojldioehi) | Cloudflare 官方插件，解决频繁人机验证问题。 | | 维护中 |
| [WARP-Clash-API](https://github.com/vvbbnn00/WARP-Clash-API) | 通过订阅使用 WARP+，支持 Clash、Shadowrocket，内置流量刷取和 IP 选优，支持 Docker compose 一键部署。 | | 维护中 |
| [ip-api](https://github.com/ccbikai/ip-api) | 利用 Cloudflare Workers 快速搭建 IP 地址和地理位置信息接口。 |  | 维护中 |
| [ChatGPT-Telegram-Workers](https://github.com/TBXark/ChatGPT-Telegram-Workers) | 轻松部署 Cloudflare Workers 上的 Telegram ChatGPT 机器人，带详细教程。 | | 维护中 |
| [RSSWorker](https://github.com/yllhwa/RSSWorker) | 轻量级 RSS 订阅工具，部署于 Cloudflare Worker。 | | 维护中 |
| [deeplx-for-cloudflare](https://github.com/ifyour/deeplx-for-cloudflare) | 在 Cloudflare 部署 DeepLX 翻译服务。 |  | 维护中 |
| [Cloudflare-No-Tracked](https://github.com/fwqaaq/Cloudflare-No-Tracked) | 去除 B 站、小红书跟踪链接，支持 Telegram bot 版本。 |  | 维护中 |
| [dnschecker](https://dnschecker.org/) | Cloudflare 官方推荐的域名解析检测工具。 | | 有效中 |
| [blockedinchina](https://www.comparitech.com/privacy-security-tools/blockedinchina/) | Cloudflare 官方推荐的检测域名是否被墙工具。 | | 有效中 |
| [prisma-with-cloudflare-d1](https://www.prisma.io/docs/orm/overview/databases/cloudflare-d1) | 介绍如何使用 Prisma 与 Cloudflare D1 数据库交互。 | | 有效中 |
| [cohere2openai-cf-worker](https://github.com/ckt1031/cohere2openai-cf-worker) | Cloudflare Worker 将 Cohere API 转换为 OpenAI API，易部署。 | | 维护中 |
| [cohere2openai](https://github.com/beanqi/cohere2openai) | Cloudflare Worker 将 Cohere API 转换为 OpenAI API。 | | 维护中 |
| [locnode](https://github.com/minlearn/locnode) | 自建轻量联合社区，首款能在 Cloudflare 运行的轻量联合社区。 |  | 维护中 |
| [Siri Ultra](https://github.com/fatwang2/siri-ultra) | 运行于 Cloudflare Workers 的助手，支持任意 LLM 模型。 | | 维护中 |
| [cobalt page function](https://github.com/jiacai2050/blog-snippets/blob/main/cloudflare/cobalt.js) | 利用页面函数调用 cobalt 接口，获取视频下载地址。 |  | 维护中 |
| [CloudFlare Radar](https://radar.cloudflare.com/scan) | 查看网站技术栈。 | | 维护中 |
| [wr.do](https://github.com/oiov/wr.do) | 基于 Cloudflare 的多租户 DNS 分发系统，免费提供 DNS 解析和短链接生成。 | https://wr.do | 维护中 |
| [cloudflare-proxy-sites](https://github.com/seadfeng/cloudflare-proxy-sites) | Cloudflare Workers web proxy，支持二级域名访问。 |  | 维护中 |
| [sublink-worker](https://github.com/7Sageer/sublink-worker) | 部署在 Cloudflare Worker 上的轻量级代理节点订阅转换工具，支持多协议订阅链接转换和自定义规则。 | | 维护中 |

## 教程

| 名称 | 特性 | 在线地址 | 状态 |
| --- | --- | --- | --- |
| [cloudflare-quickstart](https://github.com/zgimszhd61/cloudflare-quickstart) | Cloudflare Workers 快速入门指南。 | | 更新中 |
| [cloudflare-tunnel](https://dmesg.app/cloudflare) | 关于使用 Cloudflare Zero Trust 创建大内网及解决被墙服务器问题的技术博客。 | | 更新中 |
| [cloudflare-worker-gmail-resend-enterprise-email](https://cleanclip.cc/zh/developer/cloudflare-worker-gmail-resend-enterprise-email) | Cloudflare + Gmail + Resend 十分钟搭建免费企业邮箱。 | | 更新中 |