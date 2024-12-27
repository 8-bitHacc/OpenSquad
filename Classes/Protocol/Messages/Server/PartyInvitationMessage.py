from Classes.Logic.Reflectable.LogicPartyReflectable import LogicPartyReflectable
from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Logic.Reflector.LogicRawOutReflector import LogicRawOutReflector

class PartyInvitationMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)

    def encode(self, receiver):
        rawOut = LogicRawOutReflector(self)
        self.reflect(rawOut, receiver)
        rawOut.destruct()

    def getMessageType(self):
        return 24726

    def reflect(self, reflector: LogicRawOutReflector, receiver):
        reflector.reflectNextReflectable(LogicPartyReflectable, 1021, None)