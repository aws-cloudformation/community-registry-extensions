#!/bin/bash
#
# Deregister all versions of a resource.
#
# This should not be done for a resource that is in production and used by customers.
# This script is more of a helper for development and testing, but we may need 
# something similar if we start to hit the limit of 50 type versions.
#
# Run this from the resource directory, for example `resources/S3_DeleteBucketContents/`

TYPE_NAME=$(cat .rpdk-config | jq -r .typeName)

# Iterate over all versions and deregister them
aws cloudformation list-type-versions --type RESOURCE --type-name $TYPE_NAME | jq     '.TypeVersionSummaries[] | .Arn' | xargs -n1 aws cloudformation deregister-type --arn

# The above will fail for the default version
aws cloudformation deregister-type --type RESOURCE --type-name $TYPE_NAME

