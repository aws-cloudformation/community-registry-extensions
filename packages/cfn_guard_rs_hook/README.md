# cfn_guard_rs_hook

Works with `cloudformation-cli-python-lib` to remove duplicate code when creating a CloudFormation registry hook that leverages the library `cfn_guard_rs`.

## Example
There is an [example](example/) hook available for you to reference how to implement this package.

## How to use
1. Create a Python CloudFormation hook using the [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/initiating-hooks-project-python.html)
1. Generate the model using `cfn generate`
1. Update the `handlers.py` with the following text. Update `TYPE_NAME` as appropriate.
```python
import logging
from cfn_guard_rs_hook import GuardHook

from . import rules as Rules
from .models import TypeConfigurationModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "Sample::S3::DefaultLockEnabled"

hook = GuardHook(TYPE_NAME, TypeConfigurationModel, Rules)
test_entrypoint = hook.test_entrypoint
```
4. Create a folder called `rules` in the `src/<hook_name>` folder
1. In the `rules` folder create an `__init__.py` file that is empty
1. In the `rules` folder create files representing the CloudFormation Guard rules you want to use

## How to use configuration with CloudFormation Guard rules
This library uses [Jinja](https://jinja.palletsprojects.com) to configure the CloudFormation Guard rules. This plugin will use the values
from the `typeConfiguration` section to plug into jinja template.

### Example
In the type json configuration file we have the following `typeConfiguration`
```json
"typeConfiguration": {
    "properties": {
        "DefaultLockEnabled": {
            "description": "Default Lock Enabled true/false",
            "default": "true",
            "type": "boolean"
        }
    },
    "additionalProperties": false
},
```
Then in our guard template we can use that parameter:
```
...
%s3_buckets_default_lock_enabled.Properties.ObjectLockEnabled == "{{ DefaultLockEnabled }}"
...
```
