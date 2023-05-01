"This custom resource lambda is used from setup.yaml to register a sample Lambda"

from crhelper import CfnResource

helper = CfnResource()

@helper.create
@helper.update
def create_reg(event, _):
    "Create the registration entry in the table"
    pass #TODO

@helper.delete
def delete_reg(_, __):
    "Delete the registration entry from the table"
    pass

def handler(event, context):
    "Handle the invocation from the CloudFormation custom resource"
    helper(event, context)

