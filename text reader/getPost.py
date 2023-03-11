# import json, urllib, importlib.util, subprocess, os, praw, requests, mutagen
# from mediumProcessing import createAudio, fetchVideo
# #import mediumProcessing
# from dotenv import load_dotenv
# from pathlib import Path
# from gtts import gTTS
import praw;
#from text reader.mediumProcessing import createAudio

def runGetPost(User,Pass,Sec,Cid):
    session = authenticate(User,Pass,Sec,Cid)
    post = getPost(session)
    return post


def authenticate(USER,PASS,SEC,CID):
    reddit = praw.Reddit(
        client_id=CID,
        client_secret=SEC,
        password=PASS,
        user_agent="foo",
        username=USER
    )
    print("Session acquired. Welcome user: '", reddit.user.me(),"'\n")
    return reddit

def getPost(reddit):
    print("Please enter the url of the post: ")
    posturl = input()
    print("Fetching post...")
    #submission = reddit.submission(url=posturl)
    submission = reddit.submission(url="https://www.reddit.com/r/confession/comments/1098iif/i_stole_money_from_the_rich_kids_in_my_elementary/")
    if submission == None:
        print("Error getting post")
        getPost(reddit)
    print("Post:\n", submission.selftext)
    return submission



def test():
    return None