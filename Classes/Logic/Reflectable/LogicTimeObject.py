from Classes.Logic.Reflector.LogicJSONOutReflector import LogicJSONOutReflector

class LogicTimeObject:

    @staticmethod
    def reflect(reflector: LogicJSONOutReflector, time: int = 0, enabled: bool = False):
        reflector.reflectObject("t")
        reflector.reflectInt(time, "t", 0)
        reflector.reflectBool(enabled, "p", False)
        reflector.reflectExitObject()