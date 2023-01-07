
## Snowflake::Database::Database

Allows for the creation and modification of a Snowflake Database. https:&#x2F;&#x2F;docs.snowflake.com&#x2F;en&#x2F;user-guide&#x2F;databases.html

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-snowflake-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Snowflake::Database::Database",
    "description": "Allows for the creation and modification of a Snowflake Database. https://docs.snowflake.com/en/user-guide/databases.html",
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
            "description": "Specifies the identifier for the database; must be unique for your account."
        },
        "DataRetentionTimeInDays": {
            "type": "integer",
            "description": "Specifies the number of days for which Time Travel actions can be performed on the database."
        },
        "MaxDataExtensionTimeInDays": {
            "type": "integer",
            "description": "The maximum number of days for which Snowflake can extend the data retention period for tables in the database."
        },
        "DefaultDdlCollation": {
            "type": "string",
            "description": "Specifies a default collation specification for all schemas and tables added to the database"
        },
        "Comment": {
            "type": "string",
            "description": "Specifies a comment for the database."
        }
    },
    "additionalProperties": false,
    "required": [
        "Name"
    ],
    "createOnlyProperties": [
        "/properties/Name"
    ],
    "writeOnlyProperties": [
        "/properties/MaxDataExtensionTimeInDays",
        "/properties/DefaultDdlCollation"
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
