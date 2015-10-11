"""
# Developer Documentation: 'link' command
Note: This is NOT user documentation

# Description
Links or symlinks a file in the dotlink directory to another file in the user's
filesystem. 

# Walkthrough steps
1. Get target path, link_name, and -s switch variables
2. Open dotlinks.json to be used as dict object
3. Add key to dotlinks dict for the relative path of 'target' in the dotlink directory
4. Set the value of said key to a dict containing path (string) and symbolic (boolean)
keys
..- Path is set to the generic home path of the link_name
5. Attempt link or symlink (corresonding to the symbolic boolean) and write dotlinks
back to dotlinks.json if successful

"""
import os
import sys
import json
from dotlink.lib.dotlinkgetters import get_dotlink_dir
from dotlink.lib.pathmodifiers import to_generic_home_path, to_specific_path

def link(command_relevants):
    target = command_relevants["<target>"]
    link_name = to_specific_path(command_relevants["<link_name>"])

    symbolic = command_relevants["-s"] 

    dotlink_dir = get_dotlink_dir()
    target_path = os.path.join(dotlink_dir, target)

    with open(os.path.join(dotlink_dir, "dotlinks.json"), "r") as f:
        dotlinks = json.load(f) 

    dotlinks[os.path.relpath(target_path, start=dotlink_dir)] = {
            "link_name": to_generic_home_path(link_name), 
            "symbolic": symbolic
        }


    if symbolic:
        try:
            os.symlink(os.path.expandvars(target_path), link_name)
        except OSError as e:
            print("dotlink:", e)
            print("dotlink: Symlink not created")
        else:
            with open(os.path.join(dotlink_dir, "dotlinks.json"), "w") as f:
                json.dump(dotlinks, f)
    else:
        try:
            os.link(os.path.expandvars(target_path), link_name)
        except OSError as e:
            print("dotlink:", e)
            print("dotlink: Link not created")
        else:
            with open(os.path.join(dotlink_dir, "dotlinks.json"), "w") as f:
                json.dump(dotlinks, f)
    
