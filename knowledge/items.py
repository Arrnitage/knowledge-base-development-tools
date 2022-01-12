from pyhocon import ConfigTree


class Types:
    def __init__(self):
        self.name = ""
        self.category = []
        self.effect_object = ""

    # TODO
    def set(self, options):
        pass

    # TODO
    def get(self, options):
        pass

    # TODO
    def to_string(self):
        pass


class Host:
    def __init__(self):
        self.os = ""
        self.privilege = ""

    # TODO
    def set(self, options):
        pass

    # TODO
    def get(self):
        pass

    # TODO
    def to_string(self):
        pass


class Export:
    def __init__(self):
        self.privilege = ""

    # TODO
    def set(self, options):
        pass

    # TODO
    def get(self):
        pass

    # TODO
    def to_string(self):
        pass


class Procedure:
    def __init__(self):
        self.cmd = []
        self.wmic = []
        self.powershell = []
        self.bash = []
        self.mimikatz = []
        self.cobaltstrike = []

    def set(self, options, commands: list):
        if options == "cmd":
            self.cmd = commands
        elif options == "wmic":
            self.wmic = commands
        elif options == "powershell":
            self.powershell = commands
        elif options == "bash":
            self.bash = commands
        elif options == "mimikatz":
            self.mimikatz = commands
        elif options == "cobaltstrike":
            self.cobaltstrike = commands

    def get(self, options):
        if options == "cmd":
            return self.cmd
        elif options == "wmic":
            return self.wmic
        elif options == "powershell":
            return self.powershell
        elif options == "bash":
            return self.bash
        elif options == "mimikatz":
            return self.mimikatz
        elif options == "cobaltstrike":
            return self.cobaltstrike

    # TODO
    def to_string(self):
        pass


class Description:
    def __init__(self):
        self.manual = ""

    def set(self, text):
        self.manual = text

    def get(self):
        return self.manual

    # TODO
    def to_string(self):
        pass
