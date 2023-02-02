"""
    Test cfn_guard_rs
"""
from unittest.mock import patch
import json
import yaml
import pytest
import cfn_guard_rs.errors
from cfn_guard_rs import Comparison, run_checks, DataOutput, NameInfo


@pytest.mark.parametrize(
    "template,rules,expected",
    [
        (
            "python/tests/fixtures/templates/s3_bucket_name_valid.yaml",
            "python/tests/fixtures/rules/s3_bucket_name.guard",
            DataOutput(
                data_from="cfn_guard_rs",
                rules_from="cfn_guard_rs",
                not_compliant={},
                not_applicable=[],
                compliant=["default"],
            ),
        ),
        (
            "python/tests/fixtures/templates/s3_bucket_name_invalid.yaml",
            "python/tests/fixtures/rules/s3_bucket_name.guard",
            DataOutput(
                data_from="cfn_guard_rs",
                rules_from="cfn_guard_rs",
                not_compliant={
                    "default": [
                        NameInfo(
                            rule="default",
                            path="/Resources/Bucket/Properties/BucketName",
                            provided=1,
                            expected=None,
                            comparison=Comparison(
                                operator="IsString", not_operator_exists=False
                            ),
                            message="",
                            error=None,
                        )
                    ]
                },
                not_applicable=[],
                compliant=[],
            ),
        ),
        (
            "python/tests/fixtures/templates/s3_bucket_public_access_valid.yaml",
            "python/tests/fixtures/rules/s3_bucket_public_access.guard",
            DataOutput(
                data_from="cfn_guard_rs",
                rules_from="cfn_guard_rs",
                not_compliant={},
                not_applicable=[],
                compliant=["S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED"],
            ),
        ),
        (
            "python/tests/fixtures/templates/s3_bucket_public_access_invalid.yaml",
            "python/tests/fixtures/rules/s3_bucket_public_access.guard",
            DataOutput(
                data_from="cfn_guard_rs",
                rules_from="cfn_guard_rs",
                not_compliant={
                    "S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED": [
                        NameInfo(
                            rule="S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED",
                            # pylint: disable=line-too-long
                            path="/Resources/Bucket/Properties/PublicAccessBlockConfiguration/BlockPublicAcls",
                            provided="false",
                            expected="true",
                            comparison=Comparison(
                                operator="Eq", not_operator_exists=False
                            ),
                            message="",
                            error=None,
                        )
                    ]
                },
                not_applicable=[],
                compliant=[],
            ),
        ),
    ],
)
def test_run_checks(template, rules, expected):
    """Test transactions against run_checks"""
    with open(template, encoding="utf8") as file:
        template_str = yaml.safe_load(file)
    with open(rules, encoding="utf8") as file:
        rules = file.read()

    result = run_checks(template_str, rules)
    assert result == expected


@pytest.mark.parametrize(
    "template,rules,error,parent_error,message",
    [
        (
            "python/tests/fixtures/templates/s3_bucket_public_access_valid.yaml",
            "python/tests/fixtures/rules/invalid_missing_value.guard",
            cfn_guard_rs.errors.MissingValueError,
            NameError,
            (
                "Could not resolve variable by name "
                "ecs_task_definition_execution_role_arn across scopes"
            ),
        ),
        (
            "python/tests/fixtures/templates/s3_bucket_public_access_valid.yaml",
            "python/tests/fixtures/rules/invalid_format.guard",
            cfn_guard_rs.errors.ParseError,
            ValueError,
            (
                "Parser Error when parsing Parsing Error Error parsing file  "
                "at line 1 at column 17, when handling , fragment "
                "{\n    Properties\n        BucketName is_string\n    }\n}\n"
            ),
        ),
    ],
)
def test_run_checks_errors(template, rules, error, parent_error, message):
    """Test transactions against run_checks"""
    with open(template, encoding="utf8") as file:
        template_str = yaml.safe_load(file)
    with open(rules, encoding="utf8") as file:
        rules = file.read()

    with pytest.raises(error, match=message):
        run_checks(template_str, rules)

    with pytest.raises(parent_error, match=message):
        run_checks(template_str, rules)

    with pytest.raises(cfn_guard_rs.errors.GuardError, match=message):
        run_checks(template_str, rules)


@patch("cfn_guard_rs.api.run_checks_rs")
def test_json_decode_error(mock_run_check_rs):
    """Test JSON Decode errors"""

    mock_run_check_rs.return_value = '{ "bad": }'

    with pytest.raises(json.JSONDecodeError):
        run_checks("{}", "")


def test_run_unknown_errors():
    """Test unknown errors"""

    template_filename = "python/tests/fixtures/templates/s3_bucket_name_valid.yaml"
    rules_filename = "python/tests/fixtures/rules/s3_bucket_name.guard"
    with open(template_filename, encoding="utf8") as file:
        template_str = yaml.safe_load(file)
    with open(rules_filename, encoding="utf8") as file:
        rules = file.read()

    with patch("json.loads") as mock_method:
        mock_method.side_effect = Exception("test")
        with pytest.raises(cfn_guard_rs.errors.UnknownError):
            run_checks(template_str, rules)
