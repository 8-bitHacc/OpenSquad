from Classes.Protocol.Messages.Server.FriendListMessage import FriendListMessage
from Classes.Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage
from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Protocol.Messages.Server.LoginOkMessage import LoginOkMessage
from Classes.Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Classes.Utilities.Utility import Utility


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
        #if self.accountToken == "SquadBusters":
            #l = LoginFailedMessage()
            #l.setErrorCode(1)
            #l.setMessage("Please clear your App Data in order to play.")
            #receiver["ClientConnection"].messaging.send(receiver, l)
            #return

        #if self.accountToken == "": # New Account State
            #receiver["Player"].ID = receiver["ClientConnection"].db.incrementID()
            #receiver["Player"].AuthenticationToken = Utility.createRandomToken()

        #elif len(self.accountToken) == 40: # Has Account
            #entry = receiver["ClientConnection"].db.getEntry(self.accountToken)
            #if entry is not None:
                #receiver["Player"].AuthenticationToken = self.accountToken
                #receiver["ClientConnection"].player.loadInstance(entry)
            #else:
                #l = LoginFailedMessage()
                #l.setErrorCode(2)
                #l.setMessage("Wrong shard (Account not found) (2)")
                #receiver["ClientConnection"].messaging.send(receiver, l)

        print('hello')
        ok = LoginOkMessage()
        ohd = OwnHomeDataMessage()
        print('nice')
        receiver["ClientConnection"].messaging.send(receiver, ok)
        receiver["ClientConnection"].messaging.send(receiver, ohd)

    def getMessageType(self):
        return 10101