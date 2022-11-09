#!/bin/bash
#
# Download a release from GitHub and copy it to the beta account to start the pipeline.
#
# Environment:
#
#   AWS_PROFILE if a default is not configured
#
# Args:
#
#   $1 release number, for example 0.1.0

set -eou pipefail

RELEASE_NUMBER=$1
FILE_NAME=release-${RELEASE_NUMBER}.zip
ACCOUNT_ID=$(aws sts get-caller-identity|jq -r .Account)

curl -LO https://github.com/aws-cloudformation/community-registry-extensions/archive/refs/tags/$FILE_NAME

aws s3 cp $FILE_NAME s3://cep-source-${ACCOUNT_ID}-beta-awscommunity/source.zip

