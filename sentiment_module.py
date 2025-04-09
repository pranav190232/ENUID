from transformers import pipeline
import torch 
# Check if GPU is available
device = 0 if torch.cuda.is_available() else -1

# Load the emotion classification model
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def analyze_sentiment(text):
    """Detects emotion using a pre-trained model and returns the dominant emotion."""
    result = emotion_pipeline(text)[0]
    emotion = result['label']

    # Map the detected emotion to a user-friendly response
    if emotion == "joy":
        return "happiness 😀"
    elif emotion == "sadness":
        return "sadness 😢"
    elif emotion == "anger":
        return "anger 😠"
    elif emotion == "fear":
        return "fear 😨"
    elif emotion == "surprise":
        return "surprise 😲"
    elif emotion == "disgust":
        return "disgust 🤢"
    else:
        return "neutral 😐"





