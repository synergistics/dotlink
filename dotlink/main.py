#!/usr/bin/env python

"""
dotlink.

Usage:  
    dotlink init [<path>]
    dotlink link [-s] <target> <link_name>...
    dotlink rmlink <link_name>... 
    dotlink migrate <target> <link_name> 

Arguments: 
    path         path to dotfile directory
    target       the file you want to link from
    link_name    the file and path you want to link to

Options:
    -s      symbolic

"""

import docopt
from relevancedict import relevance_dict
from lib.commandgetters import get_command, get_command_relevants

if __name__ == "__main__":
    arguments = docopt.docopt(__doc__)

    command = get_command(arguments)

    relevance_dict[command]["func"](get_command_relevants(command, arguments))


