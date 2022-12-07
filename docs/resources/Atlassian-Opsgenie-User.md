
## Atlassian::Opsgenie::User

## Opsgenie User

- [Source](https:&#x2F;&#x2F;github.com&#x2F;opsgenie&#x2F;opsgenie-cloudformation-resources) 
- [Documentation]()

Published by opsgenie

## Schema
{% highlight json %}
{
    "typeName": "Atlassian::Opsgenie::User",
    "description": "Opsgenie User",
    "sourceUrl": "https://github.com/opsgenie/opsgenie-cloudformation-resources",
    "definitions": {},
    "properties": {
        "UserId": {
            "type": "string"
        },
        "OpsgenieApiEndpoint": {
            "type": "string",
            "pattern": "^https://api(\\.eu|\\.sandbox|)\\.opsgenie\\.com$",
            "minLength": 1
        },
        "OpsgenieApiKey": {
            "type": "string",
            "pattern": "[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"
        },
        "Username": {
            "type": "string",
            "pattern": "^[a-z0-9._+-]+@[a-z0-9]+\\.[a-z]{2,6}$",
            "description": "Opsgenie Username the mail address of the user",
            "minLength": 1
        },
        "FullName": {
            "type": "string",
            "pattern": "^[a-zA-Z0-9- _.]+$",
            "minLength": 1,
            "description": "User full name"
        },
        "Role": {
            "type": "string",
            "minLength": 1,
            "description": "User role, default is User"
        }
    },
    "required": [
        "OpsgenieApiEndpoint",
        "Username",
        "FullName",
        "Role",
        "OpsgenieApiKey"
    ],
    "readOnlyProperties": [
        "/properties/UserId"
    ],
    "createOnlyProperties": [
        "/properties/Username",
        "/properties/FullName"
    ],
    "primaryIdentifier": [
        "/properties/UserId"
    ],
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
