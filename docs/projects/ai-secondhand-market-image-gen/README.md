# 闲鱼图床 CLI 工具

基于闲鱼 API 开发的命令行图片上传工具，支持多文件上传、图片压缩/格式转换、缓存去重、日志记录等功能，免费无广告，适合开发者日常使用。


## 📋 项目介绍
本工具将原 PHP 版闲鱼图床重构为 Python CLI 版本，保留核心功能的同时，适配命令行高效操作场景。通过闲鱼 API 实现图片存储，无需自建服务器，上传后可直接获取永久图片 URL，支持在文章、项目、个人博客等场景使用。


## ✨ 核心功能
- **多文件支持**：单次上传多个图片，支持通配符（如 `./images/*.png`）
- **图片处理**：
  - 自动压缩：文件超过 8MB 时，先降质量再缩尺寸，确保符合上传要求
  - 格式转换：支持将图片转为 WebP/AVIF（更小体积，兼容性好）
- **缓存去重**：基于文件 MD5 哈希缓存，相同图片无需重复上传（24 小时过期）
- **分类管理**：上传时可指定分类（如「日常」「二次元壁纸」），方便后续整理
- **日志记录**：同时输出控制台和日志文件，上传过程、错误信息可追溯
- **画廊记录**：自动生成 `gallery.json`，保存所有上传图片的 URL、分类、时间等信息


## 🛠️ 安装依赖
工具依赖 `requests`（网络请求）和 `Pillow`（图片处理），根据需求选择以下安装方式：

### 基础依赖（必装）
支持 JPG/PNG/GIF/WebP 格式，执行命令：
```bash
pip install requests pillow
```

### 可选：AVIF 格式支持
若需要将图片转为 AVIF（更优压缩比），需额外安装系统依赖和插件：
- **Windows**：
  1. 下载 [libavif 预编译包](https://github.com/AOMediaCodec/libavif/releases)
  2. 将 `avif.dll` 放入 Python 安装目录的 `Lib\site-packages`
  3. 安装插件：`pip install pillow-avif-plugin`
- **macOS**：
  ```bash
  brew install libavif  # 需先安装 Homebrew
  pip install pillow-avif-plugin
  ```
- **Linux（Ubuntu/Debian）**：
  ```bash
  sudo apt update && sudo apt install libavif-dev
  pip install pillow-avif-plugin
  ```


## 🔑 获取闲鱼 Cookie2
上传图片需先获取闲鱼账号的 `cookie2`（身份验证凭证），步骤如下：
1. 打开浏览器，访问 [闲鱼创作者平台](https://author.goofish.com/#/)
2. 登录闲鱼账号（需完成实名认证，否则 API 会拒绝上传）
3. 按 `F12` 打开「开发者工具」：
   - Chrome：切换到「Application」→「Cookies」→ `https://author.goofish.com`
   - Firefox：切换到「存储」→「Cookie」→ `https://author.goofish.com`
4. 找到 `cookie2` 字段，复制其 **Value**（字符串较长，需完整复制，不含空格）


## 🚀 使用指南
### 基本语法
```bash
python xianyu_uploader.py [文件路径1] [文件路径2] ... --cookie2 "你的cookie2值" [其他参数]
```

### 常用命令示例
#### 1. 单个文件上传（指定分类）
```bash
python xianyu_uploader.py ./photos/test.jpg --cookie2 "abc123xyz..." --category "日常"
```

#### 2. 多文件上传（通配符）
上传 `./images` 目录下所有 PNG 和 JPG 文件：
```bash
python xianyu_uploader.py ./images/*.png ./images/*.jpg --cookie2 "abc123xyz..."
```

#### 3. 开启缓存 + 格式转换
将图片转为 WebP 格式，同时启用缓存（避免重复上传）：
```bash
python xianyu_uploader.py ./wallpaper.webp --cookie2 "abc123xyz..." --format webp --enable-cache
```

#### 4. 自定义日志和缓存目录
```bash
python xianyu_uploader.py ./avatar.png --cookie2 "abc123xyz..." --category "头像" --log-file ./my_logs/upload.log --cache-dir ./my_cache
```


## ⚙️ 完整参数说明
| 参数名          | 是否必填 | 默认值                | 说明                                                                 |
|-----------------|----------|-----------------------|----------------------------------------------------------------------|
| `文件路径`      | 是       | -                     | 待上传的图片路径，支持多个文件或通配符（如 `*.png`）                 |
| `--cookie2`     | 是       | -                     | 闲鱼账号的 `cookie2` 值（从创作者平台获取）                          |
| `--category`    | 否       | 未分类                | 图片分类（如「日常」「二次元壁纸」「教程」）                         |
| `--format`      | 否       | original              | 图片格式转换，可选值：`original`（原格式）、`webp`、`avif`           |
| `--enable-cache`| 否       | False                 | 启用缓存（相同文件 24 小时内不重复上传）                             |
| `--log-file`    | 否       | ./logs/upload.log     | 日志文件路径（自动创建父目录）                                       |
| `--cache-dir`   | 否       | ./cache               | 缓存目录路径（启用缓存时生效，自动创建）                             |
| `-h/--help`     | 否       | -                     | 查看帮助信息                                                         |


## 📁 输出文件说明
1. **`gallery.json`**：
   - 自动生成在脚本运行目录，记录所有上传成功的图片信息（URL、分类、上传时间等）
   - 支持去重（按 `fileId`），最多保留 1000 条记录
2. **日志文件**：
   - 默认路径 `./logs/upload.log`，记录上传过程、错误信息，便于排查问题
3. **缓存文件**：
   - 启用缓存时，在 `./cache` 目录下生成 MD5 命名的 JSON 文件，存储缓存的图片信息


## ⚠️ 注意事项
1. **Cookie2 有效期**：
   - `cookie2` 通常有效期为 1-3 个月，过期后会提示「API 返回错误」，需重新获取
2. **API 限制**：
   - 闲鱼 API 对上传频率和单日总量有隐性限制，避免短时间内上传数百张图片
   - 支持的图片格式：JPG/PNG/GIF/WebP（AVIF 需手动转换后上传）
   - 单文件最大 50MB（超过会自动压缩，压缩失败则提示错误）
3. **账号安全**：
   - 请勿将 `cookie2` 分享给他人，避免账号被盗用
   - 建议使用个人闲置闲鱼账号，避免主账号因 API 使用违规被限制
4. **SSL 验证**：
   - 脚本默认关闭 SSL 验证（`verify=False`），若需开启，需修改代码中 `requests.post` 的 `verify` 参数为 `True`


## ❌ 常见问题
### Q1：上传失败，提示「闲鱼 API 返回错误」
- 原因 1：`cookie2` 过期或错误 → 重新获取 `cookie2`
- 原因 2：账号未实名认证 → 登录闲鱼 App 完成实名认证
- 原因 3：图片格式不支持（如 BMP）→ 转换为 JPG/PNG 后再上传

### Q2：AVIF 格式转换失败
- 检查是否安装 `libavif` 系统依赖和 `pillow-avif-plugin` 插件
- 参考「安装依赖」部分的 AVIF 支持步骤，重新安装

### Q3：缓存不生效，相同图片仍重复上传
- 检查 `--enable-cache` 参数是否添加
- 检查缓存目录（默认 `./cache`）是否有写入权限，或自定义缓存目录

### Q4：压缩后的图片质量过低
- 脚本默认压缩质量为 85%，若需调整，可修改代码中 `compress_image` 函数的 `quality` 初始值（如改为 90）


## 📄 免责声明
- 本工具仅用于个人学习和非商业用途，请勿用于违规内容上传
- 使用闲鱼 API 需遵守闲鱼平台规则，违规使用可能导致账号被限制
- 作者不对工具的稳定性、闲鱼 API 的可用性及账号安全做担保，使用前请自行评估风险