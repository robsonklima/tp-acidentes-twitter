from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = 'dFii2e07Tw0VaXmSuX8h6tzrz'
consumer_secret = 'KwatSfBx7fMaak286PlLQMN9OmmhYopfm042CPTPEjxLOy6PPz'
access_token = '218662081-AJAeChV4C4o2OnleI1YWMQeHpIStGsofPydgHqsZ'
access_token_secret = 'uRdVdxJqog8oh9Xnd9aSoBlD2VeEqDhgCTzxu1JGOoYoa'

class StdOutListener(StreamListener):
    def on_data(self, data):
        print(1)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['RedeBBB'])