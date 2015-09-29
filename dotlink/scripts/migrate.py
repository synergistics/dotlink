import os
import sys
import json
import shutil
from .link import link
from lib.dotlinkgetters import get_dotlink_dir
from lib.pathmodifiers import to_generic_home_path, to_specific_path

def migrate(command_relevants):
    dotlink_dir = get_dotlink_dir()
    src = to_specific_path(command_relevants["<src>"])
    # Brittle, what if dest is /home/jking/dotletcetera ya know? Tell users not to do this or fix it.
    dest = os.path.join(dotlink_dir, command_relevants["<dest>"] or os.path.basename(src))

    options = {
            "<target>": dest,
            "<link_name>": src,
            "-s": command_relevants["-s"]
        }

    with open(os.path.join(dotlink_dir, "dotlinks.json"), "r") as f:
        dotlinks = json.load(f)

    if to_generic_home_path(src) in map(lambda x: x["path"], dotlinks.values()):
        print("dotlink: File", src, "already linked with dotlink, cannot migrate")
        sys.exit()
    elif os.path.exists(src):
        shutil.move(src, dest)
        link(options)
    else:
        print("dotlink: " + src + ": No such file or directory" 
              "\nCannot migrate ", src, "to", os.path.join(dotlink_dir, "dotlinks.json"))
        sys.exit()
