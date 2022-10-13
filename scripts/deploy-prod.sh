#!/bin/sh
#
# Run this from the release folder to deploy to the prod account

PROFILE=cep-prod
ACCOUNT=387586997764
PUBLISH_BUILD_BUCKET_NAME=community-registry-extensions-publish-build
HANDLER_BUCKET_NAME=community-registry-extensions-prod-handler
PARAMETERS='[{"ParameterKey":"Prefix","ParameterValue":"AwsCommunity"},{"ParameterKey":"PrefixLower","ParameterValue":"awscommunity"},{"ParameterKey":"PublishBuildBucketName","ParameterValue":"community-registry-extensions-publish-build"},{"ParameterKey":"HandlerBucketName","ParameterValue":"community-registry-extensions-prod-handler"}]'

./deploy-prod.sh

