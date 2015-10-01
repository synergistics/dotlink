"""
# Developer Documentation: 'rmlink' command
Note: This is NOT user documentation

# Description
Removes a link already existing in dotlinks.json

# Walkthrough steps
1. Get name of link to be removed as link_name 
2. Make synthetic options dict to be used as the command_relevants for the link command 
3. Load dotlinks and make a copy to which the deletion will be made 
4. Remove the link on the filesystem if possible
5. Remove the link entry in the dotlinks copy 
6. Overwrite dotlinks.json with the modified dotlinks copy

"""
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
    

