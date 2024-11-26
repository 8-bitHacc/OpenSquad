from Classes.Protocol.Commands.LogicServerCommand import LogicServerCommand

class LogicChangeAvatarNameCommand(LogicServerCommand):
    def __init__(self, payload=b''):
        super().__init__(payload)

    def encode(self, receiver):
        super().encode(receiver)

    def getCommandType(self):
        return 201
