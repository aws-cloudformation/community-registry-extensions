"""
Unit tests for config.py

This can be invoked by running `pytest src` from the `BucketNotification` directory.
"""
# pylint:disable=R0801

from .config import find

def test_find():
    "Test the find function"
    cfg = {
        "TopicConfigurations": [
            {
                "Id": "Test1", 
                "TopicArn": "arn:aws:sns:us-east-1:1234567890:TestTopic",
                "Events": ["s3:ObjectCreated:*"],
                "Filter": {
                    "Key": {
                        "FilterRules": [
                            {
                                "Name": "Suffix",
                                "Value": "jpg"
                            }
                        ]
                    }
                }
            }
        ],
        "QueueConfigurations": [
            {
                "Id": "Test2", 
                "QueueArn": "arn:aws:xxxx",
                "Events": ["s3:ObjectCreated:*"],
                "Filter": {
                    "Key": {
                        "FilterRules": [
                            {
                                "Name": "Suffix",
                                "Value": "png"
                            }
                        ]
                    }
                }
            }
        ],
        "LambdaFunctionConfigurations": [
            {
                "Id": "Test3", 
                "LambdaFunctionArn": "arn:aws:xxxx",
                "Events": ["s3:ObjectCreated:*"],
                "Filter": {
                    "Key": {
                        "FilterRules": [
                            {
                                "Name": "Suffix",
                                "Value": "gif"
                            }
                        ]
                    }
                }
            }
        ]
    }
    model_id = "Test1"
    (notification, idx) = find(cfg, model_id)
    assert idx == 0
    assert notification["TopicArn"] == "arn:aws:sns:us-east-1:1234567890:TestTopic"

    cfg = {}
    (notification, idx) = find(cfg, model_id)
    assert notification is None

    

