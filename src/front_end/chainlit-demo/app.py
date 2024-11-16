import chainlit as cl
from chainlit.input_widget import Select
from openai import OpenAI
import asyncio
from datetime import datetime
import speech_recognition as sr
import hashlib
import os
from pydub import AudioSegment
from pydub.playback import play

client = OpenAI()

# 新增函数：接收语音输入并转化为文本
def save_and_convert_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("请说话...")
        audio = recognizer.listen(source)

        # 生成语音文件的hash名
        audio_data = audio.get_wav_data()
        audio_hash = hashlib.sha256(audio_data).hexdigest()
        file_name = f"{audio_hash}.wav"

        # 保存音频文件
        with open(file_name, "wb") as f:
            f.write(audio_data)

        # 使用 pydub 播放音频文件（可选）
        audio_segment = AudioSegment.from_wav(file_name)
        play(audio_segment)

        # 将语音转化为文字
        try:
            text = recognizer.recognize_google(audio, language="zh-CN")
            print(f"语音转文字结果: {text}")
            return text
        except sr.UnknownValueError:
            print("无法理解语音")
            return "抱歉，我无法理解您的语音。"
        except sr.RequestError as e:
            print(f"语音识别服务错误: {e}")
            return "抱歉，语音识别服务出现错误。"

async def get_data_from_openai(prompt, chat_history):
    print(chat_history)
    messages = chat_history + [{"role": "user", "content": prompt}]
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return completion.choices[0].message.content

@cl.on_chat_start
async def start():
    
    # 通过优化使得用户可以感受到机器人在思考
    await asyncio.sleep(1)  # 模拟思考时间

    await cl.Message(
        content=f"我是一个简单的聊天机器人。请问有什么我可以帮你的吗？"
    ).send()

@cl.on_message
async def main(message: cl.Message, chat_history=[]):
    # 新增：检查用户是否选择了语音输入
    if message.content.lower() == "语音输入":
        voice_text = save_and_convert_voice()
        message.content = voice_text
    
    # 优化数据获取函数，支持异步
    response = await get_data_from_openai(message.content, chat_history)
    
    # 更新聊天历史
    chat_history.append({"role": "user", "content": message.content})
    chat_history.append({"role": "assistant", "content": response})
    
    # 发送响应
    await cl.Message(content=response).send()