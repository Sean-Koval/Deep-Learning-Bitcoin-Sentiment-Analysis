### LAMBDA for pulling data using tweepy and publishing to Kinesis Firehose
#


import time
import json 
import boto3
import numpy as numpy
import pandas as pd

import tweepy as tp 
import matplotlib as plt 

# tweepy api for streaming data
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from configparser import SafeConfigParser

# intiliaze the parser for gather a batch of tweets
# we will want to have a way of filter the tweets
# NOTE: we will want to initialize a method for tracking how many tweets we have gathered in the stream as a batch (Some count) to tell the lambda when to stop
parser = SafeConfigParser()
parser.read('api_auth.cfg')

# 
# This is the super secret information that will allow access to the Twitter API and AWS Comprehend
# Twitter api access credentials and aws credentials.  (tweepy)
access_token = parser.get('api_tracker', 'access_token')
access_token_secret = parser.get('api_tracker', 'access_token_secret')
# consumer pub, secret keys (tweepy)
consumer_key = parser.get('api_tracker', 'consumer_key')
consumer_secret = parser.get('api_tracker', 'consumer_secret')
# IAM access keys: use this to access various aws products
aws_key_id =  parser.get('api_tracker', 'aws_key_id')
aws_key =  parser.get('api_tracker', 'aws_key')



DeliveryStreamName = 'test_bitcoin_tweet'

client = boto3.client('firehose', region_name='us-west-2',
                          aws_access_key_id=aws_key_id,
                          aws_secret_access_key=aws_key
                          )

# This is a basic listener that just prints received tweets and put them into the stream.
class StdOutListener(StreamListener):

    def on_data(self, data):
        data = 'Test message: This is twitter data.'
        client.put_record(DeliveryStreamName=DeliveryStreamName, Record={'Data': data})
        #    DeliveryStreamName=DeliveryStreamName,Record={'Data': json.loads(data)["text"]})
        msg=data
        print (msg)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['realdonaldtrump'])
