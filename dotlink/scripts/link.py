import os
import sys
import json
from dotlink.lib.dotlinkgetters import get_dotlink_dir
from dotlink.lib.pathmodifiers import to_generic_home_path, to_specific_path

def link(command_relevants):
    """Link a file in the dotlink directory to a location on the filesystem""" 

    # File in dotlink dir
    target = command_relevants["<target>"]

    # File to link to
    link_name = to_specific_path(command_relevants["<link_name>"])

    symbolic = command_relevants["-s"] 

    dotlink_dir = get_dotlink_dir()
    target_path = os.path.join(dotlink_dir, target)

    with open(os.path.join(dotlink_dir, "dotlinks.json"), "r") as f:
        dotlinks = json.load(f) 

    # Set target path relative to dotlink dir (probably the basename) in dotlink dir
    dotlinks[os.path.relpath(target_path, start=dotlink_dir)] = {
            "link_name": to_generic_home_path(link_name), 
            "symbolic": symbolic
        }

    # Will not symlink if path does not exist (does not conform to ln commmand)
    if symbolic:
        if not os.path.exists(target_path):
            print("dotlink:", target_path, ": No such file or directory")
            print("dotlink: Cannot symlink to a file that does not exist")
            sys.exit()

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
    
