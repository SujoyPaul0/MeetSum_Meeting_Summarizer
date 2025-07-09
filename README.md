# 🎙️ Talk2Summary – Meeting Summarizer from Audio

Talk2Summary is a Python-based application that takes audio input (WAV/MP3), transcribes it using OpenAI’s Whisper model, and then summarizes the conversation using a Transformer-based NLP model (T5).

Ideal for meeting notes, class lectures, podcasts, and more!

---

## ✨ Features

- ✅ Upload `.wav` or `.mp3` audio files
- 🧠 Transcribes speech to text using Whisper
- 📝 Summarizes long conversations using HuggingFace Transformers (T5)
- 🎛️ Simple and interactive **Streamlit UI**
- 🌍 Supports multiple languages (via Whisper)

---

## 🖥️ Demo

![screenshot](https://via.placeholder.com/800x400.png?text=Talk2Summary+Demo+Screenshot)

---

## 🔧 Tech Stack

| Component         | Tool/Model            |
|------------------|-----------------------|
| Speech-to-Text    | [OpenAI Whisper](https://github.com/openai/whisper) |
| Summarization     | HuggingFace Transformers (`t5-small`) |
| UI                | [Streamlit](https://streamlit.io) |
| Language          | Python 3.10+          |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Talk2Summary.git
cd Talk2Summary
