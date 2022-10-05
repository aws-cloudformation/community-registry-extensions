#!/bin/sh

set -eou pipefail

cfn-lint release/cicd.yml

rain --profile cep-cicd deploy -y\
    --params Env=cicd,Prefix=AwsCommunity,PrefixLower=awscommunity,GitBranch=main,GitUrl=https://github.com/aws-cloudformation/community-registry-extensions.git \
    release/cicd.yml

