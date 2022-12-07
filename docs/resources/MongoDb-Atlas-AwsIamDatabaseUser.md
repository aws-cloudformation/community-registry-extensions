
## MongoDb::Atlas::AwsIamDatabaseUser

## CRUD for AWS IAM MongoDB users in a project for your clusters&#x2F;databases.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;compose-x&#x2F;aws-cfn-mongodb-atlas-awsiamdatabaseuser) 
- [Documentation]()

Published by EWS Network

## Schema
{% highlight json %}
{
    "typeName": "MongoDb::Atlas::AwsIamDatabaseUser",
    "description": "CRUD for AWS IAM MongoDB users in a project for your clusters/databases.",
    "sourceUrl": "https://github.com/compose-x/aws-cfn-mongodb-atlas-awsiamdatabaseuser",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "additionalProperties": false,
    "properties": {
        "AwsIamResource": {
            "description": "The AWS IAM user or role ARN used as the database username.",
            "type": "string",
            "pattern": "^arn:aws(?:-[a-z-]+)?:iam::[0-9]{12}:(role|user)/[\\S]+$"
        },
        "ApiKeys": {
            "$ref": "#/definitions/apiKeyDefinition"
        },
        "ProjectId": {
            "description": "Unique identifier of the Atlas project to which the user belongs.",
            "type": "string",
            "pattern": "^[a-zA-Z0-9]+$"
        },
        "DatabaseAccess": {
            "type": "object",
            "additionalProperties": false,
            "patternProperties": {
                "^[a-zA-Z0-9-_]+$": {
                    "$ref": "#/definitions/databaseAccessDefinition"
                }
            }
        },
        "Scopes": {
            "type": "object",
            "additionalProperties": false,
            "patternProperties": {
                "^[a-zA-Z0-9-_]+$": {
                    "type": "string",
                    "description": "Database/Lake name to the type",
                    "enum": [
                        "CLUSTER",
                        "DATA_LAKE"
                    ]
                }
            }
        },
        "MongoDbUsername": {
            "description": "MongoDB username for the AWS IAM resource.",
            "type": "string"
        }
    },
    "definitions": {
        "databaseAccessDefinition": {
            "type": "object",
            "additionalProperties": false,
            "required": [
                "RoleName"
            ],
            "properties": {
                "RoleName": {
                    "type": "string"
                },
                "CollectionName": {
                    "type": "string"
                }
            }
        },
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
            "type": "object",
            "required": [
                "PublicKey",
                "PrivateKey"
            ]
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
            "type": "object",
            "required": [
                "RoleName"
            ]
        },
        "scopeDefinition": {
            "additionalProperties": false,
            "properties": {
                "ScopeName": {
                    "minLength": 1,
                    "type": "string"
                },
                "ScopeType": {
                    "enum": [
                        "CLUSTER",
                        "DATA_LAKE"
                    ],
                    "type": "string"
                }
            },
            "type": "object",
            "required": [
                "ScopeName",
                "ScopeType"
            ]
        }
    },
    "primaryIdentifier": [
        "/properties/MongoDbUsername"
    ],
    "readOnlyProperties": [
        "/properties/MongoDbUsername"
    ],
    "createOnlyProperties": [
        "/properties/Username",
        "/properties/ProjectId"
    ],
    "required": [
        "AwsIamResource",
        "ProjectId",
        "ApiKeys",
        "DatabaseAccess"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "secretsmanager:GetSecretValue"
            ]
        },
        "read": {
            "permissions": [
                "secretsmanager:GetSecretValue"
            ]
        },
        "update": {
            "permissions": [
                "secretsmanager:GetSecretValue"
            ]
        },
        "delete": {
            "permissions": [
                "secretsmanager:GetSecretValue"
            ]
        }
    }
}
{% endhighlight %}
