#!/bin/sh
#
# Run this from the release folder to deploy to the CICD account

export PROFILE=cep-cicd
export PACKAGE_BUCKET=community-registry-extensions-cicd-packages
export CEP_ENV=cicd
export PREFIX=AwsCommunity
export PREFIX_LOWER=awscommunity
export GIT_BRANCH=main
export GIT_URL=https://github.com/aws-cloudformation/community-registry-extensions.git
export GITHUB_SECRET_ARN=arn:aws:secretsmanager:us-east-1:531337079465:secret:github-webhook-kqkHT9
export PUBLISH_BUILD_BUCKET_NAME=community-registry-extensions-publish-build
export PROD_ACCOUNT_ID=387586997764

./deploy-cicd.sh
