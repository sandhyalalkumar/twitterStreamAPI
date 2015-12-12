import tweepy

access_token ='3857401812-2jEgTo3Vj6U6DO9AUXgsRRdJrro4FZz4fTI18Yr' 
access_token_secret = 'f4BzWopX1v66sG0df6omGwRrMTPIN5ZgDsXynt5Pn7RHm'
consumer_key ='RdhuMu2XR0UyzE070GqP4HuUD'
consumer_key_secret = 'RI6IyqmEjHnypiJwmAop4vESMOPKIRL9mIKqe89Gp05QsbUW3N'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
	print " "
	print tweet.text