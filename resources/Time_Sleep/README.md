# AwsCommunity::Time::Sleep

Put a sleep into your CloudFormation templates.

## Example

```yaml
Resources:
   Instance:
      Type: AWS::EC2::Instance
      ...
   Sleep:
      Type: AwsCommunity::Time::Sleep
      Properties:
         Seconds: 10
         SleepOnCreate: true
         SleepOnUpdate: true
         SleepOnDelete: true
         AfterResources:
         # will sleep any time the instance ID changes
         - !Ref Instance
```

## Properties
The following properties you can use in a `GetAtt`

| Attribute  | Type | Description |
| ------------- | ------------- | ------------- |
| **Seconds**  | integer  | The number of seconds to sleep.
| **SleepOnCreate**  | boolean  | If you want to sleep on creation. (default=true)
| **SleepOnUpdate** | boolean  | If you want to sleep on update. (default=true)
| **SleepOnDelete** | boolean  | If you want to sleep on delete. (default=true)
| **AfterResources** | array of strings  | A list of strings that represent when we want to do a sleep on update

## Attributes
None

## Development

Open two tabs in your terminal.

Run SAM 
```sh
sam local start-lambda
```

In another tab, run cfn test:

```sh
cd resources/Time_Sleep
cfn test"
```

## Notes

### SSM Parameter
To keep track of a resource that is a time we use a SSM parameter. We store a key in the SSM parameter store at `/CloudFormation/AwsCommunity/Time/Sleep/unique-identifier` to identify and keep track of the resource state.
