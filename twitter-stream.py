from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#consumer key, consumer secret, access token, access secret.
ckey = 'dFii2e07Tw0VaXmSuX8h6tzrz'
csecret = 'KwatSfBx7fMaak286PlLQMN9OmmhYopfm042CPTPEjxLOy6PPz'
atoken = '218662081-AJAeChV4C4o2OnleI1YWMQeHpIStGsofPydgHqsZ'
asecret = 'uRdVdxJqog8oh9Xnd9aSoBlD2VeEqDhgCTzxu1JGOoYoa'

dSet = []

class listener(StreamListener):

    def on_data(self, data):
        dSet.append(data)
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#RedeBBB"])