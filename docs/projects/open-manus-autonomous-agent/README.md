# open-manus-v2

基于 OpenAI API 构建的**轻量级 Manus 交互系统**，主打简洁、易上手的设计，适合初学者学习 LLM 应用开发，或快速集成基础对话/任务交互能力。


## 🌟 核心特性
- **轻量无冗余**：去除复杂封装，保留核心 LLM 交互逻辑，代码结构清晰易理解
- **灵活配置**：支持通过 `.env` 环境变量或 TOML 配置文件自定义 LLM 参数（API Key、模型、温度等）
- **交互式体验**：提供命令行交互界面，支持即时对话与退出控制
- **可观测性**：内置分级日志系统（DEBUG/INFO/WARNING），方便调试与运行跟踪
- **跨平台兼容**：支持 Windows/macOS/Linux，依赖少且安装简单


## 🚀 快速开始

### 1. 环境要求
- Python 3.8 及以上
- 有效的 OpenAI API Key（可从 [OpenAI 控制台](https://platform.openai.com/api-keys) 获取）


### 2. 项目克隆
```bash
# 克隆仓库到本地
git clone https://github.com/XiaomingX/open-manus-v2.git
cd open-manus-v2
```


### 3. 环境配置
#### 方式 1：使用 .env 文件（推荐）
在项目根目录新建 `.env` 文件，填入 OpenAI API Key：
```env
# .env 文件内容
OPENAI_API_KEY=your-openai-api-key-here
```

#### 方式 2：使用 TOML 配置文件（可选）
若需自定义 LLM 模型、温度等参数，可新建 `config.toml` 文件：
```toml
# config.toml 文件内容
[llm]
model = "gpt-3.5-turbo"  # 可选：gpt-4、gpt-4-turbo 等
temperature = 0.7         # 0-2 之间，值越高输出越随机

[api]
openai_api_key = "your-openai-api-key-here"  # 优先级低于 .env 文件
```


### 4. 依赖安装
```bash
# 安装核心依赖
pip install python-dotenv toml langchain-openai langchain
```


### 5. 运行系统
#### 基础运行（默认配置）
```bash
python main.py
```

#### 指定配置文件运行
```bash
python main.py --config config.toml
```

#### 开启调试日志（显示详细运行信息）
```bash
python main.py --log-level DEBUG
```


## 📝 使用示例
```
# 运行后进入交互界面
=== Manus 交互式聊天（输入 quit 退出）===

你：介绍一下 Python 装饰器
Manus：Python 装饰器是一种用于修改函数或类行为的工具，本质是可调用对象（通常是函数）...

你：quit
Manus：再见！
```


## 📂 目录结构
```
open-manus-v2/
├── main.py          # 主程序入口（含配置、LLM、交互逻辑）
├── .env             # 环境变量配置（存储 API Key，不提交到仓库）
├── config.toml      # 自定义配置文件（可选，可提交到仓库）
├── .gitignore       # Git 忽略文件（避免提交 .env、依赖目录等）
├── LICENSE          # Apache-2.0 许可证文件
└── README.md        # 项目说明文档（当前文件）
```


## 📄 许可证
本项目基于 **Apache License 2.0** 开源，详见 [LICENSE](LICENSE) 文件。


## 🤝 贡献指南
1. Fork 本仓库
2. 创建特性分支（`git checkout -b feature/your-feature`）
3. 提交代码（`git commit -m "Add your feature"`）
4. 推送分支（`git push origin feature/your-feature`）
5. 提交 Pull Request


## ❓ 常见问题
- **API Key 错误**：检查 `.env` 或 `config.toml` 中 API Key 是否正确，确保无多余空格
- **依赖安装失败**：尝试升级 pip（`pip install --upgrade pip`）后重新安装依赖
- **LLM 响应慢**：可切换为 `gpt-3.5-turbo` 模型（速度更快），或检查网络连接


要不要我帮你生成一个**快速启动脚本**（如 `run.sh` 或 `run.bat`）？脚本可自动检查依赖、加载配置并启动程序，进一步降低使用门槛。