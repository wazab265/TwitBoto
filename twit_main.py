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

''' Type 2 authentication (public data access)'''
# auth2=tweepy.AppAuthHandler(API_KEY, API_SECRET)
# api2 = tweepy.API(auth2)
# for tweet in tweepy.Cursor(api2.search, q='foodandwine').items(10):
#     print(tweet.text)



api = tweepy.API(auth)
user=api.me()

def limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
      time.sleep(1000)

search_string ='@'+user.screen_name
numbersofTweets=4

followers=dict()
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

tweets=api.user_timeline(screen_name='tim_cook',count=5)


# tmp=[] 
# # create array of tweet information: username, 
# # tweet id, date/time, text
# tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
# for j in tweets_for_csv:
#     # Appending tweets to the empty array tmp
#     tmp.append(j) 
# # Printing the tweets
# for t in tmp:
#   print(t)

  


# feed_ids=dict()
# for acc_name in feed_accs:
#   feed_user=api.get_user(screen_name=acc_name) 


# print(len(feed_accs))

# for person in user.followers():
#   followers[person.id]=person.screen_name

# # user2=api.get_user(screen_name='nithsua')
# # Status = api.show_friendship(source_id = user.id , source_screen_name = user.screen_name, target_id = user2.id, target_screen_name = user2.screen_name)
# # print(user.id)
# # print(user2.id)
# # print(Status)

# #To like tweets of friends who mention me and also follow me
# for tweet in limit_handler(tweepy.Cursor(api.search,search_string).items(numbersofTweets)):
#   try:
#     #tweet.favorite()
#     #tweet.retweet()
#     user2=tweet.user
#     Status=api.show_friendship(source_id=user.id,source_screen_name=user.screen_name,target_id=user2.id,target_screen_name=user2.screen_name)
#     if Status[0].followed_by and Status[1].followed_by:
#       print(tweet.text)
#       print('-'+ tweet.user.screen_name)
#       tweet.favorite()
#     print('****************************************************************')
#   except tweepy.TweepError as e:
#     print(e.reason)
#   except StopIteration:
#     break
