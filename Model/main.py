from wwd import WakeWordDetector
from speech import SpeechRecognizer
from dotenv import load_dotenv
from llm import LanguageModel
from text_to_speech import TextToSpeech
import os

load_dotenv()

detector = WakeWordDetector(os.getenv('PORCUPINE_ACCESS_KEY'))
speechRecognizer = SpeechRecognizer()
llm = LanguageModel()
textToSpeech = TextToSpeech()

x = 0
while True:
    # x+=1
    print('.')
    if detector.listen_for_wake_word():
        print("Hello User. How can I help?")
        
        recognized_text = speechRecognizer.listen_and_recognize()
        
        if "exit" in recognized_text.lower():
            break
        
        response = llm.get_response(recognized_text)
        
        response=textToSpeech.preprocessing(response)
        
        print(response)
        textToSpeech.speak(response, type="response")
        break

detector.close()