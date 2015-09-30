# dotlink.

# Usage:  
    dotlink init [\<path\>]
    dotlink link [-s] \<target\> <link_name>
    dotlink migrate [-s] \<src\> [<dest>] 
    dotlink rmlink \<link_name\>
    dotlink show 
    dotlink sync

# dotlinkrc
This file currently just keeps track of where dotlink was initialized

# Commands 

## init

### Description
Initializes dotlink directory. Issuing the command will create a dotlinks.json 
file in path or the current directory that keeps track of the files linked
using dotlink.

### Arguments
* [\<path\>]: The location of the dotlink directory.
Omission: dotlink will initialize in current directory.

## link

### Description
Links a file in the initialized dotlink directory to somewhere on the user's system.
The information for this link is stored in [dotlink directory]/dotlinks.json. As of 
now, do not rename this file.

### Arguments
* [-s]: Makes and records link as symbolic.
* \<target\>: The path of the file in the dotlink directory from which the link is made.
This path is assumed to be in the dotlink directory, so it should be written relative to 
its location.
* \<link_name\>: The path of the file to which the link is made on the user's system.

## migrate

### Description
Moves a file on the user's system that dotlink does NOT know about to the 
dotlink directory at the path [dotlink directory]/[dest name] or [dotlink directory]/[basename of src]
and then links this file back to src. 

### Arguments
* [-s]: Effectively the same as running link -s after moving the file, i.e. the link back 
to the old location is symbolic and is recorded accordingly.
* \<src\>: The location of the original file to be migrated
* [\<dest\>]: The location of the now moved file in the dotlink directory
Omission: See Description

## rmlink

### Description
Removes a link to the dotlink directory and its record in dotlinks.json. 
NOTE: Only removes the file to which the file in the dotlink directory links, not the actual file
in the dotlink directory. To remove the file in the dotlink directory, just do so as one would
normally delete a file. 

### Arguments
* \<link_name\>: The link to be removed

## show

### Description
Prints the contents of the dotlinks.json This option will be updated to include formatting options most likely.

### Arguments (To be added later)

## sync

### Description
Runs through all of the links recorded in dotlinks.json and attempts to make the appropriate links. 
If a file in dotlinks.json is not on the system, syncing will recreate the it with it's appropriate link. 

### Arguments (None currently)

### Example Scenario
Your dotlink directory is connected to a github repo and you clone the repo onto a different computer. Running
dotlink sync will recreate the link structure on the previous system. 

