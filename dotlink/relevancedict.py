from dotlink.scripts.init import init
from dotlink.scripts.link import link
from dotlink.scripts.rmlink import rmlink
from dotlink.scripts.show import show 
from dotlink.scripts.migrate import migrate
from dotlink.scripts.mv import mv
from dotlink.scripts.sync import sync

relevance_dict = {
    "init": {
        "relevants_model": ("<path>", "--help"),
        "func": init,
        },

    "link": {
        "relevants_model": ("-s", "<target>", "<link_name>", "--help"),
        "func": link,
        },

    "rmlink": {
        "relevants_model": ("<link_name>", "--help"),
        "func": rmlink,
        },

    "show": {
        "relevants_model": ("--help"),
        "func": show,
        },
    "migrate": {
        "relevants_model": ("-s", "<src>", "<dest>", "--help"),
        "func": migrate,
        },

    "mv": {
        "relevants_model": ("--help"),
        "func": mv,
        },

    "sync": {
        "relevants_model": ("--help"),
        "func": sync,
        },
    }
