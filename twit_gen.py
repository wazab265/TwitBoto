import time
import tweepy
from dotenv import load_dotenv
import os

load_dotenv()
# environment varaiables

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
AUTH_TOKEN_SECRET = os.getenv("AUTH_TOKEN_SECRET")


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(AUTH_TOKEN, AUTH_TOKEN_SECRET)

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.followers_count > 100:
        follower.follow()
        break
