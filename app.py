import streamlit as st
from transcriber import transcribe_audio
from summarizer import summarize_text
import os

st.title("🎙️ MeetSum - Summarize Conversation from Audio")

uploaded_file = st.file_uploader("Upload an audio file (WAV, MP3)", type=["wav", "mp3"])

if uploaded_file:
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.read())
    st.audio("temp_audio.wav")

    st.write("🔍 Transcribing...")
    transcript = transcribe_audio("temp_audio.wav")
    st.write("📝 Transcript:")
    st.text(transcript)

    st.write("🔗 Summarizing...")
    summary = summarize_text(transcript)
    st.success("✅ Summary:")
    st.write(summary)
