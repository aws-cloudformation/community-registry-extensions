
## MongoDB::Atlas::NetworkPeering

This resource allows to create, read, update and delete a network peering

- [Source]() 
- [Documentation]()

Published by MongoDB

## Schema
{% highlight json %}
{
    "typeName": "MongoDB::Atlas::NetworkPeering",
    "description": "This resource allows to create, read, update and delete a network peering",
    "definitions": {
        "apiKeyDefinition": {
            "type": "object",
            "properties": {
                "PublicKey": {
                    "type": "string"
                },
                "PrivateKey": {
                    "type": "string"
                }
            },
            "additionalProperties": false
        }
    },
    "properties": {
        "ProjectId": {
            "description": "The unique identifier of the project.",
            "type": "string"
        },
        "ContainerId": {
            "description": "Unique identifier of the Atlas VPC container for the AWS region.",
            "type": "string"
        },
        "AccepterRegionName": {
            "description": "AWS region where the peer VPC resides. Returns null if the region is the same region in which the Atlas VPC resides.",
            "type": "string"
        },
        "AwsAccountId": {
            "description": "AWS account ID of the owner of the peer VPC.",
            "type": "string"
        },
        "ProviderName": {
            "description": "The name of the provider",
            "type": "string"
        },
        "RouteTableCIDRBlock": {
            "description": "Peer VPC CIDR block or subnet.",
            "type": "string"
        },
        "VpcId": {
            "description": "Unique identifier of the peer VPC.",
            "type": "string"
        },
        "ConnectionId": {
            "description": "Unique identifier for the peering connection.",
            "type": "string"
        },
        "ErrorStateName": {
            "description": "Error state, if any.",
            "type": "string"
        },
        "StatusName": {
            "description": "The VPC peering connection status",
            "type": "string"
        },
        "Id": {
            "description": "Unique identifier of the Network Peer.",
            "type": "string"
        },
        "ApiKeys": {
            "$ref": "#/definitions/apiKeyDefinition"
        }
    },
    "additionalProperties": false,
    "required": [
        "ProjectId",
        "VpcId",
        "ApiKeys"
    ],
    "createOnlyProperties": [
        "/properties/AwsAccountId",
        "/properties/VpcId"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/StatusName",
        "/properties/ErrorStateName"
    ],
    "primaryIdentifier": [
        "/properties/Id"
    ],
    "handlers": {
        "create": {
            "permissions": [
                ""
            ]
        },
        "read": {
            "permissions": [
                ""
            ]
        },
        "delete": {
            "permissions": [
                ""
            ]
        },
        "list": {
            "permissions": [
                ""
            ]
        }
    }
}
{% endhighlight %}
