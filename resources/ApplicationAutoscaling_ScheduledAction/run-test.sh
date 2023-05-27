#!/bin/bash
set -eou pipefail

echo "Linting..."
pylint --rcfile ../../config/.pylintrc src/awscommunity_applicationautoscaling_scheduledaction/*.py

echo "Testing..."
pytest src

echo "Bandit..."
bandit -c ../../config/.banditrc -r src

echo "About to run cfn test..."
cfn validate && cfn generate && cfn submit --dry-run && cfn test -v


