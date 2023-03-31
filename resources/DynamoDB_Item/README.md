# AwsCommunity::DynamoDB::Item

Creates an item in a DynamoDB Table:

## Example

```yaml
Resources:
    Table:
        Type: AWS::DynamoDB::Table
    ...
    Item:
        Type: AwsCommunity::DynamoDB::Item
        Properties:
            TableName: !Ref Table
            Item:
                title:
                    S: Workshop 101
            Keys:
            - AttributeName: pk
              AttributeType: S
              AttributeValue: value
```

## Development

Open two tabs in your terminal.

Run SAM 
```sh
sam local start-lambda
```

In another tab, run cfn test:

```sh
cd resources/DynamoDB_Item
cfn test
```
