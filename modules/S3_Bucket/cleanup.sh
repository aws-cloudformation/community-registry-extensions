#!/bin/bash
# 
# Remove the integ buckets created by test/integ.yml
# They are set to retain in the module so they will be left after stack deletion

ACCOUNT_ID=$(aws sts get-caller-identity|jq -r .Account)
echo "ACCOUNT_ID is $ACCOUNT_ID"
aws s3 ls
aws s3 rb s3://cep-integ-s3-bucket-module-${ACCOUNT_ID}
aws s3 rb s3://cep-integ-log-s3-bucket-module-${ACCOUNT_ID}

