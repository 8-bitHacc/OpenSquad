from Classes.Logic.Reflectable.LogicCharacterEntry import LogicCharacterEntry
from Classes.Logic.Reflectable.LogicReflectable import LogicReflectable
from Classes.Utilities.Debugger import Debugger

class LogicReflectableFactory:
    reflectableTypes = {
        1006: LogicCharacterEntry
    }

    @classmethod
    def reflectableExists(cls, reflectableType: int) -> bool:
        return reflectableType in cls.reflectableTypes

    @classmethod
    def createReflectable(cls, reflectableType: int) -> LogicReflectable:
        if cls.reflectableExists(reflectableType):
            return cls.reflectableTypes[reflectableType]()
        else:
            Debugger.error(f"createReflectable - unknown type {reflectableType}")
            return LogicReflectable()