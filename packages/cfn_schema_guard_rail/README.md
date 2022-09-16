# CloudFormation - Resource Schema Guard Rail

### Notes
This is not a stable version, it's still under development


### How to use it?
Schema guard rail package has built in library of rules, that CloudFormation thinks are the best practices that resource authors must follow.
In order to start using this package you need to install it first (section below). There are following commanda available:

#### Guard-Rail
```
guard-rail --schema file://path1 --schema file://path2 --rule file://path1 --rule file://path2
```

following command will execute CloudFormation schema compliance assessment over specified schemas and, additionally, will extend built in library of rules with provided custom rules


### How to install it locally?

Use following commands

#### Clone github repo
```
git clone git@github.com:ammokhov/resource-schema-guard-rail.git

```
#### Create Virtual Environment & Activate
```
python3 -m venv env
source env/bin/activate
```

#### Install Package Locally from the root

```
pip install -e . -r requirements.txt
pre-commit install
```

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This project is licensed under the Apache-2.0 License.
