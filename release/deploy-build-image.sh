#!/bin/bash
set -eou pipefail

docker build -t cep-codebuild .
docker tag cep-codebuild:latest 531337079465.dkr.ecr.us-east-1.amazonaws.com/cep-cicd
docker push 531337079465.dkr.ecr.us-east-1.amazonaws.com/cep-cicd


