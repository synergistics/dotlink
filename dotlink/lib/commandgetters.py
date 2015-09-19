import re
from relevancedict import relevance_dict


def get_command(parsed_args):
    """Get a command from a dictionary of parsed arguments"""

    get_command_tuple = lambda x: re.match(r"^[a-zA-Z]", x[0]) and x[1] is True

    get_command_name = lambda x: x[0]

    command = list(map(get_command_name, filter(get_command_tuple, parsed_args.items())))[0]
    return command


def get_command_relevants(command, parsed_args):
    """Get the options and arguments relevant to a command"""

    relevants_model = relevance_dict[command]["relevants_model"]

    relevant = {k: v for k, v in list(filter(lambda x: x[0] in relevants_model, parsed_args.items()))}

    return relevant


