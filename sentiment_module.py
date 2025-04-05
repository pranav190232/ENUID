from transformers import pipeline

# Load only the sentiment analysis model (no sarcasm)
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(text):
    """Detects sentiment using BERT and returns a refined mood."""
    result = sentiment_pipeline(text)[0]
    label = result['label']

    # Mapping sentiment scores to chatbot-friendly moods
    if "5 stars" in label:
        return "very happy 😀"
    elif "4 stars" in label:
        return "happy 🙂"
    elif "3 stars" in label:
        return "neutral 😐"
    elif "2 stars" in label:
        return "unhappy 🙁"
    elif "1 star" in label:
        return "very sad 😢"
    else:
        return "neutral"
