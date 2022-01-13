# TODO list to hocon format
def list_format(list_class: list):
    template = """[
    
    """
    return template


# TODO multiline string to hocon format
def multiline_string_format(multiline_string_class: str):
    strs = multiline_string_class.split("\n")
    template = """
    {0}
    """.format(strs)
    return template
