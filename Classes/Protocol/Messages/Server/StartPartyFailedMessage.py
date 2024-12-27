from Classes.Protocol.PiranhaMessage import PiranhaMessage

class StartPartyFailedMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)
        self.errorCode: int = 1

    def encode(self, receiver):
        self.writeInt(self.errorCode)

    def getMessageType(self) -> int:
        return 24724

    def setErrorCode(self, c: int):
        self.errorCode = c