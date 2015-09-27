import re
import os

def to_generic_home_path(path):
    return re.sub(r"\/home\/.+?(?=/)", "$HOME", path)

def to_specific_path(path):
    return os.path.abspath(os.path.expandvars(path))
