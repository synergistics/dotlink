import os
import json
from lib.dotlinkgetters import get_dotlink_dir
from lib.pathmodifiers import make_generic_home_path

def link(command_relevants):
    target = make_generic_home_path(os.path.abspath(os.path.expandvars(command_relevants["<target>"])))
    link_name = os.path.expandvars(command_relevants["<link_name>"])
    symbolic = command_relevants["-s"] 

    dotlink_dir = get_dotlink_dir()
    link_path = os.path.join(dotlink_dir, link_name)

    with open(os.path.join(dotlink_dir, "dotlinks.json"), "r") as f:
        dotlinks = json.load(f) 

    dotlinks[target] = make_generic_home_path(link_path)

    with open(os.path.join(dotlink_dir, "dotlinks.json"), "w") as f:
        json.dump(dotlinks, f)

    if symbolic:
        try:
            os.symlink(os.path.expandvars(target), link_path)
        except Exception as e:
            print("dotlink: " + e)
    else:
        os.link(os.path.expandvars(target), link_path)


