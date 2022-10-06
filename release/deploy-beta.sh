#!/bin/sh

set -eou pipefail

cfn-lint release/cicd.yml -i W3002

aws --profile cep-beta cloudformation package --template-file release/cicd.yml --s3-bucket community-registry-extensions-beta-packages > /tmp/cicd.yml

rain --profile cep-beta deploy -y\
    --params Env=beta,Prefix=AwsCommunity,PrefixLower=awscommunity,GitBranch=release,GitUrl=https://github.com/aws-cloudformation/community-registry-extensions.git,GitHubSecretArn=arn:aws:secretsmanager:us-east-1:676545906896:secret:cep-github-webhook-secret-L1HEni \
    /tmp/cicd.yml cep-beta

