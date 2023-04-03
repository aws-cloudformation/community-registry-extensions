#!/bin/bash
#
# Expected env vars:
#   ACM_CERTIFICATE_ARN
#   HOSTED_ZONE_ID
#   ALIAS
#
echo "ACM_CERTIFICATE_ARN is ${ACM_CERTIFICATE_ARN}"
echo "HOSTED_ZONE_ID is ${HOSTED_ZONE_ID}" 
echo "ALIAS is ${ALIAS}" 
cat test/integ-template.yml | sed "s#ALIAS#${ALIAS}#g" | sed "s#ACM_CERTIFICATE_ARN#${ACM_CERTIFICATE_ARN}#g" | sed "s/HOSTED_ZONE_ID/${HOSTED_ZONE_ID}/g" > test/integ.yml



