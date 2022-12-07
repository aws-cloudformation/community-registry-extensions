
## BigID::DataSource::DynamoDB

Manage a BigID DynamoDB data source.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-cloudformation&#x2F;aws-cloudformation-rpdk.git) 
- [Documentation]()

Published by BigID

## Schema
{% highlight json %}
{
    "typeName": "BigID::DataSource::DynamoDB",
    "description": "Manage a BigID DynamoDB data source.",
    "sourceUrl": "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
    "typeConfiguration": {
        "properties": {
            "BigIdAccess": {
                "$ref": "#/definitions/BigIdAccess"
            }
        },
        "additionalProperties": false,
        "required": [
            "BigIdAccess"
        ]
    },
    "definitions": {
        "BigIdAccess": {
            "description": "Properties needed to access BigId",
            "type": "object",
            "properties": {
                "Domain": {
                    "type": "string",
                    "description": "Domain used to access BigId"
                },
                "Username": {
                    "type": "string"
                },
                "Password": {
                    "type": "string"
                }
            },
            "additionalProperties": false
        },
        "Id": {
            "type": "string",
            "description": "Connection Id"
        },
        "Name": {
            "description": "Type data source name.",
            "type": "string",
            "pattern": "^[a-zA-Z0-9_\\-]+$"
        },
        "Enabled": {
            "type": "boolean",
            "default": true
        },
        "FriendlyName": {
            "description": "Type data source friendly Name",
            "type": "string"
        },
        "Description": {
            "description": "Add a short description (optional)",
            "type": "string",
            "minLength": 0,
            "maxLength": 100
        },
        "AuthenticationMethod": {
            "description": "Authentication Method",
            "type": "string",
            "enum": [
                "Default",
                "BigID",
                "IAMRole"
            ],
            "default": "Default"
        },
        "AwsAccessKey": {
            "description": "AWS Access Key (only used when \"AuthenticationMethod\" is set to \"Default\")",
            "type": "string"
        },
        "AwsSecretKey": {
            "description": "AWS Secret Key (only used when \"AuthenticationMethod\" is set to \"Default\")",
            "type": "string"
        },
        "AwsSessionToken": {
            "description": "AWS Session Token (only used when \"AuthenticationMethod\" is set to \"Default\")",
            "type": "string"
        },
        "CredentialId": {
            "description": "Credential to use to connect to DynamoDB (only used when \"AuthenticationMethod\" is set to \"BigID\")",
            "type": "string"
        },
        "DynamodbTableNames": {
            "description": "Table Name(s) (Example: table1,table2)",
            "type": "array",
            "insertionOrder": false,
            "items": {
                "type": "string",
                "minLength": 1
            }
        },
        "AwsRegion": {
            "description": "AWS Region. Example: us-west-2. If empty, search buckets in all regions",
            "type": "string"
        },
        "ScannerGroup": {
            "description": "This data source will be scanned only by scanner instances that are included under this Scanner Group. Used primarily when remote scans are configured.",
            "type": "string",
            "default": "default"
        },
        "TestConnectionTimeoutInSeconds": {
            "description": "Test Connection Timeout",
            "type": "number",
            "minimum": 10,
            "maximum": 7200
        },
        "CustomFields": {
            "description": "Custom Parameters",
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/CustomField"
            }
        },
        "CustomField": {
            "type": "object",
            "properties": {
                "Name": {
                    "type": "string"
                },
                "Value": {
                    "type": "string",
                    "default": ""
                },
                "Type": {
                    "type": "string",
                    "default": "",
                    "enum": [
                        "clear",
                        "encrypted"
                    ]
                }
            },
            "additionalProperties": false
        },
        "BusinessOwners": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/User"
            }
        },
        "ItOwners": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/User"
            }
        },
        "User": {
            "type": "object",
            "properties": {
                "Id": {
                    "type": "string"
                },
                "Origin": {
                    "type": "string"
                },
                "Email": {
                    "type": "string"
                }
            },
            "additionalProperties": false
        },
        "Location": {
            "description": "Select the country, state, province or territory where the Data Source is located.",
            "type": "string"
        },
        "Scope": {
            "type": "string"
        },
        "SecurityTier": {
            "description": "Security Tier",
            "type": "string",
            "enum": [
                "1",
                "2",
                "3",
                "4",
                "5"
            ],
            "default": "1"
        },
        "Comments": {
            "type": "string",
            "minLength": 1,
            "maxLength": 150
        },
        "ScanTimeoutInSeconds": {
            "description": "Scan Connection Timeout",
            "type": "number"
        },
        "NumberOfParsingThreads": {
            "type": "string",
            "description": "Number of Threads",
            "default": "5",
            "pattern": "^[0-9]*$"
        },
        "EnableStructuredClustering": {
            "description": "Enable Structured Clustering",
            "type": "boolean"
        },
        "EnableClassifiers": {
            "type": "boolean"
        },
        "SampleScanOnly": {
            "description": "Sample Scan Only",
            "type": "boolean"
        },
        "EnableAdvanceClassifiers": {
            "type": "boolean"
        },
        "RdbSampleDataMaxSize": {
            "description": "Sample Scan Data Max Size (Default 100000 - Only used when \"SampleScanOnly\" is set to \"true\")",
            "type": "string"
        },
        "ScanWindowName": {
            "description": "Scannable Window",
            "type": "string"
        },
        "IsCorrelationSetSupported": {
            "type": "boolean",
            "default": false
        }
    },
    "properties": {
        "Name": {
            "$ref": "#/definitions/Name"
        },
        "Enabled": {
            "$ref": "#/definitions/Enabled"
        },
        "FriendlyName": {
            "$ref": "#/definitions/FriendlyName"
        },
        "Description": {
            "$ref": "#/definitions/Description"
        },
        "AuthenticationMethod": {
            "$ref": "#/definitions/AuthenticationMethod"
        },
        "AwsAccessKey": {
            "$ref": "#/definitions/AwsAccessKey"
        },
        "AwsSecretKey": {
            "$ref": "#/definitions/AwsSecretKey"
        },
        "AwsSessionToken": {
            "$ref": "#/definitions/AwsSessionToken"
        },
        "CredentialId": {
            "$ref": "#/definitions/CredentialId"
        },
        "DynamodbTableNames": {
            "$ref": "#/definitions/DynamodbTableNames"
        },
        "AwsRegion": {
            "$ref": "#/definitions/AwsRegion"
        },
        "ScannerGroup": {
            "$ref": "#/definitions/ScannerGroup"
        },
        "TestConnectionTimeoutInSeconds": {
            "$ref": "#/definitions/TestConnectionTimeoutInSeconds"
        },
        "CustomFields": {
            "$ref": "#/definitions/CustomFields"
        },
        "BusinessOwners": {
            "$ref": "#/definitions/BusinessOwners"
        },
        "ItOwners": {
            "$ref": "#/definitions/ItOwners"
        },
        "Location": {
            "$ref": "#/definitions/Location"
        },
        "Scope": {
            "$ref": "#/definitions/Scope"
        },
        "SecurityTier": {
            "$ref": "#/definitions/SecurityTier"
        },
        "Comments": {
            "$ref": "#/definitions/Comments"
        },
        "ScanTimeoutInSeconds": {
            "$ref": "#/definitions/ScanTimeoutInSeconds"
        },
        "NumberOfParsingThreads": {
            "$ref": "#/definitions/NumberOfParsingThreads"
        },
        "EnableStructuredClustering": {
            "$ref": "#/definitions/EnableStructuredClustering"
        },
        "EnableClassifiers": {
            "$ref": "#/definitions/EnableClassifiers"
        },
        "SampleScanOnly": {
            "$ref": "#/definitions/SampleScanOnly"
        },
        "EnableAdvanceClassifiers": {
            "$ref": "#/definitions/EnableAdvanceClassifiers"
        },
        "RdbSampleDataMaxSize": {
            "$ref": "#/definitions/RdbSampleDataMaxSize"
        },
        "ScanWindowName": {
            "$ref": "#/definitions/ScanWindowName"
        },
        "IsCorrelationSetSupported": {
            "$ref": "#/definitions/IsCorrelationSetSupported"
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "Name"
    ],
    "createOnlyProperties": [
        "/properties/Name"
    ],
    "primaryIdentifier": [
        "/properties/Name"
    ],
    "writeOnlyProperties": [
        "/properties/AwsSecretKey",
        "/properties/CustomFields"
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
