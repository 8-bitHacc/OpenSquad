from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Protocol.Messages.Server.KeepAliveServerMessage import KeepAliveServerMessage

class KeepAliveMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)

    def execute(self, receiver):
        keep = KeepAliveServerMessage()
        receiver["ClientConnection"].messaging.send(receiver, keep)
        #receiver["ClientConnection"].messaging.send(receiver, shut)

    def getMessageType(self):
        return 10108