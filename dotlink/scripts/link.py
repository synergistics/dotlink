import os
import json
from lib.dotlinkgetters import get_dotlink_dir
from lib.pathmodifiers import to_generic_home_path, to_specific_path

def link(command_relevants):
    target = command_relevants["<target>"]
    link_name = to_specific_path(command_relevants["<link_name>"])

    symbolic = command_relevants["-s"] 

    dotlink_dir = get_dotlink_dir()
    target_path = os.path.join(dotlink_dir, target)

    with open(os.path.join(dotlink_dir, "dotlinks.json"), "r") as f:
        dotlinks = json.load(f) 

    dotlinks[to_generic_home_path(target_path)] = to_generic_home_path(link_name)

    with open(os.path.join(dotlink_dir, "dotlinks.json"), "w") as f:
        json.dump(dotlinks, f)

    if symbolic:
        try:
            os.symlink(os.path.expandvars(target_path), link_name)
        except Exception as e:
            print("dotlink: " , e)
    else:
        try:
            os.link(os.path.expandvars(target_path), link_name)
        except Exception as e:
            print("dotlink: ", e)

    
