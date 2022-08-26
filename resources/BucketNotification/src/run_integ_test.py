"Run manual integration tests"

import argparse
import sys
from awscommunity_s3_bucketnotification import config_integ

def main():
    "Main"
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile', help='Use a specific AWS config profile')
    args = parser.parse_args()
    if not args.profile:
        sys.exit("--profile is required")
    config_integ.main(args.profile)

if __name__ == "__main__":
    main()
