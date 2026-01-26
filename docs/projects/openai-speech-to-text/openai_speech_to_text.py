from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
from openai import OpenAI

client = OpenAI()
speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Deepseek开源大模型Deepseek-V2的关键开发者洛夫里将加入小米，或担任小米AI实验室大模型团队负责人。知名人士透露，雷军认为小米在大模型领域起步较晚，亲自以千万级别薪酬招揽顶尖人才，小米AI实验室成立于2016年，约有250人，研究方向涵盖视频、声学、语音、语言处理等，洛夫里毕业于北京航天航空大学，曾在阿里巴巴达摩院主导多语言预训练VECO的开发与开源工作，她的加入有望加速小米在大模型领域的研发进程!",
)

response.stream_to_file(speech_file_path)