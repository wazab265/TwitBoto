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

def limit_handler(cursor):
  try:
    while True:
      try:
        yield cursor.next()
      except StopIteration:
        return #https://stackoverflow.com/a/51701040/14395149
  except tweepy.RateLimitError:
      time.sleep(1000)

search_string ='@'+user.screen_name
numbersofTweets=5

feed_accs=[
  'TheBoysTV',
  '@MyDearManorama',
  'DudespostingWs',
  'Apple',
  'Music_Santhosh',
  'SilambarasanTR_',
  'DCpeacemaker',
  'BetterCallSaul',
  'NaMu_Keechugal',
  'sagarcasm',
  'getpeid',
  'Cristiano',
  'every_daydad',
  'B_Fernandes8',
  'Sanchooo10',
  'Mrwhosetheboss',
  'MrBeast',
  'brfootball',
  'JColeNC',
  'AppleMusic',
  'ManUtd', #GGMU💪🏼
  'ChennaiIPL',
  'MacAddressYT',
  'BasicAppleGuy',
  'AndreiNeagoie',
  'tim_cook',
  'linusgsebastian',
  'LinusTech',
  'MKBHD',
]

feed_accs2=[
  'tim_cook',
  'linusgsebastian',
  # 'LinusTech',
  # 'MKBHD',
]

for acc_name in feed_accs2:
  for tweet in limit_handler(tweepy.Cursor(api.user_timeline,screen_name=acc_name).items(numbersofTweets)):
    try:
      tweet.favorite()
    except tweepy.TweepError as e:
      print(e.reason)
    except StopIteration:
      break
        
