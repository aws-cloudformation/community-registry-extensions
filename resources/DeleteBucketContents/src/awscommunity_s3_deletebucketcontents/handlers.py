"""
Handler functions for the public registry resource type
AwsCommunity::S3::DeleteBucketContents 
"""
#pylint:disable=too-many-branches

import json
import logging

import botocore

from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    exceptions,
)

from .models import ResourceModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
TYPE_NAME = "AwsCommunity::S3::DeleteBucketContents"
DELETE_BUCKET_CONTENTS_TAG = "aws-community-delete-bucket-contents"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint

def check_bucket_exists(session, bucket_name):
    "Check to see if the bucket exists"
    s3 = session.client("s3")
    try:
        s3.head_bucket(Bucket=bucket_name)
        return True
    except s3.exceptions.NoSuchBucket:
        LOG.error("Bucket does not exist: %s", bucket_name)
        return False

def check_tag(session, bucket_name):
    "Check to see if the deletion tag is on the bucket"
    s3 = session.client("s3")
    try:
        tags = s3.get_bucket_tagging(Bucket=bucket_name)
        if "TagSet" in tags:
            for tag in tags["TagSet"]:
                if tag["Key"] == DELETE_BUCKET_CONTENTS_TAG and tag["Value"] == "true":
                    return True
    except botocore.exceptions.ClientError as ce:
        # It looks like we can't actually catch s3.exceptions.NoSuchTagSet like we need to
        if "NoSuchTagSet" not in str(ce):
            raise ce
    return False

def create_tag(session, bucket_name):
    "Create the deletion tag on the bucket"
    s3 = session.client("s3")
    tags = None
    try:
        tags = s3.get_bucket_tagging(Bucket=bucket_name)
    except botocore.exceptions.ClientError as ce:
        # It looks like we can't actually catch s3.exceptions.NoSuchTagSet like we need to
        if "NoSuchTagSet" not in str(ce):
            raise ce

    if not tags:
        tags = {}
        tags["TagSet"] = []

    tags["TagSet"].append({"Key": DELETE_BUCKET_CONTENTS_TAG, "Value": "true"})
    s3.put_bucket_tagging(Bucket=bucket_name, Tagging={"TagSet": tags["TagSet"]})

def remove_tag(session, bucket_name):
    "Remove the deletion tag from the bucket"

    s3 = session.client("s3")
    tags = None
    try:
        tags = s3.get_bucket_tagging(Bucket=bucket_name)
    except botocore.exceptions.ClientError as ce:
        # It looks like we can't actually catch s3.exceptions.NoSuchTagSet like we need to
        if "NoSuchTagSet" not in str(ce):
            raise ce

    if not tags:
        return 

    new_tags = []
    for tag in tags["TagSet"]:
        # Append everything except our tag, leave everything else alone
        if tag["Key"] != DELETE_BUCKET_CONTENTS_TAG:
            new_tags.append(tag)
    s3.put_bucket_tagging(Bucket=bucket_name, Tagging={"TagSet": new_tags})

def progress_not_found(bucket_name):
    "Returns a not found progress event"
    return ProgressEvent(
        status = OperationStatus.FAILED,
        message = f"Bucket does not exist: {bucket_name}",
        errorCode = HandlerErrorCode.NotFound
    )

@resource.handler(Action.CREATE)
def create_handler(session, request, callback_context): #pylint:disable=unused-argument
    "Handle CloudFormation CREATE events"
    
    model = request.desiredResourceState
    
    LOG.debug("create_handler")
    LOG.debug("model: %s", json.dumps(model, default=str))

    progress = ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )

    try:
        # Make sure the bucket exists
        exists = check_bucket_exists(session, model.BucketName)
        if not exists:
            return progress_not_found(model.BucketName)

        # Check to see if this resource was already created
        has_tag = check_tag(session, model.BucketName)
        if has_tag:
            msg = f"Bucket is already tagged for content deletion: {model.BucketName}"
            return ProgressEvent(
                status = OperationStatus.FAILED,
                message = msg, 
                errorCode = HandlerErrorCode.AlreadyExists
            )

        # Create the tag so we know we already did this
        create_tag(session, model.BucketName)
            
    except Exception as e:
        LOG.exception(e)
        raise exceptions.InternalFailure(f"Unxpected exception: {e}")

    return progress

@resource.handler(Action.DELETE)
def delete_handler(session, request, callback_context): #pylint:disable=unused-argument
    "Handle CloudFormation DELETE events"
    model = request.desiredResourceState

    LOG.debug("delete_handler")
    LOG.debug("model: %s", json.dumps(model, default=str))

    try:
        # Make sure the bucket exists
        s3 = session.client("s3")
        exists = check_bucket_exists(session, model.BucketName)
        if not exists:
            return progress_not_found(model.BucketName)

        # Verify the tag
        if not check_tag(session, model.BucketName):
            return ProgressEvent(
                status = OperationStatus.FAILED,
                message = f"Bucket is not tagged for content deletion: {model.BucketName}",
                errorCode = HandlerErrorCode.NotFound)

        # Get the contents of the bucket

        objects_to_delete = []

        has_more_results = True
        next_key_marker = None
        next_version_id_marker = None

        while has_more_results:
            args = {
                "Bucket": model.BucketName
            }
            if next_key_marker:
                args["KeyMarker"] = next_key_marker
                args["VersionIdMarker"] = next_version_id_marker
            contents = s3.list_object_versions(**args)

            # This causes a failure if there are too many objects!
            #LOG.debug("contents: %s", json.dumps(contents, default=str))

            if "Versions" not in contents and "DeleteMarkers" not in contents:
                LOG.debug("Versions or DeleteMarkers not found in contents")
                break

            if "Versions" in contents:
                for v in contents["Versions"]:
                    d = {"Key": v["Key"]}
                    if "VersionId" in v and v["VersionId"] != "null":
                        d["VersionId"] = v["VersionId"]
                    objects_to_delete.append(d)

            if "DeleteMarkers" in contents:
                for v in contents["DeleteMarkers"]:
                    d = {"Key": v["Key"]}
                    if "VersionId" in v and v["VersionId"] != "null":
                        d["VersionId"] = v["VersionId"]
                    objects_to_delete.append(d)

            if len(objects_to_delete) == 0:
                LOG.debug("objects_to_delete is empty")
                break

            if contents["IsTruncated"] is True:
                has_more_results = True
                next_key_marker = contents["NextKeyMarker"] 
                next_version_id_marker = contents["NextVersionIdMarker"]
                if next_key_marker is None or next_version_id_marker is None:
                    LOG.warning("NextKeyMarker and NextVersionIdMarker not set")
                    break
            else:
                has_more_results = False

        # Delete the contents
        LOG.debug("Bucket has %s objects to delete", len(objects_to_delete))

        # Break into chunks of 1000 or less
        def chunks(lst, n):
            "Break an array into chunks of n size"
            for i in range(0, len(lst), n):
                yield lst[i:i + n]

        # What if this takes a long time? Should we use callbacks? TODO
        for chunk in chunks(objects_to_delete, 1000):
            LOG.debug("About to delete chunk: %s", json.dumps(chunk, default=str))
            r = s3.delete_objects(Bucket=model.BucketName, Delete={"Objects": chunk})
            LOG.debug("delete_objects response: %s", json.dumps(r, default=str))

        LOG.debug("All chunks deleted, about to remove the tag")
        # TODO - Confirm that the bucket is empty

        # Remove our tag from the bucket
        remove_tag(session, model.BucketName)

        progress = ProgressEvent(
            status=OperationStatus.SUCCESS,
            resourceModel=None,
        )

    except Exception as e:
        LOG.exception(e)
        raise exceptions.InternalFailure(f"Unxpected exception: {e}")

    return progress


@resource.handler(Action.READ)
def read_handler(session, request, callback_context): #pylint:disable=unused-argument
    "Handle CloudFormation READ events"

    model = request.desiredResourceState

    LOG.debug("read_handler")
    LOG.debug("model: %s", json.dumps(model, default=str))

    exists = check_bucket_exists(session, model.BucketName)
    if not exists:
        return progress_not_found(model.BucketName)

    # Verify the tag
    if not check_tag(session, model.BucketName):
        return ProgressEvent(
            status = OperationStatus.FAILED,
            message = f"Bucket is not tagged for content deletion: {model.BucketName}",
            errorCode = HandlerErrorCode.NotFound)

    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )


