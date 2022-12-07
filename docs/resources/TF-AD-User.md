
## TF::AD::User

CloudFormation equivalent of ad_user

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-tf-custom-types.git) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "TF::AD::User",
    "description": "CloudFormation equivalent of ad_user",
    "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
    "documentationUrl": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/ad/TF-AD-User/docs/README.md",
    "definitions": {},
    "properties": {
        "tfcfnid": {
            "description": "Internal identifier for tracking resource changes. Do not use.",
            "type": "string"
        },
        "CannotChangePassword": {
            "type": "boolean"
        },
        "City": {
            "type": "string"
        },
        "Company": {
            "type": "string"
        },
        "Container": {
            "type": "string"
        },
        "Country": {
            "type": "string"
        },
        "CustomAttributes": {
            "type": "string"
        },
        "Department": {
            "type": "string"
        },
        "Description": {
            "type": "string"
        },
        "DisplayName": {
            "type": "string"
        },
        "Division": {
            "type": "string"
        },
        "EmailAddress": {
            "type": "string"
        },
        "EmployeeId": {
            "type": "string"
        },
        "EmployeeNumber": {
            "type": "string"
        },
        "Enabled": {
            "type": "boolean"
        },
        "Fax": {
            "type": "string"
        },
        "GivenName": {
            "type": "string"
        },
        "HomeDirectory": {
            "type": "string"
        },
        "HomeDrive": {
            "type": "string"
        },
        "HomePage": {
            "type": "string"
        },
        "HomePhone": {
            "type": "string"
        },
        "Id": {
            "type": "string"
        },
        "InitialPassword": {
            "type": "string"
        },
        "Initials": {
            "type": "string"
        },
        "MobilePhone": {
            "type": "string"
        },
        "Office": {
            "type": "string"
        },
        "OfficePhone": {
            "type": "string"
        },
        "Organization": {
            "type": "string"
        },
        "OtherName": {
            "type": "string"
        },
        "PasswordNeverExpires": {
            "type": "boolean"
        },
        "PoBox": {
            "type": "string"
        },
        "PostalCode": {
            "type": "string"
        },
        "PrincipalName": {
            "type": "string"
        },
        "SamAccountName": {
            "type": "string"
        },
        "Sid": {
            "type": "string"
        },
        "SmartCardLogonRequired": {
            "type": "boolean"
        },
        "State": {
            "type": "string"
        },
        "StreetAddress": {
            "type": "string"
        },
        "Surname": {
            "type": "string"
        },
        "Title": {
            "type": "string"
        },
        "TrustedForDelegation": {
            "type": "boolean"
        }
    },
    "additionalProperties": false,
    "required": [
        "DisplayName",
        "PrincipalName",
        "SamAccountName"
    ],
    "readOnlyProperties": [
        "/properties/tfcfnid",
        "/properties/Id",
        "/properties/Sid"
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
