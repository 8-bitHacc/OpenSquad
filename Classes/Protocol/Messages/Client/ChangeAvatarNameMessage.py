from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage
from Classes.Protocol.Commands.Server.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand

class ChangeAvatarNameMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)
        self.name: str = ""

    def decode(self, receiver):
        self.name = self.readString()

    def execute(self, receiver):
        print(self.name)
        av = AvailableServerCommandMessage()
        l = LogicChangeAvatarNameCommand()
        l.setName(self.name)
        av.setCommand(l)
        receiver["ClientConnection"].messaging.send(receiver, av)

    def getMessageType(self):
        return 13971