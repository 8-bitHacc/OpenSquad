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
        self.packetVersion = 0

    def encode(self, receiver):
        self.writeLongLong(0, 1)

        # sub_852248
        self.writeLongLong(0, 1)
        self.writeInt(1399183669)
        # Constructs reflector and encodes reflectableArrays "w" and "dm"
        base = b'\x02\xe7\x11\x89\xd4a\x92\xd4a\x95\xd4a\x96\xd4a\xae\xd4a\x80\xd4a\x81\xd4a\x82\xd4a\x83\xd4a\x84\xd4a\x87\xd4a\x90\xd4a\x93\xd4a\xa0\xd4a\x86\xd4a\x88\xd4a\xa6\xd4a\x04\xa9\xcb\xc9\x02\xa2\xcb\xc9\x02\xa0\xcb\xc9\x02\xa6\xcb\xc9\x02\x00\x00\x00\x17ds3_ExpLeagueGrasslands\x8a\xbe\x92\x01\xbf\xa7\xd6\xb9\x07\xa0\xeem\x11\x89\xd4a\x92\xd4a\x95\xd4a\x96\xd4a\xae\xd4a\x80\xd4a\x81\xd4a\x82\xd4a\x83\xd4a\x84\xd4a\x87\xd4a\x90\xd4a\x93\xd4a\xa0\xd4a\x86\xd4a\x88\xd4a\xa6\xd4a\x04\xa2\xcb\xc9\x02\xa6\xcb\xc9\x02\xa9\xcb\xc9\x02\xa0\xcb\xc9\x02\x00\x00\x00\x1ads1Duo_ExpLeagueGrasslands\x8e\xbe\x92\x01\xf0\xca\xd3\xdc\t\xa0\xeem'

        self.payload += base
        self.offset += base.__len__()

        self.writeBoolean(False)
        self.writeString(self.reflectJSON(receiver["Player"]))

        self.writeLongLong(0, 0)
        self.writeLongLong(0, 1)
        # end of sub_852248

        if self.writeBoolean(True): # crashes if false
            # LogicClientAvatar::encode
            self.writeLongLong(*receiver["Player"].getPlayerID()) # AvatarID
            self.writeLongLong(*receiver["Player"].getPlayerID()) # AvatarID
            self.writeStringReference(receiver["Player"].Name) # PlayerName
            self.writeVInt(3) # State
            self.writeBoolean(True) # Enables Tutorial State? (Shows hand pointing at "PLAY")
            self.writeLongLong(0, 0) # Age ?
            self.writeVInt(100) # EXP League Level
            self.writeVInt(9999999) # EXP League Tokens Collected
            self.writeStringReference()
            self.writeVInt(0) # Diamonds Count
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0) # Trophies Amount

            self.writeVInt(3) # Commodity Count

            rawOut = LogicRawOutReflector(self)
            # TODO: Encode these entries
            self.writeVInt(3)
            for x in range(1):
                self.writeBoolean(False) # don't know if this is correct
                rawOut.reflectReflectablePointerBase("d", 300001)
                rawOut.reflectInt(69, "s", 0)

                self.writeBoolean(False)  # don't know if this is correct
                rawOut.reflectReflectablePointerBase("d", 300004)
                rawOut.reflectInt(74, "s", 0)

                self.writeBoolean(False)  # don't know if this is correct
                rawOut.reflectReflectablePointerBase("d", 300014)
                rawOut.reflectInt(5, "s", 0)

            self.writeVInt(0)

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

    def reflectJSON(self, player: PlayerInstance):
        reflected = LogicJSONOutReflector({}) # Start off with base data

        LogicShopEntry.reflect(reflected)

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

        if reflected.reflectArray(0, "skins") != 0:
            reflected.reflectNextInt(player.UnlockedSkins)
            reflected.reflectExitArray()

        # LABEL_30
        if reflected.reflectArray(0, "emos") != 0:
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "newEmos") != 0:
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "selEmos") != 0:
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "milestones") != 0:
            reflected.reflectNextInt([4700000, 4700001, 4700002, 4700003, 4700004, 4700005, 4700006, 4700007, 4700008, 4700009, 4700010, 4700011, 4700012, 4700013, 4700014, 4700015, 4700016, 4700017, 4700018, 4700019, 4700020, 4700021, 4700022, 4700023, 4700024, 4700025, 4700026, 4700027, 4700028, 4700029, 4700030, 4700031, 4700032, 4700033, 4700034, 4700035, 4700036, 4700037, 4700038, 4700039, 4700040, 4700041, 4700042, 4700043, 4700044, 4700045, 4700046, 4700047, 4700048, 4700049, 4700050, 4700051, 4700052, 4700053, 4700054, 4700055, 4700056, 4700057, 4700058, 4700059, 4700060, 4700061, 4700062, 4700063, 4700064, 4700065, 4700066, 4700067, 4700068, 4700069, 4700070, 4700071, 4700072, 4700073, 4700074, 4700075, 4700076, 4700077, 4700078, 4700079, 4700080, 4700081, 4700082, 4700083, 4700084, 4700085, 4700086, 4700087, 4700088, 4700089, 4700090, 4700091, 4700092, 4700093, 4700094, 4700095])
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
        LogicQuestEntry.reflect(reflected, player.Quests)

        # Tutorials
        reflected.reflectObject("tutorials")
        reflected.reflectArray(1, "tut")
        reflected.reflectNextInt([5000000, 5000001, 5000002, 5000003, 5000004, 5000005, 5000006, 5000007, 5000008, 5000009, 5000012])
        reflected.reflectExitArray()
        reflected.reflectExitObject()

        reflected.reflectInt(1, "sEvent", 0)

        return json.dumps(reflected.jsonData, ensure_ascii=False)