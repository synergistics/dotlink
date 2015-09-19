from scripts.init import init
# from scripts.link import link
# from scripts.rmlink import rmlink
# from scripts.migrate import migrate

relevance_dict = {
    "init": {
        "relevants_model": ("<path>"),
        "func": init
     },

    "link": {
        "relevants_model": ("-s", "<target>", "<link_name>"),
        "func": None
    },

    "rmlink": {
        "relevants_model": None
    }
}

