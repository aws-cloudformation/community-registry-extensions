"""
This module contains functions to act on a single notification configuration, 
without changing any of the existing bucket configurations, unless the 
Id for the notification is found among existing notifications. This allows 
us to treat each indiidual notification as if it were an independent resource.

The `model` argument to these functions is from the auto-generated `models.ResourceModel`.
"""

import json
import logging
from .models import ResourceModel

LOG = logging.getLogger(__name__)

def find(cfg, model_id):
    """
    Find the notification in the full config by id
    Returns (notification, idx) or (None, -1)
    """

    notification = None

    if not model_id:
        return notification

    idx = 0
    for t in cfg:
        if notification:
            break
        idx = 0
        for n in cfg[t]:
            if n["Id"] == model_id:
                notification = n
                break
            idx += 1
    if not notification:
        idx = -1

    return (notification, idx)

def get(session, bucket_arn, model_id):
    "Get a ResourceModel instance for this id or None if not found"

    # Get the full notification config on the bucket
    s3 = session.client("s3")
    cfg = s3.get_bucket_notification_configuration(bucket_arn)

    notification = find(cfg, model_id)
    if not notification:
        return None

    model = ResourceModel(Id=model_id, Events=None, Filters=None, 
                BucketArn=bucket_arn, TargetArn="", TargetType="")
    model.Id = model_id
    model.BucketArn = bucket_arn
    model.Events = notification["events"] 
    model.Filters = []
    if "Filter" in notification and "Key" in notification["Filter"]:
        if "FilterRules" in notification["Filter"]["Key"]:
            model.Filters = notification["Fillter"]["Key"]["FilterRules"]
    if "TopicArn" in notification:
        model.TargetArn = notification["TopicArn"]
        model.TargetType = "Topic"
    elif "QueueArn" in notification:
        model.TargetArn = notification["QueueArn"]
        model.TargetType = "Queue"
    elif "LambdaFunctionArn" in notification:
        model.TargetArn = notification["LambdaFunctionArn"]
        model.TargetType = "Function"
    else:
        raise Exception("Unable to set TargetArn")

    return model

def get_all(session, bucket_arn):
    "Get the complete notification configuration for the bucket"
    s3 = session.client("s3")
    cfg = s3.get_bucket_notification_configuration(bucket_arn)
    return cfg

def delete(session, bucket_arn, model_id):
    "Delete the notification on the bucket with the specified id"

    cfg = get_all(session, bucket_arn)
    if not cfg:
        raise Exception("Unable to get config for the bucket")
    notification, idx = find(cfg, model_id)
    if not notification:
        return

    if "TopicArn" in notification:
        del cfg["TopicConfigurations"][idx] 
    elif "QueueArn" in notification:
        del cfg["QueueConfigurations"][idx]
    elif "LambdaFunctionArn" in notification:
        del cfg["LambdaFunctionConfigurations"][idx]
    else:
        raise Exception("Unexpected notification missing Arn")

def get_role_name(target_name, notification_id):
    "Get the name of the role we create for S3 to notify the target"
    return target_name + "-bktntf-" + notification_id

def get_policy_name(role_name):
    "Get the policy name for the role we create"
    return role_name + "_policy"

def delete_role(session, role_name, policy_arn):
    "Delete the role we created for S3 to notifiy the target"

    iam = session.client("iam")

    try:
        if policy_arn:
            iam.delete_policy(PolicyArn=policy_arn)
        else:
            LOG.info("Unable to delete policy without policy_arn")
    except iam.exceptions.NoSuchEntityException:
        LOG.info("Tried to delete non-existent policy: %s", policy_arn)

    try:
        if role_name:
            iam.delete_role(RoleName=role_name)
        else:
            LOG.info("Unable to delete role without role_name")
    except iam.exceptions.NoSuchEntityException:
        LOG.info("Tried to delete non-existent role: %s", role_name)

def create_role(session, notification_id, target_type, target_arn, bucket_arn):
    "Create the role that S3 needs to notify the target"

    target_name = target_arn.split(":")[-1]
    iam = session.client("iam")
    sts = session.client("sts")
    account_id = sts.get_caller_identity()["Account"]

    action = ""
    if target_type == "Queue":
        action = "sqs:SendMessage"
    elif target_type == "Topic":
        action = "SNS:Publish"
    elif target_type == "Function":
        action = "lambda:InvokeFunction"
    else:
        raise Exception(f"Unexpected TargetType: {target_type}")

    # Role for the bucket to access the topic
    role_name = get_role_name(target_name, notification_id)

    # Assume role policy document for S3
    trust_policy = {
          "Id": role_name + "-TrustPolicyId",
          "Version": "2012-10-17",
          "Statement": [ {
                  "Effect": "Allow",
                  "Principal": { "Service": "s3.amazonaws.com" },
                  "Action": "sts:AssumeRole"
              }
          ]
      }

    # Check to see if the role is already there before creating.
    # This shouldn't happen unless something unexpected happened 
    # during an earlier attempt to create the resource.
    try:
        r = iam.get_role(RoleName=role_name)
        LOG.info("Role already existed: %s", role_name)
    except iam.exceptions.NoSuchEntityException:
        LOG.info("Creating %s", role_name)
        r = iam.create_role(
          RoleName=role_name,
          AssumeRolePolicyDocument=json.dumps(trust_policy))

    policy = {
        "Id": role_name + "-PolicyId",
        "Version": "2012-10-17",
        "Statement": [ {
            "Action": action,
            "Effect": "Allow",
            "Resource": target_arn,
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": bucket_arn
                },
                "StringEquals": {
                    "aws:SourceAccount": account_id
                }
            }
        } ]
    }

    policy_arn = None

    if target_type in ["Queue", "Topic"]:
        # For queues and topics we set the policy on the resource itself, 
        # rather than on the role.
        policy["Statement"][0]["Principal"] = { "Service": "s3.amazonaws.com" }
        if target_type == "Queue":
            sqs = session.client("sqs")
            queue_url = sqs.get_queue_url(QueueName=target_name)["QueueUrl"]
            sqs.set_queue_attributes(
                QueueUrl=queue_url,
                Attributes = {
                    "Policy": json.dumps(policy)
                }
            )
        else:
            sns = session.client("sns")
            sns.set_topic_attributes(
                TopicArn=target_arn,
                AttributeName="Policy",
                AttributeValue=json.dumps(policy)
            )
    else:
        # For lambda functions, we put the policy on the role
        policy_name = get_policy_name(role_name)
        policy_arn = f"arn:aws:iam::{account_id}:policy/{policy_name}"

        # Check to see if the policy exists before creating. As with the role, 
        # this should not happen, but we will assume it was the result of a prior
        # attempt to create the resource that went wrong somehow.
        try:
            r = iam.get_policy(PolicyArn=policy_arn)
            LOG.info("Policy already existed: %s", policy_arn)
        except iam.exceptions.NoSuchEntityException:
            LOG.info("Creating policy: %s", policy_name)
            r = iam.create_policy(
                PolicyName=policy_name,
                PolicyDocument=json.dumps(policy))
            policy_arn = r["Policy"]["Arn"]

    r = iam.get_role(RoleName=role_name)
    role_arn = r["Role"]["Arn"]
    LOG.info("Created role %s", role_arn)

    return role_name, policy_arn

def save(session, model):
    "Save a single notification configuration"

    # Get the current configuration for the bucket
    s3 = session.client("s3")
    cfg = s3.get_bucket_notification_configuration(model.bucketArn)
    put_config = {}
    put_config["Bucket"] = model.BucketArn
    put_config["NotificationConfiguration"] = cfg

    ntype = ""
    if model.TargetType == "Function":
        ntype = "LambdaFunctionConfigurations"
    elif model.TargetType == "Queue":
        ntype = "QueueConfigurations"
    elif model.TargetType == "Topic":
        ntype = "TopicConfigurations"
    else:
        raise Exception("Unexpected TargetType:" + model.TargetType)

    notification = find(cfg, model.Id)

    # If the notification is not present, create it 
    if not notification:
        notification = {}
        if ntype not in cfg:
            cfg[ntype] = {}
        cfg[ntype].append(notification)

    notification["Id"] = model.Id
    if model.TargetType == "Function":
        notification["LambdaFunctionArn"] = model.TargetArn
    elif model.TargetType == "Queue":
        notification["QueueArn"] = model.TargetArn
    else:
        notification["TopicArn"] = model.TargetArn
    notification["Events"] = model.Events
    notification["Filters"] = {}
    notification["Filters"]["Key"] = {}
    notification["Filters"]["Key"]["FilterRules"] = model.Filters

    # Create the role needed for S3 to notify the target
    create_role(session, model.Id, model.TargetType, model.TargetArn, model.BucketArn)

    # Re-create the entire notification configuration for the bucket 
    _ = s3.put_bucket_notification_configuration(**cfg)

