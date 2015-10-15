import os
import json
from dotlink.lib.pathmodifiers import to_generic_home_path, to_specific_path

def init(command_relevants):
    """Initialize a dotlink directory"""
    
    # Location of dotlink directory
    path = to_specific_path(command_relevants["<path>"] or ".")
    
    # Location of dotlinks.json
    json_path = os.path.join(path, "dotlinks.json")
    
    # Location of .dotlinkrc
    dotlinkrc = os.path.join(os.environ["HOME"], ".dotlinkrc")

    # If directory exists, nothing happens to it
    os.makedirs(path, exist_ok=True)

    # Don't want to overwrite file if it already has links
    if not os.path.exists(json_path):
        with open(json_path, "w") as f:
            json.dump({}, f)
    
    # Identify location of dotlink dir
    # Will have to change once more can be added to dotlinkrc
    with open(dotlinkrc, "w") as f:
        f.write("dotlink_dir = " + to_generic_home_path(path))
