# Deep-Learning-Bitcoin-Sentiment-Analysis
Repository containing work for w251 final project. The project is in regards to exploring sentiment analysis and price prediction of bitcoin using deep learning and twitter data.


#  Architecture



#### Data Pipeline

* AWS Lambda (Using ECR and Docker)
 - Gather data from twitter API V2 and store in s3
 - Pulls a chunk of tweets using a filter and rate limit and then stores in S3 using Kinesis Firehose


* Kinesis Firehose
 - Contains the PUT stream 'twitter-stream' for where the data from the lambda will be processed sent through
    - This data can be intercepted before s3 by another lambda for processing or for model training/inference

* ECR: Docker
 - Used to contain the dependencies and application code for gathering the data from Twitter
 - Will contain image that will be used by SageMaker for model inference

#### Model Pipeline

* SageMaker
 - Used to pull pre-trained weights (from model)
    - This allows for the weights to be updated in s3 (within folder) and then pulled into the model
    - Output from model (inference) will be pushed to s3 bucket

* CloudWatch
 - Used to visualize the data pipeline and model output
 - Contain a time series graph of the twitter data and the sentiment (some integer value: binary classification)


#### Project Output

* Trained Deep Learning Model (classification of bitcion related sentiment)
* Pipeline: Data collection pipeline, Model Inference, Model output stored in s3 and cloudwatch
