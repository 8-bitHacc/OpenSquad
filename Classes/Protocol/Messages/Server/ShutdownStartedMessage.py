from Classes.Protocol.PiranhaMessage import PiranhaMessage

class ShutdownStartedMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)
        self.time: int = 0

    def encode(self, receiver):
        self.writeInt(self.time)

    def getMessageType(self):
        return 28566

    def setTime(self, t: int):
        self.time = t