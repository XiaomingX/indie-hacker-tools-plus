# moneyprintV3

利用AI大模型，一键生成高清短视频  
Generate high-definition short videos with one click using AI large language models.

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub Stars](https://img.shields.io/github/stars/XiaomingX/moneyprintV3.svg?style=social)](https://github.com/XiaomingX/moneyprintV3/stargazers)

## 项目简介 (Introduction)

moneyprintV3 是一个基于AI大模型的短视频自动生成工具，旨在通过简单操作快速生成高质量、符合场景需求的高清短视频内容。无论是社交媒体素材、产品宣传片段还是创意灵感展示，都能通过该工具高效实现，降低视频制作的技术门槛。

moneyprintV3 is an AI-powered tool for automatic short video generation. It enables users to quickly create high-quality, scenario-specific HD short videos with simple operations. Whether for social media, product promotion, or creative inspiration, this tool lowers the technical barrier to video production.

## 核心功能 (Core Features)

- **一键生成**：输入文本描述即可自动生成完整短视频，无需专业剪辑技能
- **高清画质**：支持1080P/4K分辨率输出，保证视频清晰度
- **多风格适配**：支持多种视频风格（如动画、写实、卡通等）切换
- **智能配乐**：自动匹配与视频内容相符的背景音乐
- **快速导出**：优化生成流程，缩短等待时间

- **One-click Generation**：Create complete short videos from text descriptions without professional editing skills
- **HD Quality**：Supports 1080P/4K output resolution
- **Multi-style Adaptation**：Switch between various video styles (animation, realism, cartoon, etc.)
- **Intelligent Soundtrack**：Automatically matches background music with video content
- **Fast Export**：Optimized generation process for shorter waiting time

## 安装指南 (Installation)

### 前置要求 (Prerequisites)
- Python 3.8+
- 支持CUDA的GPU（推荐，加速生成速度）或CPU

### 步骤 (Steps)

1. 克隆仓库 (Clone the repository)
```bash
git clone https://github.com/XiaomingX/moneyprintV3.git
cd moneyprintV3
```

2. 创建并激活虚拟环境 (Create and activate virtual environment)
```bash
# 使用venv
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# 或使用conda
conda create -n moneyprintV3 python=3.8
conda activate moneyprintV3
```

3. 安装依赖 (Install dependencies)
```bash
pip install -r requirements.txt
```

## 使用方法 (Usage)

1. 准备输入文本（例如："一只猫在草地上追逐蝴蝶，阳光明媚的下午"）
2. 运行生成脚本 (Run the generation script)
```bash
python generate_video.py --prompt "你的文本描述" --style "写实" --resolution "1080p"
```

3. 生成的视频将保存在 `output/` 目录下

## 示例展示 (Examples)

| 输入描述 | 生成效果 |
|----------|----------|
| "海浪拍打岩石，日落时分的海边" | [查看视频](链接到示例视频) |
| "城市夜景，车流灯光形成光轨" | [查看视频](链接到示例视频) |

*注：示例视频可在项目的 `examples/` 目录中找到*

## 贡献指南 (Contributing)

欢迎通过以下方式参与项目贡献：
1. 提交Issue报告bug或提出功能建议
2.  Fork仓库并提交Pull Request（请遵循[Conventional Commits](https://www.conventionalcommits.org/)规范）
3. 完善文档或翻译内容

Please contribute to the project in the following ways:
1. Submit Issues to report bugs or suggest features
2. Fork the repository and submit Pull Requests (following [Conventional Commits](https://www.conventionalcommits.org/) standards)
3. Improve documentation or translation

## 许可证 (License)

本项目基于 [Apache License 2.0](LICENSE) 开源，详情请查看许可证文件。

## 联系我们 (Contact)

- 项目地址：[https://github.com/XiaomingX/moneyprintV3](https://github.com/XiaomingX/moneyprintV3)
- 问题反馈：提交Issue至上述仓库
