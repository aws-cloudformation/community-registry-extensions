#!/bin/bash
#
# Deploy the build image to cicd, beta, and prod
# Run this from the release folder

./deploy-build-image.sh 531337079465 cep-cicd
./deploy-build-image.sh 676545906896 cep-beta
./deploy-build-image.sh 387586997764 cep-prod

