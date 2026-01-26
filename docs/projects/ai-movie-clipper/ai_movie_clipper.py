import os
import json
import logging
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import click
from moviepy import (
    VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip,
    CompositeAudioClip, concatenate_videoclips, ColorClip
)
from moviepy.video.fx import resize, fadein, fadeout, rotate
from moviepy.audio.fx import audio_fadein, audio_fadeout, volumex


# 基础配置
DEFAULT_RESOLUTION = (1920, 1080)
DEFAULT_FPS = 30
RESOURCE_DIR = Path("./resources")
OUTPUT_DIR = Path("./output")

# 确保输出目录存在
OUTPUT_DIR.mkdir(exist_ok=True)
RESOURCE_DIR.mkdir(exist_ok=True)


# 日志配置
def setup_logger():
    logger = logging.getLogger("VideoEditor")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()


# 自然语言解析器
class NLProcessor:
    @staticmethod
    def parse_description(text: str) -> Dict:
        """将自然语言描述转换为时间轴配置"""
        # 解析时长
        duration = NLProcessor._parse_duration(text)
        
        # 解析片段
        segments = NLProcessor._parse_segments(text, duration)
        
        # 解析特效
        effects = NLProcessor._parse_effects(text)
        
        return {
            "duration": duration,
            "segments": segments,
            "effects": effects,
            "title": NLProcessor._parse_title(text)
        }
    
    @staticmethod
    def _parse_duration(text: str) -> float:
        """提取视频总时长（秒）"""
        patterns = [
            (r'(\d+)秒', lambda x: float(x)),
            (r'(\d+)分钟', lambda x: float(x) * 60),
            (r'(\d+)分(\d+)秒', lambda x, y: float(x)*60 + float(y))
        ]
        
        for pattern, converter in patterns:
            match = re.search(pattern, text)
            if match:
                return converter(*match.groups())
        return 30  # 默认30秒
    
    @staticmethod
    def _parse_segments(text: str, total_duration: float) -> List[Dict]:
        """分割文本为视频片段"""
        sentences = re.split(r'[。；,.]', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        
        if not sentences:
            return [{"start": 0, "end": total_duration, "text": "默认片段"}]
        
        # 平均分配时长
        segment_duration = total_duration / len(sentences)
        segments = []
        
        for i, sent in enumerate(sentences):
            start = i * segment_duration
            end = min((i+1) * segment_duration, total_duration)
            segments.append({
                "start": start,
                "end": end,
                "text": sent,
                "has_subtitle": "字幕" in sent or "文字" in sent
            })
        
        return segments
    
    @staticmethod
    def _parse_effects(text: str) -> List[str]:
        """提取特效关键词"""
        effects = []
        effect_map = {
            "转场": "fade",
            "淡入": "fade_in",
            "淡出": "fade_out",
            "缩放": "zoom",
            "旋转": "rotate",
            "音乐": "bgm"
        }
        
        for keyword, effect in effect_map.items():
            if keyword in text and effect not in effects:
                effects.append(effect)
        
        return effects
    
    @staticmethod
    def _parse_title(text: str) -> str:
        """提取视频标题"""
        title = text.split('。')[0][:30]
        return title if title else "AI生成视频"


# 视频编辑器
class VideoEditor:
    def __init__(self, resource_dir: Path = RESOURCE_DIR):
        self.resource_dir = resource_dir
        self.effects = {
            "fade_in": self._apply_fade_in,
            "fade_out": self._apply_fade_out,
            "zoom": self._apply_zoom,
            "rotate": self._apply_rotate
        }
    
    def create_video(self, timeline: Dict, output_path: str) -> bool:
        """根据时间轴创建视频"""
        try:
            # 1. 准备视频片段
            video_clips = self._prepare_video_clips(timeline)
            
            # 2. 准备文字片段
            text_clips = self._prepare_text_clips(timeline)
            
            # 3. 准备音频片段
            audio_clips = self._prepare_audio_clips(timeline)
            
            # 4. 合成视频
            final_clip = self._composite_clip(
                video_clips, text_clips, audio_clips, timeline["duration"]
            )
            
            # 5. 输出视频
            final_clip.write_videofile(
                output_path,
                fps=DEFAULT_FPS,
                codec='libx264',
                audio_codec='aac'
            )
            
            # 清理资源
            final_clip.close()
            logger.info(f"视频已保存至: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"视频创建失败: {str(e)}")
            return False
    
    def _prepare_video_clips(self, timeline: Dict) -> List:
        """准备视频片段"""
        clips = []
        segments = timeline["segments"]
        effects = timeline["effects"]
        
        # 尝试获取资源目录中的第一个视频，若无则创建纯色背景
        video_files = list(self.resource_dir.glob("*.mp4")) + list(self.resource_dir.glob("*.mov"))
        has_video = len(video_files) > 0
        
        for i, seg in enumerate(segments):
            # 创建基础片段
            if has_video and i == 0:  # 第一个片段使用实际视频
                clip = VideoFileClip(str(video_files[0]))
                # 裁剪到片段时长
                clip = clip.subclip(0, min(seg["end"] - seg["start"], clip.duration))
            else:  # 其他片段使用纯色背景
                clip = ColorClip(
                    size=DEFAULT_RESOLUTION,
                    color=(30, 30, 40) if i % 2 == 0 else (40, 30, 30),
                    duration=seg["end"] - seg["start"]
                )
            
            # 调整大小
            clip = resize(clip, DEFAULT_RESOLUTION)
            
            # 应用特效
            for effect in effects:
                if effect in self.effects:
                    clip = self.effects[effect](clip)
            
            # 设置片段开始时间
            clip = clip.set_start(seg["start"])
            clips.append(clip)
        
        return clips
    
    def _prepare_text_clips(self, timeline: Dict) -> List:
        """准备文字片段"""
        clips = []
        for seg in timeline["segments"]:
            if seg.get("has_subtitle") or "字幕" in timeline["effects"]:
                try:
                    # 创建文字片段
                    text_clip = TextClip(
                        seg["text"],
                        fontsize=40,
                        color='white',
                        bg_color='black',
                        size=(DEFAULT_RESOLUTION[0] * 0.8, None),
                        method='caption'
                    )
                    
                    # 设置位置和时间
                    text_clip = text_clip.set_position(('center', 'bottom'))
                    text_clip = text_clip.set_start(seg["start"])
                    text_clip = text_clip.set_duration(seg["end"] - seg["start"])
                    clips.append(text_clip)
                except Exception as e:
                    logger.warning(f"创建文字片段失败: {str(e)}")
        
        return clips
    
    def _prepare_audio_clips(self, timeline: Dict) -> List:
        """准备音频片段"""
        clips = []
        if "bgm" in timeline["effects"]:
            # 尝试加载背景音乐
            audio_files = list(self.resource_dir.glob("*.mp3")) + list(self.resource_dir.glob("*.wav"))
            if audio_files:
                audio = AudioFileClip(str(audio_files[0]))
                # 调整音量并循环
                audio = volumex(audio, 0.3)
                audio = audio.loop(duration=timeline["duration"])
                # 淡入淡出
                audio = audio_fadein(audio, 1.0)
                audio = audio_fadeout(audio, 1.0)
                clips.append(audio)
        
        return clips
    
    def _composite_clip(self, video_clips, text_clips, audio_clips, duration) -> CompositeVideoClip:
        """合成最终视频"""
        # 合并所有视频和文字片段
        all_clips = video_clips + text_clips
        
        # 创建主视频
        final_clip = CompositeVideoClip(all_clips, size=DEFAULT_RESOLUTION)
        final_clip = final_clip.set_duration(duration)
        
        # 添加音频
        if audio_clips:
            final_audio = CompositeAudioClip(audio_clips)
            final_clip = final_clip.set_audio(final_audio)
        
        return final_clip
    
    # 特效实现
    def _apply_fade_in(self, clip):
        return fadein(clip, duration=0.5)
    
    def _apply_fade_out(self, clip):
        return fadeout(clip, duration=0.5)
    
    def _apply_zoom(self, clip):
        def zoom_effect(get_frame, t):
            frame = get_frame(t)
            w, h = frame.shape[1], frame.shape[0]
            scale = 1 + 0.1 * (t / clip.duration)  # 缓慢放大
            new_w, new_h = int(w * scale), int(h * scale)
            frame = resize(frame, (new_w, new_h))
            return frame[int((new_h-h)/2):int((new_h+h)/2), 
                         int((new_w-w)/2):int((new_w+w)/2)]
        
        return clip.fl(zoom_effect)
    
    def _apply_rotate(self, clip):
        return rotate(clip, lambda t: 10 * t, resample='bilinear')


# 命令行接口
@click.group()
def cli():
    """简易AI视频剪辑工具"""
    pass


@cli.command()
@click.option('--text', '-t', help='自然语言描述')
@click.option('--output', '-o', default=str(OUTPUT_DIR / "output.mp4"), help='输出视频路径')
def create(text, output):
    """从自然语言描述创建视频"""
    if not text:
        click.echo("请使用--text提供视频描述")
        return
    
    # 1. 解析自然语言
    logger.info("解析自然语言描述...")
    timeline = NLProcessor.parse_description(text)
    logger.info(f"生成时间轴: 时长{timeline['duration']}秒, {len(timeline['segments'])}个片段")
    
    # 2. 保存时间轴（可选）
    timeline_path = OUTPUT_DIR / "timeline.json"
    with open(timeline_path, 'w', encoding='utf-8') as f:
        json.dump(timeline, f, ensure_ascii=False, indent=2)
    logger.info(f"时间轴已保存至: {timeline_path}")
    
    # 3. 创建视频
    logger.info("开始创建视频...")
    editor = VideoEditor()
    success = editor.create_video(timeline, output)
    
    if success:
        click.echo(f"✅ 视频创建成功: {output}")
    else:
        click.echo("❌ 视频创建失败")


@cli.command()
@click.option('--timeline', '-t', default=str(OUTPUT_DIR / "timeline.json"), help='时间轴JSON文件')
@click.option('--output', '-o', default=str(OUTPUT_DIR / "output.mp4"), help='输出视频路径')
def edit(timeline, output):
    """从时间轴文件创建视频"""
    if not os.path.exists(timeline):
        click.echo(f"时间轴文件不存在: {timeline}")
        return
    
    # 加载时间轴
    with open(timeline, 'r', encoding='utf-8') as f:
        timeline_data = json.load(f)
    
    # 创建视频
    editor = VideoEditor()
    success = editor.create_video(timeline_data, output)
    
    if success:
        click.echo(f"✅ 视频创建成功: {output}")
    else:
        click.echo("❌ 视频创建失败")


@cli.command()
def example():
    """显示使用示例"""
    examples = """
使用示例:
1. 从自然语言创建视频:
   python video_editor.py create -t "制作一个30秒的视频，包含3个片段，每个片段显示文字，添加淡入淡出和背景音乐"

2. 从时间轴文件创建视频:
   python video_editor.py edit -t output/timeline.json -o my_video.mp4

提示:
- 把视频素材放在resources目录下会被自动使用
- 把音频文件放在resources目录下可作为背景音乐
- 描述中可包含"转场"、"字幕"、"音乐"等关键词
    """
    click.echo(examples)


if __name__ == "__main__":
    cli()