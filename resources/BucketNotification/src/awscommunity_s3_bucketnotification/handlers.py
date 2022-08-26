"""
Resource handler implementation for AwsCommunity::S3::BucketNotification
"""

import json
import logging

from cloudformation_cli_python_lib import (
    Action,
    OperationStatus,
    ProgressEvent,
    Resource,
    exceptions,
)

#from awscommunity_s3_bucketnotification.config import get, save, delete
#from awscommunity_s3_bucketnotification.models import ResourceModel

from .config import get, save, delete
from .models import ResourceModel


# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)

TYPE_NAME = "AwsCommunity::S3::BucketNotification"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint

@resource.handler(Action.CREATE)
def create_handler(session, request, callback_context):
    "Create the bucket notification"

    model = request.desiredResourceState

    progress = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    try:
        save(session, model)
        progress.status = OperationStatus.SUCCESS
    except Exception as e:
        raise exceptions.InternalFailure(e)

    return progress

@resource.handler(Action.UPDATE)
def update_handler(session, request, callback_context):
    "Update the bucket notification"

    LOG.info("update_handler calling create_handler")

    return create_handler(session, request, callback_context)

@resource.handler(Action.DELETE)
def delete_handler(session, request, callback_context):
    "Delete the bucket notification"

    
    model = request.desiredResourceState

    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    try:
        delete(session, model.BucketArn, model.Id)
        progress.status = OperationStatus.SUCCESS
    except Exception as e:
        raise exceptions.InternalFailure(e)

    return progress


@resource.handler(Action.READ)
def read_handler(session, request, callback_context):
    "Read the bucket notification"

    
    model = request.desiredResourceState
    LOG.debug("read_handler")

    try:
        model = get(session, model.BucketArn, model.Id)

        progress: ProgressEvent = ProgressEvent(
            status=OperationStatus.IN_PROGRESS,
            resourceModel=model,
        )
        progress.status = OperationStatus.SUCCESS
    except Exception as e:
        raise exceptions.InternalFailure(e)

    return progress

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
