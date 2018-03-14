import tweepy
from tweepy import OAuthHandler
import csv
import json

consumer_key = 'dFii2e07Tw0VaXmSuX8h6tzrz'
consumer_secret = 'KwatSfBx7fMaak286PlLQMN9OmmhYopfm042CPTPEjxLOy6PPz'
access_token = '218662081-AJAeChV4C4o2OnleI1YWMQeHpIStGsofPydgHqsZ'
access_secret = 'uRdVdxJqog8oh9Xnd9aSoBlD2VeEqDhgCTzxu1JGOoYoa'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

new_york_geo = "40.789501,-73.976775,150km"
porto_alegre_geo = "-30.030924,-51.227636,50km"

tweets = api.search(q="Porto Alegre", geocode = porto_alegre_geo, count=100)

#for tweet in tweets:
    #csvFile = open('tweets.csv', 'a')
    #csvWriter = csv.writer(csvFile)
    #csvWriter.writerow({tweet.text.encode('utf-8')})
    #print(tweet._json)
    ##with open('tweets.json', 'w') as outfile:
        ##json.dump(tweet._json, outfile)