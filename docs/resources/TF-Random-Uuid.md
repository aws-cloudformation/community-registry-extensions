
## TF::Random::Uuid

CloudFormation equivalent of random_uuid

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-tf-custom-types.git) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "TF::Random::Uuid",
    "description": "CloudFormation equivalent of random_uuid",
    "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
    "documentationUrl": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/random/TF-Random-Uuid/docs/README.md",
    "definitions": {
        "KeepersDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "MapKey": {
                    "type": "string"
                },
                "MapValue": {
                    "type": "string"
                }
            },
            "required": [
                "MapKey",
                "MapValue"
            ]
        }
    },
    "properties": {
        "tfcfnid": {
            "description": "Internal identifier for tracking resource changes. Do not use.",
            "type": "string"
        },
        "Id": {
            "type": "string"
        },
        "Keepers": {
            "type": "array",
            "insertionOrder": true,
            "items": {
                "$ref": "#/definitions/KeepersDefinition"
            }
        },
        "Result": {
            "type": "string"
        }
    },
    "additionalProperties": false,
    "required": [],
    "readOnlyProperties": [
        "/properties/tfcfnid",
        "/properties/Id",
        "/properties/Result"
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
