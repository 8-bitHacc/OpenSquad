from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Protocol.Messages.Server.ServerHelloMessage import ServerHelloMessage

class ClientHelloMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)
        self.AppStore = None
        self.DeviceType = None
        self.ClientBuild = None
        self.ClientMinor = None
        self.Protocol = None
        self.ContentHash = None
        self.KeyVersion = None
        self.ClientMajor = None

    def decode(self, receiver):
        self.Protocol = self.readInt()
        self.KeyVersion = self.readInt()
        self.ClientMajor = self.readInt()
        self.ClientMinor = self.readInt()
        self.ClientBuild = self.readInt()
        self.ContentHash = self.readString()
        self.DeviceType = self.readInt()
        self.AppStore = self.readInt()

    def execute(self, receiver):
        serverHello = ServerHelloMessage()
        receiver["ClientConnection"].messaging.send(receiver, serverHello)

    def getMessageType(self):
        return 10100
