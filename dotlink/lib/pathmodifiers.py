import re

def make_generic_home_path(path):
    return re.sub(r"\/home\/.+?(?=/)", "$HOME", path)
