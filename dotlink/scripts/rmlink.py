import os
import sys
import json
from lib.dotlinkgetters import get_dotlink_dir
from lib.pathmodifiers import to_generic_home_path, to_specific_path

def rmlink(command_relevants):
    link_name = to_specific_path(command_relevants["<link_name>"])

    dotlink_dir = get_dotlink_dir()

    with open(os.path.join(dotlink_dir, "dotlinks.json"), "r") as f:
        dotlinks = json.load(f) 
        new_dotlinks = dotlinks.copy()

    if os.path.lexists(link_name) and to_generic_home_path(link_name) in dotlinks.values():
        for x in dotlinks.items(): 
            if x[1] == to_generic_home_path(link_name):
                new_dotlinks.pop(x[0], None)

        os.remove(link_name)
    else:
        print("dotlink: Unable to remove link")

    with open(os.path.join(dotlink_dir, "dotlinks.json"), "w") as f:
        json.dump(new_dotlinks, f)

