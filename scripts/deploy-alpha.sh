#!/bin/sh
#
# Run this from the release folder to deploy to the CICD account

export PROFILE=cep-alpha
export PACKAGE_BUCKET=community-registry-extensions-alpha-packages
export CEP_ENV=alpha
export PREFIX=AwsCommunity
export PREFIX_LOWER=awscommunity
export GIT_BRANCH=main
export GIT_URL=https://github.com/aws-cloudformation/community-registry-extensions.git
export GITHUB_SECRET_ARN=arn:aws:secretsmanager:us-east-1:531337079465:secret:github-webhook-kqkHT9
export PROD_ACCOUNT_ID=387586997764
export BETA_ACCOUNT_ID=676545906896
export NOTIFICATION_EMAIL="community-registry-extensions-alerts@amazon.com"

./deploy-cicd.sh awscommunity
