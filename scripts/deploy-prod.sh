#!/bin/sh
#
# Run this from the release folder to deploy to the prod account

export PROFILE=cep-prod
export ACCOUNT=387586997764
export BETA_ACCOUNT_ID=676545906896
export PUBLISH_BUILD_BUCKET_NAME=community-registry-extensions-publish-build
export HANDLER_BUCKET_NAME=community-registry-extensions-prod-handler
export PARAMETERS='[{"ParameterKey":"Prefix","ParameterValue":"AwsCommunity"},{"ParameterKey":"PrefixLower","ParameterValue":"awscommunity"},{"ParameterKey":"PublishBuildBucketName","ParameterValue":"community-registry-extensions-publish-build"},{"ParameterKey":"HandlerBucketName","ParameterValue":"community-registry-extensions-prod-handler"},{"ParameterKey":"BetaAccountId","ParameterValue":"676545906896"}]'

./deploy-prod.sh us-east-1 us-west-2

