# Hook development notes

## Prerequisites

Building and registering this hook requires:
  1. A version of the Java JDK of 8 or higher, such as [Amazon Corretto](https://aws.amazon.com/corretto).
  2. [Maven](https://maven.apache.org/)
  3. The [CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html)

## Tests

### Unit tests
Run unit tests with the following command
```
mvn clean verify
```

### Contract tests
This project also contains contract tests which are a requirement to [publish hooks for public use](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-publishing.html).

#### Prerequisites
1. Running contract tests requires the AWS SAM. See [Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html) for installation instructions.

2. Set up a retry configuration in your `~/.aws/config` global AWS configuration file. Add the `retry_mode` and `max_attempts` configurations to the profile you'll use for testing (in this case **\[default\]**):
```
[default]
retry_mode = standard
max_attempts = 15
```
For more information see [AWS CLI retries](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-retries.html)

3. Run the following commands to create a `~/.cfn-cli` directory and add the `typeConfiguration.json` file (see **Register the Hook** in the top level [README.md](../README.md) for more details on this file. 
```
mkdir ~/.cfn-cli/
cp typeConfiguration.json ~/.cfn-cli/typeConfiguration.json
```

#### Running the tests
1. Open a terminal, navigate to the project `/hooks` directory, and run the following command
```
sam local start-lambda
```

2. Open a second terminal, navigate to the project `/hooks` directory, and run the following command
```
cfn generate && mvn clean package && cfn test -v --enforce-timeout 90
```