# discord-labubu-bot 
A Discord机器人，用于**实时监控Pop Mart Labubu系列产品库存**，当产品从无库存变为有库存时，自动在指定Discord频道发送通知，支持通过命令查询当前库存状态。基于 `discord.py` 和 `SeleniumBase` 开发，轻量且易于配置。


## 🌟 功能特性
- **实时库存监控**：定时检查指定Labubu产品的库存状态（默认20秒/次，可自定义）。
- **Discord@所有人通知**：产品上架时自动发送带产品图片和链接的Embed通知，确保不遗漏补货。
- **交互式命令**：支持通过Discord命令查询机器人状态、当前所有产品库存。
- **自动保活服务**：内置Flask轻量服务，适配免费服务器（如Replit、Heroku）的进程保活需求。
- **稳定的网页解析**：基于SeleniumBase实现无头浏览器渲染，避免静态HTML解析的局限性。


## 📋 环境要求
| 依赖项                | 版本要求       | 说明                     |
|-----------------------|----------------|--------------------------|
| Python                | ≥ 3.8          | 推荐3.9+，避免兼容性问题 |
| discord.py            | ≥ 2.3.0        | Discord机器人核心库      |
| SeleniumBase          | ≥ 4.22.0       | 网页自动化与解析库       |
| Flask                 | ≥ 2.0.0        | 保活服务核心库           |
| webdriver-manager     | 内置于SeleniumBase | 自动管理浏览器驱动       |


## 🚀 安装步骤
### 1. 克隆仓库（或下载源码）
```bash
# 克隆仓库（若使用Git）
git clone https://github.com/xiaomingx/discord-labubu-bot.git
cd discord-labubu-bot

# 若不使用Git，直接下载ZIP压缩包并解压，进入解压目录
```

### 2. 创建并激活虚拟环境（推荐）
#### Windows
```cmd
# 创建虚拟环境
python -m venv venv
# 激活虚拟环境
venv\Scripts\activate
```

#### macOS / Linux
```bash
# 创建虚拟环境
python3 -m venv venv
# 激活虚拟环境
source venv/bin/activate
```

### 3. 安装依赖
```bash
# 安装所有依赖
pip install -r requirements.txt
```

#### `requirements.txt` 内容（可直接创建该文件）
```txt
discord.py>=2.3.0
seleniumbase>=4.22.0
Flask>=2.0.0
```


## ⚙️ 配置指南
打开核心脚本 `stock_monitor_bot.py`，修改顶部**配置参数**（必须修改前2项）：

| 配置参数               | 说明                                                                 |
|------------------------|----------------------------------------------------------------------|
| `TOKEN`                | Discord机器人的Token，从[Discord开发者平台](https://discord.com/developers/applications)获取 |
| `DISCORD_CHANNEL_ID`   | 接收通知的Discord频道ID（需开启开发者模式后复制，见下文“获取频道ID”） |
| `REFRESH_INTERVAL`     | 库存检查间隔（单位：秒），默认20秒，建议不要小于10秒（避免触发反爬） |
| `BUTTON_CSS_SELECTOR`  | 库存按钮的CSS选择器，默认适配Pop Mart匈牙利站，无需修改              |
| `PRODUCTS`             | 监控的产品列表，可添加/删除产品（需包含`name`、`url`、`image`字段）  |


### 如何获取关键配置？
#### 1. 获取Discord机器人Token
1. 访问[Discord开发者平台](https://discord.com/developers/applications)，点击「New Application」创建应用。
2. 进入「Bot」选项卡，点击「Add Bot」，然后点击「Reset Token」复制Token（**不要分享给他人**）。
3. 在「Privileged Gateway Intents」中，开启「Message Content Intent」（否则无法读取命令）。

#### 2. 获取Discord频道ID
1. 打开Discord客户端，进入「设置 → 高级 → 开发者模式」，开启开发者模式。
2. 右键点击需要接收通知的频道，选择「复制ID」，即为`DISCORD_CHANNEL_ID`。


## 🎯 使用指南
### 1. 运行机器人
```bash
# 激活虚拟环境后运行
python stock_monitor_bot.py
```

### 2. 验证机器人在线
在Discord频道中发送命令：
```
!ping
```
机器人会回复 `🏓 Pong! 我在线哦~`，表示运行正常。

### 3. 核心命令列表
| 命令       | 作用                                                                 |
|------------|----------------------------------------------------------------------|
| `!ping`    | 检查机器人是否在线                                                   |
| `!stock`   | 查看所有监控产品的当前库存状态（含更新时间、产品链接）               |
| `!help`    | 显示帮助信息，列出所有可用命令                                       |


### 4. 库存通知示例
当产品上架时，机器人会发送如下Embed通知：
- 标题：`🎯 Coca-Cola Labubu 有库存了！`
- 内容：包含产品链接、图片，以及更新时间
- 提醒：自动@everyone，确保所有成员收到通知


## 📝 项目结构
```
discord-labubu-bot/
├── stock_monitor_bot.py  # 核心脚本（含机器人逻辑、库存监控、保活服务）
├── requirements.txt      # 依赖列表
└── README.md             # 项目说明（本文档）
```


## ❌ 常见问题
### Q1：机器人无响应，未发送通知？
1. 检查`TOKEN`和`DISCORD_CHANNEL_ID`是否配置正确。
2. 确保机器人已加入你的Discord服务器（通过OAuth2链接邀请，需勾选「Send Messages」权限）。
3. 查看运行日志，是否有「无法获取指定频道」或「SeleniumBase错误」，针对性排查。

### Q2：SeleniumBase报错“浏览器驱动无法启动”？
- 确保网络通畅，SeleniumBase会自动下载浏览器驱动，首次运行可能需要等待。
- 若在Linux服务器上报错，需安装依赖：`sudo apt-get install chromium-browser`。

### Q3：保活服务提示“端口8080被占用”？
修改`keep_alive()`函数中的端口号，例如将`port=8080`改为`port=8081`，确保端口未被其他进程占用。


## 📄 许可证
本项目基于 **MIT许可证** 开源，允许个人和商业使用，修改或分发时需保留原版权声明。

```
MIT License

Copyright (c) 2024 你的用户名

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```


## 🤝 贡献指南
若你发现Bug或有新功能建议，欢迎：
1. 提交Issue描述问题或需求。
2. Fork仓库，修改后提交Pull Request（PR），确保代码风格与原项目一致。