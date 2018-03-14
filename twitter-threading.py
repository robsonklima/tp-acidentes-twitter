import tweepy
from tweepy import OAuthHandler
import mysql.connector

config = {
  'user': 'root',
  'password': 'Mysql@2018',
  'host': '127.0.0.1',
  'database': 'crashs',
  'raise_on_warnings': True
}

consumer_key = 'dFii2e07Tw0VaXmSuX8h6tzrz'
consumer_secret = 'KwatSfBx7fMaak286PlLQMN9OmmhYopfm042CPTPEjxLOy6PPz'
access_token = '218662081-AJAeChV4C4o2OnleI1YWMQeHpIStGsofPydgHqsZ'
access_secret = 'uRdVdxJqog8oh9Xnd9aSoBlD2VeEqDhgCTzxu1JGOoYoa'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

new_york_geo = "40.789501,-73.976775,150km"
porto_alegre_geo = "-30.030924,-51.227636,100km"

from threading import Timer

def proccess():
    tweets_api = api.search(q="acidente", geocode = porto_alegre_geo, count=100)

    for tweet in tweets_api:
        if tweet.geo:        
            print(tweet.text)
            
            cnx = mysql.connector.connect(**config)
            x = cnx.cursor()
            try:
               x.execute("""INSERT INTO accidents (date_time_occured,latitude,longitude,text,is_open_data,is_twitter) VALUES (%s,%s,%s,%s,%s,%s)""",(tweet.created_at,tweet.geo['coordinates'][0],tweet.geo['coordinates'][1],tweet.text.encode('utf-8'),0,1))
               cnx.commit()
            except:
               cnx.rollback()
            x.close()
            cnx.close()
    Timer(60.0, proccess).start()

Timer(0.0, proccess).start()

