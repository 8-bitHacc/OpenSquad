from Classes.Protocol.PiranhaMessage import PiranhaMessage

class LoginFailedMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)
        self.errorCode: int = 0
        self.redirectURL: str = None
        self.contentURL: str = None
        self.updateURL: str = None
        self.message: str = None
        self.maintenanceTime: int = 0
        self.compressedFingerprint: bytes = b""
        self.contentFiles: list = []
    
    def encode(self, receiver):
        self.writeInt(self.errorCode)

        self.writeString() # Fingerprint
        self.writeString(self.redirectURL)
        self.writeString(self.contentURL)
        self.writeString(self.updateURL)
        self.writeString(self.message)

        self.writeInt(self.maintenanceTime)
        self.writeBoolean(False)

        self.writeBytes(self.compressedFingerprint, len(self.compressedFingerprint))

        self.writeInt(len(self.contentFiles))
        for fileURL in self.contentFiles:
            self.writeString(fileURL)

        self.writeInt(0)
        self.writeInt(2)
        self.writeString()
        self.writeInt(0)
        self.writeInt(0)
        self.writeBoolean(False)
    
    def getMessageType(self) -> int:
        return 20103

    def setErrorCode(self, code: int):
        self.errorCode = code

    def setContentURL(self, url: str):
        self.contentURL = url

    def setUpdateURL(self, url: str):
        self.updateURL = url

    def setMessage(self, msg: str):
        self.message = msg

    def setMaintenanceTime(self, time: int):
        self.maintenanceTime = time

    def setCompressedFingerprint(self, f: bytes):
        self.compressedFingerprint = f

    def setContentFiles(self, files: list):
        self.contentFiles = files