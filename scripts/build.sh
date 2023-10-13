#!/usr/bin/env bash

# This script compiles, lints, and unit tests all extensions and utilities in the repo.
# It does not perform contract tests or integration tests.
# It is intended for local testing before you make a PR.
# The CICD process runs similar commands in CodeBuild buildspecs.

set -eou pipefail

echo "Building resources"

for dir in resources/*/
do
    dir=${dir%*/}    
    echo "Building $dir"

    # Get the name of the source folder
    ENTRY=$(python3.9 scripts/entry.py $dir/.rpdk-config)

    # Move into the resource directory
    pushd $dir

    # Create a short-lived python environment
    python3.9 -m venv .tmpenv
    . .tmpenv/bin/activate

    # Install dependencies
    pip install -r requirements.txt
    pip install -r requirements-dev.txt

    # Run the linter
    pylint --rcfile ../../config/.pylintrc src/$ENTRY/*.py
    
    # Run unit tests
    pytest src

    # Get rid of the Python environment
    deactivate
    rm -rf .tmpenv

    echo "Done building $dir"
    popd
    
done

