import string
from types import NoneType
from xmlrpc.client import boolean


def capitalize(name):
    """
    Capitalize each part of the name after separators
    Args:
        name (string): the name to capitalize
    """

    import re

    def capitalize_parts(s):
        return re.sub(
            r"([a-zA-Z])([a-zA-Z']*)",
            lambda m: m.group(1).upper() + m.group(2).lower(),
            s,
        )

    # Split on separators and capitalize each part
    separators = [" ", "-", "_", "'"]
    pattern = "|".join(map(re.escape, separators))
    parts = re.split(f"({pattern})", name)
    capitalized_parts = []
    for part in parts:
        if part not in separators:
            capitalized_parts.append(capitalize_parts(part))
        else:
            capitalized_parts.append(part)
    capitalized = "".join(capitalized_parts)
    return capitalized


def print_title(level, title):
    """
    Print a title with a specific level of indentation.
    Args:
        level (int): the level of indentation
        title (string): the title to print
    """
    separator = ""
    if level == 1:
        separator = "================================"
        print(f"\n\n{separator}")
        print(f" {title} ")
        print(f"{separator}\n")
    elif level == 2:
        separator = "--------------------------------"
        print(f"{separator}")
        print(f" {title} ")
        print(f"{separator}")
    else:
        separator = "----------"
        print(f"\n{separator} {title} {separator}")


def print_result(description, value, end_message: Exception | NoneType | str = None):
    """
    Print a result with a description and an optional error message.
    Args:
        description (string): the description of the result
        value (any): the value to print
        end_message (Exception | str | None, optional): Exception for error, message for success, or None/omitted if not relevant
    """
    if end_message is None:
        # If end_message is None, just print the value
        print(f"{description}: {value}")
    elif isinstance(end_message, Exception):
        # If end_message is an exception, print its type and error message
        print(f"{description}: {value} ==> 👎 {end_message}")
    else:
        # If end_message is a string, print it as a comment
        print(f"{description}: {value} ==> {end_message}")
