#!/usr/local/bin/bash
#
# Removes the resources deployed by deploy.sh

set -eoux pipefail

TYPE_NAME=$(cat .rpdk-config | jq -r .typeName)

# Iterate over all versions and deregister them
aws cloudformation list-type-versions --type HOOK \
    --type-name $TYPE_NAME | jq '.TypeVersionSummaries[] | .Arn' | \
    xargs -n1 aws cloudformation deregister-type --arn || true

# The above will fail for the default version
aws cloudformation deregister-type --type HOOK --type-name $TYPE_NAME || true

# Delete the stack
rain rm lambda-invoker-rain-sample 

