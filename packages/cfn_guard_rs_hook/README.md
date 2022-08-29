# cfn_guard_rs_hook

Works with `cloudformation-cli-python-lib` to remove duplicate code when creating a CloudFormation registry hook that leverages the library `cfn_guard_rs`.

# How to use
1. Create a Python CloudFormation hook using the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/initiating-hooks-project-python.html)
2. Generate the model using `cfn generate`
3. Update the `handlers.py` with the following text. Update `TYPE_NAME` as appropriate.
```
import logging
from cfn_guard_rs_hook import GuardHook

from . import rules as Rules
from .models import TypeConfigurationModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "Community::S3Bucket::Encryption"

hook = GuardHook(TYPE_NAME, TypeConfigurationModel, Rules)
test_entrypoint = hook.test_entrypoint
```
