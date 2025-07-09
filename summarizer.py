from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small", framework="pt")

def summarize_text(text):
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]  # Chunk long transcripts
    summaries = [summarizer(chunk, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
                 for chunk in chunks]
    return " ".join(summaries)
