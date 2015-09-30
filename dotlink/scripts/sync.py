import os
import sys
import json
from .link import link
from lib.dotlinkgetters import get_dotlink_dir
from lib.pathmodifiers import to_generic_home_path, to_specific_path

def sync(command_relevants):
    dotlink_dir = get_dotlink_dir()
    with open(os.path.join(dotlink_dir, "dotlinks.json"), "r") as f:
        dotlinks = json.load(f)
    
    for k in dotlinks:
        options = {
                "<target>": k,
                "<link_name>": dotlinks[k]["path"],
                "-s": dotlinks[k]["symbolic"]
            }
        link(options)
