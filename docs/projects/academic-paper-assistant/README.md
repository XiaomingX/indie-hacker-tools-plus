# PaperAssistant-plus

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-Apache--2.0-green)
![Repo Stars](https://img.shields.io/github/stars/XiaomingX/PaperAssistant-plus?style=social)

## 项目简介
PaperAssistant-plus 是一款轻量级科研论文辅助阅读工具，基于 Python 开发，结合 **pdfplumber** 高效解析 PDF 论文文本，依托 **GPT-4o-mini** 生成结构化归纳内容，帮助科研人员快速提炼论文核心信息（背景、问题、方法、结果、意义），大幅节省文献阅读时间。


## 核心功能
- **高效 PDF 解析**：采用活跃维护的 `pdfplumber` 库，精准提取论文文本，保留分页结构便于定位内容。
- **结构化 AI 归纳**：基于 GPT-4o-mini 生成标准化总结，涵盖「研究背景→核心问题→方法→关键结果→意义与局限」5大模块。
- **轻量易部署**：无复杂本地模型依赖，通过 OpenAI API 调用能力，只需简单配置即可运行。
- **自动结果保存**：解析与归纳结果自动保存为 `.summary.txt` 文件，支持后续查阅与整理。


## 快速开始

### 1. 环境准备
- 确保本地安装 **Python 3.8 及以上版本**（推荐 3.10+）。
- 拥有有效的 **OpenAI API 密钥**（需开通 GPT-4o-mini 调用权限）。

### 2. 克隆仓库
```bash
git clone https://github.com/XiaomingX/PaperAssistant-plus.git
cd PaperAssistant-plus
```

### 3. 安装依赖
首先在项目根目录创建 `requirements.txt` 文件，写入以下内容：
```txt
pdfplumber>=0.10.3
openai>=1.30.1
loguru>=0.7.2
```
然后执行安装命令：
```bash
pip install -r requirements.txt
```

### 4. 配置 OpenAI API 密钥
#### 方式 1：临时环境变量（终端会话内有效）
- **Linux/macOS**：
  ```bash
  export OPENAI_API_KEY="你的OpenAI API密钥"
  ```
- **Windows（PowerShell）**：
  ```powershell
  $env:OPENAI_API_KEY="你的OpenAI API密钥"
  ```

#### 方式 2：永久配置（推荐）
将 API 密钥写入系统环境变量，避免每次运行重复配置（具体步骤参考操作系统环境变量设置指南）。

### 5. 运行工具
在项目根目录执行命令，指定需要解析的 PDF 论文路径：
```bash
# 示例：解析当前目录下的 "research_paper.pdf"
python paper_assistant.py --file research_paper.pdf
```

### 6. 查看结果
程序会在 PDF 同目录下生成 `[论文名].summary.txt` 文件，示例内容如下：
```
# 研究背景与动机
该研究针对现有图像分割模型在小样本场景下精度不足的问题，指出传统方法依赖大量标注数据，难以适用于医疗影像等标注成本高的领域...

# 核心问题
1. 小样本条件下，模型泛化能力差；
2. 现有迁移学习方法易出现「负迁移」现象...
```


## 使用示例
假设需要解析论文 `2026_CVPR_Image_Segmentation.pdf`，完整流程如下：
```bash
# 1. 进入项目目录
cd PaperAssistant-plus

# 2. 配置API密钥（Linux/macOS）
export OPENAI_API_KEY="sk-xxxxxxxxx"

# 3. 运行工具
python paper_assistant.py --file ./docs/2026_CVPR_Image_Segmentation.pdf

# 4. 查看结果
cat ./docs/2026_CVPR_Image_Segmentation.summary.txt
```


## 依赖清单
| 依赖库        | 版本要求       | 功能说明                  |
|---------------|----------------|---------------------------|
| python        | ≥3.8           | 运行环境                  |
| pdfplumber    | ≥0.10.3        | PDF文本提取                |
| openai        | ≥1.30.1        | 调用GPT-4o-mini API       |
| loguru        | ≥0.7.2         | 日志记录与错误提示        |


## 许可证
本项目基于 **Apache License 2.0** 开源，详见 [LICENSE](https://github.com/XiaomingX/PaperAssistant-plus/blob/main/LICENSE) 文件。


## 贡献指南
欢迎通过以下方式参与项目改进：
1. **提交 Issue**：反馈 Bug、提出功能需求（请在 Issue 中清晰描述场景与需求）。
2. **贡献代码**：
   - Fork 本仓库到个人账号；
   - 创建特性分支（`git checkout -b feature/your-feature`）；
   - 提交代码并推送至个人仓库；
   - 发起 Pull Request 至本仓库 `main` 分支，附带修改说明。


## 致谢
- 感谢 [OpenAI](https://openai.com/) 提供 GPT-4o-mini API，为 AI 归纳能力提供核心支持；
- 感谢 [pdfplumber](https://github.com/jsvine/pdfplumber) 项目，提供高效稳定的 PDF 解析能力；
- 感谢所有为项目贡献代码或反馈问题的开发者。