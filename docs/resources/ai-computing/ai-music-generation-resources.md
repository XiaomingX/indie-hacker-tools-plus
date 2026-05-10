# AI 音乐创作资源大全 (2026 Checklist)

> [!TIP]
> **Indie Hacker Insight**: 2026 年的 AI 音乐生成已经从“玩具”进化为“生产力工具”。
> - **商业授权**：在使用 Suno 或 Udio 生成音乐时，务必确认你的订阅级别支持商业分发。
> - **混合创作**：最佳实践是使用 AI 生成基础素材，再通过 Ableton 或 Logic Pro 进行二次混音与母带处理。

---

## 🎵 核心开源项目 (GitHub Projects)

- [ ] [**Audiocraft (Meta)**](https://github.com/facebookresearch/audiocraft) - 包含 MusicGen, AudioGen, EnCodec，目前最强大的本地可控生成库。
- [ ] [**Magenta (Google)**](https://github.com/magenta/magenta) - 行业鼻祖，提供大量用于浏览器和本地的音乐生成、补全工具。
- [ ] [**InspireMusic (Alibaba)**](https://github.com/alibaba/InspireMusic) - 综合性生成框架，支持音乐、歌曲和音频的灵活控制。
- [ ] [**Muzic (Microsoft)**](https://github.com/microsoft/muzic) - 专注于音乐理解与生成的多任务框架。
- [ ] [**Stable Audio Open**](https://github.com/Stability-AI/generative-models) - Stability AI 的开源版权重，适合本地部署。
- [ ] [**MusPy**](https://github.com/salu133445/muspy) - 符号音乐（MIDI）处理与模型评估的 Python 必备工具。

---

## 🛠️ 主流在线平台 (SaaS Tools)

- [ ] [**Suno**](https://suno.com/) - 2026 年音乐生成的行业标杆，支持长达 4 分钟的高保真全曲生成（含人声）。
- [ ] [**Udio**](https://www.udio.com/) - 艺术家首选，以极高的音质和细腻的情感表达著称。
- [ ] [**Stable Audio**](https://stableaudio.com/) - 擅长生成环境音、背景配乐及短音频片段。
- [ ] [**AIVA**](https://www.aiva.ai/) - 专注于影视、游戏配乐，支持导出 MIDI 供专业制作人修改。
- [ ] [**Soundful**](https://soundful.com/) - 专为内容创作者设计，一键生成免版税背景音乐。
- [ ] [**Landr**](https://www.landr.com/) - AI 母带处理 (Mastering) 的事实标准，提升成片音质。

---

## 📖 核心研究与论文 (Articles & Papers)

- [ ] [**MusicGen**](https://arxiv.org/abs/2306.05284) - Simple and Controllable Music Generation.
- [ ] [**AudioLDM 2**](https://arxiv.org/abs/2308.05734) - 基于潜在扩散模型的通用音频生成框架。
- [ ] [**Noise2Music**](https://arxiv.org/abs/2302.03917) - 高保真文本到音乐生成的代表作。
- [ ] [**Deep Music Generation Review**](https://arxiv.org/pdf/2011.06801) - 深度学习音乐生成的系统综述。

---

## 🎓 学习资源 (Learning)

- [ ] [**The Sound of AI**](https://valeriovelardo.com/the-sound-of-ai-accelerator/) - Valerio Velardo 的深度学习音频开发加速器（非常推荐）。
- [ ] [**Magenta.js Demos**](https://magenta.tensorflow.org/demos) - 通过浏览器实时体验 AI 创作的魅力。
- [ ] [**AI Music Masterclass**](https://live.rookiesavior.net/course/lyrics-ai) - 涵盖 Suno、Soundraw 等工具实操的现代课程。

---

## 💡 选型建议
1. **快速成曲/个人娱乐**：选 **Suno**。
2. **专业编曲辅助**：选 **AIVA (MIDI)** + **Logic Pro**。
3. **本地开发/商业应用**：使用 **Audiocraft** 权重进行微调。
4. **提升听感**：最后一步务必经过 **Landr** 或 **Adobe Podcast Enhance** 处理。