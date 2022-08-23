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

from .models import ResourceModel
from .config import save

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)

# TODO - This needs to be dynamic. `Community::` when we GA an extension
# Or not... recommendation is to not change names...
TYPE_NAME = "CommunityAlpha::S3::BucketNotification"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint

@resource.handler(Action.CREATE)
def create_handler(session, request, callback_context):
    "Create the bucket notification"

    LOG.debug(json.dumps(session))
    LOG.debug(json.dumps(request))
    LOG.debug(json.dumps(callback_context))

    model = request.desiredResourceState
    LOG.debug(json.dumps(model))

    progress = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    try:
        client = session.client("s3")

        save(client, model)

        progress.status = OperationStatus.SUCCESS
    except Exception as e:
        raise exceptions.InternalFailure(e)

    return progress

@resource.handler(Action.UPDATE)
def update_handler(session, request, callback_context):
    "Update the bucket notification"

    LOG.debug(json.dumps(session))
    LOG.debug(json.dumps(request))
    LOG.debug(json.dumps(callback_context))
    
    model = request.desiredResourceState
    LOG.debug(json.dumps(model))

    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=model,
    )
    
    try:
        client = session.client("s3")

        #TODO

        progress.status = OperationStatus.SUCCESS
    except Exception as e:
        raise exceptions.InternalFailure(e)

    return progress


@resource.handler(Action.DELETE)
def delete_handler(session, request, callback_context):
    "Delete the bucket notification"

    LOG.debug(json.dumps(session))
    LOG.debug(json.dumps(request))
    LOG.debug(json.dumps(callback_context))
    
    model = request.desiredResourceState
    LOG.debug(json.dumps(model))

    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    try:
        client = session.client("s3")

        #TODO

        progress.status = OperationStatus.SUCCESS
    except Exception as e:
        raise exceptions.InternalFailure(e)

    return progress


@resource.handler(Action.READ)
def read_handler(session, request, callback_context):
    "Read the bucket notification"

    LOG.debug(json.dumps(session))
    LOG.debug(json.dumps(request))
    LOG.debug(json.dumps(callback_context))
    
    model = request.desiredResourceState
    LOG.debug(json.dumps(model))

    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    try:
        client = session.client("s3")

        #TODO

        progress.status = OperationStatus.SUCCESS
    except Exception as e:
        raise exceptions.InternalFailure(e)

    return progress


@resource.handler(Action.LIST)
def list_handler(session, request, callback_context):
    "List bucket notifications"

    LOG.debug(json.dumps(session))
    LOG.debug(json.dumps(request))
    LOG.debug(json.dumps(callback_context))
    
    progress: ProgressEvent = ProgressEvent(
        status=OperationStatus.IN_PROGRESS,
        resourceModel=None,
    )
    try:
        client = session.client("s3")

        #TODO

        progress.status = OperationStatus.SUCCESS
    except Exception as e:
        raise exceptions.InternalFailure(e)

    return progress

