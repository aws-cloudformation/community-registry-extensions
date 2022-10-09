"This webhook handler responds to pushes from GitHub, to start the pipeline"
import json
import hashlib
import hmac
import os
import boto3


def handler(event, context): #pylint:disable=W0613
    "Lambda handler"
    print(json.dumps(event, default=str))
    secret_arn = os.environ["SECRET_ARN"]
    session = boto3.session.Session()
    client = boto3.client("secretsmanager")
    get_secret_value_response = client.get_secret_value(SecretId=secret_arn)
    secret = get_secret_value_response["SecretString"]
    digest = hmac.new(
        secret.encode("utf-8"), event["body"].encode("utf-8"), hashlib.sha1
    ).hexdigest()
    sig_parts = event["headers"]["X-Hub-Signature"].split("=", 1)
    if (
        len(sig_parts) < 2
        or sig_parts[0] != "sha1"
        or not hmac.compare_digest(sig_parts[1], digest)
    ):
        print("Digest comparison failed")
        raise Exception()
    print("Secret Ok")
    payload = json.loads(event["body"])
    print("payload", json.dumps(payload, default=str))
    codebuild = session.client("codebuild")
    commit_message = payload["head_commit"]["message"]
    print("commit_message:", commit_message)
    codebuild.start_build(
        projectName=os.environ["BUILD_PROJECT"],
        environmentVariablesOverride=[
            {
                "name": "COMMIT_MESSAGE",
                "value": commit_message,
                "type": "PLAINTEXT",
            }
        ],
    )
    return {
        "statusCode": 200,
        "headers": {},
        "body": payload["head_commit"]["message"],
    }
