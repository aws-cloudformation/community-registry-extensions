#!/bin/bash
#
# Publish an extension to all regions
#
# Run this from the extension (resource/module/hook) folder
# 
# Usage: 
# 
# cd to extension directory, e.g. resources/S3_DeleteBucketContents
#
# ../release/publish-regions.sh

EXT_TYPE=$(cat .rpdk-config | jq -r .artifact_type)
echo "EXT_TYPE is $EXT_TYPE"

regions_to_publish=(us-east-1 af-south-1 ap-east-1 ap-northeast-1 ap-northeast-2 ap-northeast-3 ap-south-1 ap-southeast-1 ap-southeast-2 ap-southeast-3 ca-central-1 eu-central-1 eu-north-1 eu-south-1 eu-west-1 eu-west-2 eu-west-3 me-central-1 me-south-1 sa-east-1 us-east-2 us-west-1 us-west-2 eu-central-2 eu-south-2 ap-south-2)
#regions_to_publish=(us-east-1)

# Errors (known issues with a few regions that we have to skip for now):

# This is a registry bug

#About to poll test status for arn:aws:cloudformation:eu-south-2:387586997764:type/resource/AwsCommunity-S3-DeleteBucketContents/00000001
#NOT_TESTED
#About to publish AwsCommunity::S3::DeleteBucketContents in eu-south-2
#An error occurred (CFNRegistryException) when calling the PublishType operation: The version 00000001 for Type AwsCommunity::S3::DeleteBucketContents needs to be tested first. Please run the TestType API on this version first.
#Publishing to eu-south-2 failed
# (Same for me-central-1)

# This has something to do with a failure when registering our prod account as a publisher.

# An error occurred (CFNRegistryException) when calling the PublishType operation: The account 387586997764 is not verified as a publisher. Please register as publisher first
#Publishing to eu-central-2 failed
#Publishing to ap-south-2 failed

# Use this to test succeed-fail locally
#regions_to_publish=(us-east-1 us-seattle)

successes=()
failures=()

cfn validate
if [ "$?" -ne 0 ]
then
    exit 1
fi
cfn generate

# Create the package
echo "About to run cfn submit --dry-run to create the package"
echo ""
cfn submit --dry-run
echo ""

TYPE_NAME=$(cat .rpdk-config | jq -r .typeName)
TYPE_NAME_LOWER="$(echo $TYPE_NAME | sed s/::/-/g | tr '[:upper:]' '[:lower:]')"
# For example, awscommunity-s3-deletebucketcontents
echo "TYPE_NAME_LOWER is $TYPE_NAME_LOWER"

ZIPFILE="${TYPE_NAME_LOWER}.zip"
echo "ZIPFILE is $ZIPFILE"

ACCOUNT_ID=$(aws sts get-caller-identity|jq -r .Account)
echo "ACCOUNT_ID is $ACCOUNT_ID"

HANDLER_BUCKET="cep-handler-${ACCOUNT_ID}"

# We only need to copy the handler zip once, since it's not regional
# We use this bucket for logs also. The only drawback is if there are 
# failures, it can be hard to sort out which log file belongs to which region.

echo "Copying schema package handler to $HANDLER_BUCKET"
aws s3 cp $ZIPFILE s3://$HANDLER_BUCKET/$ZIPFILE

for region in ${regions_to_publish[@]}
do
    echo "About to start publishing to $region"

    ../../release/deregister-all.sh $region $EXT_TYPE
    ../../release/publish.sh $region $EXT_TYPE

    if [ "$?" -eq 0 ]
    then
        echo "Publishing to $region succeeded"
        successes+=($region)
    else
        echo "Publishing to $region failed"
        failures+=($region)
    fi

done

echo "The following regions succeeded:"
for s in "${successes[@]}"
do
    echo $s
done

echo "The following regions failed:"
for f in "${failures[@]}"
do
    echo $f
done

