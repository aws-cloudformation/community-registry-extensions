#!/bin/sh

set -eou pipefail

cfn-lint release/cicd.yml

rain --profile cep-cicd deploy -y\
    --params "Env=cicd,Prefix=AwsCommunity,PrefixLower=awscommunity,GitHubSecretArn=arn:aws:secretsmanager:us-east-1:531337079465:secret:github-webhook-kqkHT9,GitBranch=dockerfile,GitUrl=https://github.com/ericzbeard/community-registry-extensions.git" \
    release/cicd.yml

