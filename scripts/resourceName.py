"Gets the name of the folder with the handler code"

import json
import sys

def main(rpdk_path):
    "Get the source folder from rpdk config"

    with open(rpdk_path) as f:
        obj = json.load(f)
        entrypoint = obj["typeName"]
        print(entrypoint.replace("::", "_").lower())

if __name__ == "__main__":
    main(sys.argv[1])
