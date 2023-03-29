#!/bin/bash
#
# Expected env vars:
#   ACM_CERTIFICATE_ARN
#   HOSTED_ZONE_ID
#
echo "ACM_CERTIFICATE_ARN is ${ACM_CERTIFICATE_ARN}"
echo "HOSTED_ZONE_ID is ${HOSTED_ZONE_ID}" 
cat test/integ-template.yml | sed "s#ACM_CERTIFICATE_ARN#${ACM_CERTIFICATE_ARN}#g" | sed "s/HOSTED_ZONE_ID/${HOSTED_ZONE_ID}/g" > test/integ.yml



