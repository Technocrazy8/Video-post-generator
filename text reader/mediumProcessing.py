import subprocess
import importlib.util
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from gtts import gTTS
from pathlib import Path

def createAudio(text):
    print("\nProducing audio")
    tts = gTTS(text, lang = "en")
    tts.save("test.mp3")
    print("Audio produced\n")
    #fetchVideo()

def fetchVideo():
    print("Please specify which video you would like to use or enter 'default' to use the provided one.")
    video = input()
    if(video == "default" or video == "d" or video == "Default" or video =="D"):
        print("\nUsing 'default' as video")
    else:
        print("\nUsing '", video,"' as video")
    s1 = "../video inputs/"
    s2 = ".mp4"
    vidpath = s1+video+s2
    p = Path(vidpath)
    if(p == None):
        return fetchVideo()
    vid = open(p)
    video = VideoFileClip(vid)
    if(video == None):
        return fetchVideo()
    #print(list(p.glob("*")))
    #if ()
    return video