#!/bin/bash
#
# Run from the resource directory

ACCOUNT_ID=$(aws sts get-caller-identity|jq -r .Account)
HANDLER_BUCKET="cep-handler-${ACCOUNT_ID}"
TYPE_NAME=$(cat .rpdk-config | jq -r .typeName)
TYPE_NAME_LOWER="$(echo $TYPE_NAME | sed s/::/-/g | tr '[:upper:]' '[:lower:]')"
ZIPFILE="${TYPE_NAME_LOWER}.zip"
export PARAMETERS='[{"ParameterKey":"SchemaPackageURL","ParameterValue":"'
export PARAMETERS+="s3://${HANDLER_BUCKET}/${ZIPFILE}"
export PARAMETERS+='"}]'

echo "PARAMETERS: ${PARAMETERS}"

../../release/publish.sh us-east-1 us-west-2
