"""
Handler functions for the public registry resource type
AwsCommunity::S3::DeleteBucketContents 
"""

import logging

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
TYPE_NAME = "AwsCommunity::S3::DeleteBucketContents"

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
    
    print("create_handler")
    print(model)

    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )

    try:
        # Make sure the bucket exists
        exists = check_bucket_exists(session, model.BucketName)
        if not exists:
            return progress_not_found(model.BucketName)
    except Exception as e:
        LOG.exception(e)
        raise exceptions.InternalFailure(f"Unxpected exception: {e}")

    return progress

@resource.handler(Action.DELETE)
def delete_handler(session, request, callback_context): #pylint:disable=unused-argument
    "Handle CloudFormation DELETE events"
    model = request.desiredResourceState

    print("delete_handler")
    print(model)

    progress = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )

    try:
        # Make sure the bucket exists
        s3 = session.client("s3")
        exists = check_bucket_exists(session, model.BucketName)
        if not exists:
            return progress_not_found(model.BucketName)

        # Get the contents of the bucket

        objects_to_delete = []

        has_more_results = True
        next_key_marker = None
        next_version_id_marker = None

        while has_more_results:
            contents = s3.list_object_versions(
                Bucket = model.BucketName,
                NextKeyMarker = next_key_marker, 
                NextVersionIdMarker = next_version_id_marker)

            if len(contents.Versions) == 0 and len(contents.DeleteMarkers) == 0:
                break

            for v in contents.Versions:
                objects_to_delete.append({
                    "Key": v["Key"],
                    "VersionId": v["VersionId"]
                    })

            for v in contents.DeleteMarkers:
                objects_to_delete.append({
                    "Key": v["Key"],
                    "VersionId": v["VersionId"]
                    })

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
        print(f"Bucket has {len(objects_to_delete)} objects to delete")

        # Break into chunks of 1000 or less
        def chunks(lst, n):
            "Break an array into chunks of n size"
            for i in range(0, len(lst), n):
                yield lst[i:i + n]

        # What if this takes a long time? Should we use callbacks? TODO
        for chunk in chunks(objects_to_delete, 1000):
            s3.delete_objects(Bucket=model.BucketName, Delete={"Objects": chunk})

    except Exception as e:
        LOG.exception(e)
        raise exceptions.InternalFailure(f"Unxpected exception: {e}")

    return progress


@resource.handler(Action.READ)
def read_handler(session, request, callback_context): #pylint:disable=unused-argument
    "Handle CloudFormation READ events"

    model = request.desiredResourceState
    return ProgressEvent(
        status=OperationStatus.SUCCESS,
        resourceModel=model,
    )


