set -eou pipefail

pylint --rcfile ../../config/.pylintrc src/awscommunity_s3_deletebucketcontents/*.py

pytest src

bandit -c ../../config/.banditrc -r src

cfn validate && cfn generate && cfn submit --dry-run && cfn test

