import os
import re
import json
import time
import random
import logging
import hashlib
import requests
import urllib.parse

# ---------------------- 基础配置（用户需根据实际情况修改） ----------------------
# 阅读配置
READ_NUM = int(os.getenv('READ_NUM') or 40)  # 总阅读次数（默认40次，约20分钟）

# 推送配置（按需选择一种，填写对应Token）
PUSH_METHOD = os.getenv('PUSH_METHOD') or ""  # 可选：pushplus、telegram、wxpusher、serverchan
PUSH_CONFIG = {
    "pushplus": os.getenv("PUSHPLUS_TOKEN") or "",
    "telegram": (os.getenv("TELEGRAM_BOT_TOKEN") or "", os.getenv("TELEGRAM_CHAT_ID") or ""),
    "wxpusher": os.getenv("WXPUSHER_SPT") or "",
    "serverchan": os.getenv("SERVERCHAN_SPT") or ""
}

# 接口请求配置（需替换为自己的headers和cookies，或通过环境变量WXREAD_CURL_BASH传入）
curl_str = os.getenv('WXREAD_CURL_BASH')  # 可选：通过curl命令提取headers/cookies
# 默认headers（本地使用时请替换为自己的浏览器请求头）
HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}
# 默认cookies（本地使用时请替换为自己的微信读书cookie）
COOKIES = {
    'RK': 'xxx',
    'ptcz': 'xxx',
    'wr_skey': 'xxx',  # 关键cookie，会自动刷新
    'wr_avatar': 'xxx'
}

# 书籍与章节ID（可替换为自己需要阅读的书籍/章节ID）
BOOK_LIST = [
    "36d322f07186022636daa5e", "6f932ec05dd9eb6f96f14b9", "43f3229071984b9343f04a4",
    "d7732ea0813ab7d58g0184b8", "3d03298058a9443d052d409", "4fc328a0729350754fc56d4"
]
CHAPTER_LIST = [
    "ecc32f3013eccbc87e4b62e", "a87322c014a87ff679a21ea", "e4d32d5015e4da3b7fbb1fa",
    "16732dc0161679091c5aeb1", "8f132430178f14e45fce0f7", "c9f326d018c9f0f895fb5e4"
]

# 接口固定参数（无需修改）
BASE_DATA = {
    "appId": "wb182564874603h266381671",
    "ci": 27,
    "co": 389,
    "sm": "19聚会《三体》网友的聚会地点是一处僻静",
    "pr": 74,
    "ps": "4ee326507a65a465g015fae",
    "pc": "aab32e207a65a466g010615"
}
KEY = "3c5c8717f3daf09iop3423zafeqoi"  # 哈希计算密钥
API_URLS = {
    "read": "https://weread.qq.com/web/book/read",
    "renew_cookie": "https://weread.qq.com/web/login/renewal",
    "fix_synckey": "https://weread.qq.com/web/book/chapterInfos"
}

# ---------------------- 工具函数（核心辅助逻辑） ----------------------
def extract_headers_cookies(curl_command):
    """从curl命令中提取headers和cookies（替代默认配置）"""
    headers = {}
    cookies = {}
    # 提取headers
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers[match[0]] = match[1]
    # 提取cookies（支持 -H Cookie: 和 -b 两种格式）
    cookie_header = headers.pop('Cookie', '') if 'Cookie' in headers else ''
    cookie_b = re.search(r"-b '([^']+)'", curl_command).group(1) if re.search(r"-b '([^']+)'", curl_command) else ''
    cookie_str = cookie_b if cookie_b else cookie_header
    # 解析cookie字符串
    for cookie in cookie_str.split('; '):
        if '=' in cookie:
            key, val = cookie.split('=', 1)
            cookies[key.strip()] = val.strip()
    return headers, cookies

def encode_request_data(data):
    """请求参数编码（按key排序后拼接）"""
    sorted_items = sorted(data.items(), key=lambda x: x[0])
    return '&'.join([f"{k}={urllib.parse.quote(str(v), safe='')}" for k, v in sorted_items])

def calculate_hash(input_str):
    """计算请求签名哈希值"""
    hash1, hash2 = 0x15051505, 0x15051505
    length = len(input_str)
    index = length - 1
    while index > 0:
        hash1 = 0x7fffffff & (hash1 ^ ord(input_str[index]) << (length - index) % 30)
        hash2 = 0x7fffffff & (hash2 ^ ord(input_str[index-1]) << index % 30)
        index -= 2
    return hex(hash1 + hash2)[2:].lower()

def refresh_wr_skey():
    """刷新关键cookie：wr_skey"""
    logging.info("开始刷新cookie（wr_skey）")
    cookie_data = {"rq": "%2Fweb%2Fbook%2Fread", "ql": True}
    response = requests.post(
        API_URLS["renew_cookie"],
        headers=HEADERS,
        cookies=COOKIES,
        data=json.dumps(cookie_data, separators=(',', ':'))
    )
    # 从响应头提取新的wr_skey
    set_cookie = response.headers.get('Set-Cookie', '')
    for cookie in set_cookie.split(';'):
        if "wr_skey" in cookie:
            new_skey = cookie.split('=')[-1][:8]
            COOKIES['wr_skey'] = new_skey
            logging.info(f"cookie刷新成功，新wr_skey：{new_skey}")
            return True
    logging.error("cookie刷新失败，无法获取wr_skey")
    return False

def fix_synckey_error():
    """修复无synckey错误"""
    logging.warning("检测到无synckey，尝试修复")
    requests.post(
        API_URLS["fix_synckey"],
        headers=HEADERS,
        cookies=COOKIES,
        data=json.dumps({"bookIds":["3300060341"]}, separators=(',', ':'))
    )

# ---------------------- 推送功能（简化版） ----------------------
class MessagePusher:
    def __init__(self):
        self.proxies = {
            'http': os.getenv('http_proxy'),
            'https': os.getenv('https_proxy')
        }

    def push(self, content, method):
        """统一推送入口"""
        if method == "pushplus":
            self._push_pushplus(content, PUSH_CONFIG["pushplus"])
        elif method == "telegram":
            bot_token, chat_id = PUSH_CONFIG["telegram"]
            self._push_telegram(content, bot_token, chat_id)
        elif method == "wxpusher":
            self._push_wxpusher(content, PUSH_CONFIG["wxpusher"])
        elif method == "serverchan":
            self._push_serverchan(content, PUSH_CONFIG["serverchan"])
        else:
            logging.error("推送方式错误，仅支持pushplus/telegram/wxpusher/serverchan")

    def _push_pushplus(self, content, token):
        """PushPlus推送"""
        if not token:
            logging.error("PushPlus Token未填写")
            return
        url = "https://www.pushplus.plus/send"
        data = {"token": token, "title": "微信阅读通知", "content": content}
        self._send_request(url, data, method="POST")

    def _push_telegram(self, content, bot_token, chat_id):
        """Telegram推送（支持代理/直连切换）"""
        if not (bot_token and chat_id):
            logging.error("Telegram Token或ChatID未填写")
            return
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {"chat_id": chat_id, "text": content}
        try:
            requests.post(url, json=data, proxies=self.proxies, timeout=30)
        except:
            requests.post(url, json=data, timeout=30)  # 代理失败则直连

    def _push_wxpusher(self, content, spt):
        """WxPusher推送"""
        if not spt:
            logging.error("WxPusher SPT未填写")
            return
        url = f"https://wxpusher.zjiecode.com/api/send/message/{spt}/{content}"
        self._send_request(url, method="GET")

    def _push_serverchan(self, content, spt):
        """ServerChan推送"""
        if not spt:
            logging.error("ServerChan SPT未填写")
            return
        url = f"https://sctapi.ftqq.com/{spt}.send"
        title = "微信阅读完成" if "完成" in content else "微信阅读失败"
        data = {"title": title, "desp": content}
        self._send_request(url, data, method="POST")

    def _send_request(self, url, data=None, method="POST"):
        """通用请求发送（带重试）"""
        for attempt in range(5):
            try:
                if method == "POST":
                    resp = requests.post(url, json=data, timeout=10)
                else:
                    resp = requests.get(url, timeout=10)
                resp.raise_for_status()
                logging.info(f"推送成功，响应：{resp.text[:50]}")
                break
            except Exception as e:
                if attempt < 4:
                    sleep_time = random.randint(180, 360)
                    logging.warning(f"推送失败，{sleep_time}秒后重试：{str(e)[:30]}")
                    time.sleep(sleep_time)
                else:
                    logging.error(f"推送最终失败：{str(e)}")

# ---------------------- 主逻辑（核心运行流程） ----------------------
def main():
    # 初始化日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )

    # 第一步：从curl命令提取配置（优先于默认配置）
    if curl_str:
        global HEADERS, COOKIES
        HEADERS, COOKIES = extract_headers_cookies(curl_str)
        logging.info("已从curl命令提取headers和cookies")

    # 第二步：初始化推送器
    pusher = MessagePusher()

    # 第三步：刷新cookie（确保有效性）
    if not refresh_wr_skey():
        error_msg = "cookie刷新失败，脚本终止"
        logging.error(error_msg)
        pusher.push(error_msg, PUSH_METHOD)
        return

    # 第四步：循环执行阅读请求
    read_count = 1
    last_read_time = int(time.time()) - 30  # 上一次阅读时间（初始值提前30秒）
    logging.info(f"开始自动阅读，共需阅读{READ_NUM}次（约{READ_NUM*0.5}分钟）")

    while read_count <= READ_NUM:
        # 构造本次阅读参数
        current_data = BASE_DATA.copy()
        current_time = int(time.time())
        # 动态参数（随机选书、选章节，更新时间相关字段）
        current_data.update({
            "b": random.choice(BOOK_LIST),  # 随机选书
            "c": random.choice(CHAPTER_LIST),  # 随机选章节
            "ct": current_time,  # 当前时间戳
            "rt": current_time - last_read_time,  # 阅读时长（秒）
            "ts": current_time * 1000 + random.randint(0, 1000),  # 毫秒时间戳
            "rn": random.randint(0, 1000),  # 随机数
            "sg": hashlib.sha256(f"{current_data['ts']}{current_data['rn']}{KEY}".encode()).hexdigest()  # 签名
        })
        # 计算请求哈希值
        current_data["s"] = calculate_hash(encode_request_data(current_data))

        # 发送阅读请求
        logging.info(f"第{read_count}次阅读：书籍ID={current_data['b'][:8]}，章节ID={current_data['c'][:8]}")
        try:
            response = requests.post(
                API_URLS["read"],
                headers=HEADERS,
                cookies=COOKIES,
                data=json.dumps(current_data, separators=(',', ':'))
            )
            resp_data = response.json()
            logging.info(f"阅读响应：{json.dumps(resp_data, ensure_ascii=False)[:100]}")
        except Exception as e:
            logging.error(f"阅读请求失败：{str(e)}")
            continue

        # 处理响应结果
        if "succ" in resp_data:
            if "synckey" in resp_data:
                # 阅读成功，更新状态
                last_read_time = current_time
                read_count += 1
                progress = (read_count - 1) * 0.5  # 已阅读时长（分钟）
                logging.info(f"第{read_count-1}次阅读成功，累计时长：{progress}分钟")
                # 间隔30秒再进行下一次阅读
                time.sleep(30)
            else:
                # 无synckey，修复后重试
                fix_synckey_error()
                time.sleep(5)
        else:
            # cookie过期，刷新后重试
            logging.error("阅读失败，可能cookie已过期，尝试刷新")
            if not refresh_wr_skey():
                error_msg = "cookie刷新失败，脚本终止"
                logging.error(error_msg)
                pusher.push(error_msg, PUSH_METHOD)
                return
            time.sleep(5)

    # 第五步：阅读完成，推送结果
    finish_msg = f"微信读书自动阅读完成！\n总阅读次数：{READ_NUM}次\n累计阅读时长：{READ_NUM*0.5}分钟"
    logging.info(finish_msg)
    pusher.push(finish_msg, PUSH_METHOD)

if __name__ == "__main__":
    main()