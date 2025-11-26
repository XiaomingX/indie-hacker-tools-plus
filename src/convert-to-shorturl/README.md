# convert-to-shorturl
基于 Python + Flask + Supabase 实现的轻量短链接生成工具，核心功能聚焦于 URL 缩短、自定义短码与访问统计，代码经过精简优化，依赖少、易理解、易部署。


## 🌟 功能特点
- **URL 标准化处理**：自动补全 `http://`/`https://` 协议前缀，去除多余空格，统一小写格式
- **双模式短码生成**：支持自定义 3-20 位字母/数字短码，或自动生成 6 位随机唯一短码
- **访问统计**：记录短链接点击次数（依赖 Supabase RPC 函数）
- **友好错误提示**：表单验证、数据库异常、短码不存在等场景均有明确反馈
- **轻量无冗余**：移除非核心依赖（如 QR 码、复杂日志），仅保留核心功能所需库


## 📋 环境要求
- Python 3.8+
- 依赖库：`Flask`、`supabase-py`、`python-dotenv`


## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/your-username/convert-to-shorturl.git
cd convert-to-shorturl
```

### 2. 安装依赖
首先创建并激活虚拟环境（可选但推荐）：
```bash
# 创建虚拟环境（Windows）
python -m venv venv
venv\Scripts\activate

# 创建虚拟环境（macOS/Linux）
python3 -m venv venv
source venv/bin/activate
```

安装依赖包：
```bash
pip install -r requirements.txt
```

#### 依赖列表（`requirements.txt`）
需手动在项目根目录创建此文件，内容如下：
```txt
Flask>=2.0.0
supabase>=2.0.0
python-dotenv>=1.0.0
```


### 3. 配置 Supabase 数据库
该项目使用 Supabase 作为数据存储，需先完成以下配置：

#### 3.1 创建 Supabase 项目
1. 访问 [Supabase 官网](https://supabase.com/) 注册账号并创建新项目
2. 在项目中获取 **Supabase URL** 和 **anon public 密钥**（路径：`Project Settings > API > Project URL` / `anon public`）


#### 3.2 创建 `urls` 数据表
在 Supabase 控制台的 `SQL Editor` 中执行以下 SQL，创建存储短链接的表：
```sql
CREATE TABLE urls (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  original_url TEXT NOT NULL,  -- 原始长URL
  short_code TEXT NOT NULL UNIQUE,  -- 短码（唯一）
  created_at TEXT NOT NULL,  -- 创建时间（ISO格式）
  clicks INTEGER NOT NULL DEFAULT 0  -- 点击次数
);

-- 创建索引优化短码查询速度
CREATE INDEX idx_short_code ON urls(short_code);
```


#### 3.3 创建 `increment` RPC 函数
用于实现点击次数自增，在 `SQL Editor` 中执行：
```sql
CREATE OR REPLACE FUNCTION increment()
RETURNS TRIGGER AS $$
BEGIN
  NEW.clicks = OLD.clicks + 1;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```


### 4. 项目配置
在项目根目录创建 `.env` 文件，填入以下配置（替换为你的 Supabase 信息）：
```env
# .env 文件内容
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...（你的anon密钥）
FLASK_SECRET_KEY=（可选，不填则自动生成，建议生产环境手动设置，如：secrets.token_hex(32) 生成的值）
```


### 5. 创建模板文件
项目依赖 Flask 模板渲染页面，需在根目录创建 `templates` 文件夹，并添加以下 2 个 HTML 文件：

#### 5.1 `templates/index.html`（首页：生成短链接表单）
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>短链接生成工具</title>
    <style>
        .container { max-width: 600px; margin: 2rem auto; padding: 0 1rem; }
        .flash-error { color: #dc3545; padding: 0.5rem; border: 1px solid #dc3545; border-radius: 4px; margin-bottom: 1rem; }
        form { display: flex; flex-direction: column; gap: 1rem; }
        input { padding: 0.5rem; font-size: 1rem; }
        button { padding: 0.5rem; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
        .result { margin-top: 2rem; padding: 1rem; border: 1px solid #ddd; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>生成短链接</h1>
        
        <!-- 错误提示 -->
        {% with messages = get_flashed_messages(category_filter=["error"]) %}
            {% if messages %}
                {% for msg in messages %}
                    <div class="flash-error">{{ msg }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        <!-- 表单 -->
        <form method="POST">
            <div>
                <label>原始URL（必填）：</label>
                <input type="url" name="url" placeholder="例如：https://example.com" required>
            </div>
            <div>
                <label>自定义短码（可选，3-20位字母/数字）：</label>
                <input type="text" name="custom_code" placeholder="例如：myurl123">
            </div>
            <button type="submit">生成短链接</button>
        </form>

        <!-- 生成结果 -->
        {% if short_url %}
            <div class="result">
                <h3>生成成功！</h3>
                <p>原始URL：{{ original_url }}</p>
                <p>短链接：<a href="{{ short_url }}" target="_blank">{{ short_url }}</a></p>
            </div>
        {% endif %}
    </div>
</body>
</html>
```

#### 5.2 `templates/error.html`（错误页面）
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>错误 - 短链接工具</title>
    <style>
        .container { max-width: 600px; margin: 2rem auto; padding: 0 1rem; text-align: center; }
        .error { color: #dc3545; font-size: 1.2rem; margin: 2rem 0; }
        a { color: #007bff; text-decoration: none; }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ error }}</h1>
        <div class="error">请检查短码是否正确，或返回首页重新生成</div>
        <a href="/">返回首页</a>
    </div>
</body>
</html>
```


### 6. 启动项目
```bash
# 开发环境启动（debug模式开启）
python app.py
```

启动后访问 `http://localhost:5000` 即可使用短链接生成功能。


## 📂 项目目录结构
```
convert-to-shorturl/
├── templates/          # 前端模板文件
│   ├── index.html      # 首页（表单+结果展示）
│   └── error.html      # 错误页面
├── .env                # 环境配置文件（不提交到Git）
├── .gitignore          # Git忽略文件（建议添加venv/、.env、__pycache__/）
├── app.py              # 核心业务逻辑（Flask应用）
├── requirements.txt    # 项目依赖列表
└── README.md           # 项目说明文档（本文档）
```


## ❗ 常见问题
1. **启动报错“ModuleNotFoundError: No module named 'xxx'”**  
   解决方案：确保已激活虚拟环境，并执行 `pip install -r requirements.txt` 安装依赖。

2. **Supabase 连接失败/数据插入报错**  
   解决方案：  
   - 检查 `.env` 中的 `SUPABASE_URL` 和 `SUPABASE_KEY` 是否正确；  
   - 确认 Supabase 项目的 `anon public` 密钥权限是否开启（路径：`Project Settings > API > Policy`，确保 `urls` 表有读写权限）。

3. **自定义短码提示“已被使用”**  
   解决方案：短码在 `urls` 表中是唯一的，更换其他 3-20 位字母/数字组合即可。

4. **点击短链接后未跳转/点击计数未更新**  
   解决方案：检查 `original_url` 是否合法，或查看控制台输出的错误信息（如数据库更新失败）。


## 📌 备注
- **生产环境注意事项**：关闭 `debug=True`，使用正式的 `FLASK_SECRET_KEY`，并配置反向代理（如 Nginx）；  
- **恢复 QR 码功能**：需重新安装依赖 `qrcode`，并在 `app.py` 中还原 QR 码生成函数及前端展示逻辑；  
- **扩展建议**：可添加短链接过期时间、访问日志、用户认证等功能。


## 📄 许可证
（可选，如需开源可添加，例如 MIT 许可证）  
本项目基于 MIT 许可证开源，详情见 [LICENSE](LICENSE) 文件。
