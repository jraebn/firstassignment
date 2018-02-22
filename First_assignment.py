from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import json

ACCESS_TOKEN = '742081164-gjrfisrYpqmrQH9zXEfwa0pKDvwmdrGh2llQktHw'
ACCESS_SECRET = '86UGQvPW20NCO6lcQhq6lgJRAAxeARmFWy2AQnvIs16uI'
CONSUMER_KEY = '7iAPzH0aBh01X8PIFm4MdLbms'
CONSUMER_SECRET = "LhnoaACdc8R2M4UtnHuOkrwzOAimkhceIi3s6FnOS4T8xMGP2d"

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)

iterator = twitter_stream.statuses.sample()

tweet_count = 10
for tweet in iterator:
    tweet_count -= 1
    print json.dumps(tweet)

    if tweet_count <= 0:
        break
