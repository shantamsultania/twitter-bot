import tweepy

# For this you need to have a twitter acc
# A twitter developer acc
# Go to this link and make one if you don't have one already
# https://developer.twitter.com/en
# After making the acc just entr the required keys and done

# enter your keys
c_key = 'enter your Consumer API keys here'
c_sec = 'enter your Consumer API secret keys here'
a_key = 'enter your access token Access here'
a_sec = 'enter your Access token secret here'
auth = tweepy.OAuthHandler(c_key,c_sec)
auth.set_access_token(a_key,a_sec)
api = tweepy.API(auth)
user = api.me()
print(user.name)
def retweet():
    # use any keyword you wana retweet like i used kotlin
    Search = ('kotlin')
    n = 5
    for tweet in tweepy.Cursor(api.search,Search).items(n):
        try:
            tweet.retweet()
            print("tweet retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
retweet()