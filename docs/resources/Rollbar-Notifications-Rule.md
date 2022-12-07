
## Rollbar::Notifications::Rule

Manage a notification rule for Rollbar.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-rollbar-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Rollbar::Notifications::Rule",
    "description": "Manage a notification rule for Rollbar.",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-rollbar-resource-providers.git",
    "documentationUrl": "https://github.com/aws-ia/cloudformation-rollbar-resource-providers",
    "definitions": {
        "ProjectAccessToken": {
            "description": "Use a Project Access Token with 'write' scope. This determines onto to which project the rule will be created",
            "type": "string"
        },
        "SlackTrigger": {
            "description": "An error/ message is seen for the first time.",
            "type": "string",
            "enum": [
                "new_item",
                "occurrence",
                "deploy",
                "reactivated_item",
                "resolved_item",
                "new_version",
                "reopened_item",
                "occurrence_rate",
                "exp_repeat_item"
            ]
        },
        "PagerDutyTrigger": {
            "description": "An error/ message is seen for the first time.",
            "type": "string",
            "enum": [
                "new_item",
                "reactivated_item",
                "resolved_item",
                "occurrence_rate",
                "exp_repeat_item"
            ]
        },
        "EmailTrigger": {
            "description": "An error/ message is seen for the first time.",
            "type": "string",
            "enum": [
                "new_item",
                "occurrence",
                "deploy",
                "reactivated_item",
                "resolved_item",
                "new_version",
                "reopened_item",
                "occurrence_rate",
                "exp_repeat_item",
                "daily_summary"
            ]
        },
        "WebhookTrigger": {
            "description": "An error/ message is seen for the first time.",
            "type": "string",
            "enum": [
                "new_item",
                "occurrence",
                "deploy",
                "reactivated_item",
                "resolved_item",
                "exp_repeat_item",
                "reopened_item",
                "occurrence_rate"
            ]
        },
        "ActionableConfig": {
            "type": "object",
            "properties": {
                "MessageTemplate": {
                    "description": "Define a custom template for the Slack message. More information here https://docs.rollbar.com/docs/slack#section-tips-tricks",
                    "type": "string"
                },
                "ShowMessageButton": {
                    "description": "Show the Slack actionable buttons",
                    "type": "boolean"
                },
                "Channel": {
                    "description": "The Slack channel to send the messages",
                    "type": "string"
                }
            },
            "additionalProperties": false
        },
        "NonActionableConfig": {
            "type": "object",
            "properties": {
                "MessageTemplate": {
                    "description": "Define a custom template for the Slack message. More information here https://docs.rollbar.com/docs/slack#section-tips-tricks",
                    "type": "string"
                },
                "Channel": {
                    "description": "The Slack channel to send the messages",
                    "type": "string"
                }
            },
            "additionalProperties": false
        },
        "PagerDutyConfig": {
            "type": "object",
            "properties": {
                "ServiceKey": {
                    "description": "PagerDuty Service API Key",
                    "type": "string"
                }
            },
            "additionalProperties": false
        },
        "EmailConfig": {
            "type": "object",
            "properties": {
                "Teams": {
                    "description": "List of team names to send emails to",
                    "type": "array",
                    "uniqueItems": true,
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    }
                },
                "Users": {
                    "description": "List of usernames or email addresses to send emails to",
                    "type": "array",
                    "uniqueItems": true,
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    }
                }
            },
            "additionalProperties": false
        },
        "EmailDailySummaryConfig": {
            "type": "object",
            "properties": {
                "Teams": {
                    "description": "List of team names to send emails to",
                    "type": "array",
                    "uniqueItems": true,
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    }
                },
                "Users": {
                    "description": "List of usernames or email addresses to send emails to",
                    "type": "array",
                    "uniqueItems": true,
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    }
                },
                "SummaryTime": {
                    "description": "ime of day to send the report, in seconds past midnight UTC",
                    "type": "integer"
                },
                "SendOnlyIfData": {
                    "description": "Specify whether to send empty reports",
                    "type": "boolean"
                },
                "Environments": {
                    "description": "List of environments to include in the daily summary",
                    "type": "array",
                    "uniqueItems": true,
                    "insertionOrder": false,
                    "items": {
                        "type": "string"
                    }
                },
                "MinItemLevel": {
                    "description": "Minimum severity level to include",
                    "type": "string",
                    "enum": [
                        "debug",
                        "info",
                        "warning",
                        "error",
                        "critical"
                    ]
                }
            },
            "additionalProperties": false
        },
        "WebhookConfig": {
            "type": "object",
            "properties": {
                "Url": {
                    "description": "Defines a webhook url for this specific rule",
                    "type": "string"
                },
                "Format": {
                    "description": "Request/response format can be JSON or XML",
                    "type": "string"
                }
            },
            "additionalProperties": false
        },
        "EnvironmentFilter": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "Item Environment.",
                    "type": "string",
                    "const": "environment"
                },
                "Operation": {
                    "type": "string",
                    "enum": [
                        "eq",
                        "neq"
                    ]
                },
                "Value": {
                    "type": "string"
                }
            },
            "additionalProperties": false,
            "required": [
                "Type",
                "Operation",
                "Value"
            ]
        },
        "LevelFilter": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "Item Level.",
                    "type": "string",
                    "const": "level"
                },
                "Operation": {
                    "type": "string",
                    "enum": [
                        "eq",
                        "gte"
                    ]
                },
                "Value": {
                    "type": "string",
                    "enum": [
                        "debug",
                        "info",
                        "warning",
                        "error",
                        "critical"
                    ]
                }
            },
            "additionalProperties": false,
            "required": [
                "Type",
                "Operation",
                "Value"
            ]
        },
        "TitleFilter": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "Item Title.",
                    "type": "string",
                    "const": "title"
                },
                "Operation": {
                    "type": "string",
                    "enum": [
                        "within",
                        "nwithin",
                        "regex",
                        "nregex"
                    ]
                },
                "Value": {
                    "type": "string"
                }
            },
            "additionalProperties": false,
            "required": [
                "Type",
                "Operation",
                "Value"
            ]
        },
        "FilenameFilter": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "Matches the name of any file in the stack trace.",
                    "type": "string",
                    "const": "filename"
                },
                "Operation": {
                    "type": "string",
                    "enum": [
                        "within",
                        "nwithin",
                        "regex",
                        "nregex"
                    ]
                },
                "Value": {
                    "type": "string"
                }
            },
            "additionalProperties": false,
            "required": [
                "Type",
                "Operation",
                "Value"
            ]
        },
        "ContextFilter": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "Matches context value (if included in payload)",
                    "type": "string",
                    "const": "context"
                },
                "Operation": {
                    "type": "string",
                    "enum": [
                        "startswith",
                        "eq",
                        "neq"
                    ]
                },
                "Value": {
                    "type": "string"
                }
            },
            "additionalProperties": false,
            "required": [
                "Type",
                "Operation",
                "Value"
            ]
        },
        "MethodFilter": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "Matches any method in the stack trace",
                    "type": "string",
                    "const": "method"
                },
                "Operation": {
                    "type": "string",
                    "enum": [
                        "within",
                        "nwithin",
                        "regex",
                        "nregex"
                    ]
                },
                "Value": {
                    "type": "string"
                }
            },
            "additionalProperties": false,
            "required": [
                "Type",
                "Operation",
                "Value"
            ]
        },
        "FrameworkFilter": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "Platform/language of the item",
                    "type": "string",
                    "const": "framework"
                },
                "Operation": {
                    "type": "string",
                    "enum": [
                        "eq"
                    ]
                },
                "Value": {
                    "type": "string"
                }
            },
            "additionalProperties": false,
            "required": [
                "Type",
                "Operation",
                "Value"
            ]
        },
        "PathFilter": {
            "type": "object",
            "properties": {
                "Path": {
                    "type": "string"
                },
                "Type": {
                    "description": "Allows for filtering based on any data in the JSON payload. To view the JSON structure of your errors, check out the Raw JSON section of any occurrence",
                    "type": "string",
                    "const": "path"
                },
                "Operation": {
                    "type": "string",
                    "enum": [
                        "eq",
                        "gte",
                        "lte",
                        "within",
                        "nwithin",
                        "neq",
                        "regex",
                        "nregex",
                        "startswith"
                    ]
                },
                "Value": {
                    "type": "string"
                }
            },
            "additionalProperties": false,
            "required": [
                "Path",
                "Type",
                "Operation",
                "Value"
            ]
        },
        "PathWithExistsFilter": {
            "type": "object",
            "properties": {
                "Path": {
                    "type": "string"
                },
                "Type": {
                    "description": "Allows for filtering based on any data in the JSON payload. To view the JSON structure of your errors, check out the Raw JSON section of any occurrence",
                    "type": "string",
                    "const": "path"
                },
                "Operation": {
                    "type": "string",
                    "enum": [
                        "eq",
                        "gte",
                        "lte",
                        "within",
                        "nwithin",
                        "neq",
                        "regex",
                        "nregex",
                        "startswith",
                        "exists",
                        "nexists"
                    ]
                },
                "Value": {
                    "type": "string"
                }
            },
            "additionalProperties": false,
            "required": [
                "Path",
                "Type",
                "Operation",
                "Value"
            ]
        },
        "UniqueOccurrencesFilter": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "Number of unique IPs affected for the item",
                    "type": "string",
                    "const": "unique_occurrences"
                },
                "Operation": {
                    "type": "string",
                    "enum": [
                        "gte"
                    ]
                },
                "Value": {
                    "type": "number"
                }
            },
            "additionalProperties": false,
            "required": [
                "Type",
                "Operation",
                "Value"
            ]
        },
        "RateFilter": {
            "type": "object",
            "properties": {
                "Type": {
                    "description": "Rate of occurrences of an item",
                    "type": "string",
                    "const": "rate"
                },
                "Period": {
                    "description": "Number of seconds",
                    "type": "number"
                },
                "Count": {
                    "type": "number"
                }
            },
            "additionalProperties": false,
            "required": [
                "Type",
                "Period",
                "Count"
            ]
        },
        "Filters": {
            "description": "To keep your notifications relevant, you'll want to apply filters to limit when they send messages or create incidents.",
            "type": "array",
            "uniqueItems": true,
            "insertionOrder": false,
            "items": {
                "anyOf": [
                    {
                        "$ref": "#/definitions/EnvironmentFilter"
                    },
                    {
                        "$ref": "#/definitions/LevelFilter"
                    },
                    {
                        "$ref": "#/definitions/TitleFilter"
                    },
                    {
                        "$ref": "#/definitions/FilenameFilter"
                    },
                    {
                        "$ref": "#/definitions/ContextFilter"
                    },
                    {
                        "$ref": "#/definitions/MethodFilter"
                    },
                    {
                        "$ref": "#/definitions/FrameworkFilter"
                    },
                    {
                        "$ref": "#/definitions/PathFilter"
                    },
                    {
                        "$ref": "#/definitions/PathWithExistsFilter"
                    },
                    {
                        "$ref": "#/definitions/UniqueOccurrencesFilter"
                    },
                    {
                        "$ref": "#/definitions/RateFilter"
                    }
                ]
            }
        },
        "SlackRule": {
            "description": "Create Slack notification rule",
            "type": "object",
            "properties": {
                "Trigger": {
                    "$ref": "#/definitions/SlackTrigger"
                },
                "Filters": {
                    "$ref": "#/definitions/Filters"
                },
                "Action": {
                    "description": "The action associated with this rule",
                    "type": "string",
                    "const": "send_message"
                },
                "Config": {
                    "anyOf": [
                        {
                            "$ref": "#/definitions/ActionableConfig"
                        },
                        {
                            "$ref": "#/definitions/NonActionableConfig"
                        }
                    ]
                }
            },
            "additionalProperties": false,
            "required": [
                "Trigger"
            ]
        },
        "PagerDutyRule": {
            "description": "Create PagerDuty notification rules",
            "type": "object",
            "properties": {
                "Trigger": {
                    "$ref": "#/definitions/PagerDutyTrigger"
                },
                "Filters": {
                    "$ref": "#/definitions/Filters"
                },
                "Action": {
                    "description": "The action associated with this rule",
                    "type": "string",
                    "const": "trigger_incident"
                },
                "Config": {
                    "$ref": "#/definitions/PagerDutyConfig"
                }
            },
            "additionalProperties": false,
            "required": [
                "Trigger"
            ]
        },
        "EmailRule": {
            "description": "Create Email notification rules",
            "type": "object",
            "properties": {
                "Trigger": {
                    "$ref": "#/definitions/EmailTrigger"
                },
                "Filters": {
                    "$ref": "#/definitions/Filters"
                },
                "Action": {
                    "description": "The action associated with this rule",
                    "type": "string",
                    "const": "trigger_incident"
                },
                "Config": {
                    "anyOf": [
                        {
                            "$ref": "#/definitions/EmailConfig"
                        },
                        {
                            "$ref": "#/definitions/EmailDailySummaryConfig"
                        }
                    ]
                }
            },
            "additionalProperties": false,
            "required": [
                "Trigger"
            ]
        },
        "WebhookRule": {
            "description": "Create Webhook notification rules",
            "type": "object",
            "properties": {
                "Trigger": {
                    "$ref": "#/definitions/WebhookTrigger"
                },
                "Filters": {
                    "$ref": "#/definitions/Filters"
                },
                "Action": {
                    "description": "The action associated with this rule",
                    "type": "string",
                    "const": "trigger_incident"
                },
                "Config": {
                    "$ref": "#/definitions/WebhookConfig"
                }
            },
            "additionalProperties": false,
            "required": [
                "Trigger"
            ]
        }
    },
    "properties": {
        "ProjectAccessToken": {
            "$ref": "#/definitions/ProjectAccessToken"
        },
        "Slack": {
            "$ref": "#/definitions/SlackRule"
        },
        "PagerDuty": {
            "$ref": "#/definitions/PagerDutyRule"
        },
        "Email": {
            "$ref": "#/definitions/EmailRule"
        },
        "Webhook": {
            "$ref": "#/definitions/WebhookRule"
        },
        "Id": {
            "description": "The rule ID",
            "type": "number"
        },
        "Trigger": {
            "description": "The trigger associated with this rule",
            "type": "string"
        },
        "Action": {
            "description": "The action associated with this rule",
            "type": "string"
        },
        "RuleType": {
            "description": "the rule type",
            "type": "string"
        }
    },
    "additionalProperties": false,
    "tagging": {
        "taggable": false
    },
    "required": [
        "ProjectAccessToken"
    ],
    "createOnlyProperties": [
        "/properties/ProjectAccessToken"
    ],
    "writeOnlyProperties": [
        "/properties/Slack",
        "/properties/PagerDuty",
        "/properties/Email",
        "/properties/Webhook"
    ],
    "readOnlyProperties": [
        "/properties/Id",
        "/properties/Trigger",
        "/properties/Action",
        "/properties/RuleType"
    ],
    "primaryIdentifier": [
        "/properties/Id",
        "/properties/RuleType",
        "/properties/ProjectAccessToken"
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
