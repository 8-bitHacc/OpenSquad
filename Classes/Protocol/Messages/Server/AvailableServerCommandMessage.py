from Classes.Protocol.Commands.LogicServerCommand import LogicServerCommand
from Classes.Protocol.PiranhaMessage import PiranhaMessage

class AvailableServerCommandMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)
        self.command: LogicServerCommand = None

    def encode(self, receiver):
        self.writeVInt(self.command.getCommandType())

        self.command.encode(receiver)
        self.payload += self.command.payload

    def getMessageType(self) -> int:
        return 27968

    def setCommand(self, cmd: LogicServerCommand):
        self.command = cmd