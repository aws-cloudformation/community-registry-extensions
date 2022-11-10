#!/bin/bash
#
# Deregister all private versions of a resource in a region.
#
# Does not un-publish any published versions.
#
# Run this from the resource directory, for example `resources/S3_DeleteBucketContents/`
#
# Args
#
#   $1 Region

AWS_REGION=$1

TYPE_NAME=$(cat .rpdk-config | jq -r .typeName)

# Iterate over all versions and deregister them
aws cloudformation --region $AWS_REGION list-type-versions --type RESOURCE --type-name $TYPE_NAME | jq     '.TypeVersionSummaries[] | .Arn' | xargs -n1 aws cloudformation --region $AWS_REGION deregister-type --arn

# The above will fail for the default version
aws cloudformation --region $AWS_REGION deregister-type --type RESOURCE --type-name $TYPE_NAME

