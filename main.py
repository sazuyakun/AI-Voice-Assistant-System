from Model.models import Models
from Features.Features import features
from dotenv import load_dotenv
import os

load_dotenv()

detector, speechRecognizer, llm, textToSpeech = Models()
musicStreamer = features()

x = 0
while True:
    # x+=1
    print('.')
    if detector.listen_for_wake_word():
        print("Hello User. How can I help?")
        
        recognized_text = speechRecognizer.listen_and_recognize()
        
        if "exit" in recognized_text.lower():
            break
        if "play" in recognized_text.lower():
            song_name = musicStreamer.get_song_name(recognized_text)
            print(f"Streaming '{song_name}'...")

            player = musicStreamer.stream_music(song_name)

            input("Press Enter to stop playback and exit...")
            player.close_player()
        
        response = llm.get_response(recognized_text)
        
        response=textToSpeech.preprocessing(response)
        
        print(response)
        textToSpeech.speak(response, type="response")
        break

detector.close()