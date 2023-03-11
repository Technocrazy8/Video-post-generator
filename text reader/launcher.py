import dotenv, json, urllib, importlib.util, subprocess, os
from getPost import runGetPost
from mediumProcessing import runFetchVideo


def checkPackageDependencies():
    print("Checking package dependencies...")

    if importlib.util.find_spec("dotenv") == None:
        print("Python dotenv library not found. Proceeding to install. . .")
        subprocess.run(["pip","install","python-dotenv"])
    else:
        print("Python dotenv library detected")

    if importlib.util.find_spec("praw") == None:
        print("Python praw library not found. Proceeding to install. . .")
        subprocess.run(["pip","install","praw"])
    else:
        print("Python praw library detected")

    if importlib.util.find_spec("requests") == None:
        print("Python requests library not found. Proceeding to install. . .")
        subprocess.run(["python","-m","pip","install","requests"])
    else:
        print("Python requests library detected")

    if importlib.util.find_spec("gtts") == None:
        print("Python gTTS library not found. Proceeding to install. . .")
        subprocess.run(["pip", "install", "gTTS"])
    else:
        print("Python gTTS library detected")
    
    if importlib.util.find_spec("moviepy") == None:
        print("Python moviepy library not found. Proceeding to install. . .")
        subprocess.run(["pip","install","moviepy"])
    else:
        print("Python moviepy library detected")

    if importlib.util.find_spec("mutagen") == None:
        print("Python mutagen library not found. Proceeding to install. . .")
        subprocess.run(["pip","install","mutagen"])
    else:
        print("Python mutagen library detected")

    print("Dependencies satisfied. . .\n")


if __name__ == "__main__":
    checkPackageDependencies()
    dotenv.load_dotenv()
    USER = os.getenv('DEFAULT_USER')
    PASS = os.getenv('DEFAULT_PASS')
    SEC = os.getenv('SECRET')
    CID = os.getenv('C')
    if(USER == None or PASS == None or SEC == None or CID == None):
        print("please create a .env file with your credentials and try again")
        quit()
    post = runGetPost(USER,PASS,SEC,CID)
    video = runFetchVideo(post.selftext)