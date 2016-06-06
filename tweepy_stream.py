# Necessary imports.
import tweepy

# The OAuth parameters.
consumer_key = "secret"
consumer_secret = "secret"
access_token = "secret"
access_token_secret = "secret"

# Overwrite the on_data method to specify the desired action.
class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        with open("D:\\output.json", "a") as fileobject:
            fileobject.write(data)

# Authorize.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Build the necessary keyword list.
keyword_list = []
with open("F:\\keywords_smoking.txt") as fileobject:
    for line in fileobject:
        keyword_list.append(line[:-1])

# Open the streaming api and listen.
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = MyStreamListener())
myStream.filter(track = keyword_list, async = True, languages = ["en"])
