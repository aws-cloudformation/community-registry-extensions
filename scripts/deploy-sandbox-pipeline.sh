#!/bin/bash
#
# Deploy all sandbox environment pipelines into 1 account
# 
# Run from the release folder

set -eou pipefail

export PROFILE=developer-profile
export AWS_ACCOUNT=developer-aws-account-id
export AWS_REGION=us-east-1
export PREFIX=AwsCommunity
export PREFIX_LOWER=awscommunity
export GIT_URL=https://github.com/developer-fork/community-registry-extensions.git
export GITHUB_SECRET_ARN=arn:aws:secretsmanager:$AWS_REGION:$AWS_ACCOUNT:secret:github-webhook-developer-secret-ARN
export PROD_ACCOUNT_ID=$AWS_ACCOUNT
export BETA_ACCOUNT_ID=$AWS_ACCOUNT
export NOTIFICATION_EMAIL="developer@email.com"
export IMAGE_REPO="cep-cicd"

aws --profile $PROFILE --region $AWS_REGION ecr describe-repositories --repository-names $IMAGE_REPO || \
    aws --profile $PROFILE --region $AWS_REGION ecr create-repository --repository-name $IMAGE_REPO

./deploy-build-image.sh $AWS_ACCOUNT $PROFILE $AWS_REGION

export CEP_ENV=alpha
export GIT_BRANCH=main
export PACKAGE_BUCKET=developer-alpha-packages

./deploy-cicd.sh $PREFIX_LOWER

export CEP_ENV=prod
export GIT_BRANCH=release
export PACKAGE_BUCKET=developer-prod-packages

./deploy-cicd.sh $PREFIX_LOWER

export CEP_ENV=beta
export GIT_BRANCH=release
export PACKAGE_BUCKET=developer-beta-packages
./deploy-cicd.sh $PREFIX_LOWER

