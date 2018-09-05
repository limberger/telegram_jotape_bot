#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-trends
#  - lists the current global trending topics
#-----------------------------------------------------------------------

import tweepy

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
import sys
sys.path.append(".")
import config



class TwitterClass:
    def __init__(self):
        #-----------------------------------------------------------------------
        # create twitter API object
        #-----------------------------------------------------------------------
        self.auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        self.auth.set_access_token(config.access_key, config.access_secret)
        self.api = tweepy.API(self.auth)

    def getTrendsBrasil(self,nr=20):
        results = self.api.trends_place( 23424768 ) # Brazil: 	23424768
        result=[]
        print("Brazil Trends")

        for location in results:
            print(location)
            print( "---")
            for trend in location["trends"]:
                result.append((trend["name"], trend["query"], trend['tweet_volume']))

        tr_sorted=[]
        if len(result)>nr:
            tr_sorted = sorted(result, key=lambda k: k[2] if not k[2] is None else 0)[-nr:]
        else:
            tr_sorted = sorted(result, key=lambda k: k[2] if not k[2] is None else 0)

        return tr_sorted

if __name__ == '__main__':
    t=TwitterClass()
    print(t.getTrendsBrasil())
