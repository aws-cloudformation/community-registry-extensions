
## Snowflake::Database::Grant

Allows privileges to be granted on a database to a role. https:&#x2F;&#x2F;docs.snowflake.com&#x2F;en&#x2F;sql-reference&#x2F;sql&#x2F;grant-privilege.html

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-snowflake-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Snowflake::Database::Grant",
    "description": "Allows privileges to be granted on a database to a role. https://docs.snowflake.com/en/sql-reference/sql/grant-privilege.html",
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
        "DatabaseName": {
            "type": "string"
        },
        "Privilege": {
            "type": "string"
        },
        "Role": {
            "type": "string"
        }
    },
    "additionalProperties": false,
    "required": [
        "DatabaseName",
        "Privilege",
        "Role"
    ],
    "createOnlyProperties": [
        "/properties/DatabaseName",
        "/properties/Privilege",
        "/properties/Role"
    ],
    "primaryIdentifier": [
        "/properties/DatabaseName",
        "/properties/Privilege",
        "/properties/Role"
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
        },
        "list": {
            "permissions": []
        }
    }
}
{% endhighlight %}
