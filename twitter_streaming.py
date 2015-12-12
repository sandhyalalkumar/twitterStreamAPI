from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import thread

access_token ='3857401812-2jEgTo3Vj6U6DO9AUXgsRRdJrro4FZz4fTI18Yr' 
access_token_secret = 'f4BzWopX1v66sG0df6omGwRrMTPIN5ZgDsXynt5Pn7RHm'
consumer_key ='RdhuMu2XR0UyzE070GqP4HuUD'
consumer_key_secret = 'RI6IyqmEjHnypiJwmAop4vESMOPKIRL9mIKqe89Gp05QsbUW3N'


gcount = 1

tweet_data = []
count = 0
def user_count(data):
	for i in data:
		print str(i['user']['screen_name'])
	return None

class StdOutListener(StreamListener):

	def __init__(self, start_time, time_limit, times):
		self.limit = time_limit
		self.start_time = start_time
		self.times = times
		self.tweet_data = []

	def on_data(self, data):
		#print data
		self.tweet_data.append(data)
		global gcount 
		if(time.time() - self.start_time) >= self.limit and gcount <= self.times:
			tweet_d = self.tweet_data
			self.limit =  self.limit + 30
			gcount = gcount+1
			user_count(tweet_d)
		return True

	def on_error(self, status):
		print status

if __name__ == '__main__':
	st = time.time()
	listenObj = StdOutListener(st, 30, 5)
	authrize = OAuthHandler(consumer_key, consumer_key_secret)
	authrize.set_access_token(access_token, access_token_secret)
	new_stream = Stream(authrize,listenObj)

	#new_stream.filter(track=['python', 'javascript', 'ruby']) 
	new_stream.filter(track=['ChennaiFloods'])
