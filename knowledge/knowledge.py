import pyhocon
from knowledge.items import Types, Host, Export, Procedure, Description


class Knowledge:
    def __init__(self):
        self.k_path = ""
        self.types = Types()
        self.imports = {
            "A": Host(),
            "B": Host(),
        }
        self.exports = Export()
        self.procedures = Procedure()
        self.description = Description()

    # TODO
    def set(self, msg: dict):
        pass

    # TODO
    def get(self):
        pass

    # TODO: export hocon file and marshal it
    def write(self, file_path: str):
        return file_path

    # TODO: read a hocon file and unmarshal it
    def read(self, file_path: str):
        k = pyhocon.ConfigFactory.parse_file(file_path)
        return k
