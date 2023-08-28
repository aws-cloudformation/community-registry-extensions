"""
    Test cfn_guard_rs
"""
from unittest.mock import patch
import json
import yaml
import pytest
import cfn_guard_rs.errors
from cfn_guard_rs import (
    run_checks,
    FileReport,
    RuleReport,
    Messages,
    ClauseReport,
    UnaryReport,
    BinaryReport,
    UnaryComparison,
    UnaryCheck,
    GuardClauseReport,
    BinaryCheck,
    BinaryComparison,
)


@pytest.mark.parametrize(
    "template,rules,expected",
    [
        (
            "python/tests/fixtures/templates/s3_bucket_name_valid.yaml",
            "python/tests/fixtures/rules/s3_bucket_name.guard",
            FileReport(
                name="",
                metadata={},
                status="PASS",
                data_from="cfn_guard_rs",
                rules_from="cfn_guard_rs",
                not_compliant=[],
                not_applicable=[],
                compliant=["default"],
            ),
        ),
        (
            "python/tests/fixtures/templates/s3_bucket_name_invalid.yaml",
            "python/tests/fixtures/rules/s3_bucket_name.guard",
            FileReport(
                name="",
                metadata={},
                status="FAIL",
                data_from="cfn_guard_rs",
                rules_from="cfn_guard_rs",
                not_compliant=[
                    ClauseReport(
                        Rule=RuleReport(
                            name="default",
                            metadata={},
                            messages=Messages(),
                            checks=[
                                ClauseReport(
                                    Clause=GuardClauseReport(
                                        Unary=UnaryReport(
                                            context=" BucketName IS STRING  ",
                                            messages=Messages(
                                                custom_message="",
                                                error_message=(
                                                    "Check was not compliant as "
                                                    "property [/Resources/Bucket/Properties"
                                                    "/BucketName[L:0,C:0]] was not string."
                                                ),
                                            ),
                                            check=UnaryCheck(
                                                Resolved=UnaryComparison(
                                                    value={
                                                        "path": (
                                                            "/Resources/Bucket/"
                                                            "Properties/BucketName"
                                                        ),
                                                        "value": 1,
                                                    },
                                                    comparison=("IsString", False),
                                                )
                                            ),
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    )
                ],
                not_applicable=[],
                compliant=[],
            ),
        ),
        (
            "python/tests/fixtures/templates/s3_bucket_public_access_valid.yaml",
            "python/tests/fixtures/rules/s3_bucket_public_access.guard",
            FileReport(
                name="",
                metadata={},
                status="PASS",
                data_from="cfn_guard_rs",
                rules_from="cfn_guard_rs",
                not_compliant=[],
                not_applicable=[],
                compliant=["S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED"],
            ),
        ),
        (
            "python/tests/fixtures/templates/s3_bucket_public_access_invalid.yaml",
            "python/tests/fixtures/rules/s3_bucket_public_access.guard",
            FileReport(
                name="",
                metadata={},
                status="FAIL",
                data_from="cfn_guard_rs",
                rules_from="cfn_guard_rs",
                not_compliant=[
                    ClauseReport(
                        Rule=RuleReport(
                            name="S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED",
                            metadata={},
                            messages=Messages(),
                            checks=[
                                ClauseReport(
                                    Clause=GuardClauseReport(
                                        Binary=BinaryReport(
                                            context=(
                                                " %s3_buckets_level_public_access_"
                                                "prohibited[*].Properties."
                                                "PublicAccessBlockConfiguration."
                                                'BlockPublicAcls EQUALS  "true"'
                                            ),
                                            messages=Messages(
                                                custom_message="",
                                                error_message=(
                                                    "Check was not compliant as property"
                                                    " value [Path=/Resources/Bucket/Properties/"
                                                    "PublicAccessBlockConfiguration/BlockPublicAcls"
                                                    '[L:0,C:0] Value="false"] not equal to value '
                                                    '[Path=[L:0,C:0] Value="true"].'
                                                ),
                                            ),
                                            check=BinaryCheck(
                                                Resolved=BinaryComparison(
                                                    from_={
                                                        "path": (
                                                            "/Resources/Bucket/Properties/"
                                                            "PublicAccessBlockConfiguration/"
                                                            "BlockPublicAcls"
                                                        ),
                                                        "value": "false",
                                                    },
                                                    to_={"path": "", "value": "true"},
                                                    comparison=["Eq", False],
                                                )
                                            ),
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    )
                ],
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
    print(result)
    print(expected)
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
                "Parser Error when parsing `Parsing Error Error parsing file  "
                "at line 1 at column 17, when handling , fragment "
                "{\n    Properties\n        BucketName is_string\n    }\n}`"
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
