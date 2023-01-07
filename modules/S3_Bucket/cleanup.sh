#!/bin/bash
# Remove the buckets
# They are set to retain in the module so they will be left after stack deletion
aws s3 rb s3://cep-integ-s3-bucket-module
aws s3 rb s3://cep-integ-log-s3-bucket-module
