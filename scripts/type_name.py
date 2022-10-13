"Gets the name of the type from the rpdk config"

import json
import sys

def main(rpdk_path):
    "Get the type name from rpdk config"

    with open(rpdk_path) as f:
        obj = json.load(f)
        print(obj["typeName"])

if __name__ == "__main__":
    main(sys.argv[1])
