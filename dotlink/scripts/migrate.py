import os
import sys
import json
import shutil
from dotlink.scripts.link import link
from dotlink.lib.dotlinkgetters import get_dotlink_dir
from dotlink.lib.pathmodifiers import to_generic_home_path, to_specific_path

def migrate(command_relevants):
    """Move a file not managed with dotlink to the dotlink directory"""

    dotlink_dir = get_dotlink_dir()

    # Path of file to be moved to dotlink directory
    src = to_specific_path(command_relevants["<src>"])

    # Will create error if dotlink_dir/dest does not exist by default
    dest = os.path.join(dotlink_dir, command_relevants["<dest>"] or os.path.basename(src))

    # Docopt like options passed to link command
    options = {
            "<target>": dest,
            "<link_name>": src,
            "-s": command_relevants["-s"]
        }

    with open(os.path.join(dotlink_dir, "dotlinks.json"), "r") as f:
        dotlinks = json.load(f)

    # If file is already a link under a target
    if to_generic_home_path(src) in map(lambda x: x["link_name"], dotlinks.values()):
        print("dotlink: File", src, "already linked with dotlink, cannot migrate")
        sys.exit()
    elif os.path.exists(src):
        shutil.move(src, dest)
        link(options)
    else:
        print("dotlink:" + src + ": No such file or directory")
        sys.exit()
