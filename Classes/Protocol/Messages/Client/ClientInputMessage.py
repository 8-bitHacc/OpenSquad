from Classes.Protocol.PiranhaMessage import PiranhaMessage

class ClientInputMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)

    def decode(self, receiver):
        print(self.readInt())
        print(self.readInt())
        print(self.readVInt())

    def getMessageType(self):
        return 18856