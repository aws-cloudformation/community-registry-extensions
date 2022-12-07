
## Atlassian::Opsgenie::Team

Opsgenie Team resource schema

- [Source](https:&#x2F;&#x2F;github.com&#x2F;opsgenie&#x2F;opsgenie-cloudformation-resources) 
- [Documentation]()

Published by opsgenie

## Schema
{% highlight json %}
{
    "typeName": "Atlassian::Opsgenie::Team",
    "description": "Opsgenie Team resource schema",
    "sourceUrl": "https://github.com/opsgenie/opsgenie-cloudformation-resources",
    "definitions": {
        "Member": {
            "type": "object",
            "dependencies": {
                "UserId": [
                    "Role"
                ],
                "Role": [
                    "UserId"
                ]
            },
            "properties": {
                "UserId": {
                    "type": "string",
                    "pattern": "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$"
                },
                "Role": {
                    "type": "string",
                    "pattern": "^[a-zA-Z0-9-_.]+$"
                }
            }
        }
    },
    "properties": {
        "TeamId": {
            "description": "Team id",
            "type": "string",
            "pattern": "[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"
        },
        "Name": {
            "description": "Team name",
            "type": "string",
            "pattern": "^[a-zA-Z0-9- _.]+$"
        },
        "Description": {
            "description": "Team description",
            "type": "string",
            "minLength": 1,
            "pattern": "^[a-zA-Z0-9- _.]+$",
            "maxLength": 100
        },
        "Members": {
            "description": "Array of members",
            "type": "array",
            "items": {
                "$ref": "#/definitions/Member"
            }
        },
        "OpsgenieApiKey": {
            "description": "Api Key",
            "type": "string",
            "pattern": "[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"
        },
        "OpsgenieApiEndpoint": {
            "description": "Api endpoint",
            "type": "string",
            "pattern": "^https://api(\\.eu|\\.sandbox|)\\.opsgenie\\.com$"
        }
    },
    "required": [
        "Name"
    ],
    "primaryIdentifier": [
        "/properties/TeamId"
    ],
    "readOnlyProperties": [
        "/properties/TeamId"
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
        "update": {
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
    },
    "additionalProperties": false
}
{% endhighlight %}
