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


search_string = '@'+user.screen_name
numbersofTweets = 5
followers = dict()

'''Status with single user'''
# user2=api.get_user(screen_name='nithsua')
# Status = api.show_friendship(source_id = user.id , source_screen_name = user.screen_name, target_id = user2.id, target_screen_name = user2.screen_name)
# print(user.id)
# print(user2.id)
# print(Status)``

'''To like tweets of friends who mention me and also follow me'''
for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(numbersofTweets)):
    try:
        # tweet.favorite()
        # tweet.retweet()
        user2 = tweet.user
        Status = api.show_friendship(source_id=user.id, source_screen_name=user.screen_name,
                                     target_id=user2.id, target_screen_name=user2.screen_name)
        if Status[0].followed_by and Status[1].followed_by:
            print(tweet.text)
            print('-' + tweet.user.screen_name)
            tweet.favorite()
        print('****************************************************************')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
