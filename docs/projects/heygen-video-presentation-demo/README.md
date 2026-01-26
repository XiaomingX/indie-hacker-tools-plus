# video-presentation-heygen-jobleap

一个基于Heygen等技术实现PPT自动语音播放的演示项目，帮助用户快速将静态PPT转化为带自动语音解说的动态演示视频。

![GitHub license](https://img.shields.io/github/license/XiaomingX/video-presentation-heygen-jobleap)
![GitHub repo size](https://img.shields.io/github/repo-size/XiaomingX/video-presentation-heygen-jobleap)

## 项目简介

本项目提供了一个便捷的解决方案，通过自动化流程提取PPT内容、生成匹配的语音解说，并将两者同步合成为完整的演示视频。适用于快速制作产品介绍、培训课件、会议演讲等场景的自动化视频内容。

## 功能特点

- 支持导入常见格式的PPT文件（如.pptx）
- 自动识别PPT中的文本内容并生成语音脚本
- 集成语音合成功能（基于Heygen等服务）
- 实现PPT页面切换与语音解说的自动同步
- 输出可直接使用的视频文件

## 快速开始

### 前提条件

- Python 3.8+
- 相关API密钥（如Heygen API，需自行申请）
- 依赖库：`python-pptx`、`requests` 等（详见 `requirements.txt`）

### 安装步骤

1. 克隆本仓库
   ```bash
   git clone https://github.com/XiaomingX/video-presentation-heygen-jobleap.git
   cd video-presentation-heygen-jobleap
   ```

2. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```

3. 配置环境变量
   创建 `.env` 文件并添加必要的API密钥：
   ```env
   HEYGEN_API_KEY=your_heygen_api_key_here
   ```

### 使用方法

1. 将需要处理的PPT文件放入 `input/` 目录
2. 运行主程序
   ```bash
   python main.py --input input/your_presentation.pptx --output output/result.mp4
   ```
3. 生成的视频将保存至 `output/` 目录

## 示例

查看 `examples/` 目录下的演示视频，了解项目实际效果。

## 许可证

本项目基于 [Apache License 2.0](LICENSE) 开源，详情请查看许可证文件。

## 贡献指南

欢迎通过以下方式参与贡献：
1. 提交 Issue 反馈问题或建议
2.  Fork 仓库并提交 Pull Request 改进代码
3. 完善文档或补充使用示例

## 联系信息

项目地址：[https://github.com/XiaomingX/video-presentation-heygen-jobleap](https://github.com/XiaomingX/video-presentation-heygen-jobleap)
如有问题，可通过 Issues 与我们联系。