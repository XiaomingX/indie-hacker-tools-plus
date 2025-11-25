# openai-alt-tag

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)

利用开源模型替代方案生成图像alt标签的工具，基于Together API调用Meta Llama-Vision模型实现自动图像内容描述，助力提升网页可访问性（A11Y）。

## 🌟 项目简介

`openai-alt-tag` 提供了一种无需依赖OpenAI服务的图像alt标签生成方案，通过调用Together.xyz平台的Llama-Vision-Free视觉语言模型，将图像URL转换为精准的自然语言描述，可直接用作HTML图像的`alt`属性，适用于开发者、内容创作者快速优化网页可访问性。

## ✨ 功能特点

- 🚀 轻量集成：仅需几行代码即可实现图像描述生成
- 🔄 多平台兼容：支持Linux/macOS/Windows环境
- 🌐 支持URL图像：直接传入网络图像地址即可处理
- 🆓 免费模型支持：基于Llama-Vision-Free模型，降低使用成本

## 📋 前置要求

- Python 3.8 及以上版本
- Together API密钥（需在[Together.xyz](https://www.together.xyz/)注册获取）

## 🛠️ 安装步骤

1. 克隆仓库
   ```bash
   git clone https://github.com/XiaomingX/openai-alt-tag.git
   cd openai-alt-tag
   ```

2. 创建并激活虚拟环境（可选但推荐）
   ```bash
   # 创建虚拟环境
   python -m venv venv

   # 激活环境（Linux/macOS）
   source venv/bin/activate

   # 激活环境（Windows PowerShell）
   .\venv\Scripts\Activate.ps1
   ```

3. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

## 🔑 配置说明

1. 获取Together API密钥：
   - 访问[Together.xyz控制台](https://api.together.xyz/)
   - 注册并登录后，在"API Keys"页面创建新密钥

2. 设置环境变量：
   ```bash
   # Linux/macOS（临时生效）
   export TOGETHER_API_KEY="your_api_key_here"

   # Linux/macOS（永久生效，需重启终端）
   echo 'export TOGETHER_API_KEY="your_api_key_here"' >> ~/.bashrc  # 或 ~/.zshrc

   # Windows PowerShell（临时生效）
   $env:TOGETHER_API_KEY = "your_api_key_here"

   # Windows（永久生效）
   [Environment]::SetEnvironmentVariable("TOGETHER_API_KEY", "your_api_key_here", "User")
   ```

## 🚀 使用示例

### 基础用法
修改`generate_alt_tag.py`中的图像URL，运行脚本生成alt标签：
```
import os
from openai import OpenAI

# 初始化客户端
client = OpenAI(
    api_key=os.environ.get("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1"
)

# 生成图像描述（alt标签）
response = client.chat.completions.create(
    model="meta-llama/Llama-Vision-Free",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "生成简洁准确的图像描述，用于HTML的alt标签"},
                {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
            ]
        }
    ]
)
```

# 输出结果
print("推荐的alt标签：", response.choices[0].message.content)
运行脚本：python generate_alt_tag.py
### 输出示例推荐的alt标签：一只黑色小狗在草地上追逐飞盘，背景有白色栅栏
## 📚 扩展指南

- **处理本地图像**：需先将本地图像上传至图床获取URL（如Cloudinary、Imgur等）
- **调整描述长度**：在prompt中添加约束（例如："生成不超过20字的描述"）
- **批量处理**：结合`os`模块遍历图像目录，实现批量生成

## 🤝 贡献指南

1. Fork本仓库
2. 创建特性分支（`git checkout -b feature/amazing-feature`）
3. 提交修改（`git commit -m 'Add some amazing feature'`）
4. 推送到分支（`git push origin feature/amazing-feature`）
5. 打开Pull Request

## 📄 许可证

本项目基于MIT许可证开源，详情参见[LICENSE](LICENSE)文件。

## 📞 支持与反馈

- 提交Issue：[GitHub Issues](https://github.com/XiaomingX/openai-alt-tag/issues)
- 项目地址：[https://github.com/XiaomingX/openai-alt-tag](https://github.com/XiaomingX/openai-alt-tag)
