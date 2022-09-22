# AwsCommunity::IAM::PasswordPolicy

This resource configures your AWS IAM password policy.

For more details see [the generated readme](docs/README.md)

## Example

```yaml
Resources:
   PasswordPolicy: 
      Type: AwsCommunity::IAM::PasswordPolicy
      Properties:
         AllowUsersToChangePassword: true
         HardExpiry: false
         MaxPasswordAge: 90
         MinimumPasswordLength: 12
         PasswordReusePrevention: 6
         RequireLowercaseCharacters: true
         RequireNumbers: true
         RequireSymbols: true
         RequireUppercaseCharacters: true
```

## Development

Open two tabs in your terminal.

Run SAM 
```sh
cd resources/IAM_PasswordPolicy
make build
sam local start-lambda
```

In another tab, run cfn test:

```sh
cd resources/IAM_PasswordPolicy
cfn test
```
