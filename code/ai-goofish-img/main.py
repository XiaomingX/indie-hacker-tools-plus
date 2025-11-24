import argparse
import requests
import mimetypes
import os
import hashlib
import json
import logging
from datetime import datetime, timedelta
from PIL import Image
from PIL.Image import Resampling
import tempfile

# -------------------------- 核心配置 --------------------------
class Config:
    GOOFISH_UPLOAD_URL = "https://stream-upload.goofish.com/api/upload.api?_input_charset=utf-8&appkey=fleamarket"
    ALLOWED_TYPES = {
        "image/jpeg", "image/png", "image/gif", "image/webp", "image/jpg"
    }
    MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
    COMPRESS_THRESHOLD = 8 * 1024 * 1024  # 8MB（超过则压缩）
    CACHE_EXPIRE = 24 * 3600  # 缓存过期时间（24小时）
    DEFAULT_CACHE_DIR = "./cache"
    DEFAULT_LOG_FILE = "./logs/upload.log"
    DEFAULT_GALLERY_FILE = "./gallery.json"
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
    ERROR_MESSAGES = {
        "no_file": "未指定上传文件或文件不存在",
        "invalid_type": "不支持的文件类型，仅支持 JPG/PNG/GIF/WebP",
        "file_too_large": f"文件大小超过{MAX_FILE_SIZE//1024//1024}MB限制",
        "curl_error": "请求发送失败",
        "http_error": "HTTP请求错误",
        "parse_error": "响应解析失败",
        "api_error": "闲鱼API返回错误",
        "format_error": "响应格式异常",
        "pillow_error": "图片处理（压缩/转换）失败",
        "cache_error": "缓存操作失败"
    }

# -------------------------- 日志配置 --------------------------
def init_logging(log_file):
    """初始化日志系统"""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s: %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
    )
    return logging.getLogger(__name__)

# -------------------------- 文件验证 --------------------------
def validate_file(file_path):
    """验证文件是否合法（存在、类型、大小）"""
    # 检查文件是否存在
    if not os.path.exists(file_path):
        return False, Config.ERROR_MESSAGES["no_file"]
    
    # 检查文件大小
    file_size = os.path.getsize(file_path)
    if file_size > Config.MAX_FILE_SIZE:
        return False, Config.ERROR_MESSAGES["file_too_large"]
    
    # 检查文件类型（优先MIME，其次后缀）
    mime_type, _ = mimetypes.guess_type(file_path)
    if not mime_type:
        # 从后缀推测
        ext = os.path.splitext(file_path)[1].lower()
        mime_map = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".gif": "image/gif", ".webp": "image/webp"}
        mime_type = mime_map.get(ext)
    if not mime_type or mime_type not in Config.ALLOWED_TYPES:
        return False, Config.ERROR_MESSAGES["invalid_type"]
    
    return True, {"path": file_path, "size": file_size, "mime": mime_type}

# -------------------------- 图片处理（压缩/转换） --------------------------
def compress_image(file_path, max_size=Config.COMPRESS_THRESHOLD):
    """压缩图片到指定大小（优先降质量，再缩尺寸）"""
    try:
        with Image.open(file_path) as img:
            # 临时文件保存压缩结果
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file_path)[1])
            temp_path = temp_file.name
            temp_file.close()

            original_size = os.path.getsize(file_path)
            if original_size <= max_size:
                return True, {"path": file_path, "size": original_size, "original_size": original_size}

            # 初始参数
            quality = 85
            scale = 1.0
            attempts = 0
            max_attempts = 10

            while attempts < max_attempts and scale > 0.3:
                attempts += 1
                # 调整尺寸
                new_width = int(img.width * scale)
                new_height = int(img.height * scale)
                resized_img = img.resize((new_width, new_height), Resampling.LANCZOS)

                # 保存（根据格式调整参数）
                save_kwargs = {}
                if img.format in ["JPEG", "WEBP"]:
                    save_kwargs["quality"] = quality
                elif img.format == "PNG":
                    save_kwargs["compress_level"] = 9 - int(quality / 10)  # PNG压缩级别1-9

                resized_img.save(temp_path, img.format, **save_kwargs)
                compressed_size = os.path.getsize(temp_path)

                # 检查是否达标
                if compressed_size <= max_size:
                    return True, {
                        "path": temp_path, 
                        "size": compressed_size, 
                        "original_size": original_size
                    }

                # 调整参数
                if quality > 30:
                    quality -= 10
                else:
                    scale *= 0.9
                    quality = 85

            # 所有尝试失败
            os.unlink(temp_path)
            return False, Config.ERROR_MESSAGES["pillow_error"] + "（无法压缩到目标大小）"
    except Exception as e:
        return False, f"{Config.ERROR_MESSAGES['pillow_error']}: {str(e)}"

def convert_image_format(file_path, target_format):
    """转换图片格式（webp/avif）"""
    if target_format == "original":
        return True, {"path": file_path, "mime": mimetypes.guess_type(file_path)[0]}
    
    supported_formats = {"webp": "WEBP", "avif": "AVIF"}
    if target_format not in supported_formats:
        return False, "仅支持转换为webp或avif格式"
    
    try:
        with Image.open(file_path) as img:
            # 检查是否支持目标格式（AVIF需Pillow>=9.1.0且安装libavif）
            if supported_formats[target_format] not in img.supported_formats:
                return False, f"Pillow不支持{target_format}格式（需安装对应依赖）"
            
            # 临时文件
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f".{target_format}")
            temp_path = temp_file.name
            temp_file.close()

            # 保存（保持透明度）
            save_kwargs = {"quality": 85}
            if img.mode in ["RGBA", "P"] and target_format == "webp":
                save_kwargs["lossless"] = False  # 透明WebP支持
            elif img.mode in ["RGBA", "P"] and target_format == "avif":
                save_kwargs["lossless"] = False

            img.save(temp_path, supported_formats[target_format], **save_kwargs)
            new_mime = f"image/{target_format}"
            return True, {
                "path": temp_path, 
                "mime": new_mime, 
                "size": os.path.getsize(temp_path)
            }
    except Exception as e:
        return False, f"{Config.ERROR_MESSAGES['pillow_error']}: {str(e)}"

# -------------------------- 缓存管理 --------------------------
def get_file_hash(file_path):
    """计算文件MD5哈希（用于缓存key）"""
    try:
        with open(file_path, "rb") as f:
            md5 = hashlib.md5()
            while chunk := f.read(4096):
                md5.update(chunk)
        return md5.hexdigest()
    except Exception as e:
        return None

def get_cached_result(file_hash, cache_dir=Config.DEFAULT_CACHE_DIR):
    """获取缓存结果（若存在且未过期）"""
    if not file_hash:
        return None
    cache_file = os.path.join(cache_dir, f"{file_hash}.json")
    if not os.path.exists(cache_file):
        return None
    
    # 检查过期时间
    try:
        with open(cache_file, "r", encoding="utf-8") as f:
            cache_data = json.load(f)
        cache_time = cache_data.get("timestamp", 0)
        if datetime.now().timestamp() - cache_time > Config.CACHE_EXPIRE:
            os.unlink(cache_file)  # 删除过期缓存
            return None
        return cache_data.get("data")
    except Exception as e:
        logging.warning(f"缓存读取失败: {str(e)}")
        return None

def save_cached_result(file_hash, data, cache_dir=Config.DEFAULT_CACHE_DIR):
    """保存结果到缓存"""
    if not file_hash or not data:
        return False
    try:
        os.makedirs(cache_dir, exist_ok=True)
        cache_file = os.path.join(cache_dir, f"{file_hash}.json")
        cache_data = {
            "timestamp": datetime.now().timestamp(),
            "data": data
        }
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(cache_data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        logging.error(f"{Config.ERROR_MESSAGES['cache_error']}: {str(e)}")
        return False

# -------------------------- 闲鱼API上传 --------------------------
def upload_to_xianyu(file_info, cookie2, category="未分类"):
    """上传文件到闲鱼API"""
    file_path = file_info["path"]
    mime_type = file_info["mime"]
    file_name = os.path.basename(file_path)

    # 构造请求头
    headers = {
        "User-Agent": Config.USER_AGENT,
        "Referer": "https://author.goofish.com/",
        "Origin": "https://author.goofish.com",
        "Cookie": f"cookie2={cookie2}",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
    }

    # 构造表单数据
    with open(file_path, "rb") as f:
        files = {"file": (file_name, f, mime_type)}
        try:
            response = requests.post(
                Config.GOOFISH_UPLOAD_URL,
                headers=headers,
                files=files,
                timeout=30,
                verify=False  # 忽略SSL验证（根据需要调整）
            )
            response.raise_for_status()  # 触发HTTP错误
        except requests.exceptions.RequestException as e:
            return False, f"{Config.ERROR_MESSAGES['curl_error']}: {str(e)}"
        except Exception as e:
            return False, f"{Config.ERROR_MESSAGES['http_error']}: {str(e)}"

    # 解析响应
    try:
        resp_data = response.json()
    except json.JSONDecodeError:
        return False, f"{Config.ERROR_MESSAGES['parse_error']}: {response.text[:500]}"

    # 检查API响应状态
    if not resp_data.get("success"):
        return False, f"{Config.ERROR_MESSAGES['api_error']}: {json.dumps(resp_data, ensure_ascii=False)}"
    
    # 提取结果
    resp_object = resp_data.get("object", {})
    if not resp_object.get("url"):
        return False, f"{Config.ERROR_MESSAGES['format_error']}: {json.dumps(resp_data, ensure_ascii=False)}"

    # 格式化返回数据
    result_data = {
        "url": resp_object["url"],
        "fileName": resp_object.get("fileName", os.path.splitext(file_name)[0]),
        "size": format_file_size(resp_object.get("size", file_info["size"])),
        "pix": resp_object.get("pix", "未知"),
        "fileId": resp_object.get("fileId", ""),
        "quality": resp_object.get("quality", 100),
        "category": category,
        "uploadTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return True, result_data

# -------------------------- 辅助函数 --------------------------
def format_file_size(size):
    """格式化文件大小（B/KB/MB/GB）"""
    size = int(size)
    if size < 1024:
        return f"{size} B"
    elif size < 1024 * 1024:
        return f"{round(size / 1024, 2)} KB"
    elif size < 1024 * 1024 * 1024:
        return f"{round(size / (1024 * 1024), 2)} MB"
    else:
        return f"{round(size / (1024 * 1024 * 1024), 2)} GB"

def update_gallery(result_data, gallery_file=Config.DEFAULT_GALLERY_FILE):
    """更新画廊JSON文件（记录上传历史）"""
    try:
        # 读取现有数据
        gallery_data = []
        if os.path.exists(gallery_file):
            with open(gallery_file, "r", encoding="utf-8") as f:
                gallery_data = json.load(f) or []
        
        # 添加新记录（去重：按fileId）
        new_record = {
            "id": hashlib.md5(result_data["url"].encode()).hexdigest()[:16],
            **result_data
        }
        gallery_data = [item for item in gallery_data if item.get("fileId") != new_record["fileId"]] + [new_record]
        
        # 限制记录数（最多1000条）
        if len(gallery_data) > 1000:
            gallery_data = gallery_data[-1000:]
        
        # 保存
        with open(gallery_file, "w", encoding="utf-8") as f:
            json.dump(gallery_data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        logging.error(f"画廊更新失败: {str(e)}")
        return False

# -------------------------- CLI入口 --------------------------
def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="闲鱼图床CLI上传工具")
    parser.add_argument("files", nargs="+", help="待上传的图片文件路径（支持多个）")
    parser.add_argument("--cookie2", required=True, help="闲鱼cookie2值（从https://author.goofish.com/#/获取）")
    parser.add_argument("--category", default="未分类", help="图片分类（默认：未分类）")
    parser.add_argument("--format", choices=["original", "webp", "avif"], default="original", help="图片格式转换（默认：保持原格式）")
    parser.add_argument("--enable-cache", action="store_true", help="启用缓存（避免重复上传相同文件）")
    parser.add_argument("--log-file", default=Config.DEFAULT_LOG_FILE, help="日志文件路径（默认：./logs/upload.log）")
    parser.add_argument("--cache-dir", default=Config.DEFAULT_CACHE_DIR, help="缓存目录（默认：./cache）")
    args = parser.parse_args()

    # 初始化日志
    logger = init_logging(args.log_file)
    logger.info("=== 启动闲鱼图床CLI上传工具 ===")

    # 遍历处理每个文件
    total = len(args.files)
    success_count = 0
    for idx, file_path in enumerate(args.files, 1):
        logger.info(f"正在处理文件 {idx}/{total}: {file_path}")
        
        # 1. 文件验证
        valid, res = validate_file(file_path)
        if not valid:
            logger.error(f"文件验证失败: {res}")
            continue
        file_info = res
        logger.debug(f"文件信息: {json.dumps(file_info, ensure_ascii=False)}")

        # 2. 检查缓存（若启用）
        cached_data = None
        if args.enable_cache:
            file_hash = get_file_hash(file_path)
            cached_data = get_cached_result(file_hash, args.cache_dir)
            if cached_data:
                logger.info(f"命中缓存，跳过上传: {cached_data['url']}")
                # 更新画廊（若分类变化）
                if cached_data.get("category") != args.category:
                    cached_data["category"] = args.category
                    update_gallery(cached_data)
                success_count += 1
                print(f"✅ 成功（缓存）: {os.path.basename(file_path)} -> {cached_data['url']}")
                continue

        # 3. 图片压缩（超过阈值）
        if file_info["size"] > Config.COMPRESS_THRESHOLD:
            logger.info(f"文件超过{Config.COMPRESS_THRESHOLD//1024//1024}MB，开始压缩")
            compress_ok, compress_res = compress_image(file_path)
            if not compress_ok:
                logger.error(f"压缩失败: {compress_res}")
                continue
            # 更新文件信息为压缩后的数据
            file_info["path"] = compress_res["path"]
            file_info["size"] = compress_res["size"]
            logger.info(f"压缩完成: 原大小{format_file_size(compress_res['original_size'])} -> 新大小{format_file_size(compress_res['size'])}")

        # 4. 格式转换（若指定）
        if args.format != "original":
            logger.info(f"开始转换格式为: {args.format}")
            convert_ok, convert_res = convert_image_format(file_info["path"], args.format)
            if not convert_ok:
                logger.error(f"格式转换失败: {convert_res}")
                # 清理压缩临时文件（若有）
                if "original_size" in locals():
                    os.unlink(file_info["path"])
                continue
            # 更新文件信息为转换后的数据
            file_info["path"] = convert_res["path"]
            file_info["mime"] = convert_res["mime"]
            file_info["size"] = convert_res["size"]
            logger.info(f"格式转换完成: {args.format}，大小{format_file_size(file_info['size'])}")

        # 5. 上传到闲鱼API
        upload_ok, upload_res = upload_to_xianyu(file_info, args.cookie2, args.category)
        # 清理临时文件（压缩/转换产生的）
        if "compress_res" in locals() and compress_res["path"] != file_path:
            os.unlink(compress_res["path"])
        if "convert_res" in locals() and convert_res["path"] != file_info["path"]:
            os.unlink(convert_res["path"])
        
        if not upload_ok:
            logger.error(f"上传失败: {upload_res}")
            continue

        # 6. 保存缓存（若启用）
        if args.enable_cache:
            file_hash = get_file_hash(file_path)
            save_ok = save_cached_result(file_hash, upload_res, args.cache_dir)
            if save_ok:
                logger.info("缓存已保存")
            else:
                logger.warning("缓存保存失败")

        # 7. 更新画廊
        update_gallery(upload_res)

        # 8. 统计与输出
        success_count += 1
        logger.info(f"上传成功: {json.dumps(upload_res, ensure_ascii=False)}")
        print(f"✅ 成功: {os.path.basename(file_path)} -> {upload_res['url']}")

    # 最终统计
    logger.info(f"=== 上传完成 ===")
    logger.info(f"总计: {total} 个文件，成功: {success_count} 个，失败: {total - success_count} 个")
    print(f"\n=== 上传结果 ===")
    print(f"总计: {total} 个文件")
    print(f"成功: {success_count} 个")
    print(f"失败: {total - success_count} 个")
    print(f"画廊文件: {Config.DEFAULT_GALLERY_FILE}")
    print(f"日志文件: {args.log_file}")

if __name__ == "__main__":
    main()