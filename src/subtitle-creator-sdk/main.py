import os
import subprocess
from youtube_transcript_api import YouTubeTranscriptApi

def download_video(youtube_url, output_filename="video.mp4"):
    """
    下载YouTube视频
    """
    print("正在下载视频...")
    command_video = [
        "yt-dlp",
        youtube_url,
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "-o", output_filename
    ]
    result_video = subprocess.run(command_video, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result_video.returncode != 0:
        raise Exception(f"视频下载失败：{result_video.stderr.decode()}")
    print(f"视频下载成功：{output_filename}")
    return output_filename

def download_subtitles(video_id, subtitle_filename="sub.srt"):
    """
    下载视频字幕
    """
    try:
        # 优先级语言列表
        preferred_languages = ['zh-Hans', 'en']
        transcript = None

        # 尝试按优先级获取字幕
        for language in preferred_languages:
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
                print(f"Downloaded subtitles in language: {language}")
                break
            except Exception as e:
                continue

        # 如果没有优先语言的字幕，获取其他可用字幕
        if transcript is None:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            print("Downloaded subtitles in available language")
        
        # 将字幕保存为SRT格式
        with open(subtitle_filename, "w", encoding="utf-8") as srt_file:
            for i, entry in enumerate(transcript):
                start = entry['start']
                duration = entry['duration']
                end = start + duration
                srt_file.write(f"{i + 1}\n")
                srt_file.write(f"{format_time(start)} --> {format_time(end)}\n")
                srt_file.write(f"{entry['text']}\n\n")
        print(f"Subtitles saved to {subtitle_filename}")
        return subtitle_filename
    except Exception as e:
        raise Exception(f"字幕下载失败：{e}")

def format_time(seconds):
    """
    将秒数格式化为SRT时间戳
    """
    milliseconds = int((seconds - int(seconds)) * 1000)
    seconds = int(seconds)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def merge_video_with_subtitles(video_filename, subtitle_filename, output_filename="out_movie.mp4"):
    """
    将字幕嵌入视频
    """
    if not subtitle_filename:
        print("未找到字幕文件，跳过字幕嵌入步骤。")
        os.rename(video_filename, output_filename)
        return

    print("正在嵌入字幕...")
    command = [
        "ffmpeg",
        "-i", video_filename,
        "-vf", f"subtitles={subtitle_filename}",
        "-c:a", "copy",
        output_filename
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise Exception(f"字幕嵌入失败：{result.stderr.decode()}")

    print(f"字幕嵌入完成：{output_filename}")

def main():
    """
    主流程
    """
    youtube_url = "https://www.youtube.com/watch?v=brE21SBO2j8"
    video_id = youtube_url.split("v=")[-1]
    print(f"正在处理链接：{youtube_url}")

    try:
        # 步骤1：下载视频
        video_filename = download_video(youtube_url)

        # 步骤2：下载字幕
        subtitle_filename = download_subtitles(video_id)

        # 步骤3：嵌入字幕
        output_filename = "out_movie.mp4"
        merge_video_with_subtitles(video_filename, subtitle_filename, output_filename)

        print(f"处理完成，生成文件：{output_filename}")
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    main()