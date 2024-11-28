## LinkS（简单的外链生成器）

<br>
LinkS 是一个用 Python 编写的简单工具，可以自动为收集的网站生成几十个外部链接。
<br>

### 安装方法：

```sh
$ git clone https://github.com/tegal1337/LinkS
$ cd LinkS
$ python3 links.py
```

### 运行环境：

- Python 3.6.7（推荐）
- 需要的模块：json、requests、re、sys

### 输出示例：

```sh
dalpan@Tegal1337:~/Tools$ python3 links.py

[+] 域名       : dalpan.co
~ dalpan.co | 结果 -> www.quantcast.com 状态: 404
~ dalpan.co | 结果 -> www.builtwith.com 状态: 200
~ dalpan.co | 结果 -> www.aboutus.org 状态: 404
~ dalpan.co | 结果 -> whoisx.co.uk 状态: 200
~ ......
```