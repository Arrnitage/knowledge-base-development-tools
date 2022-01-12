from gui.utils.controls import *


def host(types):
    template = """
    {a_os_condition}
    {a_os}
    {a_privilege_condition}
    {a_privilege}
    """.format(a_os=select_os(types),
               a_os_condition=condition("os", types),
               a_privilege=privilege(types),
               a_privilege_condition=condition("privilege", types)
               )
    return template


def export():
    template = """
    {privilege}
    """.format(privilege=privilege("e"))
    return template


def procedure():
    template = """
    <h5> Windows </h5>
        {cmd}
        {wmic}
        {powershell}
    <h5> Linux </h5>
        {bash}
        {zsh}
    <h5> Tools </h5>
        {mimikatz}
        {cobaltstrike}
    """.format(cmd=input_box("cmd"),
               wmic=input_box("wmic"),
               powershell=input_box("powershell"),
               bash=input_box("bash"),
               zsh=input_box("zsh"),
               mimikatz=input_box("mimikatz"),
               cobaltstrike=input_box("cobaltstrike")
               )
    return template
