from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token ='3857401812-2jEgTo3Vj6U6DO9AUXgsRRdJrro4FZz4fTI18Yr' 
access_token_secret = 'f4BzWopX1v66sG0df6omGwRrMTPIN5ZgDsXynt5Pn7RHm'
consumer_key ='BdSJ15kEkzUPep0fL03akBryN'
consumer_key_secret = 'Rl6qRcfEd2XAiaZy0a0lQSHpEWxMaiwqIbJCvuoUO2HglXXi6f'

class StdOutListener(StreamListener):

	def on_data(self, data):
		print data
		return True

	def on_error(self, status):
		print status

if __name__ == '__main__':

	listenObj = StdOutListener()
	authrize = OAuthHandler(consumer_key, consumer_key_secret)
	authrize.set_access_token(access_token, access_token_secret)
	new_stream = Stream(authrize,listenObj)

	new_stream.filter(track=['python', 'javascript', 'ruby'])

