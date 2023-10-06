# AwsCommunity::AppSync::BreakingChangeDetection

Validates that an AWS AppSync GraphQL schema update does not introduce a change that would break existing clients of the AWS AppSync GraphQL API. There are three categories of changes in a GraphQL schema:

- **Breaking**: These are changes that are not backwards incompatible for existing API clients, such as changing the return type of an existing field or removing a field from the schema.
- **Dangerous**: These are changes that may be dangerous for existing API clients but are not necessarily breaking, such as adding a new value in an Enum or changing the default value on an argument.
- **Non-breaking**: These are changes that are backwards compatible for existing clients, such as adding a new field or type to the schema.

By default, the hook will fail when an AppSync schema update introduces a change that is in the "Breaking" category. 

## Configuration

```bash
# Create a basic type configuration json
cat <<EOF > typeConfiguration.json
{
  "CloudFormationConfiguration": {
    "HookConfiguration": {
      "TargetStacks": "ALL",
      "FailureMode": "FAIL",
      "Properties": {}
    }
  }
}
EOF

# enable the hook
aws cloudformation set-type-configuration \
  --configuration file://typeConfiguration.json \
  --type HOOK \
  --type-name AwsCommunity::AppSync::BreakingChangeDetection
```

## Original Template Example

## 

