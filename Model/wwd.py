import pvporcupine
import pyaudio
# import os
import struct
# from dotenv import load_dotenv

# load_dotenv()

class WakeWordDetector:
    def __init__(self, key):
        self.porcupine = pvporcupine.create(
            keywords=["terminator"],
            access_key=key
        )  # Replace with your wake word

        self.pa = pyaudio.PyAudio()
        self.audio_stream = self.pa.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=4096
        )

    # while True:
    def listen_for_wake_word(self):
        pcm = self.audio_stream.read(self.porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
        keyword_index = self.porcupine.process(pcm)
        return keyword_index >= 0
        # if keyword_index >= 0:
            # print("Wake word detected!")
            # break
    def close(self):
        self.audio_stream.close()
        self.pa.terminate()
        self.porcupine.delete()


# detector = WakeWordDetector(os.getenv('PORCUPINE_ACCESS_KEY'))

# x = 0
# while True:
#     x+=1
#     print(x)
#     if detector.listen_for_wake_word():
#         print("Wake word detected!")
#         break

# detector.close()