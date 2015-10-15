"""
# Developer Documentation: 'init' command
Note: This is NOT user documentation

# Description
Initializes a dotlink directory

# Walkthrough steps
1. Get path variable
2. Make directory at path 
3. Create dotlinks.json in directory with an empty dictionary to start 
4. Create $HOME/.dotlinkrc and write to file the location of the dotlink directory
just created

"""
import os
import json
from dotlink.lib.pathmodifiers import to_generic_home_path, to_specific_path

def init(command_relevants):
    path = to_specific_path(command_relevants["<path>"] or ".")
    json_path = os.path.join(path, "dotlinks.json")
    dotlinkrc = os.path.join(os.environ["HOME"], ".dotlinkrc")

    # If directory exists, nothing happens to it
    os.makedirs(path, exist_ok=True)

    # Don't want to overwrite file if it already has links
    if not os.path.exists(json_path):
        with open(json_path, "w") as f:
            json.dump({}, f)
    
    # Will have to change once more can be added to dotlinkrc
    with open(dotlinkrc, "w") as f:
        f.write("dotlink_dir = " + to_generic_home_path(path))
