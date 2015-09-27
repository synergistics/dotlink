import os
import json
from pprint import pprint
from lib.dotlinkgetters import get_dotlink_dir

def show(command_relevants):
    dotlink_dir = get_dotlink_dir()
    
    with open(os.path.join(dotlink_dir, "dotlinks.json"), "r") as f:
        dotlinks = json.load(f) 
    pprint(dotlinks)
