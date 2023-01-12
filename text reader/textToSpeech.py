import subprocess
import importlib.util
from gtts import gTTS

def createAudio(text):
    # while True:
    #     print("Please pick your language:")
    #     print("1 - english")
    print("Producing audio")
    tts = gTTS(text, lang = "en")
    tts.save("test.mp3")
    print("Audio produced")
