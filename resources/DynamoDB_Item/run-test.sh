set -eou pipefail

pylint --rcfile ../../config/.pylintrc src/awscommunity_dynamodb_item/*.py

pytest src

bandit -c ../../config/.banditrc -r src

cfn validate && cfn generate && cfn submit --dry-run && cfn test

