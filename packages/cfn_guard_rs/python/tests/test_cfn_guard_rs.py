"""
    Test cfn_guard_rs
"""
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
    "template,rules,error,parent_error",
    [
        (
            "python/tests/fixtures/templates/s3_bucket_public_access_valid.yaml",
            "python/tests/fixtures/rules/invalid_missing_value.guard",
            cfn_guard_rs.errors.MissingValue,
            NameError,
        ),
        (
            "python/tests/fixtures/templates/s3_bucket_public_access_valid.yaml",
            "python/tests/fixtures/rules/invalid_format.guard",
            cfn_guard_rs.errors.ParseError,
            ValueError,
        ),
    ],
)
def test_run_checks_errors(template, rules, error, parent_error):
    """Test transactions against run_checks"""
    with open(template, encoding="utf8") as file:
        template_str = yaml.safe_load(file)
    with open(rules, encoding="utf8") as file:
        rules = file.read()

    with pytest.raises(error):
        run_checks(template_str, rules)

    with pytest.raises(parent_error):
        run_checks(template_str, rules)
