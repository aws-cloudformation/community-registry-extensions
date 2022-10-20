#!/bin/sh

set -eou pipefail

cfn-lint cicd.yml -i W3002

aws --profile $PROFILE cloudformation package --template-file cicd.yml --s3-bucket $PACKAGE_BUCKET > cicd-package.yml

rain --profile $PROFILE deploy -y \
    --params Env=$CEP_ENV,Prefix=$PREFIX,PrefixLower=$PREFIX_LOWER,GitBranch=$GIT_BRANCH,GitUrl=$GIT_URL,GitHubSecretArn=$GITHUB_SECRET_ARN,PublishBuildBucketName=$PUBLISH_BUILD_BUCKET_NAME,ProdAccountId=$PROD_ACCOUNT_ID \
    cicd-package.yml cep-beta

