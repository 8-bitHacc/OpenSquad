from Classes.Protocol.PiranhaMessage import PiranhaMessage
from os import urandom

class ServerHelloMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)
        self.sessionKey = urandom(24)

    def encode(self, receiver):
        self.writeBytes(self.sessionKey, 24)

    def getMessageType(self):
        return 20100
