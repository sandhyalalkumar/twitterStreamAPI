import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
import json, io
import sys
import pandas as pd
import thread

access_token ='3857401812-2jEgTo3Vj6U6DO9AUXgsRRdJrro4FZz4fTI18Yr' 
access_token_secret = 'f4BzWopX1v66sG0df6omGwRrMTPIN5ZgDsXynt5Pn7RHm'
consumer_key ='RdhuMu2XR0UyzE070GqP4HuUD'
consumer_key_secret = 'RI6IyqmEjHnypiJwmAop4vESMOPKIRL9mIKqe89Gp05QsbUW3N'

def user_count(ddata):
		#print "In the fun"
		user_tweets_count={}
		for jdata in ddata:
			d = json.loads(jdata)
			k = str(d['user']['screen_name'])
			if k not in user_tweets_count:
				user_tweets_count[k] = 1
			else:
				c = user_tweets_count[k]
				c = c + 1
				user_tweets_count[k] = c
		#print user_tweets_count

		print "Total no of tweets taken : %d"%(len(user_tweets_count))
		df = pd.DataFrame(user_tweets_count.items(), columns=['user', 'tweet_count'])
		df.to_csv("twitter_user_count.csv")
		print df

class listener(StreamListener):

	def __init__(self, start_time, time_limit=60):

		self.time = start_time
		self.limit = time_limit
		self.tweet_data = []



	def on_data(self, data):
		try:
			self.tweet_data.append(data)
			#print data
			#print time.time()
			#time.sleep(2)
			if(time.time() - self.time) > self.limit:
				print "Breaking Inner loop"
				thread.start_new_thread(user_count(self.tweet_data))
			except BaseException, e:
				print 'Failed on data, ', str(e)
		return True
		exit()

	def on_error(self, status):
		print status

	

if __name__ == '__main__':
	#tim = raw_input( "Enter time in minutes:")
	n = raw_input("No of Keywords:")
	n1 = int(n)
	keywords_list = []
	while(n1 > 0):
		keywords_list.append(raw_input("Enter a keyword:"))
		n1 = n1 - 1

	#print "************************************"
	#print "Please wait for %d minutes"%tim
	#print "************************************"

	start_time = time.time()
	listenObj = listener(start_time,30)
	authrize = OAuthHandler(consumer_key, consumer_key_secret)
	authrize.set_access_token(access_token, access_token_secret)
	new_stream = Stream(authrize,listenObj)
	new_stream.filter(track=keywords_list)

	
