#!/bin/bash
set -eou pipefail

ACCOUNT=$1
PROFILE=$2
AWS_REGION=$3

aws --profile $PROFILE ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com
docker build --progress=plain -t cep-codebuild .
docker tag cep-codebuild:latest $ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com/cep-cicd
docker push $ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com/cep-cicd
