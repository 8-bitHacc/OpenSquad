from Classes.Logic.Reflectable.LogicReflectable import LogicReflectable
from Classes.Logic.Reflector.LogicRawOutReflector import LogicRawOutReflector

class LogicPartyReflectable(LogicReflectable):

    @classmethod
    def reflect(cls, reflector: LogicRawOutReflector, reflectableData: dict):
        reflector.reflectString("2PP", "partyId", "")
        reflector.reflectLong(0, 0, 1, "id", 0)

    @classmethod
    def getReflectableId(cls) -> int:
        return 1021