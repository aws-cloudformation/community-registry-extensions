#!/bin/sh

set -eou pipefail

cfn-lint release/cicd.yml

rain --profile cep-cicd deploy -y\
    --params RepoId=ericzbeard/community-registry-extensions,Branch=release-process,GitHubConnectionArn=arn:aws:codestar-connections:us-east-1:531337079465:connection/dba82310-0865-4c7e-a874-adf7a2fdbb7a \
    release/cicd.yml

