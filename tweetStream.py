# -*- coding: utf-8 -*-
"""
Created on Sat May 28 10:51:08 2016

@author: Sergej
"""

import tweepy
import config
import json

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_secret)
 
api = tweepy.API(auth)

key_words = open(r'C:\Users\Sergej\Anaconda3\keywords_smoking.txt', 'r+')

key_words = key_words.read().split('\n')

class MyListener(tweepy.StreamListener):

	def on_data(self, data):

		try:
			with open('usa_smoking_test.json', 'a') as f:
				f.write(data)
				return True
		except BaseException as e:
			print("Error on_data: %s" % str(e))
		return True


            
	def on_error(self, status):
		print(status)
		return False

twitter_stream = tweepy.Stream(auth, MyListener())
twitter_stream.filter(track = key_words,\
 async = True, languages=['en'])

print ("retrieving tweets")