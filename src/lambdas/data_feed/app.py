### LAMBDA for pulling data using tweepy and publishing to Kinesis Firehose
#

import json
import boto3

def lambda_handler(event, context):
    
    
    DeliveryStreamName = 'bitcoin_tweets'

    client = boto3.client('firehose', region_name='us-east-1')
                          #aws_access_key_id=aws_key_id,
                          #aws_secret_access_key=aws_key
                          #)

    
    
    data = b'Test message: This is twitter data.'
    try:
        # client.put_record(DeliveryStreamName=DeliveryStreamName, Record={'Data': b'foo'})
        response = client.put_record(
            DeliveryStreamName=DeliveryStreamName,
            Record={
                'Data': b'bytes'
            }
        )

        print("sucess")
    
    except Exception as e:
        print(e)
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': data
    }