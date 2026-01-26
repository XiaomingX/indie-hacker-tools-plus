# Chainlit 极简聊天机器人示例：极简陪伴式AI对话应用

一个基于Chainlit框架构建的轻量级聊天机器人演示项目，帮助开发者快速搭建交互式AI对话应用。

## 项目简介

本项目使用Chainlit框架实现了一个极简风格的陪伴式聊天机器人，支持与AI模型进行自然语言交互。代码结构简洁，易于扩展，适合作为AI对话应用的入门示例或二次开发基础。

## 快速开始（本地运行）

### 前置条件
- 已安装Python 3.8+环境
- 拥有OpenAI API密钥（可在[OpenAI官网](https://platform.openai.com/)获取）

### 运行步骤

1. **克隆仓库到本地**
   ```bash
   git clone https://github.com/你的用户名/chainlit-demo.git
   cd chainlit-demo
   ```

2. **安装依赖包**
   ```bash
   pip install -r requirements.txt
   # 或直接安装chainlit和openai
   pip install chainlit openai
   ```

3. **配置环境变量**
   - 在项目根目录创建`.env`文件
   - 打开文件并添加以下内容（替换为你的实际API密钥）：
     ```
     OPENAI_API_KEY=你的_openai_api_key_here
     ```

4. **启动应用**
   ```bash
   chainlit run app.py -w
   ```
   其中`-w`参数表示启用热重载，修改代码后无需重启服务即可生效。

## 应用效果

### 本地服务启动
成功运行后，应用会在本地8000端口启动服务

### 聊天界面展示
在浏览器中访问`http://localhost:8000`即可使用聊天功能


## 开发计划（Todo）

- 🔊 语音交互：实现语音输入与语音合成输出功能
- 📄 文档处理：支持PDF、DocX等文档的解析与问答
- 🎨 扩展功能：添加AI画图、智能代理(Agent)和检索增强生成(RAG)功能

## 技术栈
- Chainlit：构建AI对话界面的Python框架
- OpenAI API：提供对话模型支持
- Python：后端开发语言

## 贡献指南
欢迎提交Issue或Pull Request来帮助改进这个项目。对于重大变更，请先创建Issue讨论想要修改的内容。

## 许可证
[MIT](LICENSE)