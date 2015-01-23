import os
import twitter
import make_markov

TWITTER_CONSUMER_KEY=os.environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET=os.environ['TWITTER_CONSUMER_SECRET']
TWITTER_ACCESS_TOKEN=os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET=os.environ['TWITTER_ACCESS_TOKEN_SECRET']

api = twitter.Api(consumer_key=TWITTER_CONSUMER_KEY,
                    consumer_secret=TWITTER_CONSUMER_SECRET,
                    access_token_key=TWITTER_ACCESS_TOKEN,
                    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

# status = make_markov.main()
# print 'status is: ', status
status = api.PostUpdate(make_markov.main())
