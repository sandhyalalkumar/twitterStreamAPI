from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'BdSJ15kEkzUPep0fL03akBryN'
csecret = 'Rl6qRcfEd2XAiaZy0a0lQSHpEWxMaiwqIbJCvuoUO2HglXXi6f'
atoken = '3857401812-2jEgTo3Vj6U6DO9AUXgsRRdJrro4FZz4fTI18Yr'
asecret = 'f4BzWopX1v66sG0df6omGwRrMTPIN5ZgDsXynt5Pn7RHm'


class listener(StreamListener):

	def on_data(self, data):
		try:
			print data
			saveFile = open('twitDB.csv','a')
			saveFile.write(data)
			saveFile.write('\n')
			saveFile.close()
			return True
		except BaseException, e:
			print 'failed ondata,',str(e)
			time.sleep(5)


	def on_error(self, status):
		print status


auth =  OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#IndvsSA"])