# AwsCommunity::AppSync::BreakingChangeDetection

Validates that an AWS AppSync GraphQL schema update does not introduce a change that would break existing clients of the AWS AppSync GraphQL API. There are three categories of changes in a GraphQL schema:

- **Breaking**: These are changes that are backwards incompatible for existing API clients, such as changing the return type of an existing field or removing a field from the schema.
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

## Examples

- Original Template:

```
Resources:
  BasicGraphQLApi:
    Type: "AWS::AppSync::GraphQLApi"
    Properties:
      Name: BasicApi
      AuthenticationType: "AWS_IAM"
  
  BasicGraphQLSchema:
      Type: "AWS::AppSync::GraphQLSchema"
      Properties:
        ApiId: !GetAtt BasicGraphQLApi.ApiId
        Definition: |
         type Test {
           version: String!
           type: TestType
         }
         
         type Query {
           getTests: [Test]!
         }
         
         type Mutation {
           addTest(version: String!): Test
         }
         
         enum TestType {
            SIMPLE,
            COMPLEX
         }
```
###  Non-Breaking Change Example

- Adding the new field Test.name is not a breaking change.

```
Resources:
  BasicGraphQLApi:
    Type: "AWS::AppSync::GraphQLApi"
    Properties:
      Name: BasicApi
      AuthenticationType: "AWS_IAM"
  
  BasicGraphQLSchema:
      Type: "AWS::AppSync::GraphQLSchema"
      Properties:
        ApiId: !GetAtt BasicGraphQLApi.ApiId
        Definition: |
          type Test {
            version: String!
            type: TestType
            name: String
          }
          
          type Query {
            getTests: [Test]!
            getTest(version: String): Test
          }
          
          type Mutation {
            addTest(version: String!): Test
          }
          
          enum TestType {
             SIMPLE,
             COMPLEX
          }
```

###  Breaking Change Example

- Removing the Query.getTest field is a breaking change because clients will no longer be able to query it.
```
Resources:
  BasicGraphQLApi:
    Type: "AWS::AppSync::GraphQLApi"
    Properties:
      Name: BasicApi
      AuthenticationType: "AWS_IAM"
  
  BasicGraphQLSchema:
      Type: "AWS::AppSync::GraphQLSchema"
      Properties:
        ApiId: !GetAtt BasicGraphQLApi.ApiId
        Definition: |
          type Test {
            version: String!
            type: TestType
          }
          
          type Query {
            getTests: [Test]!
          }
          
          type Mutation {
            addTest(version: String!): Test
          }
          
          enum TestType {
             SIMPLE,
             COMPLEX
          }
```

### Dangerous Change Example

- Adding an Enum Value to an existing enum type is considered a "Dangerous" change as it may require changes to handling on the client. It will not break existing queries. 
```
Resources:
  BasicGraphQLApi:
    Type: "AWS::AppSync::GraphQLApi"
    Properties:
      Name: BasicApi
      AuthenticationType: "AWS_IAM"
  
  BasicGraphQLSchema:
      Type: "AWS::AppSync::GraphQLSchema"
      Properties:
        ApiId: !GetAtt BasicGraphQLApi.ApiId
        Definition: |
          type Test {
            version: String!
            type: TestType
            name: String
          }
          
          type Query {
            getTests: [Test]!
            getTest(version: String): Test
          }
          
          type Mutation {
            addTest(version: String!): Test
          }
          
          enum TestType {
             SIMPLE,
             COMPLEX
          }
```
