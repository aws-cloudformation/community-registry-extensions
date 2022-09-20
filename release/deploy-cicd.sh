#!/bin/sh

set -eou pipefail

cfn-lint release/cicd.yml

rain --profile cep-cicd deploy -y\
    --params RepoId=ericzbeard/community-registry-extensions,Branch=hook-cicd,GitHubConnectionArn=arn:aws:codestar-connections:us-east-1:531337079465:connection/d685215c-9aa8-40ed-9a85-af65f6e623a5,Env=cicd,Prefix=AwsCommunity,PrefixLower=awscommunity \
    release/cicd.yml

