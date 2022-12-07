
## PaloAltoNetworks::CloudNGFW::NGFW

## A Firewall resource offers Palo Alto Networks next-generation firewall capabilities with built-in resiliency, scalability, and life-cycle management.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-cloudformation&#x2F;aws-cloudformation-rpdk.git) 
- [Documentation]()

Published by PaloAltoNetworks

## Schema
{% highlight json %}
{
    "typeName": "PaloAltoNetworks::CloudNGFW::NGFW",
    "description": "A Firewall resource offers Palo Alto Networks next-generation firewall capabilities with built-in resiliency, scalability, and life-cycle management.",
    "sourceUrl": "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
    "definitions": {
        "LogProfileConfig": {
            "title": "LogProfileConfig",
            "description": "Add Log profile config",
            "type": "object",
            "properties": {
                "LogDestination": {
                    "title": "Logdestination",
                    "minLength": 1,
                    "maxLength": 128,
                    "type": "string"
                },
                "LogDestinationType": {
                    "title": "Logdestinationtype",
                    "enum": [
                        "S3",
                        "CloudWatchLogs",
                        "KinesisDataFirehose"
                    ],
                    "type": "string"
                },
                "LogType": {
                    "title": "Logtype",
                    "enum": [
                        "TRAFFIC",
                        "DECRYPTION",
                        "THREAT"
                    ],
                    "type": "string"
                }
            },
            "required": [
                "LogDestination",
                "LogDestinationType",
                "LogType"
            ],
            "additionalProperties": false
        }
    },
    "properties": {
        "AppIdVersion": {
            "title": "Appidversion",
            "minLength": 1,
            "maxLength": 64,
            "pattern": "^[0-9]+-[0-9]+$",
            "type": "string"
        },
        "AutomaticUpgradeAppIdVersion": {
            "title": "Automaticupgradeappidversion",
            "default": true,
            "type": "boolean"
        },
        "Description": {
            "title": "Description",
            "type": "string"
        },
        "EndpointMode": {
            "title": "Endpointmode: CustomerManaged Or ServiceManaged",
            "enum": [
                "ServiceManaged",
                "CustomerManaged"
            ],
            "type": "string"
        },
        "FirewallName": {
            "title": "Firewallname",
            "minLength": 1,
            "maxLength": 128,
            "pattern": "^[a-zA-Z0-9-]+$",
            "type": "string"
        },
        "RuleStackName": {
            "title": "Rulestackname",
            "type": "string"
        },
        "SubnetMappings": {
            "title": "Associate Subnetmappings, list of AvailabilityZone",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "Tags": {
            "title": "Tags",
            "type": "array",
            "items": {
                "type": "object"
            }
        },
        "VpcId": {
            "title": "Vpcid",
            "type": "string"
        },
        "LogDestinationConfigs": {
            "title": "Logdestinationconfigs",
            "type": "array",
            "items": {
                "$ref": "#/definitions/LogProfileConfig"
            }
        },
        "CloudWatchMetricNamespace": {
            "title": "Cloudwatchmetricnamespace",
            "type": "string"
        },
        "ProgrammaticAccessToken": {
            "type": "string"
        }
    },
    "additionalProperties": false,
    "required": [
        "EndpointMode",
        "FirewallName",
        "SubnetMappings",
        "VpcId",
        "ProgrammaticAccessToken",
        "LogDestinationConfigs"
    ],
    "createOnlyProperties": [
        "/properties/FirewallName"
    ],
    "primaryIdentifier": [
        "/properties/FirewallName"
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
        }
    }
}
{% endhighlight %}
