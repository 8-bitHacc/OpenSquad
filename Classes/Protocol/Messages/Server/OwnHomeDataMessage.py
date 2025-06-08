import time

from Classes.Instances.PlayerInstance import PlayerInstance
from Classes.Logic.LogicRandom import LogicRandom
from Classes.Logic.Reflectable.LogicCharacterEntry import LogicCharacterEntry
from Classes.Logic.Reflectable.LogicQuestEntry import LogicQuestEntry
from Classes.Logic.Reflectable.LogicShopEntry import LogicShopEntry
from Classes.Logic.Reflector.LogicJSONOutReflector import LogicJSONOutReflector
from Classes.Logic.Reflector.LogicRawOutReflector import LogicRawOutReflector
from Classes.Protocol.PiranhaMessage import PiranhaMessage
import json, random

class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)

    def encode(self, receiver):
        self.writeLongLong(*receiver["Player"].accountID)

        # sub_852248
        self.writeLongLong(*receiver["Player"].accountID)
        self.writeInt(int(time.time()))
        # Constructs reflector and encodes reflectableArrays "w" and "dm"
        self.writeHexa("02 E7 11 89 D4 61 92 D4 61 95 D4 61 96 D4 61 AE D4 61 80 D4 61 81 D4 61 82 D4 61 83 D4 61 84 D4 61 87 D4 61 90 D4 61 93 D4 61 A0 D4 61 86 D4 61 88 D4 61 A6 D4 61 04 A9 CB C9 02 A2 CB C9 02 A0 CB C9 02 A6 CB C9 02 00 00 00 17 64 73 32 5F 45 78 70 4C 65 61 67 75 65 47 72 61 73 73 6C 61 6E 64 73 8B BE 92 01 94 C6 0A A0 EE 6D 11 89 D4 61 92 D4 61 95 D4 61 96 D4 61 AE D4 61 80 D4 61 81 D4 61 82 D4 61 83 D4 61 84 D4 61 87 D4 61 90 D4 61 93 D4 61 A0 D4 61 86 D4 61 88 D4 61 A6 D4 61 04 A9 CB C9 02 A2 CB C9 02 A0 CB C9 02 A6 CB C9 02 00 00 00 1A 64 73 31 44 75 6F 5F 45 78 70 4C 65 61 67 75 65 47 72 61 73 73 6C 61 6E 64 73 8F BE 92 01 94 C6 0A A0 EE 6D")

        self.writeBoolean(False)
        self.writeString(self.reflectJSON(receiver["Player"], receiver["ClientConnection"].serverSession.preloader.offers))

        self.writeLongLong(*receiver["Player"].accountID)
        self.writeLongLong(*receiver["Player"].accountID)
        # end of sub_852248

        if self.writeBoolean(True): # crashes if false
            # LogicClientAvatar::encode
            self.writeLongLong(*receiver["Player"].accountID) # AvatarID
            self.writeLongLong(*receiver["Player"].accountID) # AvatarID
            self.writeStringReference(receiver["Player"].name) # PlayerName
            self.writeVInt(receiver["Player"].registrationState) # State
            self.writeBoolean(True) # Enables Tutorial State
            self.writeLongLong(0, 1) # Age ?
            self.writeVInt(2) # EXP League Level
            self.writeVInt(receiver["Player"].expTokens) # EXP League Tokens Collected
            self.writeStringReference("Male")
            self.writeVInt(receiver["Player"].resources[0]["val"]) # Diamonds Count
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0) # Trophies Amount

            self.writeVInt(3) # Commodity Count

            rawOut = LogicRawOutReflector(self)
            # TODO: Encode these entries
            self.writeVInt(len(receiver["Player"].resources) - 1)
            for resource in receiver["Player"].resources[1:]:
                self.writeBoolean(False) # don't know if this is correct
                rawOut.reflectReflectablePointerBase("d", 300000 + resource["id"])
                rawOut.reflectInt(resource.get("val", 0), "s", 0)

            self.writeVInt(1) # AvatarStats
            for x in range(1):
                self.writeBoolean(False)  # don't know if this is correct
                rawOut.reflectReflectablePointerBase("d", 1400000)
                rawOut.reflectInt(4, "s", 0)

            self.writeVInt(1) # Variables Set Count
            for x in range(1):
                self.writeBoolean(False) # don't know if this is correct
                rawOut.reflectReflectablePointerBase("d", 400002)
                rawOut.reflectInt(1, "s", 0)

            rawOut.destruct()

        rawOut = LogicRawOutReflector(self)
        rawOut.reflectArray(1, "chronosEvents")
        base4 = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self.payload += base4
        self.offset += len(base4)

    def getMessageType(self):
        return 24548

    def reflectJSON(self, player: PlayerInstance, shop: dict):
        reflected = LogicJSONOutReflector({}) # Start off with base data

        LogicShopEntry.reflect(reflected, shop)

        # EventManager
        reflected.reflectObject("eventManager")
        reflected.reflectObject("purchaseCounts")
        reflected.reflectExitObject()
        reflected.reflectExitObject()
        # EventManager

        timer: int = int(time.time())
        reflected.reflectInt(timer, "tick", 0)
        reflected.reflectInt(timer, "globalTick", 0)
        reflected.reflectRandom(LogicRandom(random.randint(1000, 10000)), "rnd")

        if reflected.reflectArray(1 if player.skins else 0, "skins") != 0:
            reflected.reflectNextInt(player.skins)
            reflected.reflectExitArray()

        # LABEL_30
        if reflected.reflectArray(0, "emos") != 0:
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "newEmos") != 0:
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "selEmos") != 0:
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "milestones") != 0:
            reflected.reflectNextInt([4700000, 4700001, 4700002, 4700003, 4700004, 4700005, 4700006, 4700007, 4700008, 4700009, 4700010, 4700011, 4700012, 4700013, 4700014, 4700015, 4700016, 4700017, 4700018, 4700019, 4700020, 4700021, 4700022, 4700023, 4700024, 4700025, 4700026, 4700027, 4700028, 4700029, 4700030, 4700031, 4700032, 4700033, 4700034, 4700035, 4700036, 4700037, 4700038, 4700039, 4700040, 4700041, 4700042, 4700043, 4700044, 4700045, 4700046, 4700047, 4700048, 4700049, 4700050, 4700051, 4700052, 4700053, 4700054, 4700055, 4700056, 4700057, 4700058, 4700059, 4700060, 4700061, 4700062, 4700063, 4700064, 4700065, 4700066, 4700067, 4700068, 4700069, 4700070, 4700071, 4700072, 4700073, 4700074, 4700075, 4700076, 4700077, 4700078, 4700079, 4700080, 4700081, 4700082, 4700083, 4700084, 4700085, 4700086, 4700087, 4700088, 4700089, 4700090, 4700091, 4700092, 4700093, 4700094, 4700095, 4700096])
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "premium_milestones") != 0:
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "trophy_milestones") != 0:
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "trophy_milestones") != 0:
            reflected.reflectExitArray()

        # LABEL_57
        if reflected.reflectArray(0, "spells") != 0:
            reflected.reflectExitArray()

        # LABEL_84
        #reflected.reflectIntArray([], "spellsC") # I have no idea how this works

        reflected.reflectInt(5, "ver", 0)

        # Gem Reward
        if reflected.reflectArray(0, "gemRew") != 0:
            reflected.reflectNextInt([6200000,6200002,6200000,6200002,6200002,6200000,6200008,6200000,6200008,6200001,6200003,6200001,6200003,6200001,6200003,6200001])
            reflected.reflectExitArray()

        reflected.reflectObject("gemT")
        reflected.reflectInt(1000, "t", 0)
        reflected.reflectBool(False, "p", False)
        reflected.reflectExitObject()

        reflected.reflectObject("lootLimitT")
        reflected.reflectInt(1000, "t", 0)
        reflected.reflectBool(False, "p", False)
        reflected.reflectExitObject()

        reflected.reflectInt(20000, "lootLimitUnused", 0)
        reflected.reflectInt(100, "gemRewardTokenSequence", 0)
        reflected.reflectInt(1, "plazaChestI", 0)

        reflected.reflectObject("plazaRewardT")
        reflected.reflectInt(6974, "t", 0)
        reflected.reflectBool(False, "p", False)
        reflected.reflectExitObject()

        reflected.reflectObject("plazaChestT")
        reflected.reflectInt(69746, "t", 0)
        reflected.reflectBool(False, "p", False)
        reflected.reflectExitObject()

        # Characters
        reflected.reflectObject("chars")
        LogicCharacterEntry.reflect(reflected, player)
        reflected.reflectExitObject()

        # Quests
        LogicQuestEntry.reflect(reflected, player.quests)

        # Tutorials
        reflected.reflectObject("tutorials")
        reflected.reflectArray(1, "tut")
        reflected.reflectNextInt([5000000, 5000001, 5000002, 5000003, 5000004, 5000005, 5000006, 5000007, 5000008, 5000009, 5000012])
        reflected.reflectExitArray()
        reflected.reflectExitObject()

        reflected.reflectInt(1, "sEvent", 0)

        return json.dumps(reflected.jsonData, ensure_ascii=False)