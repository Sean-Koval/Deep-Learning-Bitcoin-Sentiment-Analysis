#!/bin/bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com    

docker build -t logger .
docker tag logger seankoval/logger:v1
# URI

docker tag  hello-world:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest
docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/hello-world:latest

# call update function code


aws lambda update-function-code \
    --function-name  my-function \
    --image-uri docker push 576656114337.dkr.ecr.us-east-1.amazonaws.com/bitcoin-twitter-ml:latest

docker push seankoval/logger:v1i