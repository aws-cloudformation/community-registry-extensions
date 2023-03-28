# AwsCommunity::EC2::SecurityGroupRestrictedSSH

Validates a resource of type `AWS::EC2::SecurityGroup` and ``AWS::EC2::SecurityGroupIngress` to validate no security group rules allow port 22 (SSH) to `0.0.0.0/0`.

This will hook will fail on:

```yaml
Resources:
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: "TestingSomeRules"
      SecurityGroupIngress:
        - IpProtocol: tcp
          ToPort: 22
          FromPort: 22
          CidrIp: 0.0.0.0/0
```

or

```yaml
Resources:
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
    GroupDescription: "TestingSomeRules"
  SecurityGroupIngress:
    Type: AWS::EC2::SecurityGroupIngress
    Properties:
      GroupId: !Ref SecurityGroup
      IpProtocol: tcp
      ToPort: 22
      FromPort: 22
      CidrIp: 0.0.0.0/0
```

It will pass on

```yaml
Resources:
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: "TestingSomeRules"
      SecurityGroupIngress:
        - IpProtocol: tcp
          ToPort: 443
          FromPort: 443
          CidrIp: 0.0.0.0/0
```

and

```yaml
Resources:
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
    GroupDescription: "TestingSomeRules"
  SecurityGroupIngress:
    Type: AWS::EC2::SecurityGroupIngress
    Properties:
      GroupId: !Ref SecurityGroup
      IpProtocol: tcp
      ToPort: 22
      FromPort: 22
      CidrIp: 10.0.0.0/16
```
