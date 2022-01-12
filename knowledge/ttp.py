ttp_template = """
# offensive techniques

types {
{types}
}

imports {
    A {
{host_a}
    }
    B {
{host_b}
    }
}

exports {
{export}
}

procedures {
{procedure}
}

description {
    manual: \"\"\"
{manual}
    \"\"\"
}
""".format(types="types",
           host_a="host_a",
           host_b="host_b",
           export="export",
           procedure="procedure",
           manual="manual"
           )
