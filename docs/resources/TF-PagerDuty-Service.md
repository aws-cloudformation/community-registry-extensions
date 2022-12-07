
## TF::PagerDuty::Service

## A [service](https:&#x2F;&#x2F;v2.developer.pagerduty.com&#x2F;v2&#x2F;page&#x2F;api-reference#!&#x2F;Services&#x2F;get_services) represents something you monitor (like a web service, email service, or database service). It is a container for related incidents that associates them with escalation policies.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-tf-custom-types.git) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "TF::PagerDuty::Service",
    "description": "A [service](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Services/get_services) represents something you monitor (like a web service, email service, or database service). It is a container for related incidents that associates them with escalation policies.",
    "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
    "documentationUrl": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/pagerduty/TF-PagerDuty-Service/docs/README.md",
    "definitions": {
        "IncidentUrgencyRuleDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Type": {
                    "type": "string"
                },
                "Urgency": {
                    "type": "string"
                },
                "DuringSupportHours": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/DuringSupportHoursDefinition"
                    },
                    "maxItems": 1
                },
                "OutsideSupportHours": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/OutsideSupportHoursDefinition"
                    },
                    "maxItems": 1
                }
            },
            "required": [
                "Type"
            ]
        },
        "ScheduledActionsDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "ToUrgency": {
                    "type": "string"
                },
                "Type": {
                    "type": "string"
                },
                "At": {
                    "type": "array",
                    "insertionOrder": true,
                    "items": {
                        "$ref": "#/definitions/AtDefinition"
                    }
                }
            },
            "required": []
        },
        "SupportHoursDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "DaysOfWeek": {
                    "type": "array",
                    "insertionOrder": false,
                    "items": {
                        "type": "number"
                    }
                },
                "EndTime": {
                    "type": "string"
                },
                "StartTime": {
                    "type": "string"
                },
                "TimeZone": {
                    "type": "string"
                },
                "Type": {
                    "type": "string"
                }
            },
            "required": []
        },
        "DuringSupportHoursDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Type": {
                    "type": "string"
                },
                "Urgency": {
                    "type": "string"
                }
            },
            "required": []
        },
        "OutsideSupportHoursDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Type": {
                    "type": "string"
                },
                "Urgency": {
                    "type": "string"
                }
            },
            "required": []
        },
        "AtDefinition": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
                "Name": {
                    "type": "string"
                },
                "Type": {
                    "type": "string"
                }
            },
            "required": []
        }
    },
    "properties": {
        "tfcfnid": {
            "description": "Internal identifier for tracking resource changes. Do not use.",
            "type": "string"
        },
        "AcknowledgementTimeout": {
            "type": "string",
            "description": "Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the `\"null\"` string.\n* `escalation_policy` - (Required) The escalation policy used by this service.\n* `alert_creation` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value \"create_incidents\" is default: events will create an incident that cannot be merged. Value \"create_alerts_and_incidents\" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended.\n* `alert_grouping` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to `time`: All alerts within a specified duration will be grouped into the same incident. This duration is set in the `alert_grouping_timeout` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to `intelligent` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.\n* `alert_grouping_timeout` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the incident is resolved, set this value to `0`."
        },
        "AlertCreation": {
            "type": "string",
            "description": "Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value \"create_incidents\" is default: events will create an incident that cannot be merged. Value \"create_alerts_and_incidents\" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended.\n* `alert_grouping` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to `time`: All alerts within a specified duration will be grouped into the same incident. This duration is set in the `alert_grouping_timeout` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to `intelligent` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.\n* `alert_grouping_timeout` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the incident is resolved, set this value to `0`."
        },
        "AlertGrouping": {
            "type": "string",
            "description": "Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to `time`: All alerts within a specified duration will be grouped into the same incident. This duration is set in the `alert_grouping_timeout` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to `intelligent` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.\n* `alert_grouping_timeout` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the incident is resolved, set this value to `0`."
        },
        "AlertGroupingTimeout": {
            "type": "number",
            "description": "The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the incident is resolved, set this value to `0`."
        },
        "AutoResolveTimeout": {
            "type": "string",
            "description": "Time in seconds that an incident is automatically resolved if left open for that long. Disabled if set to the `\"null\"` string.\n* `acknowledgement_timeout` - (Optional) Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the `\"null\"` string.\n* `escalation_policy` - (Required) The escalation policy used by this service.\n* `alert_creation` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value \"create_incidents\" is default: events will create an incident that cannot be merged. Value \"create_alerts_and_incidents\" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended.\n* `alert_grouping` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to `time`: All alerts within a specified duration will be grouped into the same incident. This duration is set in the `alert_grouping_timeout` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to `intelligent` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.\n* `alert_grouping_timeout` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the incident is resolved, set this value to `0`."
        },
        "CreatedAt": {
            "type": "string"
        },
        "Description": {
            "type": "string",
            "description": "A human-friendly description of the service.\nIf not set, a placeholder of \"Managed by Terraform\" will be set.\n* `auto_resolve_timeout` - (Optional) Time in seconds that an incident is automatically resolved if left open for that long. Disabled if set to the `\"null\"` string.\n* `acknowledgement_timeout` - (Optional) Time in seconds that an incident changes to the Triggered State after being Acknowledged. Disabled if set to the `\"null\"` string.\n* `escalation_policy` - (Required) The escalation policy used by this service.\n* `alert_creation` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value \"create_incidents\" is default: events will create an incident that cannot be merged. Value \"create_alerts_and_incidents\" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended.\n* `alert_grouping` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to `time`: All alerts within a specified duration will be grouped into the same incident. This duration is set in the `alert_grouping_timeout` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to `intelligent` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.\n* `alert_grouping_timeout` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the incident is resolved, set this value to `0`."
        },
        "EscalationPolicy": {
            "type": "string",
            "description": "The escalation policy used by this service.\n* `alert_creation` - (Optional) Must be one of two values. PagerDuty receives events from your monitoring systems and can then create incidents in different ways. Value \"create_incidents\" is default: events will create an incident that cannot be merged. Value \"create_alerts_and_incidents\" is the alternative: events will create an alert and then add it to a new incident, these incidents can be merged. This option is recommended.\n* `alert_grouping` - (Optional) Defines how alerts on this service will be automatically grouped into incidents. Note that the alert grouping features are available only on certain plans. If not set, each alert will create a separate incident; If value is set to `time`: All alerts within a specified duration will be grouped into the same incident. This duration is set in the `alert_grouping_timeout` setting (described below). Available on Standard, Enterprise, and Event Intelligence plans; If value is set to `intelligent` - Alerts will be intelligently grouped based on a machine learning model that looks at the alert summary, timing, and the history of grouped alerts. Available on Enterprise and Event Intelligence plan.\n* `alert_grouping_timeout` - (Optional) The duration in minutes within which to automatically group incoming alerts. This setting applies only when `alert_grouping` is set to `time`. To continue grouping alerts until the incident is resolved, set this value to `0`."
        },
        "HtmlUrl": {
            "type": "string"
        },
        "Id": {
            "type": "string"
        },
        "LastIncidentTimestamp": {
            "type": "string"
        },
        "Name": {
            "type": "string",
            "description": "Designates either the start or the end of the scheduled action. Can be `support_hours_start` or `support_hours_end`."
        },
        "Status": {
            "type": "string"
        },
        "IncidentUrgencyRule": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/IncidentUrgencyRuleDefinition"
            },
            "maxItems": 1
        },
        "ScheduledActions": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/ScheduledActionsDefinition"
            }
        },
        "SupportHours": {
            "type": "array",
            "insertionOrder": false,
            "items": {
                "$ref": "#/definitions/SupportHoursDefinition"
            },
            "maxItems": 1
        }
    },
    "additionalProperties": false,
    "required": [
        "EscalationPolicy",
        "Name"
    ],
    "readOnlyProperties": [
        "/properties/tfcfnid",
        "/properties/CreatedAt",
        "/properties/HtmlUrl",
        "/properties/Id",
        "/properties/LastIncidentTimestamp",
        "/properties/Status"
    ],
    "primaryIdentifier": [
        "/properties/tfcfnid"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "s3:GetObject",
                "s3:DeleteObject",
                "lambda:InvokeFunction"
            ]
        },
        "read": {
            "permissions": [
                "s3:GetObject"
            ]
        },
        "update": {
            "permissions": [
                "s3:GetObject",
                "s3:DeleteObject",
                "lambda:InvokeFunction"
            ]
        },
        "delete": {
            "permissions": [
                "s3:GetObject",
                "s3:DeleteObject",
                "lambda:InvokeFunction"
            ]
        },
        "list": {
            "permissions": [
                "s3:GetObject",
                "s3:ListBucket"
            ]
        }
    }
}
{% endhighlight %}
