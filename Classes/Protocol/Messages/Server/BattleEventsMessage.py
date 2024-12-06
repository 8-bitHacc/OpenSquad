from Classes.Logic.Reflector.LogicRawOutReflector import LogicRawOutReflector
from Classes.Protocol.PiranhaMessage import PiranhaMessage

class BattleEventsMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)
        self.frameID: int = 0

    def encode(self, receiver):
        rawOut = LogicRawOutReflector(self)
        self.reflect(rawOut, receiver)
        rawOut.destruct()

    def getMessageType(self):
        return 28852

    def setFrameID(self, frame: int):
        self.frameID = frame

    def reflect(self, reflector: LogicRawOutReflector, receiver):
        reflector.reflectInt(self.frameID, "frameId", 0)
        reflector.reflectArray(0, "events")