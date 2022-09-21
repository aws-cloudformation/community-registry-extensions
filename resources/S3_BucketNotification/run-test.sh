set -eou pipefail

pylint --rcfile ../../config/.pylintrc src/awscommunity_s3_bucketnotification/*.py

pytest src

cfn validate && cfn generate && cfn submit --dry-run && cfn test

