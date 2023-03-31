#!/bin/bash
#
# Deploy the build image to cicd, beta, and prod
# Run this from the release folder

./deploy-build-image.sh 531337079465 cep-alpha us-east-1
./deploy-build-image.sh 676545906896 cep-beta us-east-1
./deploy-build-image.sh 387586997764 cep-prod us-east-1

