import subprocess
import importlib.util
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from gtts import gTTS

def createAudio(text):
    print("\nProducing audio")
    tts = gTTS(text, lang = "en")
    tts.save("test.mp3")
    print("Audio produced")
    #fetchVideo()

def fetchVideo():
    print("Please specify which video you would like to use or enter 'default' to use the provided one.")
    video = input()
    if(video == "default" or video == "d" or video == "Default"):
        print("\nUsing 'default' as video")
    else:
        print("\nUsing '", video,"' as video")
    return video