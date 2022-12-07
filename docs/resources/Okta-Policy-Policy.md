
## Okta::Policy::Policy

Manages an Okta Policy

- [Source](https:&#x2F;&#x2F;github.com&#x2F;aws-ia&#x2F;cloudformation-okta-resource-providers.git) 
- [Documentation]()

Published by AWS Community

## Schema
{% highlight json %}
{
    "typeName": "Okta::Policy::Policy",
    "description": "Manages an Okta Policy",
    "sourceUrl": "https://github.com/aws-ia/cloudformation-okta-resource-providers.git",
    "documentationUrl": "https://github.com/aws-ia/cloudformation-okta-resource-providers",
    "typeConfiguration": {
        "properties": {
            "OktaAccess": {
                "$ref": "#/definitions/OktaAccess"
            }
        },
        "additionalProperties": false
    },
    "definitions": {
        "OktaAccess": {
            "type": "object",
            "properties": {
                "Url": {
                    "type": "string",
                    "description": "Okta URL, including organization identifier"
                },
                "ApiKey": {
                    "type": "string",
                    "description": "Okta API tokens are used to authenticate requests to Okta APIs."
                }
            },
            "additionalProperties": false
        },
        "Links": {
            "type": "object",
            "properties": {
                "Self": {
                    "type": "string",
                    "description": "The Policy or Rule"
                },
                "Activate": {
                    "type": "string",
                    "description": "Action to activate a Policy or Rule (present if the Rule is currently inactive)"
                },
                "Deactivate": {
                    "type": "string",
                    "description": "Action to deactivate a Policy or Rule (present if the Rule is currently active)"
                },
                "Rules": {
                    "type": "string",
                    "description": "Action to retrieve the Rules objects for the given Policy"
                }
            },
            "additionalProperties": false
        }
    },
    "properties": {
        "Id": {
            "type": "string",
            "description": "Identifier of the Policy"
        },
        "Type": {
            "type": "string",
            "description": "Specifies the type of Policy.",
            "enum": [
                "OKTA_SIGN_ON",
                "PASSWORD",
                "MFA_ENROLL",
                "OAUTH_AUTHORIZATION_POLICY",
                "IDP_DISCOVERY",
                "ACCESS_POLICY"
            ]
        },
        "Name": {
            "type": "string",
            "description": "Name of the Policy"
        },
        "Description": {
            "type": "string",
            "description": "Description of the Policy."
        },
        "Priority": {
            "type": "integer",
            "description": "Priority of the Policy"
        },
        "Conditions": {
            "type": "object"
        }
    },
    "additionalProperties": false,
    "required": [
        "Type",
        "Name",
        "Description"
    ],
    "readOnlyProperties": [
        "/properties/Id"
    ],
    "primaryIdentifier": [
        "/properties/Id"
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
