#!/bin/sh

set -eou pipefail

cfn-lint release/cicd.yml

rain --profile cep-beta deploy -y\
    --params Env=beta,Prefix=AwsCommunity,PrefixLower=awscommunity,GitBranch=main,GitUrl=https://github.com/aws-cloudformation/community-registry-extensions.git \
    release/cicd.yml cep-beta

