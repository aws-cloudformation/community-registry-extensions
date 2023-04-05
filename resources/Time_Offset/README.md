# AwsCommunity::Time::Offset

Creates a time based resource with an offset.

## Example

```yaml
Resources:
   StarTime:
      Type: AwsCommunity::Time::Offset
      Properties:
         OffsetHours: 1
   EndTime:
      Type: AwsCommunity::Time::Offset
      Properties:
         OffsetYears: 5
   DailyNotice:
      Type: AWS::Pinpoint::Campaign
      Properties:
         ...
         Schedule:
            EndTime: !GetAtt EndTime.Utc
            Frequency: "DAILY"
            IsLocalTime: true
            StartTime: !GetAtt StartTime.Utc
            TimeZone: "UTC-07"
```

## Properties
| Properties  | Type | Description |
| ------------- | ------------- | ------------- |
| **Time**  | string  | Utc time to do the offset from. If none is provided now will be used.
| **OffsetYears**  | integer  | Number of years to offset the base timestamp.
| **OffsetMonths** | integer  | Number of months to offset the base timestamp.
| **OffsetDays** | integer  | Number of days to offset the base timestamp.
| **OffsetHours** | integer  | Number of hours to offset the base timestamp.
| **OffsetMinutes** | integer  | Number of minutes to offset the base timestamp.
| **OffsetSeconds** | integer  | Number of seconds to offset the base timestamp.

## Attributes
The following properties you can use in a `GetAtt`

| Attribute  | Type | Description |
| ------------- | ------------- | ------------- |
| **Id**  | string  | Unique ID that identifies the resource.
| **Day**  | integer  | Day returns the day of the month.
| **Hour** | integer  | Hour returns the hour within the day, in the range [0, 23].
| **Minute** | integer  | Minute returns the minute offset within the hour, in the range [0, 59].
| **Month** | integer  | Month returns the month of the year.
| **Second** | integer  | Second returns the second offset within the minute, in the range [0, 59].
| **Unix** | integer  | Unix returns a Unix time, the number of seconds elapsed since January 1, 1970 UTC.
| **Utc** | string  | The time represented in UTC time
| **Year** | integer  | Year returns the year.

## Development

Open two tabs in your terminal.

Run SAM 
```sh
sam local start-lambda
```

In another tab, run cfn test:

```sh
cd resources/Time_Offset
cfn test
```

## Notes

### SSM Parameter
Since this extension does not represent an actual resource, we have to create a Systems Manager Parameter Store entry to track its state for the purposes of satisfying the CloudFormation registry contract. We store a key in parameter store at `/CloudFormation/AwsCommunity/Time/Offset/unique-identifier`.
