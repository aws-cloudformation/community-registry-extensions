
## ConfluentCloud::IAM::ServiceAccount

Service Account as defined in Confluent Cloud IAM v2 API.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;JohnPreston&#x2F;aws-cfn-confluentcloud-iam-serviceaccount) 
- [Documentation]()

Published by EWS Network

## Schema
{% highlight json %}
{
    "typeName": "ConfluentCloud::IAM::ServiceAccount",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "description": "Service Account as defined in Confluent Cloud IAM v2 API.",
    "sourceUrl": "https://github.com/JohnPreston/aws-cfn-confluentcloud-iam-serviceaccount",
    "definitions": {
        "ConfluentCloudAPISecrets": {
            "type": "object",
            "properties": {
                "ApiKey": {
                    "description": "Confluent Cloud API Key",
                    "type": "string"
                },
                "ApiSecret": {
                    "description": "Confluent Cloud API Secret",
                    "type": "string"
                }
            },
            "additionalProperties": false
        }
    },
    "properties": {
        "Description": {
            "type": "string",
            "description": "The description associated with the Service Account",
            "pattern": "^[\\x20-\\x7E]+$"
        },
        "Name": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9-_.]+$"
        },
        "ServiceAccountId": {
            "type": "string",
            "description": "Service Account in Confluent Cloud (sa-xxxx)"
        },
        "ConfluentCloudCredentials": {
            "$ref": "#/definitions/ConfluentCloudAPISecrets"
        }
    },
    "required": [
        "Name",
        "ConfluentCloudCredentials"
    ],
    "additionalProperties": false,
    "readOnlyProperties": [
        "/properties/ServiceAccountId"
    ],
    "primaryIdentifier": [
        "/properties/ServiceAccountId"
    ],
    "createOnlyProperties": [
        "/properties/Name"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "secretsmanager:GetSecretValue"
            ]
        },
        "read": {
            "permissions": [
                "secretsmanager:GetSecretValue"
            ]
        },
        "update": {
            "permissions": [
                "secretsmanager:GetSecretValue"
            ]
        },
        "delete": {
            "permissions": [
                "secretsmanager:GetSecretValue"
            ]
        }
    }
}
{% endhighlight %}
