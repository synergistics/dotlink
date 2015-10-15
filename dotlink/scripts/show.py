import os
import json
from dotlink.lib.dotlinkgetters import get_dotlink_dir

def show(command_relevants):
    dotlink_dir = get_dotlink_dir()
    
    with open(os.path.join(dotlink_dir, "dotlinks.json"), "r") as f:
        dotlinks = json.load(f) 
    for x in list(dotlinks.items()):
        print("target:", x[0])
        print("link_name:", x[1]["link_name"])
        print("symbolic:", x[1]["symbolic"], "\n")
