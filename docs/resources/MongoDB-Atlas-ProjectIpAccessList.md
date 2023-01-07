
## MongoDB::Atlas::ProjectIpAccessList

An example resource schema demonstrating some basic constructs and validation rules.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-cloudformation&#x2F;aws-cloudformation-rpdk.git) 
- [Documentation]()

Published by MongoDB

## Schema
{% highlight json %}
{
    "additionalProperties": false,
    "definitions": {
        "accessListDefinition": {
            "additionalProperties": false,
            "properties": {
                "AwsSecurityGroup": {
                    "description": "ID of the AWS security group to allow access. Mutually exclusive with CIDRBlock and IPAddress.",
                    "type": "string"
                },
                "CIDRBlock": {
                    "description": "Accessable entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with ipAddress and AwsSecurityGroup.",
                    "type": "string"
                },
                "Comment": {
                    "description": "Comment associated with the ip access list entry.",
                    "type": "string"
                },
                "IPAddress": {
                    "description": "Accessable IP address. Mutually exclusive with CIDRBlock and AwsSecurityGroup.",
                    "type": "string"
                },
                "ProjectId": {
                    "description": "The unique identifier for the project to which you want to add one or more ip access list entries.",
                    "type": "string"
                }
            },
            "type": "object"
        },
        "apiKeyDefinition": {
            "additionalProperties": false,
            "properties": {
                "PrivateKey": {
                    "type": "string"
                },
                "PublicKey": {
                    "type": "string"
                }
            },
            "type": "object"
        }
    },
    "description": "An example resource schema demonstrating some basic constructs and validation rules.",
    "handlers": {
        "create": {
            "permissions": [
                ""
            ]
        },
        "delete": {
            "permissions": [
                ""
            ]
        },
        "read": {
            "permissions": [
                ""
            ]
        },
        "update": {
            "permissions": [
                ""
            ]
        }
    },
    "primaryIdentifier": [
        "/properties/Id"
    ],
    "properties": {
        "AccessList": {
            "items": {
                "$ref": "#/definitions/accessListDefinition"
            },
            "minItems": 1,
            "type": "array",
            "uniqueItems": true
        },
        "ApiKeys": {
            "$ref": "#/definitions/apiKeyDefinition"
        },
        "Id": {
            "description": "The unique identifier for the Project API ip access list rules.",
            "type": "string"
        },
        "ProjectId": {
            "description": "The unique identifier for the project to which you want to add one or more ip access list entries.",
            "type": "string"
        },
        "TotalCount": {
            "description": "The unique identifier for the Project ip access list rules.",
            "type": "integer"
        }
    },
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/TotalCount"
    ],
    "required": [
        "ProjectId",
        "AccessList",
        "ApiKeys"
    ],
    "sourceUrl": "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
    "typeName": "MongoDB::Atlas::ProjectIpAccessList"
}
{% endhighlight %}
