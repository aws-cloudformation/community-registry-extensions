"Handler implementation for the hook"
import logging
from cfn_guard_rs_hook import GuardHook, types

from . import rules as Rules
from .models import TypeConfigurationModel

# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "AwsCommunity::S3::PublicAccessControlsRestricted"

hook = GuardHook(TYPE_NAME, TypeConfigurationModel, Rules, [
  types.Converter("PublicAccessBlockConfiguration.BlockPublicAcls", types.to_bool),
  types.Converter("PublicAccessBlockConfiguration.BlockPublicPolicy", types.to_bool),
  types.Converter("PublicAccessBlockConfiguration.IgnorePublicAcls", types.to_bool),
  types.Converter("PublicAccessBlockConfiguration.RestrictPublicBuckets", types.to_bool),
])
test_entrypoint = hook.test_entrypoint
