
## Datadog::Integrations::AWS

## Datadog AWS Integration 2.2.1

- [Source]() 
- [Documentation]()

Published by DataDog

## Schema
{% highlight json %}
{
    "typeName": "Datadog::Integrations::AWS",
    "description": "Datadog AWS Integration 2.2.1",
    "typeConfiguration": {
        "properties": {
            "DatadogCredentials": {
                "$ref": "#/definitions/DatadogCredentials"
            }
        },
        "additionalProperties": false
    },
    "definitions": {
        "DatadogCredentials": {
            "description": "Credentials for the Datadog API",
            "properties": {
                "ApiKey": {
                    "description": "Datadog API key",
                    "type": "string"
                },
                "ApplicationKey": {
                    "description": "Datadog application key",
                    "type": "string"
                },
                "ApiURL": {
                    "description": "Datadog API URL (defaults to https://api.datadoghq.com)",
                    "type": "string"
                }
            },
            "required": [
                "ApiKey",
                "ApplicationKey"
            ],
            "type": "object",
            "additionalProperties": false
        }
    },
    "properties": {
        "AccountID": {
            "description": "Your AWS Account ID without dashes.",
            "type": "string",
            "dependencies": {
                "AccountID": [
                    "RoleName"
                ]
            }
        },
        "RoleName": {
            "description": "Your Datadog role delegation name.",
            "type": "string"
        },
        "AccessKeyID": {
            "description": "If your AWS account is a GovCloud or China account, enter the corresponding Access Key ID.",
            "type": "string"
        },
        "FilterTags": {
            "description": "The array of EC2 tags (in the form key:value) defines a filter that Datadog uses when collecting metrics from EC2.",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "HostTags": {
            "description": "Array of tags (in the form key:value) to add to all hosts and metrics reporting through this integration.",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "AccountSpecificNamespaceRules": {
            "description": "An object (in the form {\"namespace1\":true/false, \"namespace2\":true/false}) that enables or disables metric collection for specific AWS namespaces for this AWS account only.",
            "type": "object",
            "patternProperties": {
                ".*": {
                    "type": "boolean"
                }
            },
            "additionalProperties": false
        },
        "IntegrationID": {
            "description": "An identification value that represents this integration object. Combines the AccountID, RoleName, and AccessKeyID. This shouldn't be set in a stack.",
            "type": "string"
        },
        "ExternalIDSecretName": {
            "description": "The name of the AWS SecretsManager secret created in your account to hold this integration's `external_id`. Defaults to `DatadogIntegrationExternalID`. Cannot be referenced from created resource.",
            "type": "string"
        },
        "MetricsCollection": {
            "description": "Enable the infrastructure monitoring Datadog product for this AWS Account. This will enable collecting all AWS metrics in your account.",
            "type": "boolean"
        },
        "CSPMResourceCollection": {
            "description": "Enable the compliance and security posture management Datadog product. This will enable collecting information on your AWS resources and providing security validation.",
            "type": "boolean"
        },
        "ResourceCollection": {
            "description": "Enable collecting information on your AWS resources for use in Datadog products such as Network Process Monitoring.",
            "type": "boolean"
        }
    },
    "required": [],
    "primaryIdentifier": [
        "/properties/IntegrationID"
    ],
    "createOnlyProperties": [
        "/properties/AccountID",
        "/properties/RoleName",
        "/properties/AccessKeyID"
    ],
    "readOnlyProperties": [
        "/properties/IntegrationID"
    ],
    "additionalProperties": false,
    "handlers": {
        "create": {
            "permissions": [
                "secretsmanager:CreateSecret"
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
        "delete": {
            "permissions": [
                "secretsmanager:DeleteSecret",
                "secretsmanager:DescribeSecret"
            ]
        }
    }
}
{% endhighlight %}
