from mutagen.wave import WAVE
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from gtts import gTTS
from pathlib import Path

AUDIO_FILE_LENGTH = None
AUDIO_FILE = None

def runFetchVideo(text):
    createAudio(text)
    video = fetchVideo()
    return video

def createAudio(text):
    print("\nProducing audio")
    tts = gTTS(text, lang = "en")
    tts.save("test.wav")
    AUDIO_FILE_LENGTH = int(WAVE("test.wav").info.length)
    print("Audio produced\n")

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
    try:
        vid = open(p)
    except:
        print("An error occured while fetching video\n")
        print("Perhaps the video name was spelt wrong?")
        return fetchVideo()
    
    video = VideoFileClip(vid)

    if(video == None):
        print("Error fetching video")
        return fetchVideo()
    #print(list(p.glob("*")))
    #if ()
    return video