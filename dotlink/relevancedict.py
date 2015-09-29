from scripts.init import init
from scripts.link import link
from scripts.rmlink import rmlink
from scripts.show import show 
from scripts.migrate import migrate

relevance_dict = {
    "init": {
        "relevants_model": ("<path>"),
        "func": init
        },

    "link": {
        "relevants_model": ("-s", "<target>", "<link_name>"),
        "func": link
        },

    "rmlink": {
        "relevants_model": ("<link_name>"),
        "func": rmlink
        },

    "show": {
        "relevants_model": (),
        "func": show
        },
    "migrate": {
        "relevants_model": ("-s", "<src>", "<dest>"),
        "func": migrate 
        }
    }
