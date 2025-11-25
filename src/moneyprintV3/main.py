import os
import sys
import json
import random
import zipfile
import requests
import platform
import schedule
import subprocess
from uuid import uuid4
from termcolor import colored
from prettytable import PrettyTable
import g4f
import srt_equalizer

# 基础配置与路径
ROOT_DIR = os.path.dirname(sys.path[0])
CACHE_DIR = os.path.join(ROOT_DIR, '.mp')
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.json')
SONGS_DIR = os.path.join(ROOT_DIR, 'Songs')
BANNER_PATH = os.path.join(ROOT_DIR, 'assets', 'banner.txt')

# 平台常量
OPTIONS = ["YouTube Shorts Automation", "Twitter Bot", "Affiliate Marketing", "Outreach", "Quit"]
TWITTER_OPTIONS = ["Post something", "Show all Posts", "Setup CRON Job", "Quit"]
YOUTUBE_OPTIONS = ["Upload Short", "Show all Shorts", "Setup CRON Job", "Quit"]
CRON_OPTIONS = ["Once a day", "Twice a day", "Thrice a day", "Quit"]

# 辅助函数 - 配置读取
def get_config(key):
    """获取配置文件中的值"""
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f).get(key)

# 辅助函数 - 缓存路径
def get_cache_path(platform):
    """根据平台获取缓存路径"""
    paths = {
        'twitter': os.path.join(CACHE_DIR, 'twitter.json'),
        'youtube': os.path.join(CACHE_DIR, 'youtube.json'),
        'afm': os.path.join(CACHE_DIR, 'afm.json'),
        'results': os.path.join(CACHE_DIR, 'scraper_results.csv')
    }
    return paths.get(platform)

# 辅助函数 - 文件操作
def init_cache_file(path, default):
    """初始化缓存文件（不存在则创建）"""
    if not os.path.exists(path):
        with open(path, 'w') as f:
            json.dump(default, f, indent=4)

def load_cache(path):
    """加载缓存数据"""
    init_cache_file(path, {'accounts': []} if 'json' in path else {})
    with open(path, 'r') as f:
        return json.load(f)

def save_cache(path, data):
    """保存数据到缓存"""
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

# 账户管理
def get_accounts(platform):
    """获取指定平台的账户列表"""
    path = get_cache_path(platform)
    return load_cache(path).get('accounts', [])

def add_account(platform, account_data):
    """添加账户到指定平台"""
    path = get_cache_path(platform)
    data = load_cache(path)
    data['accounts'].append(account_data)
    save_cache(path, data)

def remove_account(platform, account_id):
    """从指定平台移除账户"""
    path = get_cache_path(platform)
    data = load_cache(path)
    data['accounts'] = [acc for acc in data['accounts'] if acc['id'] != account_id]
    save_cache(path, data)

# 产品管理（ Affiliate Marketing ）
def get_products():
    """获取产品列表"""
    path = get_cache_path('afm')
    return load_cache(path).get('products', [])

def add_product(product_data):
    """添加产品"""
    path = get_cache_path('afm')
    data = load_cache(path)
    data['products'] = data.get('products', []) + [product_data]
    save_cache(path, data)

# 系统初始化
def init_system():
    """初始化系统文件夹结构和基础资源"""
    # 创建缓存文件夹
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
        print(colored(f"创建缓存文件夹: {CACHE_DIR}", "green"))
    
    # 初始化缓存文件
    for platform in ['twitter', 'youtube', 'afm']:
        init_cache_file(get_cache_path(platform), {'accounts': []} if platform != 'afm' else {'products': []})
    
    # 下载音乐资源
    if not os.path.exists(SONGS_DIR):
        os.makedirs(SONGS_DIR)
        print(colored("下载音乐资源...", "blue"))
        try:
            zip_url = get_config('zip_url') or "https://filebin.net/bb9ewdtckolsf3sg/drive-download-20240209T180019Z-001.zip"
            resp = requests.get(zip_url)
            zip_path = os.path.join(SONGS_DIR, 'songs.zip')
            
            with open(zip_path, 'wb') as f:
                f.write(resp.content)
            
            with zipfile.ZipFile(zip_path, 'r') as zf:
                zf.extractall(SONGS_DIR)
            os.remove(zip_path)
            print(colored("音乐资源下载完成", "green"))
        except Exception as e:
            print(colored(f"音乐下载失败: {str(e)}", "red"))

# 平台操作类
class Twitter:
    def __init__(self, account_id, nickname, firefox_profile, topic):
        self.account_id = account_id
        self.nickname = nickname
        self.profile = firefox_profile
        self.topic = topic
        self.cache_path = get_cache_path('twitter')

    def post(self):
        """发布推文（简化版）"""
        print(colored(f"[{self.nickname}] 发布推文...", "blue"))
        # 实际发布逻辑可在此添加
        content = f"自动发布: {self.topic} 相关内容"
        
        # 保存到缓存
        data = load_cache(self.cache_path)
        for acc in data['accounts']:
            if acc['id'] == self.account_id:
                acc['posts'] = acc.get('posts', []) + [{
                    'id': str(uuid4()),
                    'date': str(os.path.getmtime(self.cache_path)),
                    'content': content
                }]
        save_cache(self.cache_path, data)
        print(colored("推文发布成功", "green"))

    def get_posts(self):
        """获取历史推文"""
        data = load_cache(self.cache_path)
        for acc in data['accounts']:
            if acc['id'] == self.account_id:
                return acc.get('posts', [])
        return []

class YouTube:
    def __init__(self, account_id, nickname, firefox_profile, niche, language):
        self.account_id = account_id
        self.nickname = nickname
        self.profile = firefox_profile
        self.niche = niche
        self.language = language
        self.cache_path = get_cache_path('youtube')

    def generate_video(self):
        """生成视频（简化版）"""
        print(colored(f"[{self.nickname}] 生成视频...", "blue"))
        # 实际生成逻辑可在此添加
        return {
            'id': str(uuid4()),
            'date': str(os.path.getmtime(self.cache_path)),
            'title': f"{self.niche} 相关视频"
        }

    def upload_video(self, video):
        """上传视频（简化版）"""
        print(colored(f"[{self.nickname}] 上传视频: {video['title']}", "blue"))
        # 保存到缓存
        data = load_cache(self.cache_path)
        for acc in data['accounts']:
            if acc['id'] == self.account_id:
                acc['videos'] = acc.get('videos', []) + [video]
        save_cache(self.cache_path, data)
        print(colored("视频上传成功", "green"))

    def get_videos(self):
        """获取历史视频"""
        data = load_cache(self.cache_path)
        for acc in data['accounts']:
            if acc['id'] == self.account_id:
                return acc.get('videos', [])
        return []

class AffiliateMarketing:
    def __init__(self, product_link, profile, account_id, nickname, topic):
        self.link = product_link
        self.profile = profile
        self.account_id = account_id
        self.nickname = nickname
        self.topic = topic

    def generate_pitch(self):
        """生成推广文案"""
        self.pitch = f"推荐产品: {self.link} - {self.topic} 必备"
        print(colored(f"生成推广文案: {self.pitch}", "blue"))

    def share_pitch(self):
        """通过Twitter分享"""
        twitter = Twitter(self.account_id, self.nickname, self.profile, self.topic)
        twitter.post()  # 实际应用中可使用生成的pitch

# 主菜单逻辑
def print_banner():
    """打印程序横幅"""
    if os.path.exists(BANNER_PATH):
        with open(BANNER_PATH, 'r') as f:
            print(colored(f.read(), "green"))

def main_menu():
    """主菜单"""
    while True:
        print("\n" + "="*30)
        print(colored("主菜单", "cyan"))
        for i, opt in enumerate(OPTIONS, 1):
            print(f"{i}. {opt}")
        print("="*30)
        
        try:
            choice = int(input("请选择功能 (1-5): "))
            if choice == 5:  # 退出
                print(colored("程序结束", "blue"))
                break
            handle_choice(choice)
        except ValueError:
            print(colored("输入错误，请输入数字", "red"))

def handle_choice(choice):
    """处理用户选择"""
    if choice == 1:
        handle_youtube()
    elif choice == 2:
        handle_twitter()
    elif choice == 3:
        handle_affiliate()
    elif choice == 4:
        print(colored("启动推广功能（简化版）", "blue"))

def handle_twitter():
    """处理Twitter功能"""
    accounts = get_accounts('twitter')
    
    if not accounts:
        print(colored("没有Twitter账户，创建一个新账户", "yellow"))
        acc_id = str(uuid4())
        add_account('twitter', {
            'id': acc_id,
            'nickname': input("账户昵称: "),
            'firefox_profile': input("Firefox配置路径: "),
            'topic': input("账户主题: "),
            'posts': []
        })
        print(colored(f"账户创建成功，ID: {acc_id}", "green"))
        return
    
    # 显示账户列表
    table = PrettyTable(['序号', '昵称', '主题'])
    for i, acc in enumerate(accounts, 1):
        table.add_row([i, acc['nickname'], acc['topic']])
    print(table)
    
    try:
        sel = int(input("选择账户 (1-{}): ".format(len(accounts)))) - 1
        account = accounts[sel]
        twitter = Twitter(account['id'], account['nickname'], account['firefox_profile'], account['topic'])
        
        while True:
            print("\n" + "="*30)
            print(colored("Twitter功能", "cyan"))
            for i, opt in enumerate(TWITTER_OPTIONS, 1):
                print(f"{i}. {opt}")
            print("="*30)
            
            opt = int(input("请选择 (1-4): "))
            if opt == 1:
                twitter.post()
            elif opt == 2:
                posts = twitter.get_posts()
                if posts:
                    table = PrettyTable(['序号', '日期', '内容'])
                    for i, p in enumerate(posts, 1):
                        table.add_row([i, p['date'][:10], p['content'][:30]])
                    print(table)
                else:
                    print(colored("没有历史推文", "yellow"))
            elif opt == 3:
                setup_cron('twitter', account['id'])
            elif opt == 4:
                break
    except (IndexError, ValueError):
        print(colored("选择错误", "red"))

def handle_youtube():
    """处理YouTube功能"""
    accounts = get_accounts('youtube')
    
    if not accounts:
        print(colored("没有YouTube账户，创建一个新账户", "yellow"))
        acc_id = str(uuid4())
        add_account('youtube', {
            'id': acc_id,
            'nickname': input("账户昵称: "),
            'firefox_profile': input("Firefox配置路径: "),
            'niche': input("内容领域: "),
            'language': input("语言: "),
            'videos': []
        })
        print(colored(f"账户创建成功，ID: {acc_id}", "green"))
        return
    
    # 显示账户列表
    table = PrettyTable(['序号', '昵称', '领域'])
    for i, acc in enumerate(accounts, 1):
        table.add_row([i, acc['nickname'], acc['niche']])
    print(table)
    
    try:
        sel = int(input("选择账户 (1-{}): ".format(len(accounts)))) - 1
        account = accounts[sel]
        youtube = YouTube(account['id'], account['nickname'], account['firefox_profile'], account['niche'], account['language'])
        
        while True:
            print("\n" + "="*30)
            print(colored("YouTube功能", "cyan"))
            for i, opt in enumerate(YOUTUBE_OPTIONS, 1):
                print(f"{i}. {opt}")
            print("="*30)
            
            opt = int(input("请选择 (1-4): "))
            if opt == 1:
                video = youtube.generate_video()
                if input("是否上传? (y/n): ").lower() == 'y':
                    youtube.upload_video(video)
            elif opt == 2:
                videos = youtube.get_videos()
                if videos:
                    table = PrettyTable(['序号', '日期', '标题'])
                    for i, v in enumerate(videos, 1):
                        table.add_row([i, v['date'][:10], v['title']])
                    print(table)
                else:
                    print(colored("没有历史视频", "yellow"))
            elif opt == 3:
                setup_cron('youtube', account['id'])
            elif opt == 4:
                break
    except (IndexError, ValueError):
        print(colored("选择错误", "red"))

def handle_affiliate():
    """处理联盟营销功能"""
    products = get_products()
    
    if not products:
        print(colored("没有产品，添加一个新产品", "yellow"))
        product_id = str(uuid4())
        twitter_id = input("关联的Twitter账户ID: ")
        add_product({
            'id': product_id,
            'affiliate_link': input("推广链接: "),
            'twitter_uuid': twitter_id
        })
        # 查找关联账户
        accounts = get_accounts('twitter')
        account = next((a for a in accounts if a['id'] == twitter_id), None)
        if account:
            afm = AffiliateMarketing(input("推广链接: "), account['firefox_profile'], account['id'], account['nickname'], account['topic'])
            afm.generate_pitch()
            afm.share_pitch()
        return
    
    # 显示产品列表
    table = PrettyTable(['序号', '推广链接', '关联Twitter ID'])
    for i, p in enumerate(products, 1):
        table.add_row([i, p['affiliate_link'][:30], p['twitter_uuid'][:8]])
    print(table)

def setup_cron(platform, account_id):
    """设置定时任务"""
    print("\n" + "="*30)
    print(colored("定时任务设置", "cyan"))
    for i, opt in enumerate(CRON_OPTIONS, 1):
        print(f"{i}. {opt}")
    print("="*30)
    
    try:
        opt = int(input("请选择 (1-4): "))
        if opt == 4:
            return
            
        cron_cmd = f"python {os.path.join(ROOT_DIR, 'src', 'cron.py')} {platform} {account_id}"
        print(colored(f"设置定时任务: {cron_cmd}", "blue"))
        
        # 实际定时任务逻辑可在此添加
        if opt == 1:
            schedule.every(1).day.do(lambda: subprocess.run(cron_cmd, shell=True))
        elif opt == 2:
            schedule.every().day.at("10:00").do(lambda: subprocess.run(cron_cmd, shell=True))
            schedule.every().day.at("16:00").do(lambda: subprocess.run(cron_cmd, shell=True))
        elif opt == 3:
            schedule.every().day.at("08:00").do(lambda: subprocess.run(cron_cmd, shell=True))
            schedule.every().day.at("12:00").do(lambda: subprocess.run(cron_cmd, shell=True))
            schedule.every().day.at("18:00").do(lambda: subprocess.run(cron_cmd, shell=True))
        
        print(colored("定时任务设置成功", "green"))
    except ValueError:
        print(colored("选择错误", "red"))

# 程序入口
if __name__ == "__main__":
    print_banner()
    init_system()
    main_menu()