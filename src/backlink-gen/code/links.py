import json
import requests
import sys
from urllib.parse import urlparse

def load_backlink_data():
    """
    读取并加载backlink.json文件
    """
    try:
        with open("code/backlink.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("[!] 未找到backlink.json文件。")
        sys.exit()
    except json.JSONDecodeError:
        print("[!] 解析backlink.json文件失败。")
        sys.exit()

def check_backlink(site, backlink_data):
    """
    检查每个反向链接的状态
    """
    for backlink in backlink_data:
        url = backlink['url'].replace("uhaka.com", site)
        try:
            response = requests.get(url)
            status_code = response.status_code
        except KeyboardInterrupt:
            sys.exit()
        except:
            status_code = "请求失败"

        domain = urlparse(url).netloc  # 使用 urlparse 提取域名部分
        print(f"~ {site} | 结果 -> {domain} 状态: {status_code}")

        if status_code == 200 or status_code == 502:
            with open("200status.txt", "a+") as file:
                file.write(url + "\n")

def main():
    """
    主函数，串联各个子功能
    """
    domain = "www.uhaka.com"  # 修改此变量来控制要添加外链的站点
    backlink_data = load_backlink_data()
    check_backlink(domain, backlink_data)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n\n -> 因为错误退出: {e}\n")