from Classes.Protocol.PiranhaMessage import PiranhaMessage

class KeepAliveServerMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)

    def getMessageType(self):
        return 20108
