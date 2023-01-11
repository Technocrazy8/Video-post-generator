#pip install --upgrade google-cloud-texttospeech
import subprocess
import importlib.util

def textRead(text):
    tts = gTTS(text, lang = "en")
    tts.save("test.mp3")

if __name__ == "__main__":

    if importlib.util.find_spec("gtts") == None:
        print("gTTS not detected \nInstalling gTTS")
        subprocess.run(["pip", "install", "gTTS"])
        print("gTTS installed")
    from gtts import gTTS
    
    print("Producing audio")
    textRead("Hello, World")
    print("audio produced")