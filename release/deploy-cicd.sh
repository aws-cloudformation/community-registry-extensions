#!/bin/sh

set -eou pipefail

cfn-lint release/cicd.yml -i W3002

aws --profile cep-cicd cloudformation package --template-file release/cicd.yml --s3-bucket community-registry-extensions-cicd-packages > /tmp/cicd.yml

rain --profile cep-cicd deploy -y\
    --params Env=cicd,Prefix=AwsCommunity,PrefixLower=awscommunity,GitBranch=main,GitUrl=https://github.com/aws-cloudformation/community-registry-extensions.git,GitHubSecretArn=arn:aws:secretsmanager:us-east-1:531337079465:secret:github-webhook-kqkHT9 \
    /tmp/cicd.yml cep-cicd

