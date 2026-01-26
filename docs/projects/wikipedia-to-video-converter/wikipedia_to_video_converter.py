import logging
import os
import re
import argparse
import asyncio
import aiohttp
import aiofiles
from urllib.parse import urlparse
from dotenv import load_dotenv
import openai
import replicate
from moviepy.editor import VideoFileClip, concatenate_videoclips

# 基础配置
logging.basicConfig(level=logging.INFO)
load_dotenv()  # 加载环境变量（需确保有.env文件存放API密钥）


async def download_video(url, save_dir, filename):
    """下载视频到指定目录"""
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, filename)
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            async with aiofiles.open(filepath, 'wb') as f:
                await f.write(await response.read())
    logging.info(f"视频已保存至: {filepath}")
    return filepath


def clean_title(url_or_title):
    """从URL或标题中提取并清理维基百科页面标题"""
    if url_or_title.startswith('http'):
        parsed = urlparse(url_or_title)
        return parsed.path.split('/')[-1]
    return url_or_title


async def get_wiki_summary(session, wiki_url):
    """获取维基百科页面的摘要信息"""
    title = clean_title(wiki_url)
    summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    
    try:
        async with session.get(summary_url) as response:
            response.raise_for_status()
            data = await response.json()
            return {
                "title": data["title"],
                "summary": data["extract"]
            }
    except aiohttp.ClientError as e:
        logging.error(f"获取摘要失败: {e}")
        return None


async def generate_prompt(master_prompt, title, summary, save_path, model="gpt-4o-mini"):
    """根据维基百科信息生成视频脚本提示词"""
    client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": master_prompt},
                {"role": "user", "content": f"标题: {title}\n摘要: {summary}"}
            ]
        )
        prompt = response.choices[0].message.content
        
        # 保存提示词
        if save_path:
            async with aiofiles.open(save_path, 'w', encoding='utf-8') as f:
                await f.write(prompt)
            logging.info(f"提示词已保存至: {save_path}")
        return prompt
    except Exception as e:
        logging.error(f"生成提示词失败: {e}")
        raise


def split_episodes(prompt, n_episodes):
    """将总提示词按集数分割"""
    episodes = re.split(r'(Episode \d+:)', prompt)
    episode_prompts = [episodes[i] + episodes[i+1] for i in range(1, len(episodes), 2)]
    
    if len(episode_prompts) != n_episodes:
        logging.error(f"分割的集数不匹配: {len(episode_prompts)} != {n_episodes}")
        return None
    return episode_prompts


async def generate_episode(session, prompt, save_dir, episode_title, model):
    """生成单集视频"""
    try:
        # 调用Replicate生成视频
        output = await asyncio.to_thread(
            replicate.run,
            model,
            input={"prompt": prompt}
        )
        video_url = str(output)
        
        # 下载视频
        return await download_video(video_url, save_dir, episode_title)
    except Exception as e:
        logging.error(f"生成视频失败 ({episode_title}): {e}")
        return None


async def combine_videos(episode_paths, output_path):
    """合并多集视频为一个完整视频"""
    if not episode_paths:
        logging.error("没有可合并的视频")
        return None
    
    clips = [VideoFileClip(path) for path in episode_paths if path]
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile(output_path)
    
    # 释放资源
    for clip in clips:
        clip.close()
    final_clip.close()
    
    logging.info(f"合并完成，保存至: {output_path}")
    return output_path


async def process_wiki_page(session, wiki_url, master_prompt_file, prompt_model, video_model, n_episodes):
    """处理单个维基百科页面，生成完整视频系列"""
    # 1. 获取维基百科信息
    wiki_info = await get_wiki_summary(session, wiki_url)
    if not wiki_info:
        return
    title, summary = wiki_info["title"], wiki_info["summary"]
    sanitized_title = title.replace(' ', '_')
    logging.info(f"开始处理: {title}")
    
    # 2. 准备目录和文件路径
    output_dir = os.path.join("output", sanitized_title)
    os.makedirs(output_dir, exist_ok=True)
    prompt_save_path = os.path.join(output_dir, f"{sanitized_title}_prompt.txt")
    
    # 3. 读取主提示词模板
    os.makedirs("inputs", exist_ok=True)  # 确保输入目录存在
    master_prompt_path = os.path.join("inputs", master_prompt_file)
    try:
        async with aiofiles.open(master_prompt_path, 'r', encoding='utf-8') as f:
            master_prompt = await f.read()
    except FileNotFoundError:
        logging.error(f"主提示词文件不存在: {master_prompt_path}")
        return
    
    # 4. 生成总提示词
    total_prompt = await generate_prompt(
        master_prompt, title, summary, prompt_save_path, prompt_model
    )
    if not total_prompt:
        return
    
    # 5. 分割为单集提示词
    episode_prompts = split_episodes(total_prompt, n_episodes)
    if not episode_prompts:
        return
    
    # 6. 并行生成所有集数
    episode_tasks = []
    for i, ep_prompt in enumerate(episode_prompts):
        ep_title = f"{sanitized_title}_episode_{i}.mp4"
        episode_tasks.append(
            generate_episode(session, ep_prompt, output_dir, ep_title, video_model)
        )
    episode_paths = await asyncio.gather(*episode_tasks)
    
    # 7. 合并所有集数
    final_video_path = os.path.join(output_dir, f"{sanitized_title}_complete.mp4")
    await combine_videos(episode_paths, final_video_path)


async def main():
    # 命令行参数配置
    parser = argparse.ArgumentParser(description='从维基百科生成视频系列')
    parser.add_argument('--urls', nargs='+', required=True, help='维基百科URL列表')
    parser.add_argument('--master-prompt', default="master_prompt.txt", 
                      help='主提示词模板文件（存放于inputs目录）')
    parser.add_argument('--prompt-model', default="gpt-4o-mini", help='生成提示词的模型')
    parser.add_argument('--video-model', default="pixverse/pixverse-v4.5", help='生成视频的模型')
    parser.add_argument('--episodes', type=int, default=3, help='生成的集数')
    args = parser.parse_args()
    
    # 处理所有URL
    async with aiohttp.ClientSession() as session:
        tasks = [
            process_wiki_page(
                session, url, args.master_prompt, 
                args.prompt_model, args.video_model, args.episodes
            ) for url in args.urls
        ]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())