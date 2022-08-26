"""
Manual integration test for the config module.
Make sure creating, editing, and deleting individual notifications
always leaves the remaining bucket notifications exactly as they were.
"""

import json
import logging
import time
import boto3

from .config import create_role, delete_role
from .config import get, save, delete, get_all
from .models import ResourceModel, KeyVal

LOG = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main(profile_name): #pylint: disable=too-many-branches
    "Execute the tests and clean up"

    session = boto3.Session(profile_name=profile_name)
    sts = session.client('sts')
    identity = sts.get_caller_identity()
    account_id = identity["Account"]
    bucket_name = f"bucketnotification-config-integ-{account_id}"
    bucket_arn = None
    queue_name = "bucketnotification-config-integ"
    queue_url = None
    queue_arn = None
    topic_name = "bucketnotification-config-integ"
    topic_arn = None
    function_name = "bucketnotification-config-integ"
    function_arn = None
    function_role_name = "bucketnotification-config-integ-function"
    function_role_arn = None
    s3 = session.client("s3")
    sqs = session.client("sqs")
    sns = session.client("sns")
    lam = session.client("lambda")
    iam = session.client('iam')
    queue_role_name = None
    queue_role_policy_arn = None
    topic_role_name = None
    topic_role_policy_arn = None
    function_invoke_role_name = None
    function_invoke_role_policy_arn = None

    try:
        # Create a bucket
        print("About to create test bucket: ", bucket_name)
        s3.create_bucket(Bucket=bucket_name)
        bucket_arn = "arn:aws:s3:::" + bucket_name
        print("Created bucket: ", bucket_name)

        # Create an SQS Queue
        print("About to create test queue:", queue_name)

        r = None
        tries = 0
        succeeded = False
        while tries < 6:
            try:
                r = sqs.create_queue(QueueName=queue_name)
                succeeded = True
                break
            except sqs.exceptions.QueueDeletedRecently:
                print("Waiting 10 seconds to retry creating queue")
                tries = tries + 1
                time.sleep(10)

        if not succeeded:
            raise Exception("Exceeded max retries for creating queue")

        queue_url = r["QueueUrl"]
        r = sqs.get_queue_attributes(
            QueueUrl=queue_url,
            AttributeNames=["QueueArn"])
        queue_arn = r["Attributes"]["QueueArn"]
        (queue_role_name, queue_role_policy_arn) = create_role(session,
                "QTest1", "Queue", queue_arn, bucket_arn)

        print("Created test queue:", queue_url)

        # Create an SNS Topic
        print("About to create topic:", topic_name)

        r = sns.create_topic(Name=topic_name)
        topic_arn = r["TopicArn"]
        (topic_role_name, topic_role_policy_arn) = create_role(session,
                "Topic1", "Topic", topic_arn, bucket_arn)

        print("Created topic:", topic_arn)

        # Create a Lambda Function
        print("About to create function:", function_name)

        # Policy for the function
        lambda_execution_policy = {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "",
              "Effect": "Allow",
              "Principal": {
                "Service": "lambda.amazonaws.com"
              },
              "Action": "sts:AssumeRole"
            }
          ]
        }

        r = iam.create_role(
          RoleName=function_role_name,
          AssumeRolePolicyDocument=json.dumps(lambda_execution_policy),
        )
        print("Sleeping for 10 seconds to avoid race condition")
        time.sleep(10) # Potential race condition
        r = iam.get_role(RoleName=function_role_name)
        function_role_arn = r["Role"]["Arn"]
        print("Created function role:", function_role_arn)

        with open('awscommunity_s3_bucketnotification/test_lambda.zip', 'rb') as f:
            zipped_code = f.read()

        r = lam.create_function(FunctionName=function_name,
                Runtime="python3.7", 
                Role=function_role_arn,
                Handler="test_lambda.handle", 
                Code=dict(ZipFile=zipped_code))
        function_arn = r["FunctionArn"]
        (function_invoke_role_name, function_invoke_role_policy_arn) = \
            create_role(session, "FuncTest1", "Function", function_arn, bucket_arn)
        print("Created function:", r["FunctionArn"])

        # Create notifications for each target type
        # (Note that we aren't testing the notifications themselves, only the config)

        ORIG_TOPIC_1 = "topic1"
        ORIG_QUEUE_1 = "queue1"
        ORIG_FUNCTION_1 = "func1"

        original_configs = {
            "TopicConfigurations": [
                {
                    "Id": ORIG_TOPIC_1, 
                    "TopicArn": topic_arn,
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
                    "Id": ORIG_QUEUE_1, 
                    "QueueArn": queue_arn,
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
                    "Id": ORIG_FUNCTION_1, 
                    "LambdaFunctionArn": function_arn,
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

        # S3 has to verify that it can send the notifications, and sometimes
        # the permissions have not yet propagated.
        tries = 0
        succeeded = False
        max_tries = 1
        while tries < max_tries:
            try:
                tries = tries + 1
                print("About to try putting notification config")
                r = s3.put_bucket_notification_configuration(
                        Bucket=bucket_name,
                        NotificationConfiguration=original_configs,
                        SkipDestinationValidation=True)
                # Skipping validation... can't get this to succeed, even with retries
                # Confirmed that the targets are valid by creating the same thing
                # in the console.
                print("Successfully put the notification config")
                succeeded = True
                break
            except Exception:
                if tries >= max_tries:
                    raise
                print("Retrying for InvalidArgument exception")
                time.sleep(10)
        if not succeeded:
            raise Exception("Exceeded max tries to put bucket notification confguration")

        def validate_config(orig, current):
            "Validate that the original config has not changed"

            # Iterate over the top level keys: TopicConfgurations, etc
            for key in orig:
                if key not in current:
                    raise Exception("Missing " + key)

                # Iterate over the array of notifications under each XConfiguration
                for orig_item in orig[key]:

                    # Check each notification in the current config for a matching key
                    id_found = False
                    for cur_item in current[key]:
                        if cur_item["Id"] == orig_item["Id"]:
                            id_found = True
                            # Make sure the dict hasn't changed
                            if cur_item != orig_item:
                                print("cur_item", json.dumps(cur_item))
                                print("orig_item", json.dumps(orig_item))
                                raise Exception("Not the same: " + orig_item["Id"])
                    if not id_found:
                        raise Exception(f"Did not find {orig_item['Id']} in {key}")

        r = get_all(session, bucket_arn)
        validate_config(original_configs, r)

        # Test getting a notification
        topic1 = get(session, bucket_arn, ORIG_TOPIC_1)
        if not topic1:
            raise Exception("Unable to get original topic")
        orig_topic = original_configs["TopicConfigurations"][0]
        assert orig_topic["Id"] == topic1.Id
        assert orig_topic["Events"] == topic1.Events
        for rule in orig_topic["Filter"]["Key"]["FilterRules"]:
            found = False
            for kv in topic1.Filters:
                if kv.Name == rule["Name"] and kv.Value == rule["Value"]:
                    found = True
            assert found
        assert orig_topic["TopicArn"] == topic1.TargetArn

        # Model a new notification and save it
        NEW_ID = "topic2"
        model = ResourceModel(Id=NEW_ID, 
                Events=["s3:ObjectRemoved:*"], 
                Filters=[KeyVal(Name="Suffix", Value="xyz")],
                BucketArn=bucket_arn,
                TargetType="Topic",
                TargetArn=topic_arn)
        save(session, model, True)

        # Make sure none of the other notifications changed
        r = get_all(session, bucket_arn)
        validate_config(original_configs, r)

        # Alter a notification
        model.Events.append("s3:ObjectRestore:*")
        save(session, model, False)

        # Make sure none of the others changed
        r = get_all(session, bucket_arn)
        validate_config(original_configs, r)
        
        # Delete the new notification
        delete(session, bucket_arn, NEW_ID)

        # Make sure none of the others changed
        r = get_all(session, bucket_arn)
        validate_config(original_configs, r)

        # Make sure it was actually deleted
        print("r", json.dumps(r))
        assert len(r["TopicConfigurations"]) == 1
        assert r["TopicConfigurations"][0]["Id"] == ORIG_TOPIC_1

        print("Done. All tests passed")
    except Exception as e:
        print("Tests failed")
        LOG.exception(e) 

    cleanup = True

    if cleanup:

        try:
            # Delete the queue
            sqs.delete_queue(QueueUrl=queue_url)
            print("Deleted test queue:", queue_url)
        except Exception as e:
            LOG.exception(e) 

        try:
            # Delete the queue role
            delete_role(session, queue_role_name, queue_role_policy_arn)
            print("Deleted test queue role:", queue_role_name)
        except Exception as e:
            LOG.exception(e) 

        try:
            # Delete the topic
            sns.delete_topic(TopicArn=topic_arn)
            print("Deleted topic:", topic_arn)
        except Exception as e:
            LOG.exception(e) 

        try:
            # Delete the topic role
            delete_role(session, topic_role_name, topic_role_policy_arn)
            print("Deleted topic role:", topic_role_name)
        except Exception as e:
            LOG.exception(e) 

        try:
            # Delete the function
            lam.delete_function(FunctionName=function_name)
            print("Deleted function:", function_name)
        except Exception as e:
            LOG.exception(e) 

        try:
            # Delete the function invoke role
            delete_role(session, function_invoke_role_name, function_invoke_role_policy_arn)
            print("Deleted function invoke role:", function_invoke_role_name)
        except Exception as e:
            LOG.exception(e) 

        try:
            # Delete the function role
            iam.delete_role(RoleName=function_role_name)
            print("Deleted function role:", function_role_name)
        except Exception as e:
            LOG.exception(e) 

        try:
            # Delete the bucket
            s3.delete_bucket(Bucket=bucket_name)
            print("Deleted bucket: ", bucket_name)
        except Exception as e:
            LOG.exception(e) 

        print("Cleanup complete")

