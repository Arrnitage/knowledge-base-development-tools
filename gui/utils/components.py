def input_box(kind, types=""):
    if types != "":
        names = types + '_' + kind
    else:
        names = kind
    template = """
    {kind}: <input type="text" name="{names}" class="input"/><br />
    """.format(kind=kind, names=names)
    return template


def select_os(types):
    names = types + '_os'
    template = """
    os: <select name="{names}">
        <option value="linux">Linux</option>
        <option value="windows">Windows</option>
    </select><br />
    """.format(names=names)
    return template


def select_privilege(types):
    names = types + '_privilege'
    template = """
    <select name="{names}">
        <option value="admin">Admin</option>
        <option value="user">User</option>
    </select><br />
    """.format(names=names)
    return template


def select_host(types):
    names = types + '_host'
    template = """
    <select name="{names}">
        <option value="sandbox">Sandbox</option>
        <option value="host">Host</option>
        <option value="domain">Domain</option>
    </select><br />
    """.format(names=names)
    return template


def condition(kind, types=""):
    if types != "":
        names = types + '_' + kind + '_condition'
    else:
        names = kind
    template = """
    <select name="{names}_condition">
        <option value="and">And</option>
        <option value="or">Or</option>
    </select>
    """.format(names=names)
    return template
