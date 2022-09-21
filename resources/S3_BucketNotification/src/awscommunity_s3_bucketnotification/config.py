"""
This module contains functions to act on a single notification configuration, 
without changing any of the existing bucket configurations, unless the 
Id for the notification is found among existing notifications. This allows 
us to treat each indiidual notification as if it were an independent resource.

The `model` argument to these functions is from the auto-generated `models.ResourceModel`.
"""

import hashlib
import json
import logging
from .models import ResourceModel, KeyVal

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)

def find(cfg, model_id):
    """
    Find the notification in the full config by id
    Returns (notification, idx) or (None, -1)
    """

    notification = None

    if not model_id:
        return notification

    idx = 0

    # Iterate over the top level XConfigurations keys, e.g. TopicConfigurations
    for t in cfg:
        if t not in [
                "TopicConfigurations", 
                "QueueConfigurations", 
                "LambdaFunctionConfigurations"]:
            continue

        if notification:
            break
        idx = 0

        # Iterate over the array of notifications
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
    cfg = get_all(session, bucket_arn)

    (notification, _) = find(cfg, model_id)
    if not notification:
        return None

    model = ResourceModel(Id=model_id, Events=None, Filters=None, 
                BucketArn=bucket_arn, TargetArn="", TargetType="")
    model.Id = model_id
    model.BucketArn = bucket_arn
    model.Events = notification["Events"] 
    model.Filters = []
    if "Filter" in notification and "Key" in notification["Filter"]:
        if "FilterRules" in notification["Filter"]["Key"]:
            for f in notification["Filter"]["Key"]["FilterRules"]:
                kv = KeyVal(Name=f["Name"], Value=f["Value"])
                model.Filters.append(kv)
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
    bucket_name = bucket_arn.split(":")[-1]
    cfg = s3.get_bucket_notification_configuration(Bucket=bucket_name)
    if "ResponseMetadata" in cfg:
        del cfg["ResponseMetadata"]
    print("get_all:", json.dumps(cfg))
    return cfg

def delete(session, bucket_arn, model_id):
    "Delete the notification on the bucket with the specified id"

    cfg = get_all(session, bucket_arn)
    if not cfg:
        print("Found empty cfg when trying to delete", bucket_arn, model_id)
        # This shouldn't happen normally, but during testing it can be empty
        return False

    (notification, idx) = find(cfg, model_id)
    if not notification:
        print(f"Id {model_id} not found in notification config for {bucket_arn}")
        return False

    target_arn = None
    notification_id = notification["Id"]
    has_policy = False

    if "TopicArn" in notification:
        target_arn = notification["TopicArn"]
        del cfg["TopicConfigurations"][idx] 
    elif "QueueArn" in notification:
        target_arn = notification["QueueArn"]
        del cfg["QueueConfigurations"][idx]
    elif "LambdaFunctionArn" in notification:
        target_arn = notification["LambdaFunctionArn"]
        has_policy = True
        del cfg["LambdaFunctionConfigurations"][idx]
    else:
        raise Exception("Unexpected notification missing Arn")

    save_config(session, bucket_arn, cfg)

    # Delete the role we created to allow S3 to send the notifications
    target_name = target_arn.split(":")[-1]
    role_name = get_role_name(target_name, notification_id)
    policy_name = None
    if has_policy:
        policy_name = get_policy_name(role_name)
    delete_role(session, role_name, policy_name)

    return True

def get_role_name(target_name, notification_id):
    "Get the name of the role we create for S3 to notify the target"
    
    # Kept running into 64 character limit here
    longname = target_name + "-bn-" + notification_id
    return hashlib.md5(longname.encode("UTF8")).hexdigest()

def get_policy_name(role_name):
    "Get the policy name for the role we create"
    return role_name + "_p"

def delete_role(session, role_name, policy_arn):
    "Delete the role we created for S3 to notifiy the target"

    iam = session.client("iam")

    #TODO - Delete the Queue/Topic policy

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
            # TODO - What if the queue already had a Policy?
            sqs.set_queue_attributes(
                QueueUrl=queue_url,
                Attributes = {
                    "Policy": json.dumps(policy)
                }
            )
        else:
            sns = session.client("sns")
            # TODO - What if the topic already had a Policy?
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

def save_config(session, bucket_arn, cfg):
    "Save a configuration"

    s3 = session.client("s3")

    # This always fails if False. Not good, since we can't tell if we 
    # actually made a mistake in configuration. TODO
    skip_validation = True
    
    bucket_name = bucket_arn.split(":")[-1]

    # Re-create the entire notification configuration for the bucket 
    _ = s3.put_bucket_notification_configuration(Bucket=bucket_name, 
            NotificationConfiguration=cfg, 
            SkipDestinationValidation=skip_validation)

def save(session, model, is_create): #pylint:disable=too-many-branches
    "Save a single notification configuration"

    # Get the current configuration for the bucket
    cfg = get_all(session, model.BucketArn)
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

    (notification, _) = find(cfg, model.Id)

    # If the notification is not present, create it 
    if not notification:
        if not is_create:
            print(f"Tried to update a nonexistent notification {model.Id} " + 
                f"on bucket {model.BucketArn}")
            return False
        notification = {}
        if ntype not in cfg:
            cfg[ntype] = []
        cfg[ntype].append(notification)
    else:
        if is_create:
            print(f"Tried to create existing notification {model.Id} " + 
                f"on bucket {model.BucketArn}")
            return False

    notification["Id"] = model.Id
    if model.TargetType == "Function":
        notification["LambdaFunctionArn"] = model.TargetArn
    elif model.TargetType == "Queue":
        notification["QueueArn"] = model.TargetArn
    else:
        notification["TopicArn"] = model.TargetArn
    notification["Events"] = model.Events
    notification["Filter"] = {}
    notification["Filter"]["Key"] = {}
    notification["Filter"]["Key"]["FilterRules"] = []
    if model.Filters:
        for f in model.Filters:
            kv = {
                "Name": f.Name,
                "Value": f.Value
            }
            notification["Filter"]["Key"]["FilterRules"].append(kv)

    # Create the role needed for S3 to notify the target
    create_role(session, model.Id, model.TargetType, model.TargetArn, model.BucketArn)

    save_config(session, model.BucketArn, cfg)
    
    return True
