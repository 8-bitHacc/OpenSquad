from Classes.Protocol.Messages.Server.SetAvatarNameResponseMessage import SetAvatarNameResponseMessage
from Classes.Protocol.PiranhaMessage import PiranhaMessage

class ChangeAvatarNameMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)
        self.name: str = ""

    def decode(self, receiver):
        self.name = self.readString()

    def execute(self, receiver):
        receiver["Player"].name = self.name
        receiver["Player"].registrationState = 3
        receiver["ClientConnection"].db.createEntry(receiver["Player"].accountToken,
                                                      receiver["Player"].createDataEntry())
        av = SetAvatarNameResponseMessage()
        av.setAvatarName(self.name)
        receiver["ClientConnection"].messaging.send(receiver, av)

    def getMessageType(self):
        return 13971