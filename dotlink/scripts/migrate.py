"""
# Developer Documentation: 'migrate' command
Note: This is NOT user documentation

# Description
Moves a file not currently known by dotlink to the dotlink directory and creates a
link/symlink to the original file's path

# Walkthrough steps
1. Get source and destination paths 
2. Make synthetic options dict to be used as the command_relevants for the link command 
3. Load dotlinks 
4. Check if the link about to be made already exists
5. Move the file in the user's filesystem to the dotlink directory
6. Run link command with the new file in the dotlink directory as the target and the
source file as the link_name as specified in the options dict

"""
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

    if to_generic_home_path(src) in map(lambda x: x["link_name"], dotlinks.values()):
        print("dotlink: File", src, "already linked with dotlink, cannot migrate")
        sys.exit()
    elif os.path.exists(src):
        shutil.move(src, dest)
        link(options)
    else:
        print("dotlink:" + src + ": No such file or directory")
        sys.exit()
