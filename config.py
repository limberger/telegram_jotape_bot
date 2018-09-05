#--------------------------------------------------------------------------------
# These tokens are needed for user authentication.
# Credentials can be generates via Twitter's Application Management:
#	https://apps.twitter.com/app/new
#--------------------------------------------------------------------------------
# config from twitter
# getting from env vars

#sample (create a shell script in a file in .gitignore (in mais case: .secret)
#export TWITTER_CONSUMER_KEY='xxxxxxxxxxxxxxxxxxxxxxxxx'
#export TWITTER_CONSUMER_SECRET='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
#export TWITTER_ACCESS_KEY='00000000-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
#export TWITTER_ACCESS_SECRET='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
#heroku config:set TELEGRAM_TOKEN="$TELEGRAM_TOKEN"
#heroku config:set TWITTER_CONSUMER_KEY="$TWITTER_CONSUMER_KEY"
#heroku config:set TWITTER_CONSUMER_SECRET="$TWITTER_CONSUMER_SECRET"
#heroku config:set TWITTER_ACCESS_KEY="$TWITTER_ACCESS_KEY"
#heroku config:set TWITTER_ACCESS_SECRET="$TWITTER_ACCESS_SECRET"

import os

consumer_key = os.environ['TWITTER_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
access_key = os.environ['TWITTER_ACCESS_KEY']
access_secret = os.environ['TWITTER_ACCESS_SECRET']
