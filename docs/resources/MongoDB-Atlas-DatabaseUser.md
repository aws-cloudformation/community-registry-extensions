
## MongoDB::Atlas::DatabaseUser

Returns, adds, edits, and removes database users.

- [Source]() 
- [Documentation]()

Published by MongoDB

## Schema
{% highlight json %}
{
    "additionalProperties": false,
    "definitions": {
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
        },
        "labelDefinition": {
            "additionalProperties": false,
            "properties": {
                "Key": {
                    "minLength": 1,
                    "type": "string"
                },
                "Value": {
                    "minLength": 1,
                    "type": "string"
                }
            },
            "type": "object"
        },
        "roleDefinition": {
            "additionalProperties": false,
            "properties": {
                "CollectionName": {
                    "type": "string"
                },
                "DatabaseName": {
                    "type": "string"
                },
                "RoleName": {
                    "minLength": 1,
                    "type": "string"
                }
            },
            "type": "object"
        },
        "scopeDefinition": {
            "additionalProperties": false,
            "properties": {
                "Name": {
                    "minLength": 1,
                    "type": "string"
                },
                "Type": {
                    "enum": [
                        "CLUSTER",
                        "DATA_LAKE"
                    ],
                    "type": "string"
                }
            },
            "type": "object"
        }
    },
    "description": "Returns, adds, edits, and removes database users.",
    "handlers": {
        "create": {
            "permissions": []
        },
        "delete": {
            "permissions": []
        },
        "list": {
            "permissions": []
        },
        "read": {
            "permissions": []
        },
        "update": {
            "permissions": []
        }
    },
    "primaryIdentifier": [
        "/properties/UserCFNIdentifier"
    ],
    "properties": {
        "DeleteAfterDate": {
            "description": "Date and time when MongoDB Cloud deletes the user. This parameter expresses its value in the ISO 8601 timestamp format in UTC and can include the time zone designation. You must specify a future date that falls within one week of making the Application Programming Interface (API) request.",
            "type": "string"
        },
        "AWSIAMType": {
            "description": "Human-readable label that indicates whether the new database user authenticates with the Amazon Web Services (AWS) Identity and Access Management (IAM) credentials associated with the user or the user's role.",
            "enum": [
                "NONE",
                "USER",
                "ROLE"
            ],
            "type": "string"
        },
        "ApiKeys": {
            "$ref": "#/definitions/apiKeyDefinition"
        },
        "DatabaseName": {
            "description": "MongoDB database against which the MongoDB database user authenticates. MongoDB database users must provide both a username and authentication database to log into MongoDB.",
            "type": "string"
        },
        "Labels": {
            "description": "List that contains the key-value pairs for tagging and categorizing the MongoDB database user. The labels that you define do not appear in the console.",
            "items": {
                "$ref": "#/definitions/labelDefinition"
            },
            "minItems": 1,
            "type": "array",
            "uniqueItems": true
        },
        "LdapAuthType": {
            "description": "Method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE.",
            "enum": [
                "NONE",
                "USER",
                "GROUP"
            ],
            "type": "string"
        },
        "X509Type": {
            "description": "Method that briefs who owns the certificate provided. If no value is given while using X509Type, Atlas uses the default value of MANAGED.",
            "enum": [
                "NONE",
                "MANAGED",
                "CUSTOMER"
            ],
            "type": "string"
        },
        "Password": {
            "description": "The user’s password. This field is not included in the entity returned from the server.",
            "type": "string"
        },
        "ProjectId": {
            "description": "Unique identifier of the Atlas project to which the user belongs.",
            "type": "string"
        },
        "Roles": {
            "description": "List that provides the pairings of one role with one applicable database.",
            "items": {
                "$ref": "#/definitions/roleDefinition"
            },
            "minItems": 1,
            "type": "array",
            "uniqueItems": true
        },
        "Scopes": {
            "description": "List that contains clusters and MongoDB Atlas Data Lakes that this database user can access. If omitted, MongoDB Cloud grants the database user access to all the clusters and MongoDB Atlas Data Lakes in the project.",
            "items": {
                "$ref": "#/definitions/scopeDefinition"
            },
            "minItems": 1,
            "type": "array",
            "uniqueItems": true
        },
        "UserCFNIdentifier": {
            "description": "A unique identifier comprised of the Atlas Project ID and Username",
            "type": "string"
        },
        "Username": {
            "description": "Human-readable label that represents the user that authenticates to MongoDB.",
            "type": "string"
        }
    },
    "readOnlyProperties": [
        "/properties/UserCFNIdentifier"
    ],
    "required": [
        "DatabaseName",
        "ProjectId",
        "Roles",
        "Username"
    ],
    "typeName": "MongoDB::Atlas::DatabaseUser"
}
{% endhighlight %}
