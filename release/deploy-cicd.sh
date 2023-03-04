#!/bin/bash
#
# See scripts/deploy-*.sh for an example of how to call this
#
# You normally won't call this manually, since it requires a number of 
# environment variables to set up.

set -eou pipefail

COMMON_STACK_NAME="cep-common-${CEP_ENV}"
TEMPLATE_DIR=$1
STACK_NAME="cep-${CEP_ENV}-${TEMPLATE_DIR}"
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

if [ -z "${PREFIX:-}" ]
then
    PREFIX="Not-needed-for-3p-templates"
fi

# Deploy the common template, then the namespace-specific template


# Deploy the common stack
rain --profile $PROFILE pkg common.yml -o ${CEP_ENV}-common-package.yml
cfn-lint ${CEP_ENV}-common-package.yml -i W3002,W2001
rain --profile $PROFILE deploy --params Env=$CEP_ENV,GitUrl=$GIT_URL,GitBranch=$GIT_BRANCH,GitHubSecretArn=$GITHUB_SECRET_ARN ${CEP_ENV}-common-package.yml $COMMON_STACK_NAME

# Deploy the namespace-specific stack
rain --profile $PROFILE pkg $TEMPLATE_FILE -o ${CEP_ENV}-package.yml
cfn-lint ${CEP_ENV}-package.yml -i W3002,W2001,W8001
rain --profile $PROFILE deploy --params Env=$CEP_ENV,PrefixLower=$PREFIX_LOWER,ProdAccountId=$PROD_ACCOUNT_ID,NotificationEmail=$NOTIFICATION_EMAIL,BetaAccountId=$BETA_ACCOUNT_ID ${CEP_ENV}-package.yml $STACK_NAME

