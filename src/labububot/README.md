# Labubu Bot 🤖  
## 什么是Labubu Bot？  
专门用于**监控Pop Mart（泡泡玛特）Labubu系列商品**的自动化工具，基于 **SeleniumBase** 开发（简化操作、提升稳定性）。能自动检查商品库存，补货时立即添加到购物车，并通过声音+Discord双重提醒，避免错过热门款。


## 核心功能  
保留原功能的同时，新增SeleniumBase带来的优势，新手也能轻松上手：  
- 🔍 **多商品同时监控**：可同时盯多个商品链接，无需手动切换页面  
- 🛒 **智能自动加购**：SeleniumBase内置“失败重试”机制，点击按钮更稳定（自动切换常规/JS点击）  
- 🔔 **Discord通知**：加购成功后，实时往指定频道发消息（含商品链接，点击即可结算）  
- 🔊 **系统声音提醒**：mac播放“玻璃声”、Windows播放“蜂鸣”，不用一直盯屏幕  
- 🛡️ **强化防检测**：SeleniumBase默认屏蔽自动化标识，搭配随机用户代理、人类行为模拟，降低账号风险  
- ⏱️ **人类操作节奏**：操作间随机停顿0.5-1.5秒，避免机器式“秒点”  
- 📝 **详细日志记录**：所有操作（检查/加购/报错）存到`labubu_bot.log`，方便排查问题  
- 🚀 **驱动自动管理**：SeleniumBase自动匹配Chrome驱动，无需手动下载（解决原“驱动不兼容”问题）  


## 准备工作（必看！少一步可能用不了）  
### 1. Python环境  
- 版本要求：Python 3.8 及以上  
- 确认方式：打开“终端”（mac）/“命令提示符”（Windows），输入 `python --version`，显示3.8+即可  
- 未安装：去[Python官网](https://www.python.org/)下载，安装时勾选“Add Python to PATH”（Windows必勾）  

### 2. Chrome浏览器  
- 要求：安装**最新版Chrome**（仅支持Chrome，不兼容Edge/Safari）  
- 确认方式：Chrome右上角“三个点”→“帮助”→“关于Google Chrome”，确保为最新版本  

### 3. Pop Mart账号登录  
- 用Chrome登录Pop Mart官网（[链接](https://www.popmart.com/us/)），且必须是“默认Chrome账号”（不要用访客模式/多账号切换）  
- 原因：Bot会复制你的Chrome登录状态，避免重新登录被平台识别  


## 安装步骤（一步一步跟着做）  
### 1. 获取代码文件（从你的仓库克隆）  
打开终端，复制以下命令下载代码（避免手输错误）：  
```bash
# 1. 克隆仓库到本地（替换为你的仓库地址）
git clone https://github.com/xiaomingx/labububot.git
# 2. 进入代码文件夹
cd labububot
```  
- 无Git环境？直接去仓库页面（https://github.com/xiaomingx/labububot）→ 点击“Code”→“Download ZIP”，解压后用终端进入文件夹（示例：`cd 桌面/labububot`）  

### 2. 安装依赖库（关键：新增SeleniumBase）  
Bot依赖SeleniumBase及其他工具库，终端输入以下命令：  
```bash
# 方式1：若有requirements.txt（建议），直接安装所有依赖
pip install -r requirements.txt

# 方式2：若无requirements.txt，手动安装核心依赖
pip install seleniumbase python-dotenv requests
```  
- 报错处理：  
  - Windows“pip不是内部命令”：重新安装Python并勾选“Add Python to PATH”  
  - mac“Permission denied”：命令前加`sudo`（如 `sudo pip install seleniumbase`），输入电脑密码（输入时不显示）  

### 3. 配置Discord通知（可选，但建议开）  
加购成功后需实时提醒？按以下步骤配置：  
1. 在代码文件夹（labububot）新建文本文件，重命名为`.env`（注意：前面有个点，后缀是`env`，不是`txt`）  
2. 打开`.env`，粘贴以下内容，替换`your_discord_webhook_url_here`为你的Discord Webhook链接：  
   ```
   DISCORD_WEBHOOK=your_discord_webhook_url_here
   ```  
3. 获取Webhook链接：  
   Discord频道→右上角“齿轮”（频道设置）→“集成”→“Webhook”→“新建Webhook”→复制“Webhook URL”  


## 配置商品（盯你想要的Labubu！）  
告诉Bot要监控哪些商品，修改`labubu_bot.py`中的`PRODUCTS`列表：  
1. 用记事本（Windows）/文本编辑（mac）打开`labubu_bot.py`  
2. 找到以下代码，替换示例链接为你的目标商品链接（从Pop Mart商品页复制）：  
   ```python
   PRODUCTS = [
       # 示例1：Labubu能量满满系列挂饰盲盒
       "https://www.popmart.com/us/products/2155/THE-MONSTERS-Big-into-Energy-Series-Vinyl-Plush-Pendant-Blind-Box",
       # 示例2：Labubu坐坐系列毛绒盲盒（可替换）
       "https://www.popmart.com/us/products/1372/THE-MONSTERS---Have-a-Seat-Vinyl-Plush-Blind-Box",
       # 新增商品：按格式粘贴链接，用英文逗号结尾
   ]
   ```  
3. 保存文件（Ctrl+S / Command+S）  


## 怎么运行Bot？  
1. 关闭所有Chrome窗口（避免与Bot启动的浏览器冲突）  
2. 打开终端，进入代码文件夹（若退出，重新输入 `cd labububot`）  
3. 输入命令启动Bot：  
   ```bash
   python labubu_bot.py
   ```  
4. 启动成功的标志：  
   - 自动弹出Chrome窗口（标题可能有“自动化”提示，属正常现象）  
   - 终端打印日志：`【初始化】正在配置 SeleniumBase 浏览器...`、`【成功】SeleniumBase 浏览器实例创建完成`  


## 运行后能看到什么输出？  
| 输出类型       | 说明                                                                 |
|----------------|----------------------------------------------------------------------|
| 日志文件       | 操作记录存到`labubu_bot.log`（代码文件夹内），示例：`2024-05-20 15:30:00 [INFO] Discord 通知发送成功：🎉 商品加购成功！链接：xxx` |
| Discord通知    | 加购成功后，频道收到含商品链接的消息，点击直接跳转到Pop Mart结算页   |
| 系统声音       | mac播放“/System/Library/Sounds/Glass.aiff”，Windows发出1000Hz、1秒蜂鸣 |
| 终端日志       | 实时显示状态：`【结果】商品有货：xxx`、`【成功】'ADD TO BAG' 按钮点击完成` |


## 为什么Bot不容易被识别？（防检测细节）  
结合SeleniumBase特性+自定义配置，模拟真实用户行为：  
1. **SeleniumBase内置防护**：默认屏蔽`navigator.webdriver`自动化标识，无需手动加`--disable-blink-features`参数  
2. **随机用户代理**：每次启动从列表中选一个标识（伪装Chrome/Safari/Edge）  
3. **复制本地Chrome Profile**：复用你的登录状态、浏览记录（脱敏处理），不是“空白浏览器”  
4. **智能点击机制**：SeleniumBase自动判断点击方式（常规/JS），失败时重试，避免被识别为“机器点击”  
5. **人类节奏停顿**：操作间随机延迟0.5-1.5秒，模拟“看页面→思考→点击”的流程  


## 重要注意事项  
1. 不要关闭Bot启动的Chrome窗口！关闭后Bot会停止，需重新运行命令启动  
2. 运行时避免高负载操作（玩游戏/开大量网页），防止Bot卡顿导致加购失败  
3. SeleniumBase会自动清理临时文件：无需手动删除“临时Chrome Profile”（原版本需手动清理）  
4. 停止Bot的方式：在终端按`Ctrl+C`（Windows/mac通用），会显示`👋 机器人已被用户手动停止`  
5. 若Bot频繁报错“Profile复制失败”：可忽略（Bot会自动用全新Profile，只需重新用Chrome登录Pop Mart即可）  


## 常见问题（FAQ）  
### Q1：启动后报错“ModuleNotFoundError: No module named 'seleniumbase'”？  
A：未安装SeleniumBase，终端输入 `pip install seleniumbase` 即可（确保网络正常）  

### Q2：Chrome窗口弹出后，终端报错“商品检查失败：页面加载超时”？  
A：可能是网络问题，检查：  
1. 本地网络是否能正常打开Pop Mart官网  
2. 若网络正常，修改代码中`sb.wait_for_page_load(timeout=5)`为`timeout=10`（延长页面加载等待时间）  

### Q3：Discord没收到通知，怎么办？  
A：1. 检查`.env`文件中Webhook链接是否正确（复制到浏览器打开，显示“Unknown Webhook”即错误，需重新获取）  
2. 确认Discord频道“集成”权限未禁用Webhook  
3. 看终端日志是否有`【警告】未配置 Discord Webhook`：若有，说明`.env`文件未创建或路径错误（需放在代码文件夹根目录）  

### Q4：商品明明有货，Bot却没加购？  
A：1. 检查终端日志是否有`【失败】未找到 'ADD TO BAG' 按钮`：可能是Pop Mart更新了按钮样式，需修改代码中`add_btn_xpath`（比如从XPATH换成CSS选择器）  
2. 确认Chrome已登录Pop Mart（Bot复制的是登录状态，未登录则无法加购）  


## 免责声明  
本工具仅用于**学习Python自动化（SeleniumBase框架）** ，请勿用于高频抢货、倒卖商品等违规行为。使用过程中若违反Pop Mart平台规则（如账号限制、订单取消），需自行承担责任。