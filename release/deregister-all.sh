#!/bin/bash
#
# Deregister all private versions of an extension in a region.
#
# Does not un-publish any published versions.
#
# Run this from the extension directory, for example `resources/S3_DeleteBucketContents/`
#
# Args
#
#   $1 Region
#   $2 RESOURCE|MODULE

AWS_REGION=$1
EXT_TYPE=$2

TYPE_NAME=$(cat .rpdk-config | jq -r .typeName)

echo "About to deregister all private versions in $AWS_REGION for $EXT_TYPE $TYPE_NAME"

# Iterate over all versions and deregister them
aws cloudformation --region $AWS_REGION list-type-versions --type $EXT_TYPE \
    --type-name $TYPE_NAME | jq     '.TypeVersionSummaries[] | .Arn' | \
    xargs -n1 aws cloudformation --region $AWS_REGION deregister-type --arn

# The above will fail for the default version
aws cloudformation --region $AWS_REGION deregister-type --type $EXT_TYPE --type-name $TYPE_NAME || true

