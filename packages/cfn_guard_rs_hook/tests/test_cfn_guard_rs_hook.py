"""
    Test cfn_guard_rs_hook
"""
from dataclasses import dataclass
import pytest
from cloudformation_cli_python_lib import (
    HookInvocationPoint,
    ProgressEvent,
    OperationStatus,
    HandlerErrorCode,
)
from cfn_guard_rs_hook import __version__, GuardHook


from .helpers import create_request
from .fixtures import rules_s3_bucket_public_access, rules_s3_bucket_default_lock_enabled


def test_version():
    """
    Test version value
    """
    assert __version__ == "0.1.0"


@dataclass
class TypeConfigurationEmpty():
    """
        Test Configuration Item
    """

@dataclass
class TypeConfigurationObjectLockEnabled():
    """
        Test Configuration Item
    """
    #pylint: disable=invalid-name
    ObjectLockEnabled: str

@pytest.mark.parametrize(
    "type_name,model,invocation_point,rules,type_configuration,expected",
    [
        (
            "Community::S3Bucket::Encryption",
            {
                "resourceProperties": {
                    "PublicAccessBlockConfiguration": {
                        "BlockPublicAcls": "true",
                        "BlockPublicPolicy": "true",
                        "IgnorePublicAcls": "true",
                        "RestrictPublicBuckets": "true",
                    }
                }
            },
            HookInvocationPoint.CREATE_PRE_PROVISION,
            rules_s3_bucket_public_access,
            TypeConfigurationEmpty(),
            ProgressEvent(
                status=OperationStatus.SUCCESS,
                errorCode=None,
                message="",
                result=None,
                callbackContext=None,
                callbackDelaySeconds=0,
                resourceModel=None,
                resourceModels=None,
                nextToken=None,
            ),
        ),
        (
            "Community::S3Bucket::Encryption",
            {
                "resourceProperties": {
                    "PublicAccessBlockConfiguration": {
                        "BlockPublicAcls": "false",
                        "BlockPublicPolicy": "true",
                        "IgnorePublicAcls": "true",
                        "RestrictPublicBuckets": "true",
                    }
                }
            },
            HookInvocationPoint.CREATE_PRE_PROVISION,
            rules_s3_bucket_public_access,
            TypeConfigurationEmpty(),
            ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.NonCompliant,
                message="Rule [S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED] failed on "
                "property [/Resources/Bucket/Properties/"
                "PublicAccessBlockConfiguration/BlockPublicAcls"
                "] failed comparison operator [Eq] and not exists of [False].",
                result=None,
                callbackContext=None,
                callbackDelaySeconds=0,
                resourceModel=None,
                resourceModels=None,
                nextToken=None,
            ),
        ),
        (
            "Community::S3Bucket::Encryption",
            {
                "resourceProperties": {
                    "ObjectLockEnabled": "false",
                }
            },
            HookInvocationPoint.CREATE_PRE_PROVISION,
            rules_s3_bucket_default_lock_enabled,
            TypeConfigurationObjectLockEnabled("true"),
            ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.NonCompliant,
                message="Rule [S3_BUCKET_DEFAULT_LOCK_ENABLED] failed on "
                "property [/Resources/Bucket/Properties/ObjectLockEnabled"
                "] and got error [\n    Violation: S3 Bucket ObjectLockEnabled "\
                "must be set to true.\n    Fix: Set the S3 property "\
                "ObjectLockEnabled parameter to true.\n  ].",
                result=None,
                callbackContext=None,
                callbackDelaySeconds=0,
                resourceModel=None,
                resourceModels=None,
                nextToken=None,
            ),
        ),
        (
            "Community::S3Bucket::Encryption",
            {
                "resourceProperties": {
                    "ObjectLockEnabled": "true",
                }
            },
            HookInvocationPoint.CREATE_PRE_PROVISION,
            rules_s3_bucket_default_lock_enabled,
            TypeConfigurationObjectLockEnabled("true"),
            ProgressEvent(
                status=OperationStatus.SUCCESS,
                errorCode=None,
                message="",
                result=None,
                callbackContext=None,
                callbackDelaySeconds=0,
                resourceModel=None,
                resourceModels=None,
                nextToken=None,
            ),
        ),
    ],
)
#pylint: disable=too-many-arguments
def test_transactions(type_name, model, invocation_point, rules, type_configuration, expected):
    """
    Test a hook call
    """
    req = create_request(invocation_point, model)
    hook = GuardHook(type_name, TypeConfigurationObjectLockEnabled, rules)

    # pylint: disable=protected-access
    result = hook._invoke_handler(
        session=None,
        request=req,
        invocation_point=invocation_point,
        callback_context={},
        type_configuration=type_configuration,
    )

    assert result == expected
