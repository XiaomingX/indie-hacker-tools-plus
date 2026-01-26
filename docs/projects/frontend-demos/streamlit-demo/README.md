# Streamlit 安装与运行指南

一个简单易懂的 Streamlit 安装和 Demo 运行教程，适合初学者快速上手。

## 什么是 Streamlit？
Streamlit 是一个用于快速构建数据应用的 Python 库，无需前端知识就能创建交互式网页应用，特别适合数据科学家和机器学习工程师使用。

## 安装 Streamlit

如果你还没有安装 Streamlit，请按照以下步骤操作：

1. 打开你的终端（Windows 用户可以使用命令提示符或 PowerShell，Mac/Linux 用户使用终端）
2. 输入以下命令并按下回车键：

```bash
# 使用 pip 安装 Streamlit
pip install streamlit
```

3. 等待安装完成（可能需要几分钟，取决于网络速度）
4. 安装成功后，你可以通过以下命令验证版本：
```bash
streamlit --version
```

## 运行 Demo 应用

安装完成后，你可以通过以下步骤运行一个 Streamlit 演示应用：

1. 确保你已经有一个名为 `app.py` 的 Python 文件（如果没有，可以创建一个简单的示例文件）
2. 在终端中，导航到 `app.py` 所在的文件夹：
   ```bash
   # 例如，进入桌面的 project 文件夹
   cd ~/Desktop/project
   ```
3. 运行以下命令启动应用：
   ```bash
   # 启动 Streamlit 应用
   streamlit run app.py
   ```
4. 运行成功后，Streamlit 会自动在你的默认浏览器中打开应用页面（通常地址是 `http://localhost:8501`）
5. 如果浏览器没有自动打开，可以手动复制终端中显示的 URL 到浏览器地址栏访问

## 常见问题

- 如果安装时出现权限错误，可以尝试使用：
  ```bash
  pip install streamlit --user
  ```

- 如果运行时提示找不到 `app.py`，请检查你是否在正确的文件夹中，或者文件名称是否正确

- 停止应用可以在终端中按下 `Ctrl + C` 组合键

## 相关关键词
- 技术：Python, Streamlit, 数据应用, 交互式网页
- 用途：快速开发, 数据可视化, 机器学习演示, 无代码前端
- 适用人群：数据科学家, 机器学习工程师, Python 开发者, 初学者