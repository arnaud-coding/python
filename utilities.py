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
        separator = "======================="
    elif level == 2:
        separator = "-----------"
    print(f"{separator}")
    print(f" {title} ")
    print(f"{separator}")
