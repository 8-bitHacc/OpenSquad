from Classes.Logic.Reflector.LogicRawOutReflector import LogicRawOutReflector
from Classes.Protocol.Commands.LogicServerCommand import LogicServerCommand

class LogicChangeAvatarNameCommand(LogicServerCommand):
    def __init__(self, payload=b''):
        super().__init__(payload)
        self.name: str = None

    def encode(self, receiver):
        refl: LogicRawOutReflector = super().encode(receiver)
        refl.reflectString(self.name, "name", None)
        refl.reflectInt(1, "changeState", 0)
        refl.reflectBool(True, "nameSetByUser")

    def getCommandType(self):
        return 1502

    def setName(self, n: str):
        self.name = n