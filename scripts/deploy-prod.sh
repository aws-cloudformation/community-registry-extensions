#!/bin/sh
#
# Run this from the release folder to deploy to the prod account

export PROFILE=cep-prod
export PACKAGE_BUCKET=community-registry-extensions-prod-packages
export CEP_ENV=prod
export PREFIX=AwsCommunity
export PREFIX_LOWER=awscommunity
export GIT_BRANCH=release
export GIT_URL=https://github.com/aws-cloudformation/community-registry-extensions.git
export GITHUB_SECRET_ARN=arn:aws:secretsmanager:us-east-1:676545906896:secret:cep-github-webhook-secret-L1HEni
export PROD_ACCOUNT_ID=387586997764
export BETA_ACCOUNT_ID=676545906896
export NOTIFICATION_EMAIL="community-registry-extensions-alerts@amazon.com"

./deploy-cicd.sh awscommunity
