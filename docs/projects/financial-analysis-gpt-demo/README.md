# finance-gpt-openai
基于 OpenAI 与 Finnhub 构建的股票投资顾问 API 演示项目，可通过获取指定日期的股票新闻，自动生成 AI 驱动的股价趋势分析与投资建议。


## 项目概述
本项目是一个轻量级的投资顾问 demo，核心功能是通过 **Finnhub API** 获取目标股票的指定日期新闻数据，再借助 **OpenAI 大模型** 对新闻内容进行总结与分析，最终输出结构化的股价趋势判断和投资建议。项目采用 FastAPI 构建后端接口，支持通过 HTTP 请求快速调用，适合学习 AI 与金融数据结合的开发流程。


## 核心功能
- **新闻数据自动获取**：对接 Finnhub API，一键拉取指定股票（默认高盛 GS）的某日新闻（标题+摘要）。
- **AI 投资建议生成**：基于 OpenAI 大模型，结合新闻内容生成逻辑清晰的新闻总结、股价趋势分析（含多假设场景）。
- **RESTful API 接口**：通过 FastAPI 提供标准化接口，支持传入日期参数，返回 JSON 格式的投资建议。
- **参数集中管理**：核心配置（API 密钥、股票代码、模型参数）统一维护，便于修改与扩展。


## 环境准备
### 1. 依赖库安装
项目依赖以下 Python 库，可通过 `pip` 批量安装：
```bash
pip install fastapi uvicorn pandas python-dotenv finnlp openai requests beautifulsoup4
```

### 2. 第三方 API 密钥获取
需提前申请两个关键 API 密钥，并配置为环境变量（避免硬编码泄露）：
- **OpenAI API Key**：用于调用大模型生成分析，需在 [OpenAI 控制台](https://platform.openai.com/api-keys) 申请。
- **Finnhub API Key**：用于获取股票新闻数据，需在 [Finnhub 官网](https://finnhub.io/) 注册申请（免费版有调用次数限制）。

### 3. 环境变量配置
#### Windows（命令行）
```cmd
set OPENAI_API_KEY=你的OpenAI密钥
set FINNHUBAPI_KEY=你的Finnhub密钥
```

#### macOS/Linux（终端）
```bash
export OPENAI_API_KEY=你的OpenAI密钥
export FINNHUBAPI_KEY=你的Finnhub密钥
```


## 项目结构
```
finance-gpt-openai/
├── robo_advisor.py       # 核心代码（API 服务、新闻获取、AI 分析逻辑）
├── README.md             # 项目说明文档
└── requirements.txt      # 依赖库清单（可选，建议添加）
```


## 快速开始
### 1. 准备依赖库路径
项目依赖 `FinNLP` 和 `FinRL-Meta` 两个开源库，需将其路径添加到 Python 环境中：
1. 从 GitHub 下载两个库的源码：
   - [FinNLP](https://github.com/AI4Finance-Foundation/FinNLP)
   - [FinRL-Meta](https://github.com/AI4Finance-Foundation/FinRL-Meta)
2. 在 `robo_advisor.py` 中，将 `sys.path.append` 的路径改为你本地的库路径（默认路径需调整）：
   ```python
   sys.path.append("你本地的FinNLP路径/FinNLP/")
   sys.path.append("你本地的FinRL-Meta路径/FinRL-Meta/")
   ```

### 2. 启动 API 服务
在项目根目录执行以下命令，启动 FastAPI 服务：
```bash
python robo_advisor.py
```
服务启动后，会显示监听地址：
```
启动投资顾问API服务...
监听地址: http://127.0.0.1:8000
获取投资建议: http://127.0.0.1:8000/advice?date=YYYY-MM-DD
```

### 3. 调用 API 获取投资建议
#### 方式 1：浏览器访问
直接在浏览器输入 URL（替换 `YYYY-MM-DD` 为目标日期，如 `2026-05-20`）：
```
http://127.0.0.1:8000/advice?date=2026-05-20
```

#### 方式 2：命令行（curl）
```bash
curl "http://127.0.0.1:8000/advice?date=2026-05-20"
```

#### 成功响应示例
```json
{
  "date": "2026-05-20",
  "stock": "GS",
  "company": "Goldman Sachs Group, Inc",
  "investment_advice": "### 新闻总结\n2026年5月20日，高盛（GS）发布Q2财报，营收超市场预期...\n### 股价趋势分析\n1. 短期趋势：财报利好可能推动股价短期上涨5%-8%...\n2. 风险假设：若美联储加息超预期，可能抵消财报利好，股价或回调3%-5%..."
}
```


## 关键配置修改
若需分析其他股票，可在 `robo_advisor.py` 的 `config` 字典中修改参数：
```python
config = {
    "stock": "AAPL",          # 改为目标股票代码（如苹果 AAPL）
    "company_name": "Apple Inc",  # 对应公司名称
    "openai_params": {
        "temperature": 0.3,   # 调整模型随机性（0.0-1.0，值越小越确定）
        "presence_penalty": -0.5  # 调整内容新颖性（-2.0-2.0）
    }
}
```


## 注意事项
1. **API 调用限制**：
   - Finnhub 免费版每日新闻调用次数有限（约 60 次/天），避免高频调用。
   - OpenAI API 会产生费用，建议在 [OpenAI 控制台](https://platform.openai.com/usage) 监控用量。
2. **新闻数据可用性**：部分日期可能无相关新闻，此时 API 会返回 `“YYYY-MM-DD没有找到相关新闻”`。
3. **安全性**：切勿将 API 密钥硬编码到代码中，或提交到 GitHub 等公开仓库。
4. **结果仅供参考**：AI 生成的投资建议不构成实际投资决策依据，需结合专业分析判断。


## 许可证
本项目基于 [MIT 许可证](https://opensource.org/licenses/MIT) 开源，允许个人或企业自由使用、修改和分发，无需额外授权（需保留原许可证声明）。
