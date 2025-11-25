# find_and_apply_to_jobs
基于 AI 与浏览器自动化的职位搜索工具，可自动读取简历、搜索目标公司实习岗位（如机器学习方向）、筛选职位并保存关键信息，适用于高效获取目标企业招聘信息，是 `browser-use` 库的实战演示项目。


## 项目功能
- **简历解析**：自动读取 PDF 格式简历，提取文本内容用于职位匹配参考
- **自动化职位搜索**：通过浏览器自动化（Chrome）访问目标公司招聘页面，搜索指定类型岗位（默认：机器学习实习）
- **职位信息保存**：将找到的有效职位（名称、公司、链接、薪资、地点）结构化存储到 `jobs.csv`，便于后续查看
- **AI 辅助决策**：基于 Azure OpenAI GPT-4o 模型理解招聘需求，辅助筛选与简历匹配的岗位


## 环境准备
1. **基础环境**
   - Python 3.9+（推荐 3.10，避免依赖兼容性问题）
   - 谷歌浏览器（Chrome 110+，需与 `browser-use` 支持的版本匹配）
   - Azure OpenAI 账号（获取 API 密钥与端点，用于 AI 岗位分析）

2. **必要文件**
   - 简历文件：命名为 `cv_04_24.pdf`，放置在项目根目录（支持多页 PDF，自动提取全文）
   - 环境配置文件：项目根目录创建 `.env` 文件，用于存储敏感信息（避免硬编码）


## 快速开始
### 1. 克隆/初始化项目
```bash
# 若使用Git，克隆仓库（无仓库则直接新建文件夹）
git clone <你的仓库地址>
cd find_and_apply_to_jobs

# 新建虚拟环境（推荐，避免依赖冲突）
python -m venv venv
# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 2. 安装依赖
通过 `pip` 安装所有必需包：
```bash
pip install python-dotenv PyPDF2 langchain-openai browser-use
```

### 3. 配置环境变量
在项目根目录创建 `.env` 文件，填入 Azure OpenAI 信息（格式如下）：
```env
# .env 文件内容
AZURE_OPENAI_KEY=你的Azure OpenAI API密钥（如：sk-xxxxxx）
AZURE_OPENAI_ENDPOINT=你的Azure OpenAI端点（如：https://xxx.openai.azure.com/）
```

### 4. 运行工具
```bash
# 执行主脚本
python job_finder.py
```
运行后将自动：
1. 加载简历内容
2. 启动 Chrome 浏览器，访问目标公司招聘页
3. 搜索机器学习实习岗位
4. 将匹配的职位信息保存到 `jobs.csv`


## 核心配置说明
### 1. 调整搜索目标
修改 `job_finder.py` 中 `main()` 函数的 `companies` 列表，添加/删除需要搜索的公司：
```python
# 示例：搜索 Google、Microsoft、NVIDIA 的实习
companies = [
    "Google",
    "Microsoft",
    "NVIDIA"  # 取消注释即可添加该公司
]
```

### 2. 更换岗位类型
默认搜索“机器学习实习”，如需修改岗位关键词，编辑 `base_task` 中的搜索描述：
```python
base_task = (
    "你是一个专业的职位搜索助手。请按以下步骤操作：\n"
    "1. 首先调用read_cv读取我的简历内容\n"
    "2. 在指定公司网站搜索【数据科学实习】岗位  # 此处修改为目标岗位类型\n"
    "3. 找到合适的职位后，使用save_job保存职位信息\n"
    "4. 确保页面为英文版本"
)
```

### 3. 浏览器路径配置
若 Chrome 安装路径与默认不同（如 Windows 系统），修改 `BrowserConfig` 中的 `browser_binary_path`：
```python
# Windows 示例路径（需根据实际安装位置调整）
browser = Browser(
    config=BrowserConfig(
        browser_binary_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        disable_security=True,
    )
)
```


## 输出文件说明
运行后生成的 `jobs.csv` 包含以下字段，用Excel或文本编辑器可打开：
| 职位名称 | 公司 | 链接 | 薪资 | 地点 |
|----------|------|------|------|------|
| Machine Learning Intern | Google | https://... | $25/hour | Mountain View, CA |


## 常见问题（FAQ）
1. **“简历文件未找到”错误**  
   - 检查简历文件名是否为 `cv_04_24.pdf`，且放置在项目根目录
   - 若需修改简历路径，更新代码中 `CV_PATH = Path.cwd() / "你的简历文件名.pdf"`

2. **Azure OpenAI 密钥错误**  
   - 确认 `.env` 文件中 `AZURE_OPENAI_KEY` 和 `AZURE_OPENAI_ENDPOINT` 拼写正确
   - 检查 Azure 账号是否有权限访问 GPT-4o 模型，且 API 密钥未过期

3. **浏览器无法启动**  
   - 确认 Chrome 版本 ≥ 110，且 `browser_binary_path` 指向正确的 Chrome 可执行文件
   - 若提示“安全设置阻止”，尝试关闭 Chrome 所有进程后重新运行


## 注意事项
- 遵守目标公司招聘页面的 `robots.txt` 规则，避免频繁请求导致 IP 被限制
- 简历内容仅本地读取，不会上传至第三方服务器，确保数据安全
- 若需自动申请职位，可扩展 `upload_cv` 函数（现有代码已包含简历上传能力，需结合具体招聘页表单调整）
