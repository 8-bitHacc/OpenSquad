from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Protocol.Messages.Server.ServerHelloMessage import ServerHelloMessage
from Classes.Protocol.Messages.Server.LoginFailedMessage import LoginFailedMessage
from Classes.Utilities.Preloader import Preloader

class ClientHelloMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)
        self.settings: dict = Preloader.ConfigurationData
        self.protocol: int = 0
        self.keyVersion: int = 0
        self.major: int = 0
        self.minor: int = 0
        self.build: int = 0
        self.contentHash: str = ""
        self.deviceType: int = 0
        self.appStore: int = 0

    def decode(self, receiver):
        self.protocol = self.readInt()
        self.keyVersion = self.readInt()
        self.major = self.readInt()
        self.minor = self.readInt()
        self.build = self.readInt()
        self.contentHash = self.readString()
        self.deviceType = self.readInt()
        self.appStore = self.readInt()

    def execute(self, receiver):
        if self.settings["Maintenance"] != 0:
            l = LoginFailedMessage()
            l.setErrorCode(10)
            receiver["ClientConnection"].messaging.send(receiver, l)

        elif not self.checkValidation():
            l = LoginFailedMessage()
            l.setErrorCode(1)
            l.setMessage(":)")
            receiver["ClientConnection"].messaging.send(receiver, l)

        elif self.major != self.settings["CurrentMajor"]:
            l = LoginFailedMessage()
            l.setErrorCode(8)
            l.setMessage("A new version of the private server is available!")
            l.setUpdateURL("https://mega.nz/file/m4c0nSyK#_YNLSBuGsO8sTjJ1Q6ANxCwPYXOMhdmXrzRtxlIMwKM")
            receiver["ClientConnection"].messaging.send(receiver, l)

        elif self.contentHash != self.settings["ContentHash"]:
            l = LoginFailedMessage()
            l.setErrorCode(7)
            l.setCompressedFingerprint(b"") # TODO: Add content update system
            receiver["ClientConnection"].messaging.send(receiver, l)
        else:
            serverHello = ServerHelloMessage()
            receiver["ClientConnection"].messaging.send(receiver, serverHello)

    def getMessageType(self) -> int:
        return 10100

    def checkValidation(self) -> bool:
        if self.protocol != 1: return False
        elif self.keyVersion != 1: return False
        return True