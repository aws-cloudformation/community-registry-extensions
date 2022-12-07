
## Atlassian::Opsgenie::Integration

## Opsgenie Integration Resource definition

- [Source](https:&#x2F;&#x2F;github.com&#x2F;opsgenie&#x2F;opsgenie-cloudformation-resources) 
- [Documentation]()

Published by opsgenie

## Schema
{% highlight json %}
{
    "typeName": "Atlassian::Opsgenie::Integration",
    "description": "Opsgenie Integration Resource definition",
    "sourceUrl": "https://github.com/opsgenie/opsgenie-cloudformation-resources",
    "definitions": {
        "respondersProperty": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string",
                    "description": "Responder type",
                    "minLength": 1
                },
                "name": {
                    "type": "string",
                    "description": "Responder name if available",
                    "minLength": 1
                },
                "username": {
                    "type": "string",
                    "description": "Responder username, if responder type is user",
                    "minLength": 1
                }
            }
        }
    },
    "properties": {
        "OpsgenieApiEndpoint": {
            "type": "string",
            "pattern": "^https://api(\\.eu|\\.sandbox|)\\.opsgenie\\.com$",
            "minLength": 1
        },
        "OpsgenieApiKey": {
            "type": "string",
            "pattern": "^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$",
            "minLength": 1
        },
        "IntegrationApiKey": {
            "type": "string",
            "minLength": 1
        },
        "IntegrationId": {
            "type": "string",
            "pattern": "[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"
        },
        "Enabled": {
            "type": "boolean",
            "description": "Integration status, default is true",
            "minLength": 1
        },
        "Name": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9- _.]+$",
            "description": "Integration name",
            "minLength": 1
        },
        "IntegrationType": {
            "type": "string",
            "description": "Integration types, only api integration types supported",
            "minLength": 1
        },
        "OwnerTeamId": {
            "type": "string",
            "description": "Id of the integration owner team.",
            "minLength": 1
        },
        "OwnerTeamName": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9-_.]+$",
            "description": "Name of the integration owner team.",
            "minLength": 1
        },
        "AllowReadAccess": {
            "type": "boolean",
            "description": "This parameter is for configuring the read access of integration",
            "minLength": 1
        },
        "AllowWriteAccess": {
            "type": "boolean",
            "description": "This parameter is for configuring the write access of integration.",
            "minLength": 1
        },
        "AllowDeleteAccess": {
            "type": "boolean",
            "description": "This parameter is for configuring the delete access of integration.",
            "minLength": 1
        },
        "AllowConfigurationAccess": {
            "type": "boolean",
            "description": "This parameter is for allowing or restricting the configuration access.",
            "minLength": 1
        },
        "Responders": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/respondersProperty"
            }
        }
    },
    "required": [
        "OpsgenieApiEndpoint",
        "OpsgenieApiKey",
        "Enabled",
        "IntegrationType",
        "Name"
    ],
    "primaryIdentifier": [
        "/properties/IntegrationId"
    ],
    "readOnlyProperties": [
        "/properties/IntegrationId",
        "/properties/IntegrationApiKey"
    ],
    "writeOnlyProperties": [
        "/properties/OwnerTeamId"
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
