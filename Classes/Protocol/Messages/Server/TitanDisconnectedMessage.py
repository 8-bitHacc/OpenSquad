from Classes.Protocol.PiranhaMessage import PiranhaMessage

class TitanDisconnectedMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)

    def encode(self, receiver):
        self.writeInt(1)

    def getMessageType(self):
        return 25892