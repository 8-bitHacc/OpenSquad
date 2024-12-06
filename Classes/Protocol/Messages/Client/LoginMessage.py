from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Protocol.Messages.Server.LoginOkMessage import LoginOkMessage
from Classes.Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage

class LoginMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)

    def execute(self, receiver):
        ok = LoginOkMessage()
        ohd = OwnHomeDataMessage()
        receiver["ClientConnection"].messaging.send(receiver, ok)
        receiver["ClientConnection"].messaging.send(receiver, ohd)

    def getMessageType(self):
        return 10101