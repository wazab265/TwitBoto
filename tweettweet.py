import tweepy
import time
auth = tweepy.OAuthHandler('bU1kKCSj4Jd3cdBp6ZrYxKxki', 'uN5lP77cegAhrjO6oKBxTngBmAXnotWvo6kHzsUgnaoYkbJDPE')
auth.set_access_token('1473939311317766146-PLiHu6sJDaZ7nsU1xNDa8w2U9q8PNX', 'Be2ST3qQfRRJyeYARplThLczddouaj0oFxGgN6Swp4XhJ')

api = tweepy.API(auth)
user=api.me()
print(user.followers_count)

def limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
      time.sleep(1000)
#Generous bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
  if follower.followers_count>100:
    follower.follow()
    break