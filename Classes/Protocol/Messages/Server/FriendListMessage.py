from Classes.Logic.Reflector.LogicRawOutReflector import LogicRawOutReflector
from Classes.Protocol.PiranhaMessage import PiranhaMessage

class FriendListMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)

    def encode(self, receiver):
        rawOut = LogicRawOutReflector(self)
        rawOut.reflectInt(0, "")

    def getMessageType(self):
        return 20108