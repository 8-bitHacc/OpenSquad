from Classes.Protocol.PiranhaMessage import PiranhaMessage

class SetAvatarNameResponseMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)

    def encode(self, receiver):
        self.writeBoolean(False)
        self.writeInt(0)
        self.writeString("Haccing")

    def getMessageType(self) -> int:
        return 28350