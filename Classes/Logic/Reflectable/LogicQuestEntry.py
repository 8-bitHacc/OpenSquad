from Classes.Logic.Reflectable.LogicTimeObject import LogicTimeObject
from Classes.Logic.Reflector.LogicJSONOutReflector import LogicJSONOutReflector

class LogicQuestEntry:

    @classmethod
    def reflect(cls, reflector: LogicJSONOutReflector, quests: list):
        reflector.reflectObject("quests")

        if reflector.reflectArray(len(quests), "questProgress", False) != 0:
            for quest in quests: cls.reflectQuest(reflector, quest)
            reflector.reflectExitArray()

        LogicTimeObject.reflect(reflector)
        LogicTimeObject.reflect(reflector, objectName="tr")

        reflector.reflectInt(0, "allowedOverflow", 0)
        reflector.reflectInt(0, "newbQuestsProgress", 0)

        reflector.reflectExitObject()

    @classmethod
    def reflectQuest(cls, reflector: LogicJSONOutReflector, quest: dict):
        reflector.reflectInt(6300000 + quest["id"], "questData", 6300000)
        reflector.reflectInt(quest.get("progress", 0), "progress", 0)
        reflector.reflectBool(quest.get("seen", False), "seen", False)
        #.reflectInt(0,) chroId won't be implemented as i don't know what it does
        reflector.currentArrayIndex += 1