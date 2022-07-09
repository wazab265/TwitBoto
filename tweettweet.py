from dotenv import load_dotenv
import os

load_dotenv()
#environment varaiables

API_KEY=os.getenv("API_KEY")
API_SECRET=os.getenv("API_SECRET")
AUTH_TOKEN=os.getenv("AUTH_TOKEN")
AUTH_TOKEN_SECRET=os.getenv("AUTH_TOKEN_SECRET")


import tweepy
import time


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(AUTH_TOKEN,AUTH_TOKEN_SECRET) 

api = tweepy.API(auth)
user=api.me()
print(user.followers_count)

def limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
      time.sleep(1000)

search_string ='python'
numbersofTweets=2

for tweet in limit_handler(tweepy.Cursor(api.search,search_string).items(numbersofTweets)):
  try:
    tweet.favorite()
    #tweet.retweet()
    print('I liked that tweet')
  except tweepy.TweepError as e:
    print(e.reason)
  except StopIteration:
    break












#Generous bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#   if follower.followers_count>100:
#     follower.follow()
#     break