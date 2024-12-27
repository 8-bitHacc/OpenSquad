from Classes.Logic.Reflector.LogicRawOutReflector import LogicRawOutReflector
from Classes.Protocol.PiranhaMessage import PiranhaMessage

class FriendListMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)

    def encode(self, receiver):
        rawOut = LogicRawOutReflector(self)
        self.reflect(rawOut, receiver)
        rawOut.destruct()

    def getMessageType(self):
        return 20946

    def reflect(self, reflector: LogicRawOutReflector, receiver):
        reflector.reflectInt(1, "type", 0) # Friend List type
        reflector.reflectArray(1, "entries")

        # FriendRegion
        # sub_A4D304
        reflector.reflectLong(reflector, 0, 2, "homeId", 0)
        reflector.reflectString("8-bitHacc", "name", None)
        reflector.reflectString("", "facebookId", None)
        reflector.reflectInt(1, "onlineStatus", 0)
        reflector.reflectInt(0, "protectionDurationSeconds", 0)
        reflector.reflectInt(1, "expLevel", 0)
        reflector.reflectInt(0, "score", 0)
        reflector.reflectInt(1, "friendState", 0)
        reflector.reflectInt(0, "ageSeconds", 0)
        reflector.reflectInt(0, "allianceBadgetData", 0) # who wrote badget like this at supercell hq, probably got tired from reflecting
        #reflector.reflectString("Alliance1", "allianceName", None)
        reflector.reflectInt(0, "allianceRole", 0)
        reflector.reflectInt(0, "allianceExpLevel", 0)
        reflector.reflectInt(0, "currentSeasonId", 0)
        reflector.reflectInt(0, "lastUpdatedAt", 0)
        reflector.reflectString("FirstName", "firstName", None)
        reflector.reflectString("8-bit Hacc", "fullName", None)
        reflector.reflectString("https://game-assets.squadbustersgame.com/de409b9c8578b20d0dda47c0a08621aee6db6a02/profile_pictures/baby_colt.png", "profilePictureURL", None)
        reflector.reflectString("SUPERCELLID", "supercellId", None)
        reflector.reflectInt(0, "aha", 0)