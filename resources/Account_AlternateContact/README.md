# AwsCommunity::Account::AlternateContact

## Design remarks
- We always require the account id (even though this is not required by the api) to make a few
  things easier to implement:
  - PrimaryIdentifier can always be Account + Contact type
  - List can work per-account if an Account Id is given (and return an error, all accounts if none
    is specified)
- Even so, the list handler is not implemented 
- The same api / resource can be used in the management and a member account, however the parameters
  can be slightly different, the resource abstracts that away, using the in-account way when the
  AccountId matches the account id of the CloudFormation Stack, and using the organizations way in
  all the other cases. 

## Testing remarks
When testing against the local account, nothing has to exist - but also there can't be a contact 
already defined

## Sample template
```yaml
Description: Create the Operations Alternate Contact for the current account
Resources:
  OperationsContact:
    Type: AwsCommunity::Account::AlternateContact
    Properties:
      AccountId: !Ref "AWS::AccountId"
      AlternateContactType: OPERATIONS
      EmailAddress: operations@example.com
      Name: Operations Distribution List
      PhoneNumber: +12065550000
      Title: Ops
```