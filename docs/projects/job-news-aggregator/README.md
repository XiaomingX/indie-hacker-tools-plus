# jobleap4u-news
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

一款自动化提取 **JobLeap 公众号 RSS 内容**、生成 AI 摘要并推送邮件的工具。基于 GPT-4o-mini 实现专业内容提炼，帮助职场人、HR 快速获取 JobLeap4u 核心资讯。


## 📋 项目简介
本工具旨在解决「手动浏览 mp.JobLeap4u 内容效率低」的问题，通过自动化流程完成：
1. 定时抓取 `https://mp.jobleap4u.com/rss` 的最新文章
2. 解析文章全文并调用 GPT-4o-mini 生成结构化摘要
3. 输出 Markdown/HTML 格式文件存档
4. 自动发送 HTML 版摘要到指定邮箱


## ✨ 核心功能
- **RSS 自动解析**：实时抓取 JobLeap4u 最新文章，提取标题、作者、发布时间等元信息
- **全文内容获取**：通过 Jina AI 接口解析文章原文，突破 RSS 摘要局限性
- **AI 结构化摘要**：基于 GPT-4o-mini 生成「核心要点+关键信息+总结评价」三段式内容
- **多格式输出**：自动保存 Markdown 原始文件与带样式的 HTML 文档
- **邮件自动推送**：支持配置多个收件人，定时接收整理好的资讯简报


## 🚀 快速开始

### 1. 环境准备
#### 1.1 安装 Python
确保本地安装 **Python 3.8 及以上版本**，可通过以下命令验证：
```bash
python --version  # 或 python3 --version
```

#### 1.2 克隆仓库
```bash
git clone https://github.com/你的用户名/jobleap4u-news.git
cd jobleap4u-news
```

#### 1.3 安装依赖
```bash
pip install -r requirements.txt
```

`requirements.txt` 内容（已包含核心依赖）：
```txt
requests>=2.31.0
python-dotenv>=1.0.0
markdown>=3.5.2
feedparser>=6.0.10
```


### 2. 配置环境变量
创建 `.env` 文件（与主脚本同级），填入以下必填配置：
```env
# -------------------------- OpenAI 配置（必填）--------------------------
# GPT-4o-mini 需 OpenAI API 密钥，获取地址：https://platform.openai.com/api-keys
OPENAI_API_KEY=sk-你的OpenAI密钥
# 国内用户可替换为代理地址（如 Cloudflare 代理）
OPENAI_BASE_URL=https://api.openai.com/v1

# -------------------------- 邮件配置（必填）--------------------------
# 邮件 SMTP 服务器（示例：163邮箱=smtp.163.com，QQ邮箱=smtp.qq.com，Gmail=smtp.gmail.com）
EMAIL_HOST=smtp.163.com
# SMTP 端口（SSL 加密通常为 465，非加密为 25，根据邮箱服务商配置）
EMAIL_PORT=465
# 发送方邮箱账号
EMAIL_USER=你的邮箱账号@163.com
# 邮箱授权码（非登录密码！需在邮箱设置中开启 SMTP 并获取）
EMAIL_PASS=你的邮箱授权码
# 发送方显示邮箱（通常与 EMAIL_USER 一致）
EMAIL_SENDER=你的邮箱账号@163.com
# 接收方邮箱（多个用逗号分隔）
EMAIL_RECEIVERS=接收者1@xxx.com,接收者2@xxx.com

# -------------------------- 可选配置 --------------------------
# 单次获取文章最大数量（默认5篇）
MAX_ARTICLE_LIMIT=5
```

> ⚠️  邮箱授权码获取说明：  
> 163/QQ 邮箱需进入「设置-账户」开启「SMTP 服务」，按提示获取授权码；Gmail 需创建应用专用密码。


### 3. 运行程序
#### 3.1 手动运行
```bash
python jobleap_rss_summary.py
```

#### 3.2 定时运行（推荐）
若需每日自动生成简报，可通过以下方式配置定时任务：

##### Windows（任务计划程序）
1. 打开「任务计划程序」→ 「创建基本任务」
2. 触发条件选择「每日」，设置执行时间（如早8点）
3. 操作选择「启动程序」，程序路径选 `python.exe`，参数填脚本路径（如 `D:\jobleap4u-news\jobleap_rss_summary.py`）

##### macOS/Linux（crontab）
1. 打开终端，输入 `crontab -e`
2. 添加定时任务（每天8点执行）：
   ```bash
   0 8 * * * /usr/bin/python3 /path/to/jobleap4u-news/jobleap_rss_summary.py
   ```
   > 提示：通过 `which python3` 查看 Python 路径


## 📂 项目目录结构
```
jobleap4u-news/
├── jobleap_rss_summary.py  # 主程序（核心逻辑入口）
├── .env                    # 环境变量配置（需手动创建）
├── requirements.txt        # 依赖列表
├── output/                 # 输出文件夹（自动生成）
│   ├── jobleap_summary_20261001_080000.md  # Markdown 摘要
│   └── jobleap_summary_20261001_080000.html # 带样式 HTML
└── README.md               # 项目说明文档
```


## 📝 输出说明
### 1. 摘要格式（Markdown/HTML）
每篇文章摘要包含以下结构化内容：
- **标题+链接**：直接跳转原文
- **元信息**：作者、发布时间
- **核心要点**：300字内概括全文核心
- **关键信息**：3个以上重要细节/数据/建议
- **总结评价**：内容价值与适用性分析

### 2. 邮件推送
发送的邮件为 HTML 格式，包含内置样式，支持在手机/电脑端自适应显示，内容与 `output` 文件夹中的 HTML 文件一致。


## ❌ 常见问题（FAQ）
### Q1: RSS 解析失败，提示「bozo_exception」
A1: 可能是 RSS 源地址变更或网络问题。  
- 验证 RSS 地址是否可访问：直接在浏览器打开 `https://mp.jobleap4u.com/rss`
- 检查网络代理：若使用代理，需在代码中配置请求代理

### Q2: LLM 调用失败，提示「401 Unauthorized」
A2: OpenAI API 密钥错误或过期。  
- 重新生成密钥：https://platform.openai.com/api-keys
- 确保密钥未设置 IP 限制

### Q3: 邮件发送失败，提示「SMTPException」
A3: 邮件配置错误，按以下步骤排查：
1. 验证 `EMAIL_HOST` 和 `EMAIL_PORT` 是否匹配服务商配置
2. 确认 `EMAIL_PASS` 是授权码而非登录密码
3. 检查发送方邮箱是否开启 SMTP 服务
4. 部分邮箱需关闭「登录保护」或配置「安全等级」

### Q4: 文章全文获取失败，提示「timeout」
A4: 目标文章链接无法访问或网络延迟。  
- 可手动访问文章链接验证可用性
- 调整代码中 `get_article_content` 函数的 `timeout` 参数（默认10秒）


## 📄 许可证
本项目采用 **MIT 许可证**，详见 [LICENSE](LICENSE) 文件。


## 🤝 贡献指南
欢迎提交 Issues 反馈 Bug 或建议，也可通过 Pull Request 参与开发：
1. Fork 本仓库
2. 创建特性分支（`git checkout -b feature/xxx`）
3. 提交修改（`git commit -m "add xxx feature"`）
4. 推送分支（`git push origin feature/xxx`）
5. 打开 Pull Request
