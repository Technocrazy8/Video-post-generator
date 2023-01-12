import json, urllib, importlib.util, requests, subprocess, os, praw
from mediumProcessing import createAudio
from dotenv import load_dotenv
from pathlib import Path
from gtts import gTTS


def authenticate():
    reddit = praw.Reddit(
        client_id=CID,
        client_secret=SEC,
        password=PASS,
        user_agent="foo",
        username=USER
    )
    print("Session acquired. Using user: ", reddit.user.me())
    return reddit

def getPost(reddit):
    print("Please enter the url of the post: ")
    posturl = input()
    print("fetching post...")
    submission = reddit.submission(url="https://www.reddit.com/r/confession/comments/1098iif/i_stole_money_from_the_rich_kids_in_my_elementary/")
    print(submission.selftext)
    return submission

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

    print("Dependencies satisfied. . .")

if __name__ == "__main__":
    checkPackageDependencies()
    load_dotenv()
    USER = os.getenv('DEFAULT_USER')
    PASS = os.getenv('DEFAULT_PASS')
    SEC = os.getenv('SECRET')
    CID = os.getenv('C')
    if(USER == None or PASS == None or SEC == None or CID == None):
        print("please create a .env file with your credentials and try again")
        quit()
    session = authenticate()
    post = getPost(session)
    createAudio(post.selftext)
