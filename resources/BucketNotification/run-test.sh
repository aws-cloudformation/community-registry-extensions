set -eou pipefail

cd src
pylint awscommunity_s3_bucketnotification/*.py
cd ..
cfn validate && cfn generate && cfn submit --dry-run && cfn test

