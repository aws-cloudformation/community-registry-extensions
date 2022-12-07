
## BigID::DataSource::S3

## Manage a BigID S3 data source

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-cloudformation&#x2F;aws-cloudformation-rpdk.git) 
- [Documentation]()

Published by BigID

## Schema
{% highlight json %}
{
    "typeName": "BigID::DataSource::S3",
    "description": "Manage a BigID S3 data source",
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
            "description": "Properties needed to access BigId.",
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
            "required": [
                "Domain",
                "Username",
                "Password"
            ],
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
        "Owners": {
            "description": "owners",
            "type": "array",
            "insertionOrder": false,
            "uniqueItems": true,
            "items": {
                "type": "string"
            }
        },
        "AwsAuthenticationType": {
            "description": "AWS Authentication Type",
            "type": "string",
            "enum": [
                "isCredentialsAuth",
                "isIamRoleAuth",
                "isAnonymousAuth",
                "isCrossAccountAuth",
                "isSTSAuth"
            ]
        },
        "AwsRoleSessionName": {
            "description": "Aws Role Session Name. Leave blank for default (only used when the \"AwsAuthenticationType\" is set to \"isCrossAccountAuth\")",
            "type": "string"
        },
        "AwsRoleArn": {
            "description": "Aws Role Arn (only used when the \"AwsAuthenticationType\" is set to \"isCrossAccountAuth\")",
            "type": "string"
        },
        "AwsAccessKey": {
            "description": "AWS Access Key (only used when the \"AwsAuthenticationType\" is set to \"isSTSAuth\" or \"isCredentialsAuth\")",
            "type": "string"
        },
        "AwsSecretKey": {
            "description": "AWS Secret Key (only used when the \"AwsAuthenticationType\" is set to \"isSTSAuth\" or \"isCredentialsAuth\")",
            "type": "string"
        },
        "AwsSessionToken": {
            "description": "AWS Session Token (only used when the \"AwsAuthenticationType\" is set to \"isSTSAuth\")",
            "type": "string"
        },
        "AwsRegion": {
            "description": "AWS Region. Example: us-west-2. If empty, search buckets in all regions",
            "type": "string"
        },
        "BucketName": {
            "description": "Bucket name",
            "type": "string"
        },
        "IncludeExcludeFiles": {
            "type": "boolean",
            "default": true
        },
        "FileTypesToExclude": {
            "description": "File Type(s). Example: type1,type2,type3",
            "type": "string"
        },
        "FolderToScan": {
            "description": "Folder to Scan",
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
                "Encoded": {
                    "type": "string"
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
        "NumberOfParsingThreads": {
            "type": "string",
            "description": "Number of Threads",
            "default": "5",
            "pattern": "^[0-9]*$"
        },
        "MetadataAclScanEnabled": {
            "description": "Will enable ACL for both Data Source and enumdata scans",
            "type": "boolean"
        },
        "DsAclScanEnabled": {
            "description": "Will enable ACL for both Data Source and Metadata scans",
            "type": "boolean"
        },
        "EnabledOcr": {
            "type": "boolean"
        },
        "OcrTimeout": {
            "description": "OCR Timeout in Seconds (only used when \"EnabledOcr\" is set to \"true\")",
            "type": "number",
            "default": 60
        },
        "OcrLanguages": {
            "description": "OCR Languages (only used when \"EnabledOcr\" is set to \"true\")",
            "type": "string",
            "enum": [
                "eng",
                "chi_sim+chi_tra",
                "ind",
                "jpn",
                "kor",
                "tha",
                "vie",
                "deu",
                "fra",
                "bul"
            ],
            "default": "eng"
        },
        "EnableClustering": {
            "type": "boolean"
        },
        "EnableClassifiers": {
            "type": "boolean"
        },
        "EnableAdvanceClassifiers": {
            "type": "boolean"
        },
        "SampleFolders": {
            "description": "Sample Files within Folders",
            "type": "boolean"
        },
        "SamplePercentage": {
            "description": "Sample Percentage. Example: 20, for scanning 20% of the folder (used only when \"SampleFolders\" is set to \"true\")",
            "type": "string",
            "default": "5"
        },
        "SampleFileContent": {
            "description": "Sample File Content",
            "type": "boolean"
        },
        "DifferentialScan": {
            "description": "For structured data sources, new objects or objects with structural changes (e.g., new columns) will be scanned.",
            "type": "boolean",
            "default": false
        },
        "IsModifiedInXDays": {
            "description": "Used only when \"DifferentialScan\" is set to \"true\"",
            "type": "boolean",
            "default": false
        },
        "XLastDays": {
            "description": "Used only when \"DifferentialScan\" and \"IsModifiedInXDays\" is set to \"true\"",
            "type": "number",
            "default": 7
        },
        "ScanWindowName": {
            "description": "Scannable Window",
            "type": "string"
        },
        "ParquetFileRegex": {
            "description": "Parquet File Regex. (Use regex to identify which parquet files will be scanned.)",
            "type": "string"
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
        "AwsAuthenticationType": {
            "$ref": "#/definitions/AwsAuthenticationType"
        },
        "AwsRoleSessionName": {
            "$ref": "#/definitions/AwsRoleSessionName"
        },
        "AwsRoleArn": {
            "$ref": "#/definitions/AwsRoleArn"
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
        "AwsRegion": {
            "$ref": "#/definitions/AwsRegion"
        },
        "BucketName": {
            "$ref": "#/definitions/BucketName"
        },
        "IncludeExcludeFiles": {
            "$ref": "#/definitions/IncludeExcludeFiles"
        },
        "FileTypesToExclude": {
            "$ref": "#/definitions/FileTypesToExclude"
        },
        "FolderToScan": {
            "$ref": "#/definitions/FolderToScan"
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
        "NumberOfParsingThreads": {
            "$ref": "#/definitions/NumberOfParsingThreads"
        },
        "MetadataAclScanEnabled": {
            "$ref": "#/definitions/MetadataAclScanEnabled"
        },
        "DsAclScanEnabled": {
            "$ref": "#/definitions/DsAclScanEnabled"
        },
        "EnabledOcr": {
            "$ref": "#/definitions/EnabledOcr"
        },
        "OcrTimeout": {
            "$ref": "#/definitions/OcrTimeout"
        },
        "OcrLanguages": {
            "$ref": "#/definitions/OcrLanguages"
        },
        "EnableClustering": {
            "$ref": "#/definitions/EnableClustering"
        },
        "EnableClassifiers": {
            "$ref": "#/definitions/EnableClassifiers"
        },
        "EnableAdvanceClassifiers": {
            "$ref": "#/definitions/EnableAdvanceClassifiers"
        },
        "SampleFolders": {
            "$ref": "#/definitions/SampleFolders"
        },
        "SamplePercentage": {
            "$ref": "#/definitions/SamplePercentage"
        },
        "SampleFileContent": {
            "$ref": "#/definitions/SampleFileContent"
        },
        "DifferentialScan": {
            "$ref": "#/definitions/DifferentialScan"
        },
        "IsModifiedInXDays": {
            "$ref": "#/definitions/IsModifiedInXDays"
        },
        "XLastDays": {
            "$ref": "#/definitions/XLastDays"
        },
        "ScanWindowName": {
            "$ref": "#/definitions/ScanWindowName"
        },
        "ParquetFileRegex": {
            "$ref": "#/definitions/ParquetFileRegex"
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
