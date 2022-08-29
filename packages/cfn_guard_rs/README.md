# cfn_guard_rs

Converts [CloudFormation Guard](https://github.com/aws-cloudformation/cloudformation-guard) into a Python library that can be used in your Python packages

# How to use
1. Include `cfn_guard_rs` in your project
1. Use `run_checks` function to run guard with `rules` (str) against resource `data` (dict)
1. Use the output (`DataOutput`) to parse the results and see if the data is compliant or not
