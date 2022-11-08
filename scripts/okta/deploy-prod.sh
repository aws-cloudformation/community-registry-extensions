#!/bin/sh
#
# Run this from the release folder to deploy to the prod account

export PROFILE=cep-prod
export CEP_ENV=prod
export PACKAGE_BUCKET=community-registry-extensions-prod-packages
export PREFIX=Okta
export PREFIX_LOWER=okta
export GIT_BRANCH=release
export GIT_URL=https://github.com/aws-ia/cloudformation-okta-resource-providers
export GITHUB_SECRET_ARN=arn:aws:secretsmanager:us-east-1:676545906896:secret:cep-github-webhook-secret-L1HEni
export PROD_ACCOUNT_ID=387586997764
export BETA_ACCOUNT_ID=676545906896
export NOTIFICATION_EMAIL="tfc-builderexperience-iac-cep+${CEP_ENV}@amazon.com"

./deploy-cicd.sh okta
