#!/bin/bash
#
# Download a release from GitHub and copy it to the beta account to start the pipeline.
#
# This script is for the Okta resources.
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

curl --output-dir /tmp -LO https://github.com/aws-ia/cloudformation-dynatrace-resource-providers/archive/refs/tags/$FILE_NAME
cd /tmp
unzip $FILE_NAME
cd cloudformation-dynatrace-resource-providers-release-$RELEASE_NUMBER
zip source.zip -r *
aws s3 cp source.zip s3://cep-source-${ACCOUNT_ID}-beta-okta/source.zip

