from Classes.Protocol.Messages.Server.FriendListMessage import FriendListMessage
from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Protocol.Messages.Server.LoginOkMessage import LoginOkMessage
from Classes.Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage

class LoginMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)
        self.accountID: list = [0, 0]
        self.accountToken: str = ""

    def decode(self, receiver: dict):
        self.accountID = self.readLong()
        self.accountToken = self.readString()
        self.readInt() # Major
        self.readInt() # Minor
        self.readInt() # Build
        self.readString()
        self.readString()
        self.readString()
        self.readString()
        self.readString()
        self.readLong()
        self.readString()
        self.readString()
        self.readString()
        self.readBoolean()

    def execute(self, receiver):
        ok = LoginOkMessage()
        ohd = OwnHomeDataMessage()
        fr = FriendListMessage()
        receiver["ClientConnection"].messaging.send(receiver, ok)
        receiver["ClientConnection"].messaging.send(receiver, ohd)
        receiver["ClientConnection"].messaging.send(receiver, fr)

    def getMessageType(self):
        return 10101