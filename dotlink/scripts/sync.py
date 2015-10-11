import os
import sys
import json
from dotlink.scripts.link import link
from dotlink.lib.dotlinkgetters import get_dotlink_dir
from dotlink.lib.pathmodifiers import to_generic_home_path, to_specific_path

def sync(command_relevants):
    dotlink_dir = get_dotlink_dir()
    with open(os.path.join(dotlink_dir, "dotlinks.json"), "r") as f:
        dotlinks = json.load(f)
    
    for k in dotlinks:
        options = {
                "<target>": k,
                "<link_name>": dotlinks[k]["link_name"],
                "-s": dotlinks[k]["symbolic"]
            }
        try:
            link(options)
        except Exception as e:
            print("dotlink:", e)
