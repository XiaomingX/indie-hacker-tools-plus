import os
from datetime import datetime
from threading import Thread
from discord.ext import commands, tasks
import discord
from seleniumbase import SB
from flask import Flask

# 配置参数 - 请根据实际情况修改
TOKEN = os.getenv("DISCORD_TOKEN", "你的机器人TOKEN")  # 建议使用环境变量
DISCORD_CHANNEL_ID = 123456789012345678  # 替换为你的频道ID
REFRESH_INTERVAL = 20  # 库存检查间隔(秒)
BUTTON_CSS_SELECTOR = ".index_btn__w5nKF"  # 库存按钮的CSS选择器

# 监控的产品列表
PRODUCTS = [
    {
        "name": "Big Into Energy Labubu",
        "url": "https://www.popmart.com/hu/products/1991",
        "image": "https://prod-eurasian-res.popmart.com/default/20260422_091913_954253____1_____1200x1200.jpg"
    },
    {
        "name": "Exciting Macaron",
        "url": "https://www.popmart.com/hu/products/527/THE-MONSTERS---Exciting-Macaron-Vinyl-Face-Blind-Box",
        "image": "https://prod-eurasian-res.popmart.com/default/20231026_101051_200156__1200x1200.jpg"
    },
    {
        "name": "Have a Seat",
        "url": "https://www.popmart.com/hu/products/1194/THE-MONSTERS---Have-a-Seat-Vinyl-Plush-Blind-Box",
        "image": "https://prod-eurasian-res.popmart.com/default/20260710_104422_660558____1_____1200x1200.jpg"
    },
    {
        "name": "Coca-Cola Labubu",
        "url": "https://www.popmart.com/hu/products/1625/THE-MONSTERS-COCA-COLA-SERIES-Vinyl-Face-Blind-Box",
        "image": "https://prod-eurasian-res.popmart.com/default/20261217_163807_637795____1_____1200x1200.jpg"
    }
]

# 初始化机器人
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 产品状态跟踪 {url: 是否有库存}
product_statuses = {product['url']: False for product in PRODUCTS}

# 保持机器人在线的简单Flask服务
app = Flask('StockMonitorBot')
@app.route('/')
def home():
    return "Stock monitor bot is running!"

def keep_alive():
    Thread(target=lambda: app.run(host='0.0.0.0', port=8080), daemon=True).start()

# 机器人事件与命令
@bot.event
async def on_ready():
    print(f'✅ 已登录为: {bot.user}')
    print(f'📊 监控产品数量: {len(PRODUCTS)}')
    stock_monitor.start()  # 启动监控任务

@bot.command(help="检查机器人是否在线")
async def ping(ctx):
    await ctx.send("🏓 Pong! 我在线哦~")

@bot.command(help="显示所有产品的当前库存状态")
async def stock(ctx):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = f"📊 产品库存状态 ({now}):\n\n"
    
    for product in PRODUCTS:
        status = "✅ 有库存" if product_statuses[product['url']] else "❌ 无库存"
        response += f"**{product['name']}**\n{status}\n{product['url']}\n\n"
    
    await ctx.send(response)

# 库存监控任务
@tasks.loop(seconds=REFRESH_INTERVAL)
async def stock_monitor():
    channel = bot.get_channel(DISCORD_CHANNEL_ID)
    if not channel:
        print("⚠️ 无法获取指定频道，请检查频道ID是否正确")
        return

    try:
        # 使用SeleniumBase初始化浏览器
        with SB(headless=True) as sb:  # headless=True表示无头模式
            for product in PRODUCTS:
                url = product['url']
                name = product['name']
                
                try:
                    # 打开网页
                    sb.open(url)
                    sb.sleep(2)  # 等待页面加载
                    
                    # 等待按钮元素加载完成并获取
                    button = sb.wait_for_element(BUTTON_CSS_SELECTOR, timeout=10)
                    
                    # 检查按钮是否可用（有库存）
                    class_attr = button.get_attribute("class")
                    is_available = "disabled" not in class_attr
                    
                    # 状态变化时发送通知
                    if is_available and not product_statuses[url]:
                        embed = discord.Embed(
                            title=f"🎯 {name} 有库存了！",
                            url=url,
                            description="赶紧去看看吧！",
                            color=discord.Color.green()
                        )
                        embed.set_image(url=product['image'])
                        embed.set_footer(text=f"更新时间: {datetime.now().strftime('%H:%M:%S')}")
                        
                        await channel.send("@everyone", embed=embed)
                        print(f"📢 发送通知: {name} 有库存了")
                        product_statuses[url] = True
                        
                    elif not is_available and product_statuses[url]:
                        print(f"ℹ️ {name} 已售罄")
                        product_statuses[url] = False
                
                except Exception as e:
                    print(f"❌ 检查 {name} 时出错: {str(e)}")
                    product_statuses[url] = False
    
    except Exception as e:
        print(f"❌ SeleniumBase 错误: {str(e)}")

# 启动机器人
if __name__ == "__main__":
    keep_alive()  # 启动保持在线服务
    bot.run(TOKEN)