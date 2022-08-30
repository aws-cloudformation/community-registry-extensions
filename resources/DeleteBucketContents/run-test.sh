set -eou pipefail

cd src
pylint awscommunity_s3_deletebucketcontents/*.py
cd ..
cfn validate && cfn generate && cfn submit --dry-run && cfn test

