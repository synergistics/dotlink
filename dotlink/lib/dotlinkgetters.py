import os
import re
import sys
from dotlink.lib.pathmodifiers import to_specific_path

def get_dotlinkrc():
    return os.path.join(os.environ.get("HOME"), ".dotlinkrc")

def get_dotlink_dir():
    dotlinkrc = get_dotlinkrc()

    if not os.path.exists(dotlinkrc):
        print("dotlink: Cannot find dotfiles directory because $HOME/.dotlinkrc does not exist")
        sys.exit()

    with open(dotlinkrc, "r") as f:
        r = re.compile(r"^dotlink_dir(\s)?=(\s)?(?P<dir>.+)")

        for line in f:
            if r.match(line):
               dotlink_dir = to_specific_path(r.match(line).group("dir"))
    return dotlink_dir
