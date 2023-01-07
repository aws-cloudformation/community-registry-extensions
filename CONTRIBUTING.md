# Contributing Guidelines

Thank you for your interest in contributing to our project. Whether it's a bug
report, new feature, correction, or additional documentation, we greatly value
feedback and contributions from our community.

Please read through this document before submitting any issues or pull requests
to ensure we have all the necessary information to effectively respond to your
bug report or contribution.


## Reporting Bugs/Feature Requests

We welcome you to use the GitHub issue tracker to report bugs or suggest features.

When filing an issue, please check existing open, or recently closed, issues to
make sure somebody else hasn't already reported the issue. Please try to
include as much information as you can. Details like these are incredibly
useful:

* A reproducible test case or series of steps
* The version of our code being used
* Any modifications you've made relevant to the bug
* Anything unusual about your environment or deployment


## Contributing via Pull Requests
Contributions via pull requests are much appreciated. Before sending us a pull request, please ensure that:

1. You are working against the latest source on the *main* branch.
2. You check existing open, and recently merged, pull requests to make sure someone else hasn't addressed the problem already.
3. You open an issue to discuss any significant work - we would hate for your time to be wasted.

To send us a pull request, please:

1. Fork the repository.
2. Modify the source; please focus on the specific change you are contributing. If you also reformat all the code, it will be hard for us to focus on your change.
3. Ensure local tests pass.
4. Commit to your fork using clear commit messages.
5. Send us a pull request, answering any default questions in the pull request interface.
6. Pay attention to any automated CI failures reported in the pull request, and stay involved in the conversation.

GitHub provides additional document on [forking a repository](https://help.github.com/articles/fork-a-repo/) and
[creating a pull request](https://help.github.com/articles/creating-a-pull-request/).


## Finding contributions to work on
Looking at the existing issues is a great way to find something to contribute on. As our projects, by default, use the default GitHub issue labels (enhancement/bug/duplicate/help wanted/invalid/question/wontfix), looking at any 'help wanted' issues is a great place to start.


## Code of Conduct
This project has adopted the [Amazon Open Source Code of Conduct](https://aws.github.io/code-of-conduct).
For more information see the [Code of Conduct FAQ](https://aws.github.io/code-of-conduct-faq) or contact
opensource-codeofconduct@amazon.com with any additional questions or comments.


## Security issue notifications
If you discover a potential security issue in this project we ask that you notify AWS/Amazon Security via our [vulnerability reporting page](http://aws.amazon.com/security/vulnerability-reporting/). Please do **not** create a public github issue.


## Licensing

See the [LICENSE](LICENSE) file for our project's licensing. We will ask you to confirm the licensing of your contribution.

## Development

Development for CloudFormation registry extensions can be done in one of
several languages. For modules, you can use either JSON or YAML. For resource
types (also known as providers), you can use Python, Java, Typescript, or Go.
Hooks can be developed in Java and Python. Full disclosure on language choice:
Java has the best support since it is the language used by AWS service teams.
We are working on improving support for the CLI and language plugin
repositories and we expect this situation to improve quickly.

### Guidelines for all languages

Please comment your code! Variable and function names don't always tell the
whole story. Assume you are explaining how your code works to a brand new
developer who has never done any registry extension development before.

Use an automatic formatter and a linter, with the settings we provide at the
top level of the repository, to keep things consistent. We don't want each
extension to be so unique that it takes an experienced contributer extra time
to adapt to the particular style of a single resource.

Create a `test/` folder at the top level of your project.  Create a template
file in that folder called `setup.yml` or `setup.json` that creates any
resources that must exist in your account prior to running contract tests. Edit
the JSON files in `example_inputs` to reference any outputs from the setup
stack. (See
https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test.html).
Rename the `example_inputs` folder to `inputs` and edit the JSON files to
reflect outputs from the setup stack. You can skip creation of `setup.yml` if your 
resource does not require any resources to be created beforehand. (One gotcha with the input files: Export variables can't have special characters in them)
if there are multiple inputs (e.g. `inputs_2_create.json`), you can reuse the same `setup.yml` or `setup.json`. Either reuse the created resources, or create more resources and a different output/export if they need to be independent. 

TODO: Can we change the init templates to just do this stuff by default?

Put a sample template into your `README.md` file to demonstrate usage. Also
create a template called `test/integ.yml` to be run by the release process to
validate your resource. It should contain all necessary setup and exercise the
full functionality of your resource, so that we can make sure there are no
breaking changes between releases.

### Unit tests and mocking

In order to submit a resource to the registry, you have to use the [AWS Serverless Application Model](https://aws.amazon.com/serverless/sam/) (SAM) to run an
exhaustive set of contract tests. SAM mocks an AWS Lambda function locally, but nothing else -
real SDK calls are made in your account, creating and deleting real resources.
There is not much point in also using an AWS API mocking library to duplicate
what `cfn test` covers. Reserve unit tests for testing discrete functions with
predictable outputs and no side effects.


### Python Development

- Formatting: [Black](https://github.com/psf/black)
- Linting: [Pylint](https://pylint.pycqa.org/en/latest/)
- Security checks: [Bandit](https://bandit.readthedocs.io/en/latest/)

Be careful with any changes you make to the basic project layout created by
`cfn init`. The registry backend makes some assumptions that can lead to
unexpected errors if you rearrange files or folders.

Ideally, `handlers.py` is a thin wrapper over a more generic module that you
write to actually do whatever work your resource does. In order to invoke this
module from a `__main__` function for faster local testing, place a file in
the `src` directory that imports it.

```
$ tree
.
├── my_resource_type
│   ├── __init__.py
│   ├── logic.py
│   ├── logic_integ.py
│   ├── handlers.py
│   ├── models.py
├── requirements.txt
└── run_logic_integ.py
```

In the above listing of the `src` directory, `logic.py` has your business
logic. It is imported by `handlers.py` and `logic_integ.py`, which is invoked
from `run_logic_integ.py`.

If you have unit tests that you wish to run with `pytest`, place them inline or
in the same folder with `handlers.py` with `test` in the filename, for example,
`logic_test.py`.

#### Python tips

Don't put any `.zip` files into your `src/my_resource_type` folder. The
registry backend will assume this is the desired entry point for your handlers.

Don't try to create a module by writing a `setup.py` file in `src` and `pip
install`ing it locally. Module imports need to have the style of `from .models
import ResourceModel` or they won't work when deployed.

In order to run SAM to test your resource, you have to first run `cfn submit
--dry-run` in order to create the `build/` folder that SAM relies on.

Create a Python environment and use Python v3.7 for resource type and hook development.

```sh
python3.7 -m venv .env
source .env/bin/activate
```

The top level `requirements.txt` only needs runtime dependencies for your
handler. For dev dependencies, such as `pylint` and
`cloudformation-cli-python-plugin`, freeze those into `src/requirements`, which
is ignored by registry publishing. TODO: Should we standardize this at the repo
level?

## Release Process

See [./RELEASE.md](RELEASE.md) for details on how our release process works.

