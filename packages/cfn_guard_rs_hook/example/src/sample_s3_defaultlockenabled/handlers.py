import logging
from cfn_guard_rs_hook import GuardHook

from . import rules as Rules
from .models import TypeConfigurationModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "Sample::S3::DefaultLockEnabled"

hook = GuardHook(TYPE_NAME, TypeConfigurationModel, Rules)
test_entrypoint = hook.test_entrypoint
