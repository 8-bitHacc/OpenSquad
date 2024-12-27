from Classes.Logic.Reflector.LogicRawOutReflector import LogicRawOutReflector
from Classes.Protocol.Commands.LogicCommand import LogicCommand
from Classes.Utilities.Debugger import Debugger

class LogicServerCommand(LogicCommand):
    def __init__(self, payload = b""):
        super().__init__(payload)
        self.payload = payload

    def encode(self, receiver) -> LogicRawOutReflector:
        rawOut = LogicRawOutReflector(self)

        super().encode(receiver)
        rawOut.reflectInt(self.getCommandType(), "id", 0)
        if self.getCommandType() == -1:
            Debugger.error("LogicServerCommand::reflect() id is not set!")

        return rawOut
    
    def getCommandType(self) -> int:
        return -1