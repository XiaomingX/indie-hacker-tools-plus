from urllib.parse import urlparse, parse_qs, urlunparse, urlencode
import re

# -------------------------- 配置常量 - 可根据需求修改 --------------------------
# 需要跳过的文件后缀（图片、脚本等资源文件）
SKIPPED_EXTENSIONS = (
    '.jpg', '.jpeg', '.png', '.gif', '.js', '.css', '.svg', '.ico', 
    '.webp', '.woff', '.woff2', '.ttf', '.eot', '.mp4', '.avi', '.mp3'
)

# 需要跳过的路径模式（博客文章、分页等）
SKIPPED_PATH_REGEX = [
    r'/posts/', r'/blog/',          # 博客文章
    r'/page/\d+/',                  # 分页路径
]

# 路径标准化替换规则 (正则模式, 替换值)
PATH_REPLACEMENTS = [
    (r'/+', '/'),                   # 合并连续斜杠
    (r'/index\.html$', ''),         # 标准化index.html为根路径
    (r'/(cat|item|user)/\d+/(details|profile)\.html?', r'/\1/id/\2.html'),  # 标准化ID路径
    (r'/(\d{4})/(\d{2})/(\d{2})/', r'/yyyy/mm/dd/'),  # 标准化日期格式(/)
    (r'/(\d{4})-(\d{2})-(\d{2})/', r'/yyyy-mm-dd/'),  # 标准化日期格式(-)
    (r'/(\d{4})-(\d{2})-(\d{2})_to_(\d{4})-(\d{2})-(\d{2})/', r'/yyyy-mm-dd_to_yyyy-mm-dd/'),
    (r'^/(en|zh|fr|de|es|ru)/', r'/lang/'),  # 标准化语言标识
    (r'/v\d+(\.\d+)*', r'/version'),         # 标准化版本号
    (r'/[a-f0-9\-]{36}/', r'/uuid/'),        # 标准化UUID
    (r'\.(php|asp|aspx)$', r'.html'),        # 标准化脚本后缀
    (r'/category/[^/]+/', r'/category/category/'),  # 标准化类别路径
    (r'/product/sku/[^/]+/', r'/product/sku/sku/'),  # 标准化产品SKU
    (r'(/\w+)/\1/', r'\1/'),                 # 移除重复子路径
    (r'/(\d{1,3}\.){3}\d{1,3}/', r'/ip-address/'),  # 标准化IP地址
    (r'/[\w\.-]+@[\w\.-]+\.[a-z]{2,}/', r'/email/'),  # 标准化邮箱
]

# 需要移除的查询参数（跟踪参数等）
UNNECESSARY_PARAMS = [
    'utm_source', 'utm_medium', 'utm_campaign', 'ref', 'session_id', 
    'lang', 'sort', 'order', 'fbclid', 'gclid', 'tracking_id', 
    'version', 'token', 'session'
]

# 需要标准化值的查询参数 (参数名: 标准化后的值)
STANDARDIZED_PARAMS = {
    'id': 'id',
    'page': 'page',
    'offset': 'offset',
    'limit': 'limit',
    'timestamp': 'ts'
}

# -------------------------- 工具函数 --------------------------
def normalize_scheme() -> str:
    """统一协议为https"""
    return 'https'

def normalize_netloc(netloc: str) -> str:
    """标准化域名：转为小写、移除www前缀、处理默认端口"""
    netloc = netloc.lower()
    
    # 移除www.前缀
    if netloc.startswith('www.'):
        netloc = netloc[4:]
    
    # 移除默认端口（http默认80，https默认443）
    if ':' in netloc:
        domain, port = netloc.split(':', 1)
        if (port == '80' or port == '443'):
            netloc = domain
    
    return netloc

def process_path(path: str) -> str | None:
    """处理路径：标准化并检查是否需要跳过"""
    original_path = path
    
    # 应用所有路径替换规则
    for pattern, repl in PATH_REPLACEMENTS:
        path = re.sub(pattern, repl, path)
    
    # 移除末尾斜杠（根路径除外）
    if path != '/' and path.endswith('/'):
        path = path.rstrip('/')
    
    # 检查是否需要跳过该路径
    if path.endswith(SKIPPED_EXTENSIONS):
        return None
    
    for pattern in SKIPPED_PATH_REGEX:
        if re.search(pattern, path):
            return None
    
    return path

def process_query_params(query: str) -> str:
    """处理查询参数：过滤不必要参数并标准化值"""
    if not query:
        return ''
    
    params = parse_qs(query)
    
    # 移除不必要的参数
    for param in UNNECESSARY_PARAMS:
        params.pop(param, None)
    
    # 标准化参数值
    for param, standardized_value in STANDARDIZED_PARAMS.items():
        if param in params:
            params[param] = [standardized_value]
    
    # 标准化布尔值参数
    for key in list(params.keys()):
        if params[key] in (['true'], ['false']):
            params[key] = ['bool']
    
    # 移除空值参数
    params = {k: v for k, v in params.items() if v != ['']}
    
    # 按参数名排序，避免顺序不同导致的差异
    sorted_params = {k: params[k] for k in sorted(params)}
    
    return urlencode(sorted_params, doseq=True)

def normalize_url(url: str) -> str | None:
    """将URL标准化为统一格式，返回None表示应跳过该URL"""
    parsed = urlparse(url)
    
    # 处理各部分
    scheme = normalize_scheme()
    netloc = normalize_netloc(parsed.netloc)
    path = process_path(parsed.path)
    
    # 如果路径被标记为跳过，整体跳过
    if path is None:
        return None
    
    query = process_query_params(parsed.query)
    
    # 组合标准化后的各部分（忽略params和fragment）
    return urlunparse((
        scheme,
        netloc,
        path,
        '',  # 忽略params
        query,
        ''   # 忽略fragment
    ))

# -------------------------- 主函数 --------------------------
def decluster_urls(input_urls: list[str]) -> list[str]:
    """
    对URL列表进行去重和聚类处理
    
    参数:
        input_urls: 原始URL列表
        
    返回:
        去重后的原始URL列表（保留第一个出现的URL）
    """
    declustered = []
    seen_normalized = set()
    
    for url in input_urls:
        try:
            normalized = normalize_url(url)
            # 只保留未见过且未被过滤的URL
            if normalized and normalized not in seen_normalized:
                seen_normalized.add(normalized)
                declustered.append(url)
        except Exception as e:
            # 跳过解析失败的URL，避免整体崩溃
            print(f"处理URL失败: {url}, 错误: {e}")
            continue
    
    return declustered

# -------------------------- 示例运行 --------------------------
def main():
    test_urls = [
        "http://example.com/page.php?id=1",
        "https://example.com/page.php?id=1",
        "http://example.com//page.php?id=2",
        "http://example.com/page.php?id=3&page=2",
        "http://example.com/cat/9/details.html",
        "http://example.com/cat/11/details.html",
        "http://example.com/blog/why-people-suck-a-study",
        "http://example.com/blog/how-to-lick-your-own-toes",
        "http://example.com/banner.jpg",
        "http://example.com/assets/background.jpg",
        "http://example.com/page/1/",
        "http://example.com/page/2/",
        "http://example.com/posts/a-brief-history-of-time",
        "http://example.com/?utm_source=google&utm_medium=cpc",
        "http://example.com/?ref=affiliate",
        "http://example.com/page.php?id=1&session_id=12345",
        "http://example.com/2021/08/01/article-title",
        "http://example.com/2021-08-01/article-title",
        "http://example.com/?sort=asc&order=desc",
        "http://example.com/?fbclid=XYZ123",
        "http://example.com/user/456/profile.html",
        "http://www.example.com/lang/en/page.php",
        "http://example.com/v1.0.0/resource",
        "http://example.com/user/123e4567-e89b-12d3-a456-426614174000/profile.html",
        "http://example.com/192.168.1.1/details",
        "http://example.com/user/email@example.com"
    ]

    result = decluster_urls(test_urls)
    print("去重后的URL列表:")
    for url in result:
        print(url)

if __name__ == "__main__":
    main()