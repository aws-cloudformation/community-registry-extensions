#!/bin/sh
#
# Run this from the release folder to deploy third party pipelines
#
# For example, to deploy the Okta pipeline to the Alpha account:
#
#    ./deploy-3p.sh okta alpha
#
# Remember to deploy them in this order: alpha, prod, beta

export PREFIX_LOWER=$1
export CEP_ENV=$2
export PROFILE=cep-${CEP_ENV}
export PACKAGE_BUCKET=community-registry-extensions-alpha-packages
if [ "$CEP_ENV" == "alpha" ]
then
    export GIT_BRANCH=main
else
    export GIT_BRANCH=release
fi
export GIT_URL=https://github.com/aws-ia/cloudformation-${PREFIX_LOWER}-resource-providers
export GITHUB_SECRET_ARN=arn:aws:secretsmanager:us-east-1:531337079465:secret:github-webhook-kqkHT9
export PROD_ACCOUNT_ID=387586997764
export BETA_ACCOUNT_ID=676545906896
export NOTIFICATION_EMAIL="community-registry-extensions-alerts@amazon.com"

./deploy-cicd.sh ${PREFIX_LOWER}
