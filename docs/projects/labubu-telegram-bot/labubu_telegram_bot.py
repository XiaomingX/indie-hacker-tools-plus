# --------------------------
# 1. 导入依赖模块（SeleniumBase 核心 + 辅助工具）
# 说明：SeleniumBase 封装了 Selenium 重复逻辑，无需手动管理 Driver、等待条件
# --------------------------
from seleniumbase import SB  # SeleniumBase 核心类（替代原生 Selenium Driver）
from selenium.webdriver.common.by import By  # 保留原定位方式，兼容习惯
from dotenv import load_dotenv  # 读取.env环境变量
import os
import platform
import tempfile
import shutil
import time
import random
import requests
import logging


# --------------------------
# 2. 配置与常量定义（与原逻辑一致，方便修改）
# --------------------------
# 加载.env文件（Discord Webhook 敏感信息）
load_dotenv()

# 日志配置（记录运行状态到文件）
logging.basicConfig(
    filename="labubu_bot.log",
    filemode="a",
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO
)

# Discord 通知配置（从.env读取）
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

# 随机用户代理列表（防检测，SeleniumBase 可自动生成，但保留自定义更灵活）
USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
]

# 监控商品列表（替换为你的目标商品链接）
PRODUCTS = [
    "https://www.popmart.com/us/products/2155/THE-MONSTERS-Big-into-Energy-Series-Vinyl-Plush-Pendant-Blind-Box",
    "https://www.popmart.com/us/products/1372/THE-MONSTERS---Have-a-Seat-Vinyl-Plush-Blind-Box"
]


# --------------------------
# 3. 基础工具函数（原逻辑保留，适配 SeleniumBase 无改动）
# --------------------------
def get_random_user_agent():
    """随机获取浏览器用户代理（防检测）"""
    return random.choice(USER_AGENTS)


def human_like_delay():
    """模拟人类操作延迟（0.5-1.5秒）"""
    time.sleep(random.uniform(0.5, 1.5))


def play_sound_alert():
    """商品加购成功时播放系统提示音（分系统适配）"""
    try:
        if platform.system() == "Darwin":  # macOS
            os.system('afplay /System/Library/Sounds/Glass.aiff')
        elif platform.system() == "Windows":  # Windows
            import winsound
            winsound.Beep(1000, 1000)
        else:  # Linux
            os.system('paplay /usr/share/sounds/freedesktop/stereo/complete.oga')
    except Exception as e:
        print(f"【警告】提示音播放失败：{str(e)}")


def send_discord_alert(message):
    """通过 Discord Webhook 发送加购通知"""
    if not DISCORD_WEBHOOK:
        logging.warning("未配置 Discord Webhook，无法发送通知")
        return

    data = {"content": message}
    try:
        response = requests.post(DISCORD_WEBHOOK, json=data)
        if response.status_code == 204:
            logging.info(f"Discord 通知发送成功：{message}")
            play_sound_alert()
        else:
            print(f"【警告】Discord 通知失败，状态码：{response.status_code}")
    except Exception as e:
        print(f"【错误】Discord 通知发送出错：{e}")


# --------------------------
# 4. SeleniumBase 浏览器配置（核心优化：替代原 get_driver 函数）
# 说明：SeleniumBase 自动管理 Driver 生命周期，无需手动 quit()，内置防检测
# --------------------------
def get_sb_instance():
    """创建并配置 SeleniumBase 实例（含临时 Profile、防检测配置）"""
    print("【初始化】正在配置 SeleniumBase 浏览器...")

    # 1. 创建临时目录（用于复制本地 Chrome Profile，复用登录状态）
    home_dir = os.path.expanduser("~")
    local_chrome_profile = os.path.join(home_dir, "Library/Application Support/Google/Chrome/Default")
    temp_profile_dir = tempfile.mkdtemp()
    print(f"【临时文件】创建临时 Profile 目录：{temp_profile_dir}")

    # 2. 复制本地 Chrome Profile（失败则用全新 Profile，不影响主流程）
    try:
        shutil.copytree(local_chrome_profile, os.path.join(temp_profile_dir, "Default"))
        print("【成功】本地 Chrome Profile 复制完成（复用登录状态）")
    except Exception as e:
        print(f"【警告】Profile 复制失败：{str(e)}，将使用全新 Profile")

    # 3. 配置 SeleniumBase 参数（内置防检测，无需手动加大量 options）
    sb_options = [
        f"--user-data-dir={temp_profile_dir}",  # 使用临时 Profile
        f"--user-agent={get_random_user_agent()}",  # 随机用户代理
        "--start-maximized",  # 窗口最大化
        "--disable-notifications",  # 关闭通知
        "--disable-popup-blocking",  # 关闭弹窗拦截
        "--disable-images",  # 禁用图片加载（提速）
        "--disable-javascript",  # 禁用 JS（按需开启/关闭）
        # SeleniumBase 内置防检测：无需手动加 --disable-blink-features 等参数
    ]

    # 4. 创建 SeleniumBase 实例（use_auto_close=True 退出时自动关闭浏览器）
    sb = SB(
        browser="chrome",  # 指定浏览器（默认 Chrome）
        options=sb_options,
        use_auto_close=True,  # 上下文结束自动关闭浏览器
        verify_delay=0.5,  # 元素操作前的验证延迟（防误触）
        auto_extend_wait=2  # 元素未找到时自动延长等待（最多2秒，提高稳定性）
    )

    # 5. 额外防检测配置（补充 SeleniumBase 未覆盖的细节）
    sb.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })

    print("【成功】SeleniumBase 浏览器实例创建完成")
    return sb, temp_profile_dir  # 返回实例+临时目录（后续需清理临时文件）


# --------------------------
# 5. 核心业务函数（基于 SeleniumBase 简化操作）
# 说明：SeleniumBase 的 wait_for_* 方法替代原 WebDriverWait，click 内置重试
# --------------------------
def add_to_cart(sb, product_url):
    """商品加购（SeleniumBase 智能点击，无需手动写3种点击方式）"""
    print(f"\n【加购】开始处理商品：{product_url}")
    try:
        # 打印当前页面信息（排查问题用）
        print(f"【页面信息】当前标题：{sb.get_title()}")
        print(f"【页面信息】当前 URL：{sb.get_current_url()}")

        human_like_delay()

        # 1. 等待并定位 "ADD TO BAG" 按钮（SeleniumBase 自动重试，超时3秒）
        print("【查找】正在寻找 'ADD TO BAG' 按钮...")
        add_btn_xpath = "//div[contains(text(), 'ADD TO BAG')]"
        try:
            sb.wait_for_element_present(By.XPATH, add_btn_xpath, timeout=3)
            add_btn = sb.find_element(By.XPATH, add_btn_xpath)
            print("【成功】找到 'ADD TO BAG' 按钮")
        except Exception as e:
            print(f"【失败】未找到 'ADD TO BAG' 按钮：{str(e)}")
            return False

        # 2. 滚动按钮到可视区域（SeleniumBase 简化 JS 执行）
        print("【操作】滚动页面，让按钮显示在中间...")
        sb.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'})", add_btn)
        human_like_delay()

        # 3. 智能点击（SeleniumBase 内置：常规点击+JS点击自动切换，失败重试）
        try:
            sb.click(add_btn)  # 直接调用 sb.click()，无需手动处理多种点击方式
            print("【成功】'ADD TO BAG' 按钮点击完成")
        except Exception as e:
            print(f"【失败】按钮点击失败：{str(e)}")
            return False

        # 4. 加购成功后通知
        print(f"【成功】商品加购流程完成：{product_url}")
        send_discord_alert(f"🎉 商品加购成功！链接：{product_url}")
        return True

    except Exception as e:
        print(f"【错误】加购函数出错：{str(e)}")
        return False


def check_product_availability(sb, product_url):
    """商品可用性检查（轻量判断，不执行加购）"""
    try:
        print(f"\n【检查】判断商品是否有货：{product_url}")
        sb.get(product_url)  # 打开商品页（SeleniumBase 自动等待页面加载）

        # 等待页面完全加载（SeleniumBase 封装的页面加载等待）
        sb.wait_for_page_load(timeout=5)

        # 检查 "ADD TO BAG" 按钮是否存在（两种定位方式备用）
        try:
            # 方式1：CSS 选择器（精准匹配）
            sb.wait_for_element_present(By.CSS_SELECTOR, "div.index_usBtn__2KlEx.index_red__kx6Ql.index_btnFull__F7k90", timeout=3)
            print(f"【结果】商品有货：{product_url}")
            return True
        except:
            # 方式2：XPATH（兼容样式变化）
            try:
                sb.wait_for_element_present(By.XPATH, "//div[contains(text(), 'ADD TO BAG')]", timeout=2)
                print(f"【结果】商品有货：{product_url}")
                return True
            except:
                print(f"【结果】商品缺货/下架：{product_url}")
                return False
    except Exception as e:
        print(f"【错误】商品可用性检查出错：{str(e)}")
        return False


# --------------------------
# 6. 机器人主循环（适配 SeleniumBase 实例管理）
# --------------------------
def run_bot_cycle():
    """单次监控循环（创建 SB 实例→检查商品→清理临时文件）"""
    sb = None
    temp_profile_dir = None
    try:
        print("\n" + "="*50)
        print("【循环】开始新一轮商品检查...")

        # 1. 创建 SeleniumBase 实例（获取实例+临时目录）
        try:
            sb, temp_profile_dir = get_sb_instance()
        except Exception as e:
            print(f"【错误】SeleniumBase 实例创建失败：{str(e)}")
            time.sleep(random.uniform(8, 12))  # 失败后重试延迟
            return

        # 2. 循环检查所有商品（持续运行，直到手动停止）
        while True:
            for product_url in PRODUCTS:
                try:
                    print(f"\n【循环】正在处理商品：{product_url}")
                    sb.get(product_url)  # 打开商品页
                    sb.wait_for_page_load(timeout=5)  # 等待页面加载完成

                    # 检查商品是否有货，有货则加购
                    try:
                        sb.wait_for_element_present(By.XPATH, "//div[contains(text(), 'ADD TO BAG')]", timeout=3)
                        print(f"【发现】商品有货，准备加购：{product_url}")
                        add_result = add_to_cart(sb, product_url)
                        if add_result:
                            print(f"【完成】商品加购成功：{product_url}")
                        human_like_delay()
                    except:
                        print(f"【状态】商品暂时缺货：{product_url}")
                        continue

                    # 商品间延迟（防操作过快）
                    human_like_delay()

                except Exception as e:
                    print(f"【错误】处理商品 {product_url} 时出错：{str(e)}")
                    continue

            # 一轮检查完成后延迟（减轻服务器压力）
            print("\n【循环】所有商品检查完成，1-2秒后开始下一轮...")
            time.sleep(random.uniform(1, 2))

    except Exception as e:
        print(f"\n【错误】机器人循环出错：{str(e)}")
    finally:
        # 清理临时 Profile 目录（避免占用磁盘空间）
        if temp_profile_dir and os.path.exists(temp_profile_dir):
            try:
                shutil.rmtree(temp_profile_dir)
                print(f"【清理】临时 Profile 目录已删除：{temp_profile_dir}")
            except Exception as e:
                print(f"【警告】临时目录清理失败：{str(e)}")
        # SeleniumBase 已自动关闭浏览器，无需手动 quit()


def run_bot():
    """机器人主入口（初始化提示+持续循环）"""
    print("🤖 Pop Mart Labubu 商品监控机器人（基于 SeleniumBase）")
    print("🎯 正在监控的商品列表：")
    for i, product in enumerate(PRODUCTS, 1):
        print(f"  {i}. {product}")
    print("⏰ 测试模式启动，立即开始监控\n")

    # 持续运行（直到手动按 Ctrl+C 停止）
    while True:
        run_bot_cycle()


# --------------------------
# 7. 程序入口（与原逻辑一致）
# --------------------------
if __name__ == "__main__":
    print("="*50)
    print("🚀 Labubu Bot 启动中（基于 SeleniumBase）...")
    print("⚠️ 重要提示：请确保本地 Chrome 已登录 Pop Mart 账号！")
    print("⏰ 测试模式：无延迟，立即开始监控")
    print("="*50)

    # 安装提醒（首次运行需执行）
    print("\n【提示】若未安装 SeleniumBase，请先执行：pip install seleniumbase")

    try:
        run_bot()
    except KeyboardInterrupt:
        print("\n👋 机器人已被用户手动停止")
    except Exception as e:
        print(f"\n❌ 机器人因未知错误停止：{str(e)}")
    finally:
        print("\n✨ 机器人会话结束")