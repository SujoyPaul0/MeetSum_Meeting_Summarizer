# 🎙️ MeetSum – Meeting Summarizer from Audio

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

![image](https://github.com/user-attachments/assets/5660602d-2ad4-4c4b-9e35-fef551ccd20e)


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

```
git clone https://github.com/yourusername/Talk2Summary.git
cd Talk2Summary
```

Here’s a professional and clean `README.md` file for your **Talk2Summary (Meeting Summarizer)** app that takes audio input, transcribes it using Whisper, and summarizes it using a Transformer model:

* * *

## 📦 Installation ### 1. Clone the Repository ```bash
git clone https://github.com/yourusername/MeetSum_Meeting_Summarizer.git
cd Talk2Summary`` 

### 2\. Create a Virtual Environment (optional but recommended)

`python -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate` 

### 3\. Install Dependencies

`pip install -r requirements.txt` 

### 4\. Install FFmpeg (Required for Whisper)

*   Download from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
    
*   Add `ffmpeg/bin` to your system PATH
    
*   Verify with:
    
    `ffmpeg -version` 
    

* * *

🚀 Run the App
--------------

`streamlit run app.py` 

Then open your browser at: `http://localhost:8501`

* * *

📁 Project Structure
--------------------

bash

`.
├── app.py # Streamlit frontend ├── summarizer.py # HuggingFace T5 summarizer ├── transcriber.py # Whisper audio transcription ├── requirements.txt # Python dependencies └── README.md # Project documentation` 

* * *

🧠 Future Improvements
----------------------

*    Real-time microphone recording
    
*    Speaker diarization (who said what)
    
*    Multi-language transcription toggle
    
*    Deploy as a web app (e.g., Streamlit Cloud or Hugging Face Spaces)
    

* * *

🙋‍♂️ Author
------------

**Sujoy Paul**  
📧 \[sujoy@example.com\]  
🔗 [LinkedIn](https://linkedin.com/in/sujoy) | [GitHub](https://github.com/yourusername)

* * *

📝 License
----------

MIT License – feel free to use, modify, and distribute!

yaml

 `--- Let me know if you want this customized with: - A real screenshot from your app - Your actual GitHub repo link - Microphone support added I can also zip and send a deploy-ready project structure!` 

![Export to Google Doc](chrome-extension://iapioliapockkkikccgbiaalfhoieano/assets/create.svg)![Copy with formatting](chrome-extension://iapioliapockkkikccgbiaalfhoieano/assets/copy.svg)![Select for Multi-select](chrome-extension://iapioliapockkkikccgbiaalfhoieano/assets/multi-select.svg)
