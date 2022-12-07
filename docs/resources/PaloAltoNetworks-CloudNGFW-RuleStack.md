
## PaloAltoNetworks::CloudNGFW::RuleStack

## A rulestack defines the NGFW&#39;s advanced access control (APP-ID, URL Filtering) and threat prevention behavior.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-cloudformation&#x2F;aws-cloudformation-rpdk.git) 
- [Documentation]()

Published by PaloAltoNetworks

## Schema
{% highlight json %}
{
    "typeName": "PaloAltoNetworks::CloudNGFW::RuleStack",
    "description": "A rulestack defines the NGFW's advanced access control (APP-ID, URL Filtering) and threat prevention behavior.",
    "sourceUrl": "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
    "definitions": {
        "RuleStack": {
            "title": "RuleStack",
            "type": "object",
            "properties": {
                "Scope": {
                    "title": "Scope",
                    "default": "Local",
                    "enum": [
                        "Global",
                        "Local"
                    ],
                    "type": "string"
                },
                "LookupXForwardedFor": {
                    "title": "LookupXForwardedFor",
                    "default": "None",
                    "enum": [
                        "SecurityPolicy",
                        "None"
                    ],
                    "type": "string"
                },
                "MinAppIdVersion": {
                    "title": "Minappidversion",
                    "default": "8433-6838",
                    "pattern": "8\\d\\d\\d\\-\\d\\d\\d\\d",
                    "type": "string"
                },
                "Profiles": {
                    "$ref": "#/definitions/RuleStackProfiles"
                },
                "Description": {
                    "title": "Description",
                    "maxLength": 512,
                    "type": "string"
                },
                "Deploy": {
                    "title": "Deploy",
                    "description": "Deploy RuleStack YES/NO",
                    "default": "YES",
                    "type": "string"
                }
            },
            "additionalProperties": false
        },
        "RuleStackProfiles": {
            "title": "RuleStackProfiles",
            "type": "object",
            "properties": {
                "AntiSpywareProfile": {
                    "title": "Antispywareprofile",
                    "default": "BestPractice",
                    "enum": [
                        "BestPractice",
                        "None"
                    ],
                    "type": "string"
                },
                "AntiVirusProfile": {
                    "title": "Antivirusprofile",
                    "default": "BestPractice",
                    "enum": [
                        "BestPractice",
                        "None"
                    ],
                    "type": "string"
                },
                "VulnerabilityProfile": {
                    "title": "Vulnerabilityprofile",
                    "default": "BestPractice",
                    "enum": [
                        "BestPractice",
                        "None"
                    ],
                    "type": "string"
                },
                "URLFilteringProfile": {
                    "title": "Urlfilteringprofile",
                    "default": "None",
                    "enum": [
                        "BestPractice",
                        "None"
                    ],
                    "type": "string"
                },
                "FileBlockingProfile": {
                    "title": "Fileblockingprofile",
                    "default": "BestPractice",
                    "enum": [
                        "Custom",
                        "BestPractice",
                        "None"
                    ],
                    "type": "string"
                },
                "OutboundTrustCertificate": {
                    "title": "Outboundtrustcertificate",
                    "maxLength": 63,
                    "type": "string"
                },
                "OutboundUntrustCertificate": {
                    "title": "Outbounduntrustcertificate",
                    "maxLength": 63,
                    "type": "string"
                }
            },
            "additionalProperties": false
        },
        "Tag": {
            "title": "Tag",
            "type": "object",
            "properties": {
                "Key": {
                    "title": "Key",
                    "minLength": 1,
                    "maxLength": 128,
                    "type": "string"
                },
                "Value": {
                    "title": "Value",
                    "minLength": 1,
                    "maxLength": 128,
                    "type": "string"
                }
            },
            "required": [
                "Key",
                "Value"
            ],
            "additionalProperties": false
        },
        "Rule": {
            "title": "Rule",
            "type": "object",
            "properties": {
                "RuleName": {
                    "title": "Rulename",
                    "minLength": 1,
                    "maxLength": 48,
                    "pattern": "^[a-zA-Z0-9-]+$",
                    "type": "string"
                },
                "Description": {
                    "title": "Description",
                    "maxLength": 512,
                    "type": "string"
                },
                "RuleListType": {
                    "title": "RuleListType",
                    "description": "RuleList type: LocalRule, PreRule, PostRule",
                    "type": "string"
                },
                "Priority": {
                    "title": "Priority",
                    "description": "Priority of the Rule",
                    "type": "integer"
                },
                "Enabled": {
                    "title": "Enabled",
                    "default": true,
                    "type": "boolean"
                },
                "Source": {
                    "$ref": "#/definitions/RuleSource"
                },
                "NegateSource": {
                    "title": "Negatesource",
                    "default": false,
                    "type": "boolean"
                },
                "Destination": {
                    "$ref": "#/definitions/RuleDestination"
                },
                "NegateDestination": {
                    "title": "Negatedestination",
                    "default": false,
                    "type": "boolean"
                },
                "Applications": {
                    "title": "Applications",
                    "default": [
                        "any"
                    ],
                    "type": "array",
                    "items": {
                        "type": "string",
                        "maxLength": 63
                    }
                },
                "Category": {
                    "$ref": "#/definitions/UrlCategory"
                },
                "Protocol": {
                    "title": "Protocol",
                    "default": "application-default",
                    "maxLength": 63,
                    "type": "string"
                },
                "ProtPortList": {
                    "title": "ProtPortList",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "maxLength": 63
                    }
                },
                "AuditComment": {
                    "title": "Auditcomment",
                    "maxLength": 512,
                    "type": "string"
                },
                "Action": {
                    "title": "Action",
                    "default": "Allow",
                    "enum": [
                        "Allow",
                        "DenySilent",
                        "DenyResetServer",
                        "DenyResetBoth"
                    ],
                    "type": "string"
                },
                "Logging": {
                    "title": "Logging",
                    "default": false,
                    "type": "boolean"
                },
                "DecryptionRuleType": {
                    "title": "Decryptionruletype",
                    "enum": [
                        "SSLOutboundInspection"
                    ],
                    "type": "string"
                },
                "Tags": {
                    "title": "Tags",
                    "maxItems": 200,
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Tag"
                    }
                }
            },
            "required": [
                "RuleName",
                "RuleListType",
                "Priority"
            ],
            "additionalProperties": false
        },
        "RuleSource": {
            "title": "RuleSource",
            "type": "object",
            "properties": {
                "Cidrs": {
                    "title": "Cidrs",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "maxLength": 24
                    }
                },
                "PrefixLists": {
                    "title": "Prefixlists",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "maxLength": 63
                    }
                },
                "Countries": {
                    "title": "Countries",
                    "description": "Country code",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "maxLength": 2
                    }
                },
                "Feeds": {
                    "title": "Feeds",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "maxLength": 63
                    }
                }
            },
            "additionalProperties": false
        },
        "RuleDestination": {
            "title": "RuleDestination",
            "type": "object",
            "properties": {
                "Cidrs": {
                    "title": "Cidrs",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "maxLength": 24
                    }
                },
                "FqdnLists": {
                    "title": "Fqdnlists",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "maxLength": 63
                    }
                },
                "PrefixLists": {
                    "title": "Prefixlists",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "maxLength": 63
                    }
                },
                "Countries": {
                    "title": "Countries",
                    "description": "Country code",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "maxLength": 2
                    }
                },
                "Feeds": {
                    "title": "Feeds",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "maxLength": 63
                    }
                }
            },
            "additionalProperties": false
        },
        "UrlCategory": {
            "title": "UrlCategory",
            "type": "object",
            "properties": {
                "URLCategoryNames": {
                    "title": "Urlcategorynames",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "maxLength": 128
                    }
                },
                "Feeds": {
                    "title": "Feeds",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "maxLength": 63
                    }
                }
            },
            "additionalProperties": false
        },
        "CustomSecurityProfiles": {
            "description": "Custom Security Profiles object",
            "type": "object",
            "properties": {
                "FileBlocking": {
                    "$ref": "#/definitions/FileBlocking"
                }
            },
            "additionalProperties": false
        },
        "FileBlocking": {
            "title": "FileBlocking",
            "type": "object",
            "properties": {
                "Direction": {
                    "title": "Direction",
                    "default": "both",
                    "enum": [
                        "upload",
                        "download",
                        "both"
                    ],
                    "type": "string"
                },
                "FileType": {
                    "title": "FileType",
                    "type": "string"
                },
                "Description": {
                    "title": "Description",
                    "minLength": 1,
                    "maxLength": 255,
                    "type": "string"
                },
                "Action": {
                    "title": "Action",
                    "default": "alert",
                    "enum": [
                        "alert",
                        "block",
                        "continue"
                    ],
                    "type": "string"
                },
                "AuditComment": {
                    "title": "Auditcomment",
                    "type": "string"
                }
            },
            "required": [
                "FileType"
            ],
            "additionalProperties": false
        },
        "SecurityObjects": {
            "description": "Security objects",
            "type": "object",
            "properties": {
                "PrefixList": {
                    "$ref": "#/definitions/PrefixLists"
                },
                "FqdnList": {
                    "$ref": "#/definitions/FqdnLists"
                },
                "CustomUrlCategory": {
                    "$ref": "#/definitions/CustomUrlCategory"
                },
                "IntelligentFeed": {
                    "$ref": "#/definitions/IntelligentFeed"
                },
                "CertificateObject": {
                    "$ref": "#/definitions/CertificateObject"
                }
            },
            "additionalProperties": false
        },
        "PrefixLists": {
            "title": "PrefixLists",
            "description": "SecurityObjects PrefixList",
            "type": "object",
            "properties": {
                "Name": {
                    "title": "Name",
                    "minLength": 1,
                    "maxLength": 58,
                    "pattern": "^[a-zA-Z0-9-]+$",
                    "type": "string"
                },
                "PrefixList": {
                    "title": "Prefixlist",
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "AuditComment": {
                    "title": "Auditcomment",
                    "maxLength": 512,
                    "type": "string"
                },
                "Description": {
                    "title": "Description",
                    "maxLength": 512,
                    "type": "string"
                }
            },
            "required": [
                "Name",
                "PrefixList"
            ],
            "additionalProperties": false
        },
        "FqdnLists": {
            "title": "FqdnList",
            "type": "object",
            "properties": {
                "Name": {
                    "title": "Name",
                    "minLength": 1,
                    "maxLength": 58,
                    "pattern": "^[a-zA-Z0-9-]+$",
                    "type": "string"
                },
                "Description": {
                    "title": "Description",
                    "maxLength": 512,
                    "type": "string"
                },
                "FqdnList": {
                    "title": "Fqdnlist",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 255,
                        "pattern": "^[a-zA-Z0-9._-]+$"
                    }
                },
                "AuditComment": {
                    "title": "Auditcomment",
                    "maxLength": 512,
                    "type": "string"
                }
            },
            "required": [
                "Name",
                "FqdnList"
            ],
            "additionalProperties": false
        },
        "CustomUrlCategory": {
            "title": "CustomURLCategory",
            "type": "object",
            "properties": {
                "URLTargets": {
                    "title": "Urltargets",
                    "type": "array",
                    "items": {
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 255
                    }
                },
                "Name": {
                    "title": "Name",
                    "minLength": 1,
                    "maxLength": 58,
                    "pattern": "^[a-zA-Z0-9-]+$",
                    "type": "string"
                },
                "Description": {
                    "title": "Description",
                    "minLength": 1,
                    "maxLength": 255,
                    "type": "string"
                },
                "Action": {
                    "title": "Action",
                    "type": "string",
                    "default": "none",
                    "enum": [
                        "none",
                        "allow",
                        "alert",
                        "block"
                    ]
                },
                "AuditComment": {
                    "title": "Auditcomment",
                    "type": "string"
                }
            },
            "required": [
                "URLTargets"
            ],
            "additionalProperties": false
        },
        "IntelligentFeed": {
            "title": "IntelligentFeed",
            "type": "object",
            "properties": {
                "Name": {
                    "title": "Name",
                    "minLength": 1,
                    "maxLength": 63,
                    "pattern": "^[a-zA-Z0-9-]+$",
                    "type": "string"
                },
                "Description": {
                    "title": "Description",
                    "maxLength": 512,
                    "type": "string"
                },
                "Certificate": {
                    "title": "Certificate",
                    "type": "string"
                },
                "FeedURL": {
                    "title": "Feedurl",
                    "minLength": 1,
                    "maxLength": 255,
                    "pattern": "^(http|https)://.+$",
                    "type": "string"
                },
                "Type": {
                    "title": "Type",
                    "enum": [
                        "IP_LIST",
                        "URL_LIST"
                    ],
                    "type": "string"
                },
                "Frequency": {
                    "title": "Frequency",
                    "enum": [
                        "HOURLY",
                        "DAILY"
                    ],
                    "type": "string"
                },
                "Time": {
                    "title": "Time",
                    "default": 3,
                    "minimum": 0,
                    "maximum": 23,
                    "type": "integer"
                },
                "AuditComment": {
                    "title": "Auditcomment",
                    "maxLength": 512,
                    "type": "string"
                }
            },
            "required": [
                "Name",
                "FeedURL",
                "Type",
                "Frequency"
            ],
            "additionalProperties": false
        },
        "CertificateObject": {
            "title": "Certificate Object",
            "type": "object",
            "properties": {
                "Name": {
                    "title": "Name",
                    "minLength": 1,
                    "maxLength": 63,
                    "pattern": "^[a-zA-Z0-9-]+$",
                    "type": "string"
                },
                "Description": {
                    "title": "Description",
                    "maxLength": 512,
                    "type": "string"
                },
                "CertificateSignerArn": {
                    "title": "Certificatesignerarn",
                    "type": "string"
                },
                "CertificateSelfSigned": {
                    "title": "Certificateselfsigned",
                    "default": false,
                    "type": "boolean"
                },
                "AuditComment": {
                    "title": "Auditcomment",
                    "maxLength": 512,
                    "type": "string"
                }
            },
            "required": [
                "Name"
            ],
            "additionalProperties": false
        }
    },
    "properties": {
        "RuleStackName": {
            "description": "Rule stack name",
            "minLength": 1,
            "maxLength": 128,
            "pattern": "^[a-zA-Z0-9-]+$",
            "type": "string"
        },
        "RuleStack": {
            "$ref": "#/definitions/RuleStack"
        },
        "RuleList": {
            "description": "list of rules",
            "type": "array",
            "uniqueItems": false,
            "items": {
                "$ref": "#/definitions/Rule"
            }
        },
        "SecurityObjects": {
            "$ref": "#/definitions/SecurityObjects"
        },
        "CustomSecurityProfiles": {
            "$ref": "#/definitions/CustomSecurityProfiles"
        },
        "ProgrammaticAccessToken": {
            "type": "string"
        }
    },
    "additionalProperties": false,
    "required": [
        "RuleStackName",
        "ProgrammaticAccessToken"
    ],
    "createOnlyProperties": [
        "/properties/RuleStackName"
    ],
    "primaryIdentifier": [
        "/properties/RuleStackName"
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
