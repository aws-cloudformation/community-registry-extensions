#!/bin/bash
#
# Run from the resource directory

../../release/deregister-all.sh us-east-1
../../release/publish.sh us-east-1
../../release/deregister-all.sh us-west-2
../../release/publish.sh us-west-2

