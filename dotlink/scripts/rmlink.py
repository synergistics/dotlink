import os
import sys
import json
from lib.dotlinkgetters import get_dotlink_dir
from lib.pathmodifiers import to_generic_home_path, to_specific_path

def rmlink(command_relevants, know_in_dotlinks=False):
    link_name = to_specific_path(command_relevants["<link_name>"])

    dotlink_dir = get_dotlink_dir()

    with open(os.path.join(dotlink_dir, "dotlinks.json"), "r") as f:
        dotlinks = json.load(f)
        new_dotlinks = dotlinks.copy()

    if know_in_dotlinks or to_generic_home_path(link_name) in map(lambda x: x["path"], dotlinks.values()):
        if os.path.exists(link_name):
            os.remove(link_name)
        else:
            print("dotlink: " + link_name + ": No such file or directory" 
                  "\nOnly removing link records in ", os.path.join(dotlink_dir, "dotlinks.json"))

        for x in dotlinks.items():
            if x[1]["path"] == to_generic_home_path(link_name):
                new_dotlinks.pop(x[0], None)

        with open(os.path.join(dotlink_dir, "dotlinks.json"), "w") as f:
            json.dump(new_dotlinks, f)
    else:
        print("dotlink: Unable to remove link: Link not found in ", os.path.join(dotlink_dir, "dotlinks.json"))

