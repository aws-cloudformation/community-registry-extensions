#!/bin/sh
#
# Run this from the release folder to deploy to the CICD account

PROFILE=cep-cicd
PACKAGE_BUCKET=community-registry-extensions-cicd-packages
CEP_ENV=cicd
PREFIX=AwsCommunity
PREFIX_LOWER=awscommunity
GIT_BRANCH=main
GIT_URL=https://github.com/aws-cloudformation/community-registry-extensions.git
GITHUB_SECRET_ARN=arn:aws:secretsmanager:us-east-1:531337079465:secret:github-webhook-kqkHT9
PUBLISH_BUILD_BUCKET_NAME=community-registry-extensions-publish-build

./deploy-cicd.sh
