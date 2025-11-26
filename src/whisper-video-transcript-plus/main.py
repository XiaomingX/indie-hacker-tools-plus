import logging
import math
import os
import shutil
import subprocess
import cv2
import numpy as np
import pandas as pd
import pickle
from faster_whisper import WhisperModel
from moviepy.editor import (
    TextClip, VideoFileClip, CompositeVideoClip, 
    AudioFileClip, concatenate_videoclips
)
from moviepy.video.tools.subtitles import SubtitlesClip
from googletrans import Translator

# 配置FFmpeg和ImageMagick路径（根据你的环境修改）
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"
os.environ["IMAGEMAGICK_BINARY"] = "/opt/homebrew/bin/convert"

# 日志配置
logging.basicConfig(level=logging.INFO)
logging.getLogger("faster_whisper").setLevel(logging.DEBUG)


# 通用工具函数
def download_video(url: str, save_name: str, res: str = "720") -> None:
    """从URL下载视频（依赖yt-dlp）"""
    command = [
        "yt-dlp",
        "-S", f"res:{res}",  # 选择分辨率
        "-o", save_name,     # 保存文件名
        url
    ]
    subprocess.run(command, check=True)
    logging.info(f"视频已下载：{save_name}")


def get_video_info(video_path: str) -> tuple[float, tuple[int, int]]:
    """获取视频时长（秒）和分辨率（宽,高）"""
    with VideoFileClip(video_path) as clip:
        duration = clip.duration
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"无法打开视频文件：{video_path}")
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    return duration, (width, height)


def split_video(input_path: str, split_duration: int = 600) -> list[str]:
    """分割长视频（默认每段10分钟），返回分割后的视频路径列表"""
    total_duration, _ = get_video_info(input_path)
    num_splits = math.ceil(total_duration / split_duration)
    base_path = input_path[:-4]  # 去除.mp4后缀
    split_paths = []

    for i in range(num_splits):
        start = i * split_duration
        end = min((i + 1) * split_duration, total_duration)
        output_path = f"{base_path}_part_{i+1}.mp4"
        with VideoFileClip(input_path).subclip(start, end) as clip:
            clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
        split_paths.append(output_path)
        logging.info(f"分割视频：{output_path}（{start:.1f}s - {end:.1f}s）")
    return split_paths


def merge_videos(input_paths: list[str], output_path: str) -> None:
    """合并多个视频文件"""
    clips = [VideoFileClip(path) for path in input_paths]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(
        output_path,
        fps=clips[0].fps,
        temp_audiofile="temp-audio.m4a",
        remove_temp=True,
        codec="libx264",
        audio_codec="aac"
    )
    [clip.close() for clip in clips]
    logging.info(f"合并视频完成：{output_path}")


def create_work_dir(folder_name: str, video_path: str) -> str:
    """创建工作目录并移动视频文件，返回视频在工作目录中的路径"""
    os.makedirs(folder_name, exist_ok=True)
    dest_path = os.path.join(folder_name, os.path.basename(video_path))
    shutil.move(video_path, dest_path)
    logging.info(f"工作目录创建完成：{folder_name}，视频已移动至：{dest_path}")
    return dest_path


def save_pkl(data, save_path: str) -> None:
    """保存数据到pkl文件"""
    with open(save_path, "wb") as f:
        pickle.dump(data, f)
    logging.info(f"数据已保存到：{save_path}")


def load_pkl(load_path: str):
    """从pkl文件加载数据"""
    with open(load_path, "rb") as f:
        data = pickle.load(f)
    logging.info(f"从{load_path}加载数据完成")
    return data


def translate_ja_to_zh(text: str) -> str:
    """日语转中文（依赖googletrans）"""
    if not text.strip():
        return ""
    try:
        translator = Translator(service_urls=["translate.google.com"])
        return translator.translate(text, src="ja", dest="zh-cn").text
    except Exception as e:
        logging.warning(f"翻译失败：{e}，返回原文本")
        return text


def delete_files(file_paths: list[str]) -> None:
    """删除临时文件"""
    for path in file_paths:
        if os.path.exists(path):
            os.remove(path)
            logging.info(f"临时文件已删除：{path}")


# 视频转录与字幕生成核心类
class VideoTranscriber:
    """视频转录与字幕生成核心类"""
    def __init__(self, video_path: str = None, video_paths: list[str] = None):
        """
        初始化：支持单个视频或多个视频
        :param video_path: 单个视频路径
        :param video_paths: 多个视频路径列表
        """
        if video_path:
            self.video_paths = [video_path]
        elif video_paths:
            self.video_paths = video_paths
        else:
            raise ValueError("必须传入 video_path 或 video_paths")
        
        # 获取视频基础信息（用第一个视频的分辨率作为统一字幕尺寸）
        _, self.video_size = get_video_info(self.video_paths[0])
        self.work_dir = os.path.dirname(self.video_paths[0])  # 工作目录（视频所在目录）

    def transcribe(self, model_size: str = "base", device: str = "cpu", 
                   language: str = "ja", task: str = "translate") -> dict:
        """
        转录视频为DataFrame（包含时间戳、文本、置信度等）
        :return: 键为视频路径，值为转录结果DataFrame的字典
        """
        # 初始化faster_whisper模型
        model = WhisperModel(model_size, device=device, compute_type="int8")  # int8适合CPU
        result_dict = {}

        for video_path in self.video_paths:
            # 转录视频（生成时间戳片段）
            segments, _ = model.transcribe(
                video_path,
                language=language,
                beam_size=3,
                vad_filter=False,  # 关闭VAD过滤（简化逻辑，可根据需求开启）
                task=task
            )
            segments = list(segments)
            logging.info(f"视频转录完成：{video_path}（共{len(segments)}个片段）")

            # 提取转录信息到DataFrame
            video_duration, _ = get_video_info(video_path)
            result_df = pd.DataFrame({
                "start": [s.start for s in segments],
                "end": [s.end for s in segments],
                "text": [s.text.strip() for s in segments],
                "confidence": [10 ** s.avg_logprob for s in segments]  # 置信度（0-1）
            }).query("end <= @video_duration")  # 过滤超出视频时长的片段

            result_dict[video_path] = result_df
            # 保存转录结果到CSV（方便后续查看/编辑）
            csv_path = f"{video_path[:-4]}_transcript.csv"
            result_df.to_csv(csv_path, index=False)
            logging.info(f"转录结果已保存到：{csv_path}")

        # 保存完整结果到pkl（可选，用于后续增强）
        save_pkl(result_dict, os.path.join(self.work_dir, "transcribe_result.pkl"))
        return result_dict

    def add_subtitles(self, result_dict: dict, font: str = "Arial", 
                      fontsize: int = 30, color: str = "white") -> list:
        """
        给视频添加字幕，生成带字幕的新视频
        :param result_dict: 转录结果字典（transcribe方法的输出）
        :return: 带字幕的视频路径列表
        """
        output_videos = []

        # 定义字幕生成器（统一样式）
        def subtitle_generator(txt):
            return TextClip(
                txt,
                font=font,
                fontsize=fontsize,
                color=color,
                stroke_color="black",  # 黑色描边（增强可读性）
                stroke_width=2,
                size=self.video_size,
                method="caption",  # 自动换行
                align="South"     # 底部对齐
            )

        for video_path, result_df in result_dict.items():
            # 转换DataFrame为字幕格式：[(start, end), text]
            subtitles = [((row["start"], row["end"]), row["text"]) 
                         for _, row in result_df.iterrows()]
            subs_clip = SubtitlesClip(subtitles, subtitle_generator)

            # 合成视频与字幕
            with VideoFileClip(video_path) as video_clip:
                final_clip = CompositeVideoClip([
                    video_clip,
                    subs_clip.set_pos(("center", "bottom"))  # 字幕放在底部中央
                ])

                # 保存带字幕的视频
                output_path = f"{video_path[:-4]}_with_subs.mp4"
                final_clip.write_videofile(
                    output_path,
                    fps=video_clip.fps,
                    temp_audiofile="temp-audio.m4a",
                    remove_temp=True,
                    codec="libx264",
                    audio_codec="aac"
                )
            output_videos.append(output_path)
            logging.info(f"带字幕视频生成完成：{output_path}")

        return output_videos


# 转录结果增强类
class ResultEnhancer:
    """转录结果增强类（处理重复文本、长片段分割等问题）"""
    def __init__(self, transcribe_dict: dict):
        self.transcribe_dict = transcribe_dict  # 原始转录结果
        self.enhanced_dict = transcribe_dict.copy()  # 增强后结果

    def fix_consecutive_text(self, threshold: int = 5) -> dict:
        """修复连续重复文本（如“嗯...嗯...嗯”）"""
        for video_path, df in self.transcribe_dict.items():
            # 检测连续重复文本片段
            consecutive_indices = []
            current_text = None
            current_count = 1

            for idx, row in df.iterrows():
                if row["text"] == current_text:
                    current_count += 1
                    if current_count >= threshold:
                        consecutive_indices.append(idx)
                else:
                    current_text = row["text"]
                    current_count = 1

            if not consecutive_indices:
                logging.info(f"视频{video_path}无连续重复文本，无需修复")
                continue

            # 移除连续重复片段，用单个片段替代（简化处理）
            clean_df = df.drop(consecutive_indices).reset_index(drop=True)
            # 在重复片段的起始位置添加一个总结文本
            if consecutive_indices:
                first_idx = consecutive_indices[0]
                clean_df = pd.concat([
                    clean_df.iloc[:first_idx],
                    pd.DataFrame({
                        "start": [df.iloc[first_idx]["start"]],
                        "end": [df.iloc[consecutive_indices[-1]]["end"]],
                        "text": [df.iloc[first_idx]["text"] + "（已合并重复片段）"],
                        "confidence": [df.iloc[consecutive_indices]["confidence"].mean()]
                    }),
                    clean_df.iloc[first_idx:]
                ], ignore_index=True)

            self.enhanced_dict[video_path] = clean_df
            logging.info(f"视频{video_path}连续重复文本修复完成（移除{len(consecutive_indices)}个片段）")
        return self.enhanced_dict

    def split_long_segments(self, max_duration: int = 10) -> dict:
        """分割过长的字幕片段（默认超过10秒的片段）"""
        for video_path, df in self.enhanced_dict.items():
            df["duration"] = df["end"] - df["start"]
            long_segments = df[df["duration"] > max_duration]

            if long_segments.empty:
                logging.info(f"视频{video_path}无过长片段，无需分割")
                continue

            # 分割过长片段（平均分成多段）
            clean_df = df[df["duration"] <= max_duration].copy()
            for _, long_row in long_segments.iterrows():
                segment_count = math.ceil(long_row["duration"] / max_duration)
                segment_duration = long_row["duration"] / segment_count

                # 生成分割后的片段
                split_segments = []
                for i in range(segment_count):
                    split_segments.append({
                        "start": long_row["start"] + i * segment_duration,
                        "end": long_row["start"] + (i + 1) * segment_duration,
                        "text": long_row["text"],  # 文本不变，仅分割时间戳
                        "confidence": long_row["confidence"]
                    })

                # 插入分割后的片段
                clean_df = pd.concat([
                    clean_df,
                    pd.DataFrame(split_segments)
                ], ignore_index=True).sort_values("start").reset_index(drop=True)

            self.enhanced_dict[video_path] = clean_df.drop(columns=["duration"])
            logging.info(f"视频{video_path}过长片段分割完成（处理{len(long_segments)}个片段）")
        return self.enhanced_dict


# 主函数
def main():
    # --------------------------
    # 步骤1：准备视频（二选一）
    # --------------------------
    # 选项A：从URL下载视频（需安装yt-dlp：pip install yt-dlp）
    # video_url = "https://example.com/your-video-url.mp4"  # 替换为你的视频URL
    # download_video(url=video_url, save_name="test_video.mp4", res="720")
    # video_path = "test_video.mp4"

    # 选项B：使用本地已有的视频
    video_path = "test_video.mp4"  # 替换为你的本地视频路径

    # （可选）创建单独的工作目录，整理文件
    work_dir = "video_subtitle_workdir"
    video_path = create_work_dir(folder_name=work_dir, video_path=video_path)

    # --------------------------
    # 步骤2：分割长视频（可选，超过10分钟建议分割）
    # --------------------------
    total_duration, _ = get_video_info(video_path)
    split_duration = 600  # 每段10分钟
    if total_duration > split_duration:
        logging.info(f"视频时长{total_duration:.1f}s，超过{split_duration}s，开始分割")
        split_paths = split_video(input_path=video_path, split_duration=split_duration)
    else:
        split_paths = [video_path]

    # --------------------------
    # 步骤3：初始化转录器并转录视频
    # --------------------------
    # 模型选择：base（快，精度一般）、large-v3（准，慢，需更多资源）
    transcriber = VideoTranscriber(video_paths=split_paths)
    transcribe_result = transcriber.transcribe(
        model_size="base",  # 学生电脑CPU建议用base/small模型
        device="cpu",
        language="ja",  # 源语言：日语（根据视频语言修改）
        task="translate"  # 任务：翻译（转为中文），可选"transcribe"（仅转录原语言）
    )

    # --------------------------
    # 步骤4：（可选）增强转录结果
    # --------------------------
    enhancer = ResultEnhancer(transcribe_dict=transcribe_result)
    # 修复连续重复文本（超过5次重复）
    enhanced_result = enhancer.fix_consecutive_text(threshold=5)
    # 分割过长片段（超过10秒）
    enhanced_result = enhancer.split_long_segments(max_duration=10)

    # --------------------------
    # 步骤5：给视频添加字幕
    # --------------------------
    subtitled_videos = transcriber.add_subtitles(
        result_dict=enhanced_result,
        fontsize=30,  # 字幕大小（根据视频分辨率调整）
        color="white"
    )

    # --------------------------
    # 步骤6：合并分割的字幕视频（如果之前分割过）
    # --------------------------
    if len(subtitled_videos) > 1:
        final_output = f"{video_path[:-4]}_final_with_subs.mp4"
        merge_videos(input_paths=subtitled_videos, output_path=final_output)
        # （可选）删除分割的临时视频
        delete_files(split_paths + subtitled_videos)
        logging.info(f"最终带字幕视频：{final_output}")
    else:
        logging.info(f"最终带字幕视频：{subtitled_videos[0]}")


if __name__ == "__main__":
    main()