"This custom resource lambda is used from setup.yaml to register a sample Lambda"

from crhelper import CfnResource

helper = CfnResource()

@helper.create
@helper.update
def create_reg(event, _):
    "Create the registration entry in the table"
    print("create_reg called")

@helper.delete
def delete_reg(_, __):
    "Delete the registration entry from the table"
    print("delete_reg called")

def handler(event, context):
    "Handle the invocation from the CloudFormation custom resource"
    helper(event, context)

