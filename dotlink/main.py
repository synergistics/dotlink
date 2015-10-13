#!/usr/bin/env python

"""
dotlink.

Usage:  
    dotlink init [<path>]
    dotlink link [-s] <target> <link_name>
    dotlink rmlink <link_name>
    dotlink migrate [-s] <src> [<dest>] 
    dotlink show 
    dotlink sync
    dotlink <command> --help

Commands:
    init : Initialize a dotlink directory
    link : Link a file in the dotlink directory to a location on the filesystem
    rmlink : Remove the link of a file in the dotlink directory
    migrate : Move a file not managed with dotlink to the dotlink 
    show : List the current dotlinks on the filesystem 
    sync : Synchronize the filesystem with links specified in dotlinks.json 

"""

import sys
import docopt
from dotlink.relevancedict import relevance_dict
from dotlink.lib.commandgetters import get_command, get_command_relevants
from dotlink.lib.gethelp import get_help

commands = relevance_dict.keys()

def main():
    if "--help" in sys.argv: 
        for x in sys.argv:
            if x in commands:
                print(get_help(x))
                sys.exit()

    arguments = docopt.docopt(__doc__)
    command = get_command(arguments)
    relevance_dict[command]["func"](get_command_relevants(command, arguments))

if __name__ == "__main__":
    main()
