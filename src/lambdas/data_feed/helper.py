# ssh from vscode into instnce
# ssh ubuntu@ec2-184-72-196-52.compute-1.amazonaws.com


### Getting tweet volume count
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace with your own search query
query = 'covid -is:retweet'

counts = client.get_recent_tweets_count(query=query, granularity='day')

for count in counts:
    print(count)



### Writing tweets to a file
import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace with your own search query
query = 'covid -is:retweet'

# Name and path of the file where you want the Tweets written to
file_name = 'tweets.txt'

with open(file_name, 'a+') as filehandle:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                                  tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(
            limit=1000):
        filehandle.write('%s\n' % tweet.id)


### getting more than 100 tweets at a time

import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace with your own search query
query = 'covid -is:retweet'

# Replace the limit=1000 with the maximum number of Tweets you want
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                              tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=1000):
    print(tweet.id)




### return recent tweets from the last 7 days

import tweepy

client = tweepy.Client(bearer_token='REPLACE_ME')

# Replace with your own search query
query = 'from:suhemparack -is:retweet'

tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)