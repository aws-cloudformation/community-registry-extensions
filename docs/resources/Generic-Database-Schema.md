
## Generic::Database::Schema

## Uses the Aurora Data API to execute SQL and enforce a schema within a database cluster. Currently only supports Aurora Postgres.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-types&#x2F;tree&#x2F;master&#x2F;generic-database-schema) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "Generic::Database::Schema",
    "description": "Uses the Aurora Data API to execute SQL and enforce a schema within a database cluster. Currently only supports Aurora Postgres.",
    "sourceUrl": "https://github.com/iann0036/cfn-types/tree/master/generic-database-schema",
    "definitions": {
        "PrimaryKey": {
            "type": "object",
            "properties": {
                "Name": {
                    "description": "The name of the primary key. Cannot be updated after creation.",
                    "type": "string",
                    "pattern": "^[a-zA-Z0-9-_]+$"
                },
                "Type": {
                    "description": "The type of the primary key. Cannot be updated after creation.",
                    "type": "string",
                    "pattern": "^[a-zA-Z0-9-_]+$"
                },
                "Default": {
                    "description": "The default value of the primary key. Cannot be updated after creation.",
                    "type": "string"
                }
            },
            "required": [
                "Name",
                "Type"
            ],
            "additionalProperties": false
        },
        "Column": {
            "type": "object",
            "properties": {
                "Name": {
                    "description": "The name of the column. Creates the column if it doesn't exist. Cannot be updated after creation.",
                    "type": "string",
                    "pattern": "^[a-zA-Z0-9-_]+$"
                },
                "Type": {
                    "description": "The type of the column. Cannot be updated after creation.",
                    "type": "string",
                    "pattern": "^[a-zA-Z0-9-_]+$"
                },
                "Nullable": {
                    "description": "Whether the column is nullable. Cannot be updated after creation.",
                    "type": "boolean"
                },
                "Default": {
                    "description": "The default value of the column. Cannot be updated after creation.",
                    "type": "string"
                }
            },
            "required": [
                "Name",
                "Type"
            ],
            "additionalProperties": false
        },
        "Table": {
            "type": "object",
            "properties": {
                "Name": {
                    "description": "The name of the table. Creates the table if it doesn't exist.",
                    "type": "string",
                    "pattern": "^[a-zA-Z0-9-_]+$"
                },
                "Columns": {
                    "description": "An array of columns to manage within the database.",
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Column"
                    },
                    "insertionOrder": true
                },
                "PrimaryKey": {
                    "$ref": "#/definitions/PrimaryKey"
                }
            },
            "required": [
                "Name"
            ],
            "additionalProperties": false
        },
        "Database": {
            "type": "object",
            "properties": {
                "Name": {
                    "description": "The name of the database. Creates the database if it doesn't exist.",
                    "type": "string",
                    "pattern": "^[a-zA-Z0-9-_]+$"
                },
                "Tables": {
                    "description": "An array of tables to manage within the database.",
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Table"
                    },
                    "insertionOrder": true
                },
                "Extensions": {
                    "description": "An array of extensions to enable within the database.",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "pattern": "^[a-zA-Z0-9-_]+$"
                    },
                    "insertionOrder": true
                },
                "SQL": {
                    "description": "An array of SQL statements to execute within the database.",
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "insertionOrder": true
                }
            },
            "required": [
                "Name"
            ],
            "additionalProperties": false
        },
        "User": {
            "type": "object",
            "properties": {
                "Name": {
                    "description": "The username of the user. Creates the user/role.",
                    "type": "string",
                    "pattern": "^[a-zA-Z0-9-_]+$"
                },
                "SecretId": {
                    "description": "The Secrets Manager secret ID or ARN of the credentials to set for the user ('password' field of the JSON secret value).",
                    "type": "string"
                },
                "SuperUser": {
                    "description": "Whether to give the user rds_superuser privileges.",
                    "type": "boolean"
                },
                "Grants": {
                    "description": "An array of grants to assign to the user.",
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Grant"
                    },
                    "insertionOrder": true
                }
            },
            "required": [
                "Name"
            ],
            "additionalProperties": false
        },
        "Grant": {
            "type": "object",
            "properties": {
                "Database": {
                    "description": "The name of the database. If the grant Table field is omitted, this represents a database grant, otherwise represents a table grant.",
                    "type": "string"
                },
                "Table": {
                    "description": "The name of the table. The grant Database field must specify the containing database and the database must be specified in the Databases section of the base of the type.",
                    "type": "string"
                },
                "Privileges": {
                    "description": "An array of privileges to grant (CONNECT, SELECT, etc.).",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "pattern": "^[a-zA-Z0-9]+$"
                    },
                    "insertionOrder": true,
                    "minItems": 1
                }
            },
            "required": [
                "Database",
                "Privileges"
            ],
            "additionalProperties": false
        }
    },
    "properties": {
        "ExecutionId": {
            "description": "A unique identifier to track this execution.",
            "type": "string"
        },
        "ClusterArn": {
            "description": "The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.",
            "type": "string",
            "pattern": "^arn:.*:rds:.*:.*:cluster:.+$"
        },
        "SecretArn": {
            "description": "The name or ARN of the secret that enables access to the DB cluster.",
            "type": "string"
        },
        "Databases": {
            "description": "An array of databases to manage within the cluster.",
            "type": "array",
            "items": {
                "$ref": "#/definitions/Database"
            },
            "insertionOrder": true
        },
        "SQL": {
            "description": "An array of SQL statements to execute within the postgres database.",
            "type": "array",
            "items": {
                "type": "string"
            },
            "insertionOrder": true
        },
        "Users": {
            "description": "An array of users within the cluster.",
            "type": "array",
            "items": {
                "$ref": "#/definitions/User"
            },
            "insertionOrder": true
        },
        "SQLIdempotency": {
            "description": "Whether arbitrary SQL statements are executed once (IDEMPOTENT), or on every update (RUN_ONCE).",
            "type": "string",
            "enum": [
                "IDEMPOTENT",
                "RUN_ONCE"
            ]
        }
    },
    "additionalProperties": false,
    "required": [
        "ClusterArn",
        "SecretArn"
    ],
    "readOnlyProperties": [
        "/properties/ExecutionId"
    ],
    "writeOnlyProperties": [
        "/properties/ClusterArn",
        "/properties/SecretArn",
        "/properties/Databases",
        "/properties/SQL",
        "/properties/Users",
        "/properties/SQLIdempotency"
    ],
    "createOnlyProperties": [
        "/properties/ClusterArn"
    ],
    "primaryIdentifier": [
        "/properties/ExecutionId"
    ],
    "taggable": false,
    "handlers": {
        "create": {
            "permissions": [
                "rds:DescribeDBClusters",
                "secretsmanager:GetSecretValue",
                "rds-data:ExecuteStatement",
                "rds-data:BeginTransaction",
                "rds-data:CommitTransaction",
                "dynamodb:DescribeTable",
                "dynamodb:CreateTable",
                "dynamodb:PutItem"
            ]
        },
        "read": {
            "permissions": [
                "dynamodb:DescribeTable",
                "dynamodb:CreateTable",
                "dynamodb:GetItem"
            ]
        },
        "update": {
            "permissions": [
                "rds:DescribeDBClusters",
                "secretsmanager:GetSecretValue",
                "rds-data:ExecuteStatement",
                "rds-data:BeginTransaction",
                "rds-data:CommitTransaction",
                "dynamodb:DescribeTable",
                "dynamodb:CreateTable",
                "dynamodb:UpdateItem",
                "dynamodb:GetItem"
            ]
        },
        "delete": {
            "permissions": [
                "dynamodb:DescribeTable",
                "dynamodb:CreateTable",
                "dynamodb:DeleteItem",
                "dynamodb:GetItem"
            ]
        },
        "list": {
            "permissions": [
                "dynamodb:DescribeTable",
                "dynamodb:CreateTable",
                "dynamodb:Scan"
            ]
        }
    }
}
{% endhighlight %}
