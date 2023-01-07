
## TF::AD::Computer

CloudFormation equivalent of ad_computer

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-tf-custom-types.git) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "TF::AD::Computer",
    "description": "CloudFormation equivalent of ad_computer",
    "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
    "documentationUrl": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/ad/TF-AD-Computer/docs/README.md",
    "definitions": {},
    "properties": {
        "tfcfnid": {
            "description": "Internal identifier for tracking resource changes. Do not use.",
            "type": "string"
        },
        "Container": {
            "type": "string"
        },
        "Description": {
            "type": "string"
        },
        "Dn": {
            "type": "string"
        },
        "Guid": {
            "type": "string"
        },
        "Id": {
            "type": "string"
        },
        "Name": {
            "type": "string"
        },
        "Pre2kname": {
            "type": "string"
        },
        "Sid": {
            "type": "string"
        }
    },
    "additionalProperties": false,
    "required": [
        "Name"
    ],
    "readOnlyProperties": [
        "/properties/tfcfnid",
        "/properties/Dn",
        "/properties/Guid",
        "/properties/Id",
        "/properties/Sid"
    ],
    "primaryIdentifier": [
        "/properties/tfcfnid"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "s3:GetObject",
                "s3:DeleteObject",
                "lambda:InvokeFunction"
            ]
        },
        "read": {
            "permissions": [
                "s3:GetObject"
            ]
        },
        "update": {
            "permissions": [
                "s3:GetObject",
                "s3:DeleteObject",
                "lambda:InvokeFunction"
            ]
        },
        "delete": {
            "permissions": [
                "s3:GetObject",
                "s3:DeleteObject",
                "lambda:InvokeFunction"
            ]
        },
        "list": {
            "permissions": [
                "s3:GetObject",
                "s3:ListBucket"
            ]
        }
    }
}
{% endhighlight %}
