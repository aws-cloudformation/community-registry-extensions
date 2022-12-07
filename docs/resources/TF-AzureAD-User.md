
## TF::AzureAD::User

## Manages a User within Azure Active Directory.

-&gt; **NOTE:** If you&#39;re authenticating using a Service Principal then it must have permissions to &#x60;Directory.ReadWrite.All&#x60; within the &#x60;Windows Azure Active Directory&#x60; API.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-tf-custom-types.git) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "TF::AzureAD::User",
    "description": "Manages a User within Azure Active Directory.\n\n-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to `Directory.ReadWrite.All` within the `Windows Azure Active Directory` API.",
    "sourceUrl": "https://github.com/iann0036/cfn-tf-custom-types.git",
    "documentationUrl": "https://github.com/iann0036/cfn-tf-custom-types/blob/docs/resources/azuread/TF-AzureAD-User/docs/README.md",
    "definitions": {},
    "properties": {
        "tfcfnid": {
            "description": "Internal identifier for tracking resource changes. Do not use.",
            "type": "string"
        },
        "AccountEnabled": {
            "type": "boolean",
            "description": "`true` if the account should be enabled, otherwise `false`. Defaults to `true`."
        },
        "City": {
            "type": "string",
            "description": "The city in which the user is located."
        },
        "CompanyName": {
            "type": "string",
            "description": "The company name which the user is associated. This property can be useful for describing the company that an external user comes from."
        },
        "Country": {
            "type": "string",
            "description": "The country/region in which the user is located; for example, “US” or “UK”."
        },
        "Department": {
            "type": "string",
            "description": "The name for the department in which the user works."
        },
        "DisplayName": {
            "type": "string",
            "description": "The name to display in the address book for the user."
        },
        "ForcePasswordChange": {
            "type": "boolean",
            "description": "`true` if the User is forced to change the password during the next sign-in. Defaults to `false`."
        },
        "GivenName": {
            "type": "string",
            "description": "The given name (first name) of the user."
        },
        "Id": {
            "type": "string"
        },
        "ImmutableId": {
            "type": "string",
            "description": "The value used to associate an on-premise Active Directory user account with their Azure AD user object. Deprecated in favour of `onpremises_immutable_id`."
        },
        "JobTitle": {
            "type": "string",
            "description": "The user’s job title."
        },
        "Mail": {
            "type": "string"
        },
        "MailNickname": {
            "type": "string",
            "description": "The mail alias for the user. Defaults to the user name part of the User Principal Name."
        },
        "Mobile": {
            "type": "string",
            "description": "The primary cellular telephone number for the user. Deprecated in favour of `mobile_phone`."
        },
        "MobilePhone": {
            "type": "string",
            "description": "The primary cellular telephone number for the user."
        },
        "ObjectId": {
            "type": "string"
        },
        "OfficeLocation": {
            "type": "string",
            "description": "The office location in the user's place of business."
        },
        "OnpremisesImmutableId": {
            "type": "string",
            "description": "The value used to associate an on-premise Active Directory user account with their Azure AD user object. This must be specified if you are using a federated domain for the user's userPrincipalName (UPN) property when creating a new user account."
        },
        "OnpremisesSamAccountName": {
            "type": "string"
        },
        "OnpremisesUserPrincipalName": {
            "type": "string"
        },
        "Password": {
            "type": "string",
            "description": "The password for the User. The password must satisfy minimum requirements as specified by the password policy. The maximum length is 256 characters."
        },
        "PhysicalDeliveryOfficeName": {
            "type": "string",
            "description": "The office location in the user's place of business. Deprecated in favour of `office_location`."
        },
        "PostalCode": {
            "type": "string",
            "description": "The postal code for the user's postal address. The postal code is specific to the user's country/region. In the United States of America, this attribute contains the ZIP code."
        },
        "State": {
            "type": "string",
            "description": "The state or province in the user's address."
        },
        "StreetAddress": {
            "type": "string",
            "description": "The street address of the user's place of business."
        },
        "Surname": {
            "type": "string",
            "description": "The user's surname (family name or last name)."
        },
        "UsageLocation": {
            "type": "string",
            "description": "The usage location of the User. Required for users that will be assigned licenses due to legal requirement to check for availability of services in countries. The usage location is a two letter country code (ISO standard 3166). Examples include: `NO`, `JP`, and `GB`. Cannot be reset to null once set."
        },
        "UserPrincipalName": {
            "type": "string",
            "description": "The User Principal Name of the User."
        },
        "UserType": {
            "type": "string"
        }
    },
    "additionalProperties": false,
    "required": [
        "DisplayName",
        "Password",
        "UserPrincipalName"
    ],
    "readOnlyProperties": [
        "/properties/tfcfnid",
        "/properties/Id",
        "/properties/Mail",
        "/properties/ObjectId",
        "/properties/OnpremisesSamAccountName",
        "/properties/OnpremisesUserPrincipalName",
        "/properties/UserType"
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
    },
    "writeOnlyProperties": [
        "/properties/Password"
    ]
}
{% endhighlight %}
