#!/bin/sh

set -eou pipefail

cfn-lint release/cicd-prod.yml
cfn-lint release/cicd-prod-regional.yml

rain --profile cep-prod deploy -y\
    --params SourceBucketName=community-registry-extensions-prod-source,TypeRegistrationLogBucketName=community-registry-extensions-prod-logs \
    release/cicd-prod.yml cep-prod

# TODO - Stack sets to deploy cicd-prod-regional.yml

