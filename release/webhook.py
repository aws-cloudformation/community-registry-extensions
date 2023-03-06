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
    # TODO - assemble the expected value and compare against the untrusted value 
    # instead of parsing an untrusted value prior to comparing
    print("Secret Ok")
    payload = json.loads(event["body"])
    print("payload", json.dumps(payload, default=str))
    # "ref": "refs/heads/release",
    branch = payload["ref"].split("/")[2]

    # Figure out which repo this is and pass it in as an 
    # env variable to the build project, so it knows which
    # repo to clone and which pipeline to start, to accomodate
    # 3rd party extentions like Okta that have their own pipeline.

    repo = payload["repository"]["full_name"]
    print("repo is:", repo)

    # We have to hard code associations between repos and extension prefixes here
    # so we can re-use this webhook across all namespaces.
    extension_prefix = None
    repo1 = repo.split("/")[1]
    if repo1 == "community-registry-extensions":
        extension_prefix = "awscommunity"
    elif repo1 == "cloudformation-okta-resource-providers":
        extension_prefix = "okta"
    elif repo1 == "cloudformation-github-resource-providers":
        extension_prefix = "github"
    elif repo1 == "cloudformation-fastly-resource-providers":
        extension_prefix = "fastly"
    elif repo1 == "cloudformation-rollbar-resource-providers":
        extension_prefix = "rollbar"
    elif repo1 == "cloudformation-snowflake-resource-providers":
        extension_prefix = "snowflake"
    elif repo1 == "cloudformation-cloudflare-resource-providers":
        extension_prefix = "cloudflare"
    elif repo1 == "cloudformation-pagerduty-resource-providers":
        extension_prefix = "pagerduty"
    elif repo1 == "cloudformation-newrelic-resource-providers":
        extension_prefix = "newrelic"
    elif repo1 == "cloudformation-gitlab-resource-providers":
        extension_prefix = "gitlab"
    elif repo1 == "cloudformation-dynatrace-resource-providers":
        extension_prefix = "dynatrace"
    elif repo1 == "cloudformation-databricks-resource-providers":
        extension_prefix = "databricks"
    else:
        raise Exception("Unexpected repo: " + repo)

    giturl = f"https://github.com/{repo}.git"
    print("giturl is:", giturl)

    if branch == os.environ["GIT_BRANCH"]:
        print("Starting build for branch:", branch)
        codebuild = session.client("codebuild")

        # Get the commit message for S3 source metadata 
        raw_commit_message = payload["head_commit"]["message"]
        print("raw_commit_message:", raw_commit_message)

        # Take just the first line of a multi-line commit message
        commit_message = raw_commit_message.split("\n")[0]
        print("commit_message:", commit_message)

        codebuild.start_build(
            projectName=os.environ["BUILD_PROJECT"],
            environmentVariablesOverride=[
                {
                    "name": "COMMIT_MESSAGE",
                    "value": commit_message,
                    "type": "PLAINTEXT",
                },
                {
                    "name": "REPO",
                    "value": repo,
                    "type": "PLAINTEXT"
                },
                {
                    "name": "GIT_URL", 
                    "value": giturl, 
                    "type": "PLAINTEXT"
                },
                {
                    "name": "EXTENSION_PREFIX",
                    "value": extension_prefix,
                    "type": "PLAINTEXT"
                }
            ],
        )
    else:
        print("Not starting build for branch:", branch, " Looking for :" , os.environ['GIT_BRANCH'])
    return {
        "statusCode": 200,
        "headers": {},
        "body": payload["head_commit"]["message"],
    }
