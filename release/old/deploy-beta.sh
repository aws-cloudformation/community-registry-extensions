#!/bin/sh

set -eou pipefail

STACK_NAME=cep-beta
TEMPLATE_DIR="."

if [ ! -z "${1:-}" ]
then
    TEMPLATE_DIR=$1
    STACK_NAME="cep-beta-${TEMPLATE_DIR}"
fi
TEMPLATE_FILE="${TEMPLATE_DIR}/cicd.yml"

if [ -z "${GIT_BRANCH:-}" ]
then
    GIT_BRANCH="Not-needed-for-3p-templates"
fi

if [ -z "${GIT_URL:-}" ]
then
    GIT_URL="Not-needed-for-3p-templates"
fi

if [ -z "${GITHUB_SECRET_ARN:-}" ]
then
    GITHUB_SECRET_ARN="Not-needed-for-3p-templates"
fi

cfn-lint $TEMPLATE_FILE -i W3002,W2001

aws --profile $PROFILE cloudformation package --template-file $TEMPLATE_FILE --s3-bucket $PACKAGE_BUCKET > beta-package.yml

rain --profile $PROFILE deploy  \
    --params Env=$CEP_ENV,Prefix=$PREFIX,PrefixLower=$PREFIX_LOWER,GitBranch=$GIT_BRANCH,GitUrl=$GIT_URL,GitHubSecretArn=$GITHUB_SECRET_ARN,ProdAccountId=$PROD_ACCOUNT_ID,NotificationEmail=$NOTIFICATION_EMAIL,BetaAccountId=$BETA_ACCOUNT_ID \
    beta-package.yml $STACK_NAME

