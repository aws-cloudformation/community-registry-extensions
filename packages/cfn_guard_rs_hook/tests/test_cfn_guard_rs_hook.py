"""
    Test cfn_guard_rs_hook
"""
from dataclasses import dataclass

import pytest
from cloudformation_cli_python_lib import (
    HandlerErrorCode,
    HookInvocationPoint,
    OperationStatus,
    ProgressEvent,
)

from cfn_guard_rs_hook import GuardHook, __version__, types

from .fixtures import (
    rules_invalid_syntax,
    rules_s3_bucket_default_lock_enabled,
    rules_s3_bucket_public_access,
)
from .helpers import create_request


def test_version():
    """
    Test version value
    """
    assert __version__ == "0.1.0"


@dataclass
class TypeConfigurationObjectLockEnabled:
    """
    Test Configuration Item
    """

    # pylint: disable=invalid-name
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
            None,
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
            None,
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
                "] and got error [\n    Violation: S3 Bucket ObjectLockEnabled "
                "must be set to true.\n    Fix: Set the S3 property "
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
            rules_invalid_syntax,
            None,
            ProgressEvent(
                status=OperationStatus.FAILED,
                errorCode=HandlerErrorCode.InvalidRequest,
                message=(
                    "Parser Error when parsing Parsing Error Error parsing file  "
                    "at line 4 at column 1, when handling , fragment rule "
                    "S3_BUCKET_DEFAULT_LOCK_ENABLED when %s3_buckets_default_lock_enabled !empty "
                    "{\n  %s3_buckets_default_lock_enabled.Properties.ObjectLockEnabled exists\n"
                    '  %s3_buckets_default_lock_enabled.Properties.ObjectLockEnabled == ""\n  '
                    "<<\n    Violation: S3 Bucket ObjectLockEnabled must be set to true.\n    "
                    "Fix: Set the S3 property ObjectLockEnabled parameter to true.\n  >>\n}\n"
                ),
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
# pylint: disable=too-many-arguments
def test_transactions(
    type_name, model, invocation_point, rules, type_configuration, expected
):
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


@pytest.mark.parametrize(
    "type_name,model,expected,converters",
    [
        (
            "Community::S3Bucket::Encryption",
            {"test": {"key": "true"}},
            {
                "Resources": {
                    "ResourceName": {
                        "Type": "Community::S3Bucket::Encryption",
                        "Properties": {"test": {"key": True}},
                    }
                }
            },
            [types.Converter("test.key", types.to_bool)],
        ),
        (
            "Community::S3Bucket::Encryption",
            {"test": ["0", "1"]},
            {
                "Resources": {
                    "ResourceName": {
                        "Type": "Community::S3Bucket::Encryption",
                        "Properties": {"test": [0, 1]},
                    }
                }
            },
            [types.Converter("test[*]", types.to_int)],
        ),
        (
            "Community::S3Bucket::Encryption",
            {"Tags": [{"Key": "Key", "Value": "1"}, {"Key": "Key", "Value": "2"}]},
            {
                "Resources": {
                    "ResourceName": {
                        "Type": "Community::S3Bucket::Encryption",
                        "Properties": {
                            "Tags": [
                                {"Key": "Key", "Value": 1},
                                {"Key": "Key", "Value": 2},
                            ]
                        },
                    }
                }
            },
            [types.Converter("Tags[*].Value", types.to_int)],
        ),
        (
            "Community::S3Bucket::Encryption",
            {"test": {"nested": {"key": "3.14159"}}},
            {
                "Resources": {
                    "ResourceName": {
                        "Type": "Community::S3Bucket::Encryption",
                        "Properties": {"test": {"nested": {"key": 3.14159}}},
                    }
                }
            },
            [types.Converter("test.nested.key", types.to_float)],
        ),
    ],
)
def test_make_cloudformation(type_name, model, expected, converters):
    """
    Tests the functionality to make a CloudFormation template from the resource properties
    """
    hook = GuardHook(type_name, {}, rules_s3_bucket_default_lock_enabled, converters)

    # pylint: disable=protected-access
    assert hook._make_cloudformation(model, "ResourceName", type_name) == expected
