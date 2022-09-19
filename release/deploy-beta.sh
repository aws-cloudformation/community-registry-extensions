#!/bin/sh

set -eou pipefail

cfn-lint release/cicd.yml

rain --profile cep-beta deploy -y\
    --params RepoId=ericzbeard/community-registry-extensions,Branch=beta,GitHubConnectionArn=arn:aws:codestar-connections:us-east-1:676545906896:connection/8310f1ae-92ef-415a-ae1a-176a04ce8ed4,Env=beta \
    release/cicd.yml cep-beta

