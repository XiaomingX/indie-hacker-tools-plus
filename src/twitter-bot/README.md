# twitter-bot

一个基于 **OpenAI** 和 **X (原Twitter) API** 的自动化推文机器人，可随机生成提示词、AI创作推文内容并自动发布，支持限流异常处理，降低人工运营成本。


## 🌟 核心功能
- **随机提示词生成**：支持「科技」「生活感悟」两类主题，自动生成符合场景的创作方向
- **AI智能推文创作**：调用GPT-4o-mini模型生成简洁、有互动性的推文，自动去除首尾引号
- **一键自动发布**：通过Tweepy直接对接X API，无需手动操作
- **限流自动处理**：检测到X API限定时，自动计算重试时间并提示，避免频繁报错


## 📋 环境要求
- Python 3.9+
- 有效的 **OpenAI API Key**（用于生成推文）
- X (Twitter) 开发者账号及API密钥（用于发布推文）


## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/XiaomingX/twitter-bot.git
cd twitter-bot
```

### 2. 安装依赖
创建并激活虚拟环境（可选但推荐），再安装依赖包：
```bash
# 安装依赖
pip install -r requirements.txt
```

需在项目根目录创建 `requirements.txt` 文件，内容如下：
```txt
openai>=1.0.0
tweepy>=4.14.0
python-dotenv>=1.0.0
```

### 3. 配置密钥
1. 在项目根目录创建 `.env` 文件（注意文件名前有小数点）
2. 按以下格式填写API密钥（需自行申请，获取方式见下方）：
```env
# OpenAI API 配置
OPENAI_API_KEY=your_openai_api_key

# X (Twitter) API 配置
CONSUMER_KEY=your_twitter_consumer_key
CONSUMER_SECRET=your_twitter_consumer_secret
ACCESS_TOKEN=your_twitter_access_token
ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
```


## 🔧 密钥获取指南
| 配置项                | 获取渠道                                                                 |
|-----------------------|--------------------------------------------------------------------------|
| `OPENAI_API_KEY`      | [OpenAI控制台](https://platform.openai.com/api-keys)（注册账号后创建）    |
| `CONSUMER_KEY`等      | [X Developer Platform](https://developer.twitter.com/)（创建项目后获取） |

> 注意：X API需申请「Standard」或以上访问权限，确保具备「发布推文」的接口调用权限。


## 🎯 使用方法
直接运行主程序，机器人会自动完成「生成提示词 → AI创作推文 → 发布到X」的全流程：
```bash
python tweet_generator.py
```

### 运行流程说明
1. 程序加载 `.env` 中的密钥，初始化OpenAI和X客户端
2. 随机选择「科技」或「生活感悟」主题，生成对应的创作提示词
3. 调用GPT-4o-mini生成符合280字符限制的推文内容
4. 自动发布推文，若触发限流则提示重试时间，若失败则打印错误信息


## ❓ 常见问题
1. **「API Key错误」报错**  
   检查 `.env` 文件中密钥是否填写完整，是否存在空格或拼写错误；确认OpenAI/X账号是否有可用额度。

2. **「限流（TooManyRequests）」提示**  
   程序会自动识别限流信息并显示重试时间，等待对应时长后重新运行即可（X API普通账号有每日调用次数限制）。

3. **推文生成后为空**  
   检查OpenAI API密钥是否有效，或尝试提高 `generate_tweet` 函数中的 `temperature` 值（如从0.2调整为0.5）增加生成稳定性。


## 📄 许可证
本项目基于 **MIT License** 开源，可自由修改和商用，但需保留原作者信息。

```
MIT License

Copyright (c) 2024 XiaomingX

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```


## 🤝 贡献指南
欢迎提交Issue或Pull Request优化功能，提交前请确保代码格式规范，并附上功能说明或bug修复理由。

---

仓库地址：[https://github.com/XiaomingX/twitter-bot](https://github.com/XiaomingX/twitter-bot)