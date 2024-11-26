from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage

class GoHomeMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)

    def execute(self, receiver):
        keep = OwnHomeDataMessage()
        receiver["ClientConnection"].messaging.send(receiver, keep)

    def getMessageType(self):
        return 13493