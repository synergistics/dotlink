import os
import json

def init(command_relevants):
    path = os.path.abspath(os.path.expandvars(command_relevants["<path>"] or "."))
    jsonPath = os.path.join(path, "dotlinks.json")
    dotlinkrc = os.path.join(os.environ["HOME"], ".dotlinkrc")

    os.makedirs(path, exist_ok=True)

    with open(jsonPath, "w") as f:
        json.dump({}, f)
    
    with open(dotlinkrc, "w") as f:
        f.write("dotlinkdir: " + path)
