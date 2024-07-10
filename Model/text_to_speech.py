from gtts import gTTS
import pygame
import time
import re

class TextToSpeech:
    def __init__(self):
        pygame.mixer.init()
    
    def preprocessing(self, text):
        pattern = r'[^\w\s,.]'
        cleaned_text = re.sub(pattern, '', text)
        return cleaned_text

    def speak(self, text, type):
        tts = gTTS(text=text, lang='en')
        tts.save("response.mp3")
        pygame.mixer.music.load(type+".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
