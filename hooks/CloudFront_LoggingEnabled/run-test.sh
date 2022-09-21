set -eou pipefail

pylint --rcfile ../../config/.pylintrc src/awscommunity_cloudfront_loggingenabled/*.py

pytest src

cfn validate && cfn generate && cfn submit --dry-run && cfn test

