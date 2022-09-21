import logging
import traceback
from typing import Any, MutableMapping, Optional


from cloudformation_cli_python_lib import (
    Action,
    HandlerErrorCode,
    OperationStatus,
    ProgressEvent,
    Resource,
    SessionProxy,
    identifier_utils,
)

from .models import ResourceHandlerRequest, ResourceModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)

# Set logging level
# (https://docs.python.org/3/library/logging.html#levels)
# Consider using logging.DEBUG for development and testing only
LOG.setLevel(logging.DEBUG)

TYPE_NAME = "AwsCommunity::CloudFront::WebACLAssociation"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint


@resource.handler(Action.CREATE)
def create_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
) -> ProgressEvent:
    """Create Handler Method """
    model = request.desiredResourceState
    # Example:
    try:

        # primary identifier from example
        client = _get_session_client(
            session,
            "cloudfront",
        )

        webacl_association_kwargs = _webacl_association_helper(
            model=model, request=request
        )

        cloudfront_distribution_id = (
            webacl_association_kwargs["DistributionArn"].split(":")[-1].split("/")[-1]
        )
        web_acl_id = (
            webacl_association_kwargs["WebAclArn"].split(":")[-1].split("/")[-1]
        )
        response = client.get_distribution_config(Id=cloudfront_distribution_id)
        old_config = response["DistributionConfig"]
        if old_config["WebACLId"] == web_acl_id:
            return ProgressEvent(
                status=OperationStatus.FAILED,
                HandlerErrorCode=HandlerErrorCode.AlreadyExists,
                Message="The provided web ACL association configurations already exists",
            )
        etag = response["ResponseMetadata"]["HTTPHeaders"]["etag"]
        new_config = old_config
        new_config["WebACLId"] = webacl_association_kwargs["WebAclArn"]
        client.update_distribution(
            DistributionConfig=new_config,
            Id=cloudfront_distribution_id,
            IfMatch=etag,
        )
        model.Name = webacl_association_kwargs["DistributionArn"]

    except Exception as e:
        return ProgressEvent.failed(
            HandlerErrorCode.NotFound,
            "Resource creation failed due to some service exception. " + str(e),
        )

    return ProgressEvent(status=OperationStatus.SUCCESS, resourceModel=model)


@resource.handler(Action.UPDATE)
def update_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
) -> ProgressEvent:
    """Update Handler Method """
    model = request.desiredResourceState
    # TODO: put code here
    try:

        # primary identifier from example
        client = _get_session_client(
            session,
            "cloudfront",
        )
        webacl_association_kwargs = _webacl_association_helper(
            model=model, request=request
        )

        cloudfront_distribution_id = (
            webacl_association_kwargs["DistributionArn"].split(":")[-1].split("/")[-1]
        )

        response = client.get_distribution_config(Id=cloudfront_distribution_id)
        old_config = response["DistributionConfig"]
        if old_config["WebACLId"] == "":
            LOG.debug("UPDATE working cp 3")
            return ProgressEvent.failed(
                HandlerErrorCode.NotFound,
                "The provided web ACL association configurations does not exists",
            )
        etag = response["ResponseMetadata"]["HTTPHeaders"]["etag"]
        new_config = old_config
        new_config["WebACLId"] = webacl_association_kwargs["WebAclArn"]
        client.update_distribution(
            DistributionConfig=new_config,
            Id=cloudfront_distribution_id,
            IfMatch=etag,
        )
        LOG.debug("UPDATE working cp 5")
    except Exception as e:
        return ProgressEvent.failed(
            HandlerErrorCode.NotFound,
            "Resource update failed due to some service exception. " + str(e),
        )

    return ProgressEvent(status=OperationStatus.SUCCESS, resourceModel=model)


@resource.handler(Action.DELETE)
def delete_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
) -> ProgressEvent:
    """Delete Handler Method """
    model = request.desiredResourceState
    # TODO: put code here
    try:

        # primary identifier from example
        client = _get_session_client(
            session,
            "cloudfront",
        )

        webacl_association_kwargs = _webacl_association_helper(
            model=model, request=request
        )

        cloudfront_distribution_id = (
            webacl_association_kwargs["DistributionArn"].split(":")[-1].split("/")[-1]
        )

        response = client.get_distribution_config(Id=cloudfront_distribution_id)
        old_config = response["DistributionConfig"]

        if old_config["WebACLId"] == "":
            return ProgressEvent.failed(
                HandlerErrorCode.NotFound,
                "The provided web ACL association configurations does not exists",
            )
        etag = response["ResponseMetadata"]["HTTPHeaders"]["etag"]
        new_config = old_config
        new_config["WebACLId"] = ""
        client.update_distribution(
            DistributionConfig=new_config, Id=cloudfront_distribution_id, IfMatch=etag
        )

    except Exception as e:
        return ProgressEvent.failed(
            HandlerErrorCode.NotFound,
            "Resource delete failed due to some service exception. " + str(e),
        )

    return ProgressEvent(status=OperationStatus.SUCCESS, resourceModel=None)


@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
) -> ProgressEvent:
    """Read Handler Method """
    model = request.desiredResourceState
    # primary identifier from example
    try:

        client = _get_session_client(
            session,
            "cloudfront",
        )

        webacl_association_kwargs = _webacl_association_helper(
            model=model, request=request
        )

        cloudfront_distribution_id = (
            webacl_association_kwargs["DistributionArn"].split(":")[-1].split("/")[-1]
        )
        response = client.get_distribution_config(Id=cloudfront_distribution_id)
        old_config = response["DistributionConfig"]
        if old_config["WebACLId"] == "":
            return ProgressEvent.failed(
                HandlerErrorCode.NotFound,
                "The provided web ACL association configurations does not exists",
            )
    except Exception as e:
        return ProgressEvent.failed(
            HandlerErrorCode.NotFound,
            "The provided web ACL association configurations does not exists."
           + " Or the read operation failed in the custom reesource type. " + e,
        )
    return ProgressEvent(status=OperationStatus.SUCCESS, resourceModel=model)


def _get_session_client(
    session: Optional[SessionProxy],
    service_name: str,
) -> type:
    """Create and return a session client for a given service"""

    if isinstance(
        session,
        SessionProxy,
    ):
        client = session.client(
            service_name,
        )
        return client
    return None


def _webacl_association_helper(
    model: ResourceModel,
    request: ResourceHandlerRequest,
) -> dict:
    """Create and return a dictionary of arguments for import_key_pair()"""
    LOG.debug("_webacl_association_helper()")

    webacl_association_kwargs = {
        "DistributionArn": model.DistributionArn,
        "WebAclArn": model.WebAclArn,
    }

    return webacl_association_kwargs
