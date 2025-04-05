#import speech_recognition as sr
#import edge_tts
#import asyncio
#import os
#import pygame

## 🎧 New TTS using Microsoft Edge voices
#async def speak_async(text):
#    """Uses Microsoft Edge TTS for more human-like speech."""
#    voice = "en-US-JennyNeural"  # Change to different voices if needed
#    tts = edge_tts.Communicate(text, voice)
#    
#    # Save the audio to a temporary file
#    temp_file = "temp_output.mp3"
#    await tts.save(temp_file)
#    
#    # Initialize pygame mixer and play the audio
#    pygame.mixer.init()
#    pygame.mixer.music.load(temp_file)
#    pygame.mixer.music.play()
#    
#    # Wait for the audio to finish playing
#    while pygame.mixer.music.get_busy():
#        pygame.time.Clock().tick(10)
#    
#    # Clean up the temporary file
#    os.remove(temp_file)

#def speak(text):
#    """Wrapper function to run the async TTS"""
#    asyncio.run(speak_async(text))

## 🎤 Speech Recognition (Unchanged)
#def recognize_speech():
#    """Captures and converts speech to text with error handling."""
#    recognizer = sr.Recognizer()
#    with sr.Microphone() as source:
#        print("Listening... (speak now)")
#        recognizer.adjust_for_ambient_noise(source)
#        try:
#            audio = recognizer.listen(source)
#            text = recognizer.recognize_google(audio)
#            print(f"You said: {text}")
#            return text
#        except sr.UnknownValueError:
#            print("Sorry, I couldn't understand. Try typing instead.")
#            return ""
#        except sr.RequestError:
#            print("Speech recognition service is unavailable. Try typing.")
#            return ""

## Example usage
#if __name__ == "__main__":
#    text = recognize_speech()
#    if text:
#        speak(text)

# import speech_recognition as sr
# import edge_tts
# import asyncio
# import os
# import pygame
# import time

# # 🎧 Text-to-Speech Function
# async def speak_async(text):
#     """Uses Microsoft Edge TTS for human-like speech."""
#     voice = "en-US-JennyNeural"
#     tts = edge_tts.Communicate(text, voice)
    
#     temp_file = "temp_output.mp3"
#     await tts.save(temp_file)

#     pygame.mixer.init()
#     pygame.mixer.music.load(temp_file)
#     pygame.mixer.music.play()

#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)

#     pygame.mixer.quit()  # Close pygame properly
#     time.sleep(1)  # Ensure file release
#     os.remove(temp_file)

# def speak(text):
#     """Wrapper function to run the async TTS"""
#     asyncio.run(speak_async(text))

# # 🎤 Speech Recognition Function
# def recognize_speech():
#     """Captures and converts speech to text with error handling."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening... (speak now)")
#         recognizer.adjust_for_ambient_noise(source)
#         try:
#             audio = recognizer.listen(source)
#             text = recognizer.recognize_google(audio)
#             print(f"You said: {text}")
#             return text
#         except sr.UnknownValueError:
#             print("Sorry, I couldn't understand. Try typing instead.")
#             return ""
#         except sr.RequestError:
#             print("Speech recognition service is unavailable. Try typing.")
#             return ""



import speech_recognition as sr
import requests
import os
import pygame
import asyncio

# 🎧 Eleven Labs API Configuration
ELEVEN_LABS_API_KEY = "sk_39abca70825b90d6c64bcdf9f485c65e9ab8d1bc04363264"  # Replace with your actual API key
ELEVEN_LABS_VOICE_ID = "cgSgspJ2msm6clMCkdW9"  # You can change this to other voices available in Eleven Labs
ELEVEN_LABS_URL = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVEN_LABS_VOICE_ID}"


def synthesize_speech(text):
    """Uses Eleven Labs API for realistic voice synthesis."""
    headers = {
        "Content-Type": "application/json",
        "xi-api-key": ELEVEN_LABS_API_KEY,
    }
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
    
    response = requests.post(ELEVEN_LABS_URL, json=data, headers=headers)
    if response.status_code == 200:
        audio_file = "temp_output.mp3"
        with open(audio_file, "wb") as f:
            f.write(response.content)
        
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        pygame.mixer.quit()
        os.remove(audio_file)
    else:
        print("Error in TTS request:", response.text)

def speak(text):
    """Wrapper function for Eleven Labs TTS."""
    synthesize_speech(text)

# 🎤 Speech Recognition Function (Unchanged)
def recognize_speech():
    """Captures and converts speech to text with error handling."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... (speak now)")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand. Try typing instead.")
            return ""
        except sr.RequestError:
            print("Speech recognition service is unavailable. Try typing.")
            return ""
