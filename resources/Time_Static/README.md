# AwsCommunity::Time::Static

Creates a static time based resource.

## Example

```yaml
Resources:
  CreationTime:
    Type: AwsCommunity::Time::Static
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      Tags:
      - Key: CreatedAt
        Value: !Ref CreationTime
Outputs:
  CreationDay:
    Value: !Sub "${CreationTime.Year}-${CreationTime.Month}-${CreationTime.Day}"
```

## Properties
None

## Attributes
The following properties you can use in a `GetAtt`

| Attribute  | Type | Description |
| ------------- | ------------- | ------------- |
| **Id**  | string  | UTC returns the time in UTC format.
| **Day**  | integer  | Day returns the day of the month.
| **Hour** | integer  | Hour returns the hour within the day, in the range [0, 23].
| **Minute** | integer  | Minute returns the minute offset within the hour, in the range [0, 59].
| **Month** | integer  | Month returns the month of the year.
| **Second** | integer  | Second returns the second offset within the minute, in the range [0, 59].
| **Unix** | integer  | Unix returns a Unix time, the number of seconds elapsed since January 1, 1970 UTC.
| **Year** | integer  | Year returns the year.

## Development

Open two tabs in your terminal.

Run SAM 
```sh
sam local start-lambda
```

In another tab, run cfn test:

```sh
cd resources/Time_Static
cfn test -- -k "contract_create_delete or contract_create_create or contract_create_read or contract_check_asserts_work"
```

## Notes

### SSM Parameter
To keep track of a resource that is a time we use a SSM parameter. We store a key in the SSM parameter store at `/CloudFormation/AwsCommunity/Time/Static/unique-identifier` to identify and keep track of the resource state.
