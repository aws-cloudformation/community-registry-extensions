"""
Resource handler implementation for AwsCommunity::S3::BucketNotification
"""

import logging

from cloudformation_cli_python_lib import (
    Action,
    OperationStatus,
    ProgressEvent,
    HandlerErrorCode,
    Resource,
    exceptions,
)

from .config import get, save, delete
from .models import ResourceModel

VALID_TARGET_TYPES = ["Queue", "Topic", "LambdaFunction"]

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)

TYPE_NAME = "AwsCommunity::S3::BucketNotification"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint

@resource.handler(Action.CREATE)
def create_handler(session, request, callback_context): #pylint:disable=unused-argument
    "Create the bucket notification"

    model = request.desiredResourceState

    print("create_handler")
    print(model.Id)
    print(model.BucketArn)
    print(model.TargetType)
    print(model.TargetArn)
    print(model.Events)
    print(model.Filters)

    progress = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )

    if model.TargetType not in VALID_TARGET_TYPES:
        progress.status = OperationStatus.FAILED
        progress.errorCode = HandlerErrorCode.InvalidTypeConfiguration
        progress.message = "Invalid TargetType"
        return progress

    try:
        if save(session, model, True):
            progress.status = OperationStatus.SUCCESS
        else:
            progress.status = OperationStatus.FAILED
            progress.errorCode = HandlerErrorCode.AlreadyExists
            progress.message = "Already exists"
    except Exception as e:
        raise exceptions.InternalFailure(e)

    return progress

@resource.handler(Action.UPDATE)
def update_handler(session, request, callback_context): #pylint:disable=unused-argument
    "Update the bucket notification"

    model = request.desiredResourceState

    print("update_handler")
    print(model.Id)
    print(model.BucketArn)
    print(model.TargetType)
    print(model.TargetArn)
    print(model.Events)
    print(model.Filters)

    progress = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )

    if model.TargetType not in VALID_TARGET_TYPES:
        progress.status = OperationStatus.FAILED
        progress.errorCode = HandlerErrorCode.InvalidTypeConfiguration
        progress.message = "Invalid TargetType"
        return progress

    try:
        if save(session, model, False):
            progress.status = OperationStatus.SUCCESS
        else:
            progress.status = OperationStatus.FAILED
            progress.errorCode = HandlerErrorCode.NotFound
            progress.message = "Id not found"
    except Exception as e:
        raise exceptions.InternalFailure(e)

    return progress

@resource.handler(Action.DELETE)
def delete_handler(session, request, callback_context): #pylint:disable=unused-argument
    "Delete the bucket notification"

    
    model = request.desiredResourceState

    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    try:
        if delete(session, model.BucketArn, model.Id):
            progress.status = OperationStatus.SUCCESS
        else:
            progress.status = OperationStatus.FAILED
            progress.errorCode = HandlerErrorCode.NotFound
            progress.message = "Not found"
    except Exception as e:
        raise exceptions.InternalFailure(e)

    return progress


@resource.handler(Action.READ)
def read_handler(session, request, callback_context): #pylint:disable=unused-argument
    "Read the bucket notification"

    model = request.desiredResourceState
    print("read_handler")

    try:
        model = get(session, model.BucketArn, model.Id)

        if model:
            return ProgressEvent(
                status = OperationStatus.SUCCESS,
                resourceModel=model
            )
        return ProgressEvent(
            status = OperationStatus.FAILED,
            errorCode = HandlerErrorCode.NotFound,
            message = "Not found"
        )
    except Exception as e:
        raise exceptions.InternalFailure(e)

# It doesn't really make sense for us to implement a list handler here, 
# since we can't tell if we created the bucket notifications on all 
# buckets in an account.

#@resource.handler(Action.LIST)
#def list_handler(session, request, callback_context):
#    "List bucket notifications"
#
#    
#    progress: ProgressEvent = ProgressEvent(
#        status=OperationStatus.IN_PROGRESS,
#        resourceModels=None,
#    )
#    try:
#
#        progress.status = OperationStatus.SUCCESS
#    except Exception as e:
#        raise exceptions.InternalFailure(e)
#
#    return progress
#
