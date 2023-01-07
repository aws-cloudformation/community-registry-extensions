"""Actions executed by the resource."""
from typing import Mapping

from cloudformation_cli_python_lib import SessionProxy
from cloudformation_cli_python_lib.exceptions import (
    AlreadyExists,
    InvalidRequest,
    AccessDenied,
    Throttling,
    ServiceInternalError,
    NotFound,
)

from .constants import TYPE_NAME
from .models import ResourceModel


def create(session: SessionProxy, model: ResourceModel, current_account_id: str):
    """Create a resource based on the model"""
    if _exists(session, model, current_account_id):
        raise AlreadyExists(TYPE_NAME, get_identifier(model))
    _put(session, model, current_account_id)


def update(session: SessionProxy, model: ResourceModel, current_account_id: str) -> None:
    """Update a resource based on the model"""
    if not _exists(session, model, current_account_id):
        raise NotFound(TYPE_NAME, get_identifier(model))
    _put(session, model, current_account_id)


def delete(session: SessionProxy, model: ResourceModel, current_account_id: str) -> None:
    """Delete a resource based on the model."""
    # We don't need to check if it exists, the API returns an error if it doesn't
    _delete(session, model, current_account_id)


def read(session: SessionProxy, model: ResourceModel, current_account_id: str) -> ResourceModel:
    """Read the resource, using the identifier in the model."""
    # We don't need to check if it exists, the API returns an error if it doesn't
    return _get(session, model, current_account_id)


def get_identifier(model: ResourceModel) -> str:
    """Return the identifier as a string (it's a combined identifier)."""
    return f"{model.AccountId}/{model.AlternateContactType}"


def _exists(session: SessionProxy, model: ResourceModel, current_account_id: str) -> bool:
    """Check if the given resource exists."""
    try:
        _get(session, model, current_account_id)
        return True
    except NotFound:
        return False


def _put(session: SessionProxy, model: ResourceModel, current_account_id: str) -> None:
    """Create or update the resource."""
    account = session.client("account")
    try:
        account.put_alternate_contact(
            AlternateContactType=model.AlternateContactType,
            EmailAddress=model.EmailAddress,
            Name=model.Name,
            PhoneNumber=model.PhoneNumber,
            Title=model.Title,
            **_api_kwargs(current_account_id, model),
        )
    except account.exceptions.ValidationException as e:
        raise InvalidRequest(e) from e
    except account.exceptions.AccessDeniedException as e:
        raise AccessDenied(e) from e
    except account.exceptions.TooManyRequestsException as e:
        raise Throttling(e) from e
    except account.exceptions.InternalServerException as e:
        raise ServiceInternalError(e) from e


def _delete(session: SessionProxy, model: ResourceModel, current_account_id: str) -> None:
    """Remove the resource."""
    account = session.client("account")
    try:
        account.delete_alternate_contact(
            AlternateContactType=model.AlternateContactType,
            **_api_kwargs(current_account_id, model),
        )
    except account.exceptions.ResourceNotFoundException as e:
        raise NotFound(TYPE_NAME, get_identifier(model)) from e
    except account.exceptions.ValidationException as e:
        raise InvalidRequest(e) from e
    except account.exceptions.AccessDeniedException as e:
        raise AccessDenied(e) from e
    except account.exceptions.TooManyRequestsException as e:
        raise Throttling(e) from e
    except account.exceptions.InternalServerException as e:
        raise ServiceInternalError(e) from e


def _get(session: SessionProxy, model: ResourceModel, current_account_id: str) -> ResourceModel:
    """Get the current configuration"""
    account = session.client("account")
    try:
        info = account.get_alternate_contact(
            AlternateContactType=model.AlternateContactType,
            **_api_kwargs(current_account_id, model),
        )["AlternateContact"]
        return ResourceModel(
            AccountId=model.AccountId,  # not returned in response
            AlternateContactType=info["AlternateContactType"],
            EmailAddress=info["EmailAddress"],
            Name=info["Name"],
            PhoneNumber=info["PhoneNumber"],
            Title=info["Title"],
        )
    except account.exceptions.ResourceNotFoundException as e:
        raise NotFound(TYPE_NAME, get_identifier(model)) from e
    except account.exceptions.ValidationException as e:
        raise InvalidRequest(e) from e
    except account.exceptions.AccessDeniedException as e:
        raise AccessDenied(e) from e
    except account.exceptions.TooManyRequestsException as e:
        raise Throttling(e) from e
    except account.exceptions.InternalServerException as e:
        raise ServiceInternalError(e) from e


def _api_kwargs(account_id: str, model: ResourceModel) -> Mapping:
    """
    Return arguments for account api that are dependend on the targeted account.

    This is needed, because the Account API will throw access denied if you specify
    the accountId when you're not the management account (even if the account id
    is your own account).
    """
    if account_id == model.AccountId:
        return {}

    return {"AccountId": model.AccountId}
