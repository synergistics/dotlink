import os
import sys
import json
from dotlink.lib.dotlinkgetters import get_dotlink_dir
from dotlink.lib.pathmodifiers import to_generic_home_path, to_specific_path

def rmlink(command_relevants):
    """Remove the link of a file in the dotlink directory"""

    link_name = to_specific_path(command_relevants["<link_name>"])
    dotlink_dir = get_dotlink_dir()

    with open(os.path.join(dotlink_dir, "dotlinks.json"), "r") as f:
        dotlinks = json.load(f)
        new_dotlinks = dotlinks.copy()

    # Only remove the dotlink in dotlinks.json and the link file if possible, otherwise just remove the record
    if to_generic_home_path(link_name) in map(lambda x: x["link_name"], dotlinks.values()):
        if os.path.exists(link_name):
            try:
                os.remove(link_name)
            except OSError as e:
                print("dotlink:", e)
                print("dotlink: Proceeding to remove link in dotlinks.json")
        else:
            print("dotlink:", link_name, ": No such file or directory" 
                  "\nOnly removing link records in", os.path.join(dotlink_dir, "dotlinks.json"))

        for x in dotlinks.items():
            if x[1]["link_name"] == to_generic_home_path(link_name):
                new_dotlinks.pop(x[0], None)

        with open(os.path.join(dotlink_dir, "dotlinks.json"), "w") as f:
            json.dump(new_dotlinks, f)
    else:
        print("dotlink: Unable to remove link: Link not found in", 
              os.path.join(dotlink_dir, "dotlinks.json"), "under any targets")
    

