import os 

def get_help(command):
    command_docs_dir = os.path.join(os.path.normpath(os.path.join(os.path.dirname(__file__), "../")), "command_docs/")
    with open(os.path.join(command_docs_dir, command + ".txt"), "r") as f:
        return f.read()
