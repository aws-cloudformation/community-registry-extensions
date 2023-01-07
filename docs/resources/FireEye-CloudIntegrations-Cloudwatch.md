
## FireEye::CloudIntegrations::Cloudwatch

This Resource Type will create necessary resources in your AWS account to forward cloudwatch logs to FireEye Helix. Visit FireEye Cloud Integration Portal for more info and to generate a pre-populated CloudFormation Template

- [Source]() 
- [Documentation]()

Published by FireEye, Inc.

## Schema
{% highlight json %}
{
    "typeName": "FireEye::CloudIntegrations::Cloudwatch",
    "description": "This Resource Type will create necessary resources in your AWS account to forward cloudwatch logs to FireEye Helix. Visit FireEye Cloud Integration Portal for more info and to generate a pre-populated CloudFormation Template",
    "properties": {
        "ApiKey": {
            "description": "Helix API Key",
            "type": "string"
        },
        "LogGroupName": {
            "description": "CloudWatch LogGroup to monitor",
            "type": "string"
        },
        "Region": {
            "description": "LogGroup AWS region",
            "type": "string"
        },
        "ExecRole": {
            "description": "Lambda Execution role",
            "type": "string"
        },
        "HelixUploadUrl": {
            "description": "Helix API upload URL",
            "type": "string"
        },
        "primaryIdentifier": {
            "description": "",
            "type": "string"
        }
    },
    "additionalProperties": false,
    "required": [
        "LogGroupName",
        "Region",
        "ExecRole",
        "HelixUploadUrl",
        "ApiKey"
    ],
    "readOnlyProperties": [
        "/properties/primaryIdentifier"
    ],
    "primaryIdentifier": [
        "/properties/primaryIdentifier"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "iam:PassRole",
                "lambda:CreateFunction",
                "lambda:GetFunction",
                "lambda:AddPermission",
                "logs:PutSubscriptionFilter",
                "logs:DescribeSubscriptionFilters"
            ]
        },
        "read": {
            "permissions": []
        },
        "update": {
            "permissions": [
                "iam:PassRole",
                "lambda:CreateFunction",
                "lambda:GetFunction",
                "lambda:DeleteFunction",
                "lambda:AddPermission",
                "logs:PutSubscriptionFilter",
                "logs:DescribeSubscriptionFilters",
                "logs:DeleteSubscriptionFilter"
            ]
        },
        "delete": {
            "permissions": [
                "lambda:GetFunction",
                "lambda:DeleteFunction",
                "logs:DeleteSubscriptionFilter",
                "logs:DescribeSubscriptionFilters"
            ]
        },
        "list": {
            "permissions": []
        }
    }
}
{% endhighlight %}
