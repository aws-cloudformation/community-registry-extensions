
## Generic::Transcribe::Vocabulary

## A custom vocabulary that you can use to change the way Amazon Transcribe handles transcription of an audio file.

- [Source](https:&#x2F;&#x2F;github.com&#x2F;iann0036&#x2F;cfn-types&#x2F;tree&#x2F;master&#x2F;generic-transcribe-vocabulary) 
- [Documentation]()

Published by Ian Mckay

## Schema
{% highlight json %}
{
    "typeName": "Generic::Transcribe::Vocabulary",
    "description": "A custom vocabulary that you can use to change the way Amazon Transcribe handles transcription of an audio file.",
    "sourceUrl": "https://github.com/iann0036/cfn-types/tree/master/generic-transcribe-vocabulary",
    "properties": {
        "LanguageCode": {
            "description": "The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see [What is Amazon Transcribe?](https://docs.aws.amazon.com/transcribe/latest/dg/what-is-transcribe.html).",
            "type": "string"
        },
        "Phrases": {
            "type": "array",
            "description": "An array of strings that contains the vocabulary entries.",
            "items": {
                "type": "string",
                "pattern": ".+"
            }
        },
        "VocabularyFileUri": {
            "description": "The S3 location of the text file that contains the definition of the custom vocabulary. The URI must be in the same region as the API endpoint that you are calling.",
            "type": "string",
            "pattern": "(s3://|http(s*)://).+"
        },
        "VocabularyName": {
            "description": "The name of the vocabulary. The name must be unique within an AWS account. The name is case sensitive.",
            "type": "string",
            "pattern": "^[0-9a-zA-Z._-]+",
            "minLength": 1,
            "maxLength": 200
        }
    },
    "additionalProperties": false,
    "required": [
        "VocabularyName",
        "LanguageCode"
    ],
    "createOnlyProperties": [
        "/properties/VocabularyName"
    ],
    "writeOnlyProperties": [
        "/properties/VocabularyFileUri",
        "/properties/Phrases"
    ],
    "primaryIdentifier": [
        "/properties/VocabularyName"
    ],
    "handlers": {
        "create": {
            "permissions": [
                "transcribe:CreateVocabulary",
                "transcribe:GetVocabulary"
            ]
        },
        "read": {
            "permissions": [
                "transcribe:GetVocabulary"
            ]
        },
        "update": {
            "permissions": [
                "transcribe:UpdateVocabulary",
                "transcribe:GetVocabulary"
            ]
        },
        "delete": {
            "permissions": [
                "transcribe:DeleteVocabulary",
                "transcribe:GetVocabulary"
            ]
        },
        "list": {
            "permissions": [
                "transcribe:ListVocabularies"
            ]
        }
    }
}
{% endhighlight %}
