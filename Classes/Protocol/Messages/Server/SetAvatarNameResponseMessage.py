from Classes.Protocol.PiranhaMessage import PiranhaMessage

class SetAvatarNameResponseMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)
        self.avatarName: str = None

    def encode(self, receiver):
        self.writeBoolean(False)
        self.writeInt(0)
        self.writeString(self.avatarName)

    def getMessageType(self) -> int:
        return 28350

    def setAvatarName(self, name: str):
        self.avatarName = name