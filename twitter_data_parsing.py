import json 
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as pylot

data_path = 'twitter_data.json'

tweets_data = []
tweets_file = open(data_path, "r")

for line in tweets_file:
	try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
	except:
		continue

print len(tweets_data)

tweets = pd.DataFrame()
tweets['text'] = map(lambda tweetp:tweetp['text'], tweets_data)
tweets['lang'] = map(lambda tweetp:tweetp['lang'], tweets_data)
tweets['country'] = map(lambda tweetp:tweetp['place']['country'] if tweetp['place'] != None else None, tweets_data) 

print tweets

#tweets.to_csv('tweets_data_frame.txt', encoding='utf-8')



