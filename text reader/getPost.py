import requests
import json, urllib, importlib.util
import praw
import subprocess
import os
from dotenv import load_dotenv

def authenticate():
    #session = requests.Session()
    if importlib.util.find_spec("praw") == None:
        subprocess.run(["pip","install","praw"])
    if importlib.util.find_spec("requests") == None:
        subprocess.run(["python","-m","pip","install","requests"])
    reddit = praw.Reddit(
        client_id=USER,
        password=PASS
    )
    print(reddit.user.me)



def getPost(url):
    res = requests.get('https://www.reddit.com/r/AskReddit/comments/zy5kmq/what_fact_are_you_just_tired_of_explaining_to/')
    print(res)
    #foo = json.loads(res.text)
    #print(res.url)
    json_url = urllib.request.urlopen('https://www.reddit.com/r/AskReddit/comments/zy5kmq/what_fact_are_you_just_tired_of_explaining_to/')
    data = json.loads(json_url.read())
    print (data)
    #print(res.headers)
    #print(res.text)
    foo = res.json()
    #print(res.json)
    #res.json()

if __name__ == "__main__":
    # if importlib.util.find_spec("praw") == None:
    #     subprocess.run(["pip","install","praw"])
    if importlib.util.find_spec("dotenv") == None:
        subprocess.run(["pip","install","python-dotenv"])
    load_dotenv()
    USER = os.getenv('DEFAULT_USER')
    PASS = os.getenv('DEFAULT_PASS')
    #getPost("ffo")
    authenticate()