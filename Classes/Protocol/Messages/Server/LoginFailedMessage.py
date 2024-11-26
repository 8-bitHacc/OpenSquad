from Classes.Protocol.PiranhaMessage import PiranhaMessage

class LoginFailedMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)
    
    def encode(self, receiver):
        self.writeInt(1)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString("βαλια")
        self.writeInt(0)
        self.writeBoolean(False)
        self.writeBytes(b"", 0)
        self.writeInt(-1)

        self.writeInt(0)
        self.writeInt(2)
        self.writeString()
        self.writeInt(0)
        self.writeInt(0)
        self.writeBoolean(False)
    
    def getMessageType(self):
        return 20103