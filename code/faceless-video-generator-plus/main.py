import os
import re
import json
import time
import requests
import replicate
import fal_client
from dotenv import load_dotenv
from openai import OpenAI
from typing import Optional, Dict, List, Callable, Tuple
from moviepy.editor import (
    ImageClip, CompositeVideoClip, concatenate_videoclips, AudioFileClip
)
from PIL import Image
import numpy as np
import cv2
import shortcap

# 加载环境变量与配置
load_dotenv()

def load_config(config_file='config.json'):
    """加载配置文件"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(os.path.dirname(script_dir), config_file)
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

config = load_config()

# 初始化OpenAI客户端
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)

# 全局常量
STORY_TYPES = [
    "Scary", "Mystery", "Bedtime", "Interesting History", "Urban Legends",
    "Motivational", "Fun Facts", "Long Form Jokes", "Life Pro Tips", "Philosophy", "Love"
]
STORY_TYPE_HASHTAGS = {
    "Scary": "#scary", "Mystery": "#mystery", "Bedtime": "#bedtime",
    "Interesting History": "#history", "Urban Legends": "#urbanlegends",
    "Motivational": "#motivation", "Fun Facts": "#funfacts",
    "Long Form Jokes": "#joke", "Life Pro Tips": "#lifeprotips",
    "Philosophy": "#philosophy", "Love": "#love"
}
FONT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../font/TitanOne.ttf")


# 工具辅助函数
def create_resource_dir(script_dir: str, story_type: str, title: str) -> str:
    """创建故事资源目录"""
    clean_title = re.sub(r'[^\w\s-]', '', title.strip().strip('"'))
    clean_title = re.sub(r'[-\s]+', '_', clean_title)
    
    data_dir = os.path.join(os.path.dirname(script_dir), "data")
    story_dir = os.path.join(data_dir, story_type, clean_title)
    os.makedirs(story_dir, exist_ok=True)
    return story_dir

def call_openai_api(messages: List[Dict], max_retries: int = 3) -> Optional[str]:
    """统一调用OpenAI API"""
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=config['openai']['model'],
                temperature=config['openai']['temperature'],
                messages=messages
            )
            return response.choices[0].message.content
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"OpenAI API重试({attempt+1}/{max_retries})：{e}")
                time.sleep(1)
            else:
                print(f"OpenAI API失败：{e}")
    return None

def pick_option(options: List[str], prompt: str) -> str:
    """通用选择函数"""
    print(f"\n{prompt}：")
    for i, opt in enumerate(options, 1):
        print(f"{i}. {opt}")
    while True:
        try:
            choice = int(input("请输入序号："))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            print("序号超出范围，请重试")
        except ValueError:
            print("输入不是数字，请重试")

def create_blank_image(filename: str, width: int = 720, height: int = 1280) -> None:
    """生成空白图片"""
    blank_img = Image.new('RGB', (width, height), color='black')
    blank_img.save(filename)
    print(f"生成空白图片：{filename}")

def extract_and_parse_json(response: str) -> Dict:
    """提取并解析响应中的JSON"""
    cleaned = response.strip().strip("`").strip()
    if cleaned.startswith("json"):
        cleaned = cleaned[4:].strip()
    
    json_match = re.search(r"\{.*\}", cleaned, re.DOTALL)
    if not json_match:
        print("响应中未找到JSON")
        return {}
    
    try:
        return json.loads(json_match.group())
    except json.JSONDecodeError as e:
        print(f"JSON解析失败：{e}")
        return {}


# 核心生成函数
def get_story_type_guidelines(story_type: str) -> str:
    """获取故事类型专属规则"""
    guidelines = {
        "philosophy": "1. 含核心哲学问题；2. 角色体现不同观点；3. 开放式结尾引发思考",
        "life pro tips": "1. 日常可落地；2. 步骤清晰；3. 说明好处与示例",
        "fun facts": "1. 有惊喜感；2. 关联生活；3. 解释背景",
        "long form jokes": "1. 完整叙事；2. 角色鲜明；3. 反转笑点",
        "bedtime": "1. 主角亲切；2. 情节温和；3. 语言舒缓"
    }
    return guidelines.get(story_type.lower(), f"1. 主角明确；2. 场景生动；3. 符合{story_type}风格")

def generate_story_and_title(story_type: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """生成故事标题、描述、内容"""
    char_limit = (config['story_generation']['char_limit_min'], config['story_generation']['char_limit_max'])
    prompt = f"""生成{story_type}类内容，格式：
    标题：[吸引眼球的标题]
    描述：[100-150字概述，含2-3个标签+#facelessvideos.app]
    内容：[符合{char_limit[0]}-{char_limit[1]}字符，遵循规则：{get_story_type_guidelines(story_type)}]"""

    messages = [
        {"role": "system", "content": "你是专业内容创作者，擅长各类故事生成，严格按格式输出"},
        {"role": "user", "content": prompt}
    ]

    response = call_openai_api(messages)
    if not response:
        return None, None, None
    
    parts = response.split("\n\n", 2)
    if len(parts) != 3:
        return None, None, None
    
    title = parts[0].replace("标题：", "").strip()
    description = parts[1].replace("描述：", "").strip()
    content = parts[2].replace("内容：", "").strip()
    
    first_tag = STORY_TYPE_HASHTAGS[story_type]
    if "#" not in description:
        description += f" {first_tag} #facelessvideos.app"
    return title, description, content

def generate_characters(story: str) -> Optional[List[Dict]]:
    """生成角色信息"""
    prompt = f"""基于故事生成角色列表（JSON格式），含name/ethnicity/gender/age/facial_features/body_type/hair_style/accessories：
    故事：{story}
    输出仅保留JSON数组，无其他文字"""

    messages = [
        {"role": "system", "content": "你是角色设计师，擅长从故事提取角色外貌特征"},
        {"role": "user", "content": prompt}
    ]

    response = call_openai_api(messages)
    if not response:
        return None
    
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        array_match = re.search(r'\[.*\]', response, re.DOTALL)
        return json.loads(array_match.group()) if array_match else None

def generate_storyboard(title: str, story: str, story_type: str, character_names: List[str] = None) -> Dict:
    """生成分镜"""
    max_scenes = config['storyboard']['max_scenes']
    prompt = f"""生成{story_type}分镜（JSON格式），最多{max_scenes}个场景：
    标题：{title}
    角色：{character_names if character_names else '无'}
    故事：{story}
    每个场景含：scene_number（序号）、description（60-70字视觉描述）、subtitles（故事原句）、transition_type（zoom-in/zoom-out）
    输出仅保留JSON，结构：{{"project_info":{{"title":"","timestamp":""}},"storyboards":[]}}"""

    messages = [
        {"role": "system", "content": "你是分镜师，擅长将文字转化为视觉场景，严格按格式输出JSON"},
        {"role": "user", "content": prompt}
    ]

    response = call_openai_api(messages)
    return extract_and_parse_json(response) if response else {"project_info": {"title": title, "timestamp": time.ctime()}, "storyboards": []}

def generate_image(prompt: str, generator_type: str = "replicate", max_retries: int = 3) -> Optional[bytes]:
    """生成图片（支持replicate/fal）"""
    gen_config = config[f"{generator_type}_flux_api"]
    for attempt in range(max_retries):
        try:
            if generator_type == "replicate":
                image_urls = replicate.run(gen_config["model"], input={
                    "prompt": prompt,
                    "aspect_ratio": gen_config["aspect_ratio"],
                    "num_inference_steps": gen_config["num_inference_steps"],
                    "disable_safety_checker": gen_config["disable_safety_checker"]
                })
                image_url = image_urls[0] if image_urls else None
            else:
                handler = fal_client.submit(gen_config["model"], arguments={
                    "prompt": prompt,
                    "image_size": gen_config["image_size"],
                    "num_images": gen_config["num_images"]
                })
                result = handler.get()
                image_url = result["images"][0]["url"] if result and "images" in result else None
            
            if not image_url:
                raise ValueError(f"{generator_type}未返回图片URL")
            
            resp = requests.get(image_url)
            resp.raise_for_status()
            return resp.content
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"{generator_type}图片生成重试({attempt+1}/{max_retries})：{e}")
                time.sleep(1)
            else:
                print(f"{generator_type}图片生成失败：{e}")
    return None

def generate_and_download_images(
    storyboard_project: Dict, story_dir: str, image_style: str, generator_func: Callable
) -> List[str]:
    """生成并保存所有场景图片"""
    image_files = []
    characters = storyboard_project.get("characters", [])
    start_time = time.time()

    for scene in storyboard_project["storyboards"]:
        prompt = scene["description"] + f" | {image_style}"
        if characters:
            char_desc = " | ".join([f"{c['name']}: {c['ethnicity']} {c['age']} {c['facial_features']} {c['hair_style']}" for c in characters])
            prompt += " | " + char_desc
        prompt = re.sub(r'\{\{.*?\}\}', '', prompt)

        img_content = generator_func(prompt)
        img_path = os.path.join(story_dir, f"scene_{scene['scene_number']}.png")
        
        if img_content:
            with open(img_path, 'wb') as f:
                f.write(img_content)
            print(f"场景{scene['scene_number']}图片保存：{img_path}")
        else:
            create_blank_image(img_path)
            print(f"场景{scene['scene_number']}图片生成失败，用空白图替代")
        
        image_files.append(img_path)
        scene["image"] = img_path

    print(f"图片生成耗时：{time.time() - start_time:.2f}秒")
    return image_files

def generate_audio(text: str, output_path: str, voice_name: str = "alloy") -> bool:
    """生成音频（TTS）"""
    try:
        speech_rate = config['tts']['speech_rate']
        result = client.audio.speech.create(
            model="tts-1", voice=voice_name, input=text, speed=speech_rate, response_format="mp3"
        )
        with open(output_path, "wb") as f:
            f.write(result.content)
        print(f"音频保存：{output_path}")
        return True
    except Exception as e:
        print(f"音频生成失败：{e}")
        return False

def zoom_transition(clip, mode: str = "in") -> ImageClip:
    """缩放转场效果"""
    fps = clip.fps if hasattr(clip, "fps") else 24
    duration = clip.duration
    total_frames = max(1, int(duration * fps))

    def apply_zoom(get_frame, t):
        frame = get_frame(t)
        h, w = frame.shape[:2]
        frame_idx = t * fps if mode == "in" else total_frames - (t * fps)
        zoom_ratio = 1 + (frame_idx * 0.3 / total_frames)
        
        tx = (w - (w / zoom_ratio)) / 2
        ty = (h - (h / zoom_ratio)) / 2
        M = np.array([[zoom_ratio, 0, -tx * zoom_ratio], [0, zoom_ratio, -ty * zoom_ratio]])
        return cv2.warpAffine(frame, M, (w, h))

    return clip.fl(apply_zoom)

def create_video(storyboard_project: Dict, story_dir: str, voice_name: str) -> Optional[str]:
    """生成带字幕的视频"""
    video_path = os.path.join(story_dir, "story_video.mp4")
    audio_dir = os.path.join(story_dir, "audio")
    os.makedirs(audio_dir, exist_ok=True)
    
    clips = []
    for scene in storyboard_project["storyboards"]:
        audio_path = os.path.join(audio_dir, f"scene_{scene['scene_number']}.mp3")
        if not generate_audio(scene["subtitles"], audio_path, voice_name):
            continue
        
        img_clip = ImageClip(scene["image"]).set_duration(AudioFileClip(audio_path).duration)
        img_clip = zoom_transition(img_clip, mode="in" if scene["transition_type"] == "zoom-in" else "out")
        img_clip = img_clip.set_audio(AudioFileClip(audio_path))
        clips.append(img_clip)
    
    if not clips:
        print("无有效片段，无法生成视频")
        return None
    
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(video_path, fps=24)
    print(f"基础视频生成完成：{video_path}")
    
    subtitle_video_path = video_path.replace(".mp4", "_with_subtitles.mp4")
    shortcap.add_captions(
        video_file=video_path,
        output_file=subtitle_video_path,
        font=FONT_PATH,
        font_size=70,
        font_color="white",
        stroke_width=3,
        stroke_color="black",
        highlight_current_word=True,
        word_highlight_color="yellow",
        line_count=1,
        padding=70,
        position="center"
    )
    print(f"带字幕视频生成完成：{subtitle_video_path}")
    return subtitle_video_path


# 主流程
def main():
    """端到端视频生成流程"""
    # 1. 选择参数
    story_type = pick_option(STORY_TYPES, "选择故事类型")
    image_style = pick_option(["photorealistic", "cinematic", "anime", "comic-book", "pixar-art"], "选择图片风格")
    voice_name = pick_option(["alloy", "echo", "fable", "onyx", "nova", "shimmer"], "选择配音风格")
    image_generator = lambda prompt: generate_image(prompt, generator_type="replicate")

    # 2. 生成故事
    print("\n1/5：生成故事与标题...")
    title, description, story = generate_story_and_title(story_type)
    if not all([title, description, story]):
        print("故事生成失败，退出")
        return

    # 3. 创建目录
    print("2/5：创建资源目录...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    story_dir = create_resource_dir(script_dir, story_type, title)
    with open(os.path.join(story_dir, "story_english.txt"), "w", encoding="utf-8") as f:
        f.write(f"{title}\n\n{description}\n\n{story}")

    # 4. 生成角色
    print("3/5：生成角色...")
    characters = []
    if story_type.lower() not in ["life pro tips", "fun facts"]:
        characters = generate_characters(story) or []
    character_names = [c["name"] for c in characters] if characters else []

    # 5. 生成分镜
    print("4/5：生成分镜...")
    storyboard_project = generate_storyboard(title, story, story_type, character_names)
    storyboard_project["characters"] = characters
    if not storyboard_project["storyboards"]:
        print("分镜生成失败，退出")
        return

    # 6. 生成图片
    print("5/5：生成图片与视频...")
    image_files = generate_and_download_images(storyboard_project, story_dir, image_style, image_generator)
    if not image_files:
        print("图片生成失败，退出")
        return

    # 7. 保存分镜配置
    with open(os.path.join(story_dir, "storyboard_project.json"), "w", encoding="utf-8") as f:
        json.dump(storyboard_project, f, ensure_ascii=False, indent=2)

    # 8. 生成视频
    final_video_path = create_video(storyboard_project, story_dir, voice_name)
    if final_video_path:
        print(f"\n全部流程完成！最终视频：{final_video_path}")

def test_single_module():
    """测试单个模块（示例：图片生成）"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = create_resource_dir(script_dir, "Test", "Test_Scene")
    img_content = generate_image("a cute cat, pixar style", generator_type="replicate")
    if img_content:
        with open(os.path.join(test_dir, "test_cat.png"), "wb") as f:
            f.write(img_content)
        print(f"测试图片保存：{os.path.join(test_dir, 'test_cat.png')}")

if __name__ == "__main__":
    main()
    # test_single_module()  # 如需测试单个模块，注释上面的main()并取消此行注释