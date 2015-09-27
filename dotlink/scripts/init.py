import os
import json
from lib.pathmodifiers import make_generic_home_path

def init(command_relevants):
    path = os.path.abspath(os.path.expandvars(command_relevants["<path>"] or "."))
    json_path = os.path.join(path, "dotlinks.json")
    dotlinkrc = os.path.join(os.environ["HOME"], ".dotlinkrc")

    os.makedirs(path, exist_ok=True)

    with open(json_path, "w") as f:
        json.dump({}, f)
    
    with open(dotlinkrc, "w") as f:
        f.write("dotlink_dir = " + make_generic_home_path(path))
