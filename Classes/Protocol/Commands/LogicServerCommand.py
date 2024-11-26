from Classes.Protocol.Commands.LogicCommand import LogicCommand

class LogicServerCommand(LogicCommand):
    def __init__(self, payload = b""):
        super().__init__(payload)
        self.payload = payload

    def encode(self, receiver):
        self.writeVInt(self.getCommandType())
        super().encode(receiver)
    
    def getCommandType(self):
        return super().getCommandType()