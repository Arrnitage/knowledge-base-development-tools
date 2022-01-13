def help_msg():
    print("""
Usage: 
    python3 convert-cql.py <path>
    """)


def green_color(string):
    return "\033[92m" + string + "\033[0m"


def blue_color(string):
    return "\033[94m" + string + "\033[0m"


def str2list(string: str, list_class: list):
    for i in string.split("~"):
        list_class.append(i)
    return list_class
