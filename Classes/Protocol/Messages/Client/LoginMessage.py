from Classes.Instances.PlayerInstance import PlayerInstance
from Classes.Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage
from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Protocol.Messages.Server.LoginOkMessage import LoginOkMessage
from Classes.Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Classes.Utilities.Utility import Utility


class LoginMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)
        self.accountID: list[int] = []
        self.accountToken: str = None

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
        receiver["ClientConnection"].player = PlayerInstance()
        receiver["Player"] = receiver["ClientConnection"].player

        if self.accountToken == "":
            entryID: list = self.incrementID(receiver["ClientConnection"].db.incrementID())
            receiver["ClientConnection"].db.currentID = entryID
            receiver["Player"].accountID = entryID
            receiver["Player"].accountToken = Utility.createRandomToken()
        else:
            receiver["Player"].accountID = self.accountID
            receiver["Player"].accountToken = self.accountToken
            entry = receiver["ClientConnection"].db.getEntry(self.accountToken)
            if entry is not None: receiver["Player"].loadInstance(entry)

        ok = LoginOkMessage()
        ohd = OwnHomeDataMessage()
        receiver["ClientConnection"].messaging.send(receiver, ok)
        receiver["ClientConnection"].messaging.send(receiver, ohd)

    def getMessageType(self):
        return 10101

    def incrementID(self, aID: list[int]) -> list[int]:
        aID[1] += 1
        if aID[1] % 100 == 0:
            aID[0] += 1

        return aID