
## Snowflake::Role::Role

## Allows for the creation and modification of a Snowflake Role. https:&#x2F;&#x2F;docs.snowflake.com&#x2F;en&#x2F;user-guide&#x2F;security-access-control-overview.html#roles

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-snowflake-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Snowflake::Role::Role",
    "description": "Allows for the creation and modification of a Snowflake Role. https://docs.snowflake.com/en/user-guide/security-access-control-overview.html#roles",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-snowflake-resource-providers.git",
    "documentationUrl": "https://github.com/aws-ia/cloudformation-snowflake-resource-providers",
    "typeConfiguration": {
        "properties": {
            "SnowflakeAccess": {
                "$ref": "#/definitions/SnowflakeAccess"
            }
        },
        "additionalProperties": false,
        "required": [
            "SnowflakeAccess"
        ]
    },
    "definitions": {
        "SnowflakeAccess": {
            "type": "object",
            "properties": {
                "Account": {
                    "type": "string"
                },
                "Username": {
                    "type": "string"
                },
                "Password": {
                    "type": "string"
                }
            },
            "required": [
                "Account",
                "Username",
                "Password"
            ],
            "additionalProperties": false
        }
    },
    "properties": {
        "Name": {
            "type": "string",
            "description": "Specifies the identifier for the role; must be unique for your account."
        },
        "Comment": {
            "type": "string",
            "description": "Specifies a comment for the role."
        }
    },
    "additionalProperties": false,
    "required": [
        "Name"
    ],
    "createOnlyProperties": [
        "/properties/Name"
    ],
    "primaryIdentifier": [
        "/properties/Name"
    ],
    "handlers": {
        "create": {
            "permissions": []
        },
        "read": {
            "permissions": []
        },
        "update": {
            "permissions": []
        },
        "delete": {
            "permissions": []
        },
        "list": {
            "permissions": []
        }
    }
}
{% endhighlight %}
