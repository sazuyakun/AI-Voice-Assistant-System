from Model.wwd import WakeWordDetector
from Model.speech import SpeechRecognizer
from Model.llm import LanguageModel
from Model.text_to_speech import TextToSpeech

def Models():
    return WakeWordDetector(), SpeechRecognizer(), LanguageModel(), TextToSpeech()