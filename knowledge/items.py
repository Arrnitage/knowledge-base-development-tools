from common.utils import str2list
from common.hocon import list_format, multiline_string_format


class Types:
    def __init__(self):
        self.name = ""
        self.category = []
        self.effect_object = ""

    def set(self, option: str, value: str):
        if option == "name":
            self.name = value
        elif option == "category":
            self.category = str2list(value, self.category)
        elif option == "effect_object":
            self.effect_object = value

    def get(self, option: str):
        if option == "name":
            return self.name
        elif option == "category":
            return self.category
        elif option == "effect_object":
            return self.effect_object

    def to_string(self, option: str):
        if option == "name":
            return self.name
        elif option == "category":
            return list_format(self.category)
        elif option == "effect_object":
            return self.effect_object


class Host:
    def __init__(self):
        self.os = ""
        self.privilege = ""

    def set(self, option: str, value: str):
        if option == "os":
            self.os = value
        elif option == "privilege":
            self.privilege = value

    def get(self, option: str):
        if option == "os":
            return self.os
        elif option == "privilege":
            return self.privilege

    def to_string(self, option: str):
        if option == "os":
            return self.os
        elif option == "privilege":
            return self.privilege


class Export:
    def __init__(self):
        self.privilege = ""

    def set(self, option: str, value: str):
        if option == "privilege":
            self.privilege = value

    def get(self, option: str):
        if option == "privilege":
            return self.privilege

    def to_string(self, option: str):
        if option == "privilege":
            return self.privilege


class Procedure:
    def __init__(self):
        self.cmd = []
        self.wmic = []
        self.powershell = []
        self.bash = []
        self.mimikatz = []
        self.cobaltstrike = []

    def set(self, option: str, value: str):
        if option == "cmd":
            self.cmd = str2list(value, self.cmd)
        elif option == "wmic":
            self.wmic = str2list(value, self.wmic)
        elif option == "powershell":
            self.powershell = str2list(value, self.powershell)
        elif option == "bash":
            self.bash = str2list(value, self.bash)
        elif option == "mimikatz":
            self.mimikatz = str2list(value, self.mimikatz)
        elif option == "cobaltstrike":
            self.cobaltstrike = str2list(value, self.cobaltstrike)

    def get(self, option: str):
        if option == "cmd":
            return self.cmd
        elif option == "wmic":
            return self.wmic
        elif option == "powershell":
            return self.powershell
        elif option == "bash":
            return self.bash
        elif option == "mimikatz":
            return self.mimikatz
        elif option == "cobaltstrike":
            return self.cobaltstrike

    def to_string(self, option: str):
        if option == "cmd":
            return list_format(self.cmd)
        elif option == "wmic":
            return list_format(self.wmic)
        elif option == "powershell":
            return list_format(self.powershell)
        elif option == "bash":
            return list_format(self.bash)
        elif option == "mimikatz":
            return list_format(self.mimikatz)
        elif option == "cobaltstrike":
            return list_format(self.cobaltstrike)


class Description:
    def __init__(self):
        self.manual = ""

    def set(self, text: str):
        self.manual = text

    def get(self):
        return self.manual

    def to_string(self):
        return multiline_string_format(self.manual)
