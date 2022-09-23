#!/bin/sh

set -eou pipefail

cfn-lint release/cicd.yml

rain --profile cep-cicd deploy -y\
    --params Env=cicd,Prefix=AwsCommunity,PrefixLower=awscommunity \
    release/cicd.yml

