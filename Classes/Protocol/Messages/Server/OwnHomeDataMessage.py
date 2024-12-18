import time

from Classes.Instances.PlayerInstance import PlayerInstance
from Classes.Logic.LogicRandom import LogicRandom
from Classes.Logic.Reflectable.LogicCharacterEntry import LogicCharacterEntry
from Classes.Logic.Reflectable.LogicQuestEntry import LogicQuestEntry
from Classes.Logic.Reflectable.LogicShopEntry import LogicShopEntry
from Classes.Logic.Reflectable.LogicTimeObject import LogicTimeObject
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
        base = b'\x02\xe7\x11\x89\xd4a\x92\xd4a\x95\xd4a\x96\xd4a\xae\xd4a\x80\xd4a\x81\xd4a\x82\xd4a\x83\xd4a\x84\xd4a\x87\xd4a\x90\xd4a\x93\xd4a\xa0\xd4a\x86\xd4a\x88\xd4a\xa6\xd4a\x04\xa9\xcb\xc9\x02\xa2\xcb\xc9\x02\xa0\xcb\xc9\x02\xa6\xcb\xc9\x02\x00\x00\x00\x17ds3_ExpLeagueGrasslands\x8a\xbe\x92\x01\xbf\xa7\xd6\xb9\x07\xa0\xeem\x11\x89\xd4a\x92\xd4a\x95\xd4a\x96\xd4a\xae\xd4a\x80\xd4a\x81\xd4a\x82\xd4a\x83\xd4a\x84\xd4a\x87\xd4a\x90\xd4a\x93\xd4a\xa0\xd4a\x86\xd4a\x88\xd4a\xa6\xd4a\x04\xa2\xcb\xc9\x02\xa6\xcb\xc9\x02\xa9\xcb\xc9\x02\xa0\xcb\xc9\x02\x00\x00\x00\x1ads1Duo_ExpLeagueGrasslands\x8e\xbe\x92\x01\xf0\xca\xd3\xdc\t\xa0\xeem\x00'

        self.payload += base
        self.offset += base.__len__()

        self.writeString(self.reflectJSON(receiver["Player"]))

        # dont know what that is
        base2 = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01'
        self.payload += base2
        self.offset += len(base2)

        if self.writeBoolean(True): # making it false crashes for some odd reason...
            # LogicClientAvatar::encode
            self.writeLong(*receiver["Player"].getPlayerID()) # AvatarID
            self.writeLong(*receiver["Player"].getPlayerID()) # AvatarID
            self.writeStringReference(receiver["Player"].Name) # PlayerName
            self.writeVInt(6)
            self.writeBoolean(True) # Enables Tutorial State? (Shows hand pointing at "PLAY")
            self.writeLong(0, 154) # what?
            self.writeVInt(1) # dont know
            self.writeVInt(0) # EXP League Tokens Collected
            self.writeStringReference(None)
            self.writeVInt(0) # Diamonds Count
            self.writeVInt(2)
            self.writeVInt(1)
            self.writeVInt(0) # Trophies Amount

            self.writeVInt(3) # Commodity Count

            # TODO: Encode these entries
            self.writeVInt(2)

            clientAvatar = b'\x00\xa1\xcf$\x01\xa0\x84=\x00\xa4\xcf$\x01\x9f\x9a\x0c\x00\x02\x00\x82\xea0\x01\x01\x00\x84\xea0\x01\xa8\x0f'

            self.payload += clientAvatar
            self.offset += len(clientAvatar)

        base4 = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        self.payload += base4
        self.offset += len(base4)

    def getMessageType(self):
        return 24548

    def getJSON(self) -> str:
        return '''{
  "shop": {
    "id": 11,
    "special": [
      {
        "id": 1,
        "c": 5,
        "a": 1,
        "dd": 5200027,
        "d": 300014,
        "cr": 300000
      },
      {
        "id": 2,
        "c": 25,
        "a": 5,
        "dd": 5200028,
        "d": 300014,
        "cr": 300000
      }
    ],
    "i": [
      {
        "id": 3,
        "a": 1,
        "bLimit": true,
        "dd": 5200024,
        "d": 4500006,
        "cr": 300000
      },
      {
        "id": 4,
        "c": 5,
        "a": 10,
        "bLimit": true,
        "dd": 5200010,
        "d": 800000,
        "cr": 300000
      },
      {
        "id": 5,
        "c": 5,
        "a": 10,
        "bLimit": true,
        "dd": 5200010,
        "d": 800004,
        "cr": 300000
      }
    ],
    "e": [
      {
        "id": 8,
        "c": 20,
        "a": 1,
        "bLimit": true,
        "dd": 5200021,
        "d": 4200047,
        "cr": 300012
      },
      {
        "id": 7,
        "c": 20,
        "a": 1,
        "bLimit": true,
        "dd": 5200021,
        "d": 4200115,
        "cr": 300012
      },
      {
        "id": 6,
        "c": 40,
        "a": 1,
        "bLimit": true,
        "dd": 5200022,
        "d": 4200063,
        "cr": 300012
      }
    ],
    "s": [
      {
        "id": 11,
        "c": 0,
        "a": 1,
        "bLimit": true,
        "dd": 5200024,
        "d": 4500002,
        "cr": 69
      },
      {
        "id": 10,
        "c": 0,
        "a": 1,
        "bLimit": true,
        "dd": 5200024,
        "d": 4500002,
        "cr": 69
      },
      {
        "id": 9,
        "c": 0,
        "a": 1,
        "bLimit": true,
        "dd": 5200019,
        "d": 5500067,
        "cr": 69
      }
    ],
    "t": {
      "t": 1000
    }
  },
  "eventManager": {
    "purchaseCounts": {}
  },
  "tick": 33517122184,
  "global_t": 33517115968,
  "rnd": 0,
  "newEv": [],
  "skins": [
    5500004
  ],
  "emos": [
    4200000,
    4200001,
    4200002,
    4200003,
    4200004,
    4200005,
    4200006,
    4200007,
    4200008,
    4200009,
    4200038
  ],
  "newEmos": [
    4200038
  ],
  "selEmos": [
    4200000,
    4200004,
    4200008,
    4200003
  ],
  "milestones": [
    4700000,
    4700001,
    4700002,
    4700003
  ],
  "exp_league_premium": [],
  "ver": 5,
  "gemRew": [
    6200000
  ],
  "gemT": {
    "t": 10
  },
  "lootLimitT": {
    "t": 10
  },
  "lootLimitUnused": 20000,
  "gemRewardTokenSequence": 100,
  "plazaRewardT": {
    "t": 20,
    "p": true
  },
  "plazaChestT": {
    "t": 69746,
    "p": true
  },
  "chars": {
    "c": [
      {
        "data": 800000,
        "abLvl": -1
      },
      {
        "data": 800004,
        "abLvl": -1
      },
      {
        "data": 800002,
        "skin": 5500004,
        "pts": 69,
        "abLvl": -1,
        "useCount": 1
      }
    ],
    "s": [
      {
        "d": 2700000
      },
      {
        "d": 2700002
      },
      {
        "d": 2700006
      }
    ],
    "seen": [
      65695,
      0
    ],
    "lastUnlock": 800002
  },
  "quests": {
    "questProgress": [
      {
        "questData": 6300062,
        "seen": true
      },
      {
        "questData": 6300063,
        "seen": true
      },
      {
        "questData": 6300066,
        "seen": true
      }
    ],
    "t": {
      "t": -1,
      "p": true
    },
    "tr": {
      "t": -1,
      "p": true
    },
    "allowedOverflow": 3,
    "newbQuestsProgress": 3
  },
  "tutorials": {
    "tut": [
      5000000,
      5000001,
      5000002,
      5000003,
      5000004,
      5000005,
      5000006,
      5000007,
      5000008,
      5000009,
      5000018
    ]
  },
  "pProg": 5,
  "sEvent": 2
}'''
    def reflectJSON(self, player: PlayerInstance):
        reflected = LogicJSONOutReflector({}) # Start off with base data

        LogicShopEntry.reflect(reflected)

        # EventManager
        reflected.reflectObject("eventManager")
        reflected.reflectObject("purchaseCounts")
        reflected.reflectExitObject()
        reflected.reflectExitObject()
        # EventManager

        tick = int(time.time())
        reflected.reflectInt(tick, "tick", 0)
        reflected.reflectInt(tick, "globalTick", 0)
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
            reflected.reflectNextInt(6200000)
            reflected.reflectExitArray()

        LogicTimeObject.reflect(reflected, 0, objectName="gemT")

        LogicTimeObject.reflect(reflected, 1000, objectName="lootLimitT")

        reflected.reflectInt(20000, "lootLimitUnused", 0)
        reflected.reflectInt(100, "gemRewardTokenSequence", 0)
        reflected.reflectInt(1, "plazaChestI", 0)

        LogicTimeObject.reflect(reflected, 6974, True, objectName="plazaRewardT")

        LogicTimeObject.reflect(reflected, 0, objectName="plazaChestT")

        # Characters
        reflected.reflectObject("chars")
        LogicCharacterEntry.reflect(reflected, player)
        reflected.reflectExitObject()

        # Quests
        LogicQuestEntry.reflect(reflected, player.Quests)

        # Tutorials
        reflected.reflectObject("tutorials")
        reflected.reflectArray(10, "tut")
        for tut in [5000001,5000002,5000003,5000004,5000005,5000006,5000007,5000008,5000009,5000012]:
            reflected.reflectNextInt(tut)

        reflected.reflectExitArray()
        reflected.reflectExitObject()

        # Battle Logs (Unused)
        reflected.reflectObject("bRes")
        reflected.reflectExitObject()

        reflected.reflectInt(0, "pProg", 0)
        reflected.reflectInt(0, "sEvent", 0)

        return json.dumps(reflected.jsonData, ensure_ascii=False)