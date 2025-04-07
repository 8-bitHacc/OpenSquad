from Classes.Instances.PlayerInstance import PlayerInstance
from Classes.Logic.Reflectable.LogicReflectable import LogicReflectable
from Classes.Logic.Reflector.LogicJSONOutReflector import LogicJSONOutReflector

class LogicCharacterEntry(LogicReflectable):

    @classmethod
    def reflect(cls, reflector: LogicJSONOutReflector, player: PlayerInstance) -> None:
        if reflector.reflectArray(len(player.members), "c", False) != 0:
            reflector.currentArrayIndex = 0
            for char in player.members:
                cls.reflectCharacter(reflector, char)
            reflector.reflectExitArray()

        if reflector.reflectArray(0, "s", False) != 0:
            reflector.currentArrayIndex = 0
            for spell in [0, 2, 6]:
                reflector.reflectInt(2700000 + spell, "d", 0)
                reflector.currentArrayIndex += 1
            reflector.reflectExitArray()

        reflector.reflectArray(0, "p") # Not going to do checks for this as it won't add to the list anyway...
        reflector.reflectArray(0, "seen")
        reflector.reflectInt(8000002, "lastUnlock", 8000000)

    @classmethod
    def reflectCharacter(cls, reflector: LogicJSONOutReflector, characterData: dict) -> None:
        reflector.reflectInt(800000 + characterData["id"], "data", 0)
        reflector.reflectInt(5500000 + characterData.get("skin", 0), "skin", 5500000)
        reflector.reflectInt(characterData.get("pts", 0), "pts", 0)
        reflector.reflectInt(characterData.get("lvl", 0), "lvl", 0)
        reflector.reflectInt(characterData.get("ab", 0), "abLvl", 0)
        # Force Left is unknown
        reflector.reflectInt(characterData.get("used", 0), "useCount", 0)
        reflector.currentArrayIndex += 1

    @classmethod
    def getReflectableType(cls) -> int:
        return 1006