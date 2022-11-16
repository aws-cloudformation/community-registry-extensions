"""
Generate a third party cicd template based on a Prefix and a Resource name

For example

python3 gen_3p_template.py Oktank MyResource > ../release/oktank/cicd.yml

This is a one time operation. Additional resources will likely be added 
by hand after this.

"""

import sys
from jinja2 import Environment, FileSystemLoader, select_autoescape

def main(args):
    "Main"
    env = Environment(loader=FileSystemLoader("./"))
    template = env.get_template("cicd-3p-template.yml")
    print(template.render(Prefix=args[0], Resource=args[1]))

if __name__ == "__main__":
    main(sys.argv[1:])

