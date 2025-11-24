# faceless-video-generator-plus

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://www.python.org/downloads/)

一款**端到端无脸视频自动生成工具**，可一键完成「故事创作→角色设计→分镜生成→图片渲染→音频合成→字幕添加→视频导出」全流程，无需手动处理多媒体素材，适合内容创作者快速产出短视频内容。


## 📋 核心功能
- **智能内容生成**：基于OpenAI API自动生成故事（支持恐怖、睡前故事、生活技巧等11种类型）、角色描述（外貌/年龄/特征）和分镜脚本；
- **多风格图片渲染**：支持`replicate`/`fal`双API生成图片，可选写实、动漫、皮克斯等5种视觉风格，生成失败自动用空白图兜底；
- **自动音频合成**：调用OpenAI TTS生成多风格配音（6种音色可选），音频时长与分镜字幕精准匹配；
- **视频与字幕整合**：自动合并图片+音频，添加逐词高亮字幕（支持自定义字体/颜色），输出带字幕的最终视频；
- **结构化资源管理**：自动创建项目目录，按「故事类型→标题」分类保存故事文本、分镜配置、图片/音频/视频文件。


## 🚀 快速开始

### 1. 环境要求
- Python 3.8+
- 依赖工具：`ffmpeg`（用于视频合成，需提前安装，[下载指南](https://ffmpeg.org/download.html)）


### 2. 克隆仓库
```bash
git clone https://github.com/XiaomingX/faceless-video-generator-plus.git
cd faceless-video-generator-plus
```


### 3. 安装依赖
1. 建议创建虚拟环境（可选但推荐）：
   ```bash
   # 创建虚拟环境
   python -m venv venv
   # 激活环境（Windows）
   venv\Scripts\activate
   # 激活环境（Mac/Linux）
   source venv/bin/activate
   ```

2. 安装Python依赖：
   ```bash
   pip install -r requirements.txt
   ```
   （需手动创建`requirements.txt`，内容见「📦 依赖列表」）


### 4. 配置文件
需创建2个核心配置文件，放在项目根目录：

#### 4.1 `.env`（存储API密钥）
```env
# OpenAI API配置（用于故事生成、TTS）
OPENAI_API_KEY=your-openai-api-key
OPENAI_BASE_URL=https://api.openai.com/v1  # 国内用户可替换为代理地址

# Replicate API配置（用于图片生成）
REPLICATE_API_TOKEN=your-replicate-token

# Fal API配置（用于图片生成，可选）
FAL_API_KEY=your-fal-api-key
```
- API密钥申请：
  - OpenAI：[https://platform.openai.com/](https://platform.openai.com/)
  - Replicate：[https://replicate.com/](https://replicate.com/)
  - Fal：[https://fal.ai/](https://fal.ai/)


#### 4.2 `config.json`（工具参数配置）
```json
{
  "openai": {
    "model": "gpt-3.5-turbo",  # 故事生成模型
    "temperature": 0.7          # 创意度（0-1，越高越随机）
  },
  "story_generation": {
    "char_limit_min": 500,      # 故事最小字符数
    "char_limit_max": 1500      # 故事最大字符数
  },
  "storyboard": {
    "max_scenes": 10            # 最大分镜数量
  },
  "tts": {
    "speech_rate": 1.0          # 语速（0.5-2.0）
  },
  "replicate_flux_api": {
    "model": "black-forest-labs/flux-schnell",  # Replicate图片模型
    "aspect_ratio": "16:9",
    "num_inference_steps": 4,
    "disable_safety_checker": false
  },
  "fal_flux_api": {
    "model": "fal-ai/flux-schnell",  # Fal图片模型
    "image_size": "1024x1792",
    "num_images": 1,
    "num_inference_steps": 4,
    "enable_safety_checker": true
  }
}
```


### 5. 运行工具
直接执行主脚本，按交互提示选择参数：
```bash
python main.py
```
示例流程：
1. 选择故事类型（如「Bedtime」睡前故事）
2. 选择图片风格（如「pixar-art」皮克斯风格）
3. 选择配音音色（如「shimmer」明亮音色）

生成完成后，文件会保存在 `data/[故事类型]/[故事标题]/` 目录下，最终视频为 `story_video_with_subtitles.mp4`。


## 📂 项目目录结构
```
faceless-video-generator-plus/
├── main.py               # 主程序（整合所有核心逻辑）
├── .env                  # API密钥配置（需手动创建）
├── config.json           # 工具参数配置（需手动创建）
├── requirements.txt      # 依赖列表（需手动创建）
├── font/                 # 字体目录（存放TitanOne.ttf，用于字幕）
│   └── TitanOne.ttf      # 字幕字体文件（可替换）
├── data/                 # 生成资源目录（自动创建）
│   └── [故事类型]/       # 按故事类型分类
│       └── [故事标题]/   # 按故事标题分类
│           ├── story_english.txt  # 故事文本
│           ├── storyboard_project.json  # 分镜配置
│           ├── scene_1.png        # 场景图片
│           ├── audio/             # 音频目录
│           │   └── scene_1.mp3    # 场景音频
│           └── story_video_with_subtitles.mp4  # 最终视频
├── LICENSE               # Apache-2.0许可证
└── README.md             # 项目说明（当前文件）
```


## 📦 依赖列表
将以下内容保存为 `requirements.txt`，用于安装依赖：
```txt
requests>=2.31.0
replicate>=0.28.0
fal-client>=0.4.0
python-dotenv>=1.0.0
openai>=1.13.3
moviepy>=1.0.3
pillow>=10.2.0
numpy>=1.26.4
opencv-python>=4.9.0.80
shortcap>=0.1.5
```


## 📄 许可证
本项目基于 **Apache License 2.0** 开源，详见 [LICENSE](https://github.com/XiaomingX/faceless-video-generator-plus/blob/main/LICENSE) 文件。


## ⚠️ 注意事项
1. API使用限制：部分API（如OpenAI、Replicate）有免费额度，超出后需付费，请关注API控制台的用量；
2. 生成耗时：图片和视频生成速度依赖网络和API响应，复杂故事可能需要1-5分钟；
3. 字体文件：字幕需 `TitanOne.ttf` 字体，可从 [Google Fonts](https://fonts.google.com/specimen/Titan+One) 下载后放入 `font/` 目录。


## 🤝 贡献指南
1. 欢迎提交Issue反馈bug或需求；
2. 如需提交代码，请先fork仓库，创建特性分支（`feature/xxx`），提交PR前确保代码格式规范；
3. 所有贡献需遵循Apache-2.0许可证。