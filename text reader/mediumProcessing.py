import subprocess
import importlib.util
from gtts import gTTS

def createAudio(text):
    print("Producing audio")
    tts = gTTS(text, lang = "en")
    tts.save("test.mp3")
    print("Audio produced")