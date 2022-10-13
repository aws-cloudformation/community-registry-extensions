#!/bin/sh
#
# Run this from the release folder to deploy to the beta account

PROFILE=cep-beta
PACKAGE_BUCKET=community-registry-extensions-beta-packages
CEP_ENV=beta
PREFIX=AwsCommunity
PREFIX_LOWER=awscommunity
GIT_BRANCH=release
GIT_URL=https://github.com/aws-cloudformation/community-registry-extensions.git
GITHUB_SECRET_ARN=arn:aws:secretsmanager:us-east-1:676545906896:secret:cep-github-webhook-secret-L1HEni
PUBLISH_BUILD_BUCKET_NAME=community-registry-extensions-publish-build

./deploy-cicd.sh
