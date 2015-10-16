dotlink.

Description: 
  dotlink is a lightweight dotfile manager based on hard and symbolic
  links. dotlink allows one to keep all configuration files in one location to
  which links are made to other locations in the file system. There are three
  locations in the file system associated with dotlink:

  1. The dotlink directory
    This is the directory at which a user's configuration files are placed
  2. The dotlinkrc
    Currently, this file denotes the location of the dotlink directory. It is
    likely to be used for more things as dotlink expands
  3. The dotlinks.json file
    This file is inside the dotlink directory. It keeps track of all the links
    made to files in the files system made with dotlink such that every time a
    new link is made, it is recorded. The file is used for synchronizing the
    filesystem with the "image" of the links in the filesystem described in
    dotlinks.json. In this way, for example, dotfiles stored in a git repository
    can be cloned to another computer using dotlink and the same links made on
    the original computer can be recreated on the new.

Usage: 
  dotlink init [<path>] dotlink link [-s] <target> <link_name> 
  dotlink rmlink <link_name> dotlink migrate [-s] <src> [<dest>] 
  dotlink show 
  dotlink sync
  dotlink <command> --help

Commands: 
  init : Initialize a dotlink directory 
  link : Link a file in the dotlink directory to a location on the filesystem 
  rmlink : Remove the link of a file in the dotlink directory 
  migrate : Move a file not managed with dotlink to
the dotlink directory
  show : List the current dotlinks on the filesystem 
  sync : Synchronize the filesystem with links specified in dotlinks.json 

 
