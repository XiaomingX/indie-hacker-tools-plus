# whisper-video-transcript-plus

A powerful, easy-to-use video transcription and subtitle generation tool built with **Faster Whisper** (for high-speed speech recognition) and **MoviePy** (for video editing). It supports multi-language transcription, automatic subtitle synthesis, long video processing, and transcription result optimization—perfect for students, content creators, and anyone needing quick video subtitle solutions.


## 📋 Table of Contents
- [Project Overview](#-project-overview)
- [Key Features](#-key-features)
- [Prerequisites](#-prerequisites)
- [Quick Start](#-quick-start)
- [Detailed Usage](#-detailed-usage)
- [Parameter Configuration](#-parameter-configuration)
- [Project Structure](#-project-structure)
- [Common Issues & Fixes](#-common-issues--fixes)
- [Contributing](#-contributing)
- [License](#-license)


## 📖 Project Overview
`whisper-video-transcript-plus` simplifies the end-to-end workflow of turning video audio into accurate subtitles. It addresses common pain points like long video memory constraints, messy transcription results (e.g., repeated text), and tedious manual subtitle editing. 

Core workflow:  
`Video Input (Local/URL) → [Optional: Split Long Video] → Speech Transcription/Translation → [Optional: Optimize Results] → Subtitle Synthesis → [Optional: Merge Videos] → Final Video with Subtitles`


## ✨ Key Features
1. **Flexible Video Input**  
   - Process local MP4 files or download videos directly from URLs (via `yt-dlp`).
2. **Long Video Handling**  
   - Automatically splits videos longer than 10 minutes (configurable) to avoid memory overload, then merges results.
3. **Multi-Language Support**  
   - Transcribe speech in 100+ languages (e.g., Japanese, English, Chinese) or translate directly to Chinese (default: Japanese → Chinese).
4. **High-Quality Subtitles**  
   - Customizable subtitle styles (font, size, color, stroke) for better readability.
5. **Transcription Optimization**  
   - Fix repeated text segments (e.g., "um... um...") and split overly long subtitles (e.g., >10 seconds).
6. **Result Export**  
   - Saves transcriptions as CSV (for manual editing) and PKL (for later reuse).


## 🛠️ Prerequisites
Before running the tool, ensure you have the following installed:

### 1. Python Environment
- Python 3.8+ (recommended: 3.10)  
  Download from [python.org](https://www.python.org/downloads/) or use a virtual environment (e.g., `venv`):
  ```bash
  # Create virtual environment
  python -m venv venv
  # Activate (Windows)
  venv\Scripts\activate
  # Activate (Mac/Linux)
  source venv/bin/activate
  ```

### 2. Dependencies
Install required Python packages via `pip`:
```bash
pip install faster-whisper moviepy pandas opencv-python googletrans==4.0.0-rc1 yt-dlp
```

### 3. FFmpeg & ImageMagick
These tools are required for video/audio processing and subtitle rendering:
- **Mac**: Use Homebrew  
  ```bash
  brew install ffmpeg imagemagick
  ```
- **Linux (Ubuntu/Debian)**:
  ```bash
  sudo apt update && sudo apt install ffmpeg imagemagick
  ```
- **Windows**:
  1. Download FFmpeg from [ffmpeg.org/download.html](https://ffmpeg.org/download.html#build-windows) (choose "Full Build").
  2. Extract FFmpeg and add its `bin` folder to your **system environment variables** (e.g., `C:\ffmpeg-6.0-full_build\bin`).
  3. Download ImageMagick from [imagemagick.org/script/download.php#windows](https://imagemagick.org/script/download.php#windows) (check "Add to PATH" during installation).


## 🚀 Quick Start
Follow these steps to generate subtitles for a video in 5 minutes:

### 1. Clone the Repository
```bash
git clone https://github.com/XiaomingX/whisper-video-transcript-plus.git
cd whisper-video-transcript-plus
```

### 2. Prepare Your Video
Choose one of two options:
- **Option A: Use a local video**  
  Place your MP4 file (e.g., `my_video.mp4`) in the project root.
- **Option B: Download a video from URL**  
  Get the video URL (e.g., YouTube, Bilibili) and update the `video_url` variable in `main.py`.

### 3. Run the Main Script
Edit `main.py` to set your video source (local path or URL), then run:
```bash
python main.py
```

### 4. Get Results
- The final video with subtitles will be saved in `video_subtitle_workdir/` (auto-created).
- Transcriptions are exported as CSV (e.g., `my_video_transcript.csv`) for manual editing.


## 📝 Detailed Usage
### Scenario 1: Process a Local Video
1. Update the `video_path` in `main()` (line ~280 in `main.py`):
   ```python
   # Option B: Use local video
   video_path = "my_local_video.mp4"  # Replace with your video path
   ```
2. Run `python main.py`.

### Scenario 2: Download and Process a Video from URL
1. Uncomment the "Option A" section in `main()` and set your video URL:
   ```python
   # Option A: Download video from URL
   video_url = "https://www.youtube.com/watch?v=your-video-id"  # Replace with your URL
   download_video(url=video_url, save_name="downloaded_video.mp4", res="720")
   video_path = "downloaded_video.mp4"
   ```
2. Run `python main.py` (the video will auto-download first).

### Scenario 3: Skip Result Enhancement (Faster Processing)
If you don’t need to fix repeated text or split long subtitles, comment out the enhancement steps in `main()`:
```python
# --------------------------
# Step 4: (Optional) Enhance Transcription Results (skip this for speed)
# --------------------------
# enhancer = ResultEnhancer(transcribe_dict=transcribe_result)
# enhanced_result = enhancer.fix_consecutive_text(threshold=5)
# enhanced_result = enhancer.split_long_segments(max_duration=10)
enhanced_result = transcribe_result  # Use original results directly
```


## ⚙️ Parameter Configuration
Customize the tool by adjusting key parameters in `main.py` or the core classes:

| Parameter               | Location                  | Description                                                                 | Default Value       |
|-------------------------|---------------------------|-----------------------------------------------------------------------------|---------------------|
| `model_size`            | `transcriber.transcribe()`| Faster Whisper model size (trade-off between speed and accuracy). Options: `tiny`/`base`/`small`/`medium`/`large-v3` | `"base"` (CPU-friendly) |
| `language`              | `transcriber.transcribe()`| Source language of the video (use [ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), e.g., "ja" for Japanese, "en" for English). | `"ja"`              |
| `task`                  | `transcriber.transcribe()`| "transcribe" (keep original language) or "translate" (to Chinese).          | `"translate"`       |
| `split_duration`        | `split_video()`           | Max duration per video segment (for long videos, in seconds).               | 600s (10 minutes)   |
| `fontsize`              | `transcriber.add_subtitles()` | Subtitle font size (adjust for video resolution: 30 for 720p, 40 for 1080p). | 30                  |
| `threshold` (consecutive text) | `enhancer.fix_consecutive_text()` | Minimum number of repeated text segments to trigger cleanup.          | 5                   |
| `max_duration` (long segments) | `enhancer.split_long_segments()` | Max subtitle duration (in seconds) before splitting.              | 10s                 |


## 📂 Project Structure
```
whisper-video-transcript-plus/
├── main.py               # Core script (all logic integrated: transcription, subtitles, enhancement)
├── README.md             # Project documentation (you're reading this!)
├── LICENSE               # MIT License file
├── video_subtitle_workdir/  # Auto-created work directory (stores input/output files)
│   ├── my_video.mp4      # Input video (local or downloaded)
│   ├── my_video_transcript.csv  # Transcription result (editable CSV)
│   ├── my_video_with_subs.mp4  # Final video with subtitles
│   └── transcribe_result.pkl  # Transcription result (for later reuse)
└── venv/                 # Virtual environment (optional, for dependency isolation)
```


## ❌ Common Issues & Fixes
### 1. "FFmpeg not found" Error
- **Root Cause**: FFmpeg is not installed or not added to system `PATH`.
- **Fix**: 
  - Verify FFmpeg installation with `ffmpeg -version` (should return version info).
  - Recheck the [Prerequisites](#-prerequisites) section for OS-specific FFmpeg setup.

### 2. Slow Transcription (CPU Only)
- **Fix**: 
  - Use a smaller model (e.g., `"tiny"` instead of `"large-v3"`)—adds ~2x speedup.
  - For GPU acceleration (NVIDIA): Install PyTorch with CUDA (`pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118`) and set `device="cuda"` in `transcriber.transcribe()`.

### 3. GoogleTrans Translation Failure
- **Root Cause**: Rate limits or regional blocks for Google Translate API.
- **Fix**:
  - Wait 5–10 minutes before retrying (avoids rate limits).
  - Use a VPN (if blocked in your region).
  - Switch to `"transcribe"` mode (no translation) by updating `task="transcribe"` in `transcriber.transcribe()`.

### 4. "ImageMagick binary not found" Error
- **Fix**: 
  - Reinstall ImageMagick and ensure "Add to PATH" is checked during installation (Windows).
  - For Mac/Linux: Verify with `convert --version` (ImageMagick’s CLI tool).


## 🤝 Contributing
We welcome contributions to improve this tool! Here’s how to contribute:

1. **Fork the Repository**  
   Click the "Fork" button at the top of [https://github.com/XiaomingX/whisper-video-transcript-plus](https://github.com/XiaomingX/whisper-video-transcript-plus).

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/your-username/whisper-video-transcript-plus.git
   cd whisper-video-transcript-plus
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name  # e.g., feature/add-srt-export
   ```

4. **Make Changes**  
   - Follow PEP 8 style guidelines (use `flake8` for linting).
   - Add tests for new features (if applicable).
   - Update `README.md` if you modify usage or parameters.

5. **Commit & Push**
   ```bash
   git add .
   git commit -m "feat: add SRT subtitle export"  # Use conventional commits
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request (PR)**  
   Go to the original repository and click "Compare & pull request"—describe your changes clearly.


## 📄 License
This project is licensed under the **MIT License**—see the [LICENSE](https://github.com/XiaomingX/whisper-video-transcript-plus/blob/main/LICENSE) file for details. You’re free to:
- Use, copy, modify, and distribute the software for personal/commercial purposes.
- Include the software in proprietary products (with attribution).


---

If you find this tool useful, please give it a ⭐ on GitHub! For bugs, feature requests, or questions, open an [issue](https://github.com/XiaomingX/whisper-video-transcript-plus/issues) in the repository.