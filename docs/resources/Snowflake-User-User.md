
## Snowflake::User::User

Allows for the creation and modification of a Snowflake User. https:&#x2F;&#x2F;docs.snowflake.com&#x2F;en&#x2F;user-guide&#x2F;admin-user-management.html

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-snowflake-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Snowflake::User::User",
    "description": "Allows for the creation and modification of a Snowflake User. https://docs.snowflake.com/en/user-guide/admin-user-management.html",
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
            "description": "Identifier for the user; must be unique for your account."
        },
        "Password": {
            "type": "string",
            "description": "The password for the user"
        },
        "LoginName": {
            "type": "string",
            "description": "Name that the user enters to log into the system. Login names for users must be unique across your entire account."
        },
        "DisplayName": {
            "type": "string",
            "description": "Name displayed for the user in the Snowflake web interface."
        },
        "FirstName": {
            "type": "string",
            "description": "First name of the user."
        },
        "MiddleName": {
            "type": "string",
            "description": "Middle name of the user."
        },
        "LastName": {
            "type": "string",
            "description": "Last name of the user."
        },
        "Email": {
            "type": "string",
            "description": "Email address for the user."
        },
        "MustChangePassword": {
            "type": "boolean",
            "description": "Specifies whether the user is forced to change their password on next login (including their first/initial login) into the system.",
            "default": false
        },
        "Disabled": {
            "type": "boolean",
            "description": "Specifies whether the user is disabled.",
            "default": false
        },
        "DaysToExpiry": {
            "type": "integer",
            "description": "Specifies the number of days after which the user status is set to Expired and the user is no longer allowed to log in."
        },
        "MinsToUnlock": {
            "type": "integer",
            "description": "Specifies the number of minutes until the temporary lock on the user login is cleared."
        },
        "DefaultWarehouse": {
            "type": "string",
            "description": "Specifies the namespace (database only or database and schema) that is active by default for the user's session upon login."
        },
        "DefaultRole": {
            "type": "string",
            "description": "Specifies the primary role that is active by default for the user's session upon login."
        },
        "MinsToBypassMfa": {
            "type": "integer",
            "description": "Specifies the number of minutes to temporarily bypass MFA for the user."
        },
        "RsaPublicKey": {
            "type": "string",
            "description": "Specifies the user's RSA public key; used for key pair authentication."
        },
        "RsaPublicKey2": {
            "type": "string",
            "description": "Specifies the user's second RSA public key; used to rotate the public and private keys for key pair authentication based on an expiration schedule set by your organization."
        },
        "Comment": {
            "type": "string",
            "description": "Specifies a comment for the user."
        }
    },
    "additionalProperties": false,
    "required": [
        "Name",
        "Password"
    ],
    "createOnlyProperties": [
        "/properties/Name"
    ],
    "writeOnlyProperties": [
        "/properties/Password",
        "/properties/DaysToExpiry",
        "/properties/MiddleName",
        "/properties/MinsToUnlock",
        "/properties/MinsToBypassMfa",
        "/properties/RsaPublicKey",
        "/properties/RsaPublicKey2"
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
