#!/bin/bash
set -eou pipefail

ACCOUNT=$1
PROFILE=$2

aws --profile $PROFILE ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ACCOUNT.dkr.ecr.us-east-1.amazonaws.com
docker build -t cep-codebuild .
docker tag cep-codebuild:latest $ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/cep-cicd
docker push $ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/cep-cicd


