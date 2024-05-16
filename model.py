# backend/model.py
from transformers import pipeline

# Load pre-trained sentiment-analysis pipeline with PyTorch
sentiment_model = pipeline("sentiment-analysis", framework="pt")

def analyze_sentiment(text):
    return sentiment_model(text)
