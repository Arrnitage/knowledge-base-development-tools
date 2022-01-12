from gui.utils.components import *


def privilege(types):
    template = """
    privilege: {privilege_component}
    """.format(privilege_component=select_privilege(types))
    return template
