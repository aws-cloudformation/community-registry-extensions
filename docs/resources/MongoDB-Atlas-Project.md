
## MongoDB::Atlas::Project

Retrieves or creates projects in any given Atlas organization.

- [Source]() 
- [Documentation]()

Published by MongoDB

## Schema
{% highlight json %}
{
    "typeName": "MongoDB::Atlas::Project",
    "description": "Retrieves or creates projects in any given Atlas organization.",
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
        },
        "projectSettings": {
            "type": "object",
            "properties": {
                "IsCollectDatabaseSpecificsStatisticsEnabled": {
                    "type": "boolean"
                },
                "IsDataExplorerEnabled": {
                    "type": "boolean"
                },
                "IsPerformanceAdvisorEnabled": {
                    "type": "boolean"
                },
                "IsRealtimePerformancePanelEnabled": {
                    "type": "boolean"
                },
                "IsSchemaAdvisorEnabled": {
                    "type": "boolean"
                }
            },
            "additionalProperties": false
        },
        "projectTeam": {
            "type": "object",
            "properties": {
                "TeamId": {
                    "type": "string"
                },
                "RoleNames": {
                    "items": {
                        "$ref": "#/definitions/Roles"
                    },
                    "type": "array",
                    "uniqueItems": true
                }
            },
            "additionalProperties": false
        },
        "projectApiKey": {
            "type": "object",
            "properties": {
                "Key": {
                    "type": "string"
                },
                "RoleNames": {
                    "items": {
                        "$ref": "#/definitions/Roles"
                    },
                    "type": "array",
                    "uniqueItems": true
                }
            },
            "additionalProperties": false
        },
        "Roles": {
            "type": "string"
        }
    },
    "properties": {
        "Name": {
            "description": "Name of the project to create.",
            "type": "string",
            "default": ""
        },
        "OrgId": {
            "description": "Unique identifier of the organization within which to create the project.",
            "type": "string",
            "default": ""
        },
        "ProjectOwnerId": {
            "description": "Unique identifier of the organization within which to create the project.",
            "type": "string",
            "default": ""
        },
        "WithDefaultAlertsSettings": {
            "description": "Unique identifier of the organization within which to create the project.",
            "type": "boolean",
            "default": "false"
        },
        "Id": {
            "description": "The unique identifier of the project.",
            "type": "string",
            "default": ""
        },
        "Created": {
            "description": "The ISO-8601-formatted timestamp of when Atlas created the project.",
            "type": "string"
        },
        "ClusterCount": {
            "description": "The number of Atlas clusters deployed in the project.",
            "type": "integer"
        },
        "ProjectSettings": {
            "$ref": "#/definitions/projectSettings"
        },
        "ApiKeys": {
            "$ref": "#/definitions/apiKeyDefinition"
        },
        "ProjectTeams": {
            "items": {
                "$ref": "#/definitions/projectTeam"
            },
            "type": "array",
            "uniqueItems": true
        },
        "ProjectApiKeys": {
            "items": {
                "$ref": "#/definitions/projectApiKey"
            },
            "type": "array",
            "uniqueItems": true
        }
    },
    "additionalProperties": false,
    "required": [
        "Name",
        "OrgId"
    ],
    "createOnlyProperties": [
        "/properties/Name"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/Created",
        "/properties/ClusterCount"
    ],
    "primaryIdentifier": [
        "/properties/Id"
    ],
    "handlers": {
        "create": {
            "permissions": []
        },
        "read": {
            "permissions": []
        },
        "delete": {
            "permissions": []
        }
    }
}
{% endhighlight %}
