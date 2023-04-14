#!/bin/bash

set -eou pipefail

mvn clean verify javadoc:javadoc && cfn test -v --enforce-timeout 90
