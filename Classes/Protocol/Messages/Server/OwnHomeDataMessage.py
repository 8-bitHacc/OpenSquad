import time

from Classes.Logic.LogicRandom import LogicRandom
from Classes.Logic.Reflectable.LogicCharacterEntry import LogicCharacterEntry
from Classes.Logic.Reflector.LogicJSONOutReflector import LogicJSONOutReflector
from Classes.Protocol.PiranhaMessage import PiranhaMessage
import json, random

class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)
        self.packetVersion = 0

    def encode(self, receiver):
        self.writeLong(0, 1)
        self.writeLong(0, 1)

        # sub
        self.writeInt(1399183669)
        base = b'\x02\xe7\x11\x89\xd4a\x92\xd4a\x95\xd4a\x96\xd4a\xae\xd4a\x80\xd4a\x81\xd4a\x82\xd4a\x83\xd4a\x84\xd4a\x87\xd4a\x90\xd4a\x93\xd4a\xa0\xd4a\x86\xd4a\x88\xd4a\xa6\xd4a\x04\xa9\xcb\xc9\x02\xa2\xcb\xc9\x02\xa0\xcb\xc9\x02\xa6\xcb\xc9\x02\x00\x00\x00\x17ds2_ExpLeagueGrasslands\x8a\xbe\x92\x01\xbf\xa7\xd6\xb9\x07\xa0\xeem\x11\x89\xd4a\x92\xd4a\x95\xd4a\x96\xd4a\xae\xd4a\x80\xd4a\x81\xd4a\x82\xd4a\x83\xd4a\x84\xd4a\x87\xd4a\x90\xd4a\x93\xd4a\xa0\xd4a\x86\xd4a\x88\xd4a\xa6\xd4a\x04\xa2\xcb\xc9\x02\xa6\xcb\xc9\x02\xa9\xcb\xc9\x02\xa0\xcb\xc9\x02\x00\x00\x00\x1ads1Duo_ExpLeagueGrasslands\x8e\xbe\x92\x01\xf0\xca\xd3\xdc\t\xa0\xeem\x00'

        self.payload += base
        self.offset += base.__len__()

        #jsonRefl = self.getJSON()
        #jsonData = json.loads(jsonRefl)
        #jsonData["rnd"] = LogicRandom().iterateRandomSeed(random.randint(1000, 10000))
        self.writeString(self.reflectJSON(receiver))

        # dont know what that is
        base2 = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01'
        self.payload += base2
        self.offset += len(base2)

        # LogicClientAvatar::encode
        self.writeLong(*receiver["Player"].getPlayerID()) # AvatarID
        self.writeLong(*receiver["Player"].getPlayerID()) # AvatarID
        self.writeStringReference(receiver["Player"].Name) # PlayerName
        self.writeVInt(6)
        self.writeBoolean(False) # Enables Tutorial State? (Shows hand pointing at "PLAY")
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

        clientAvatar = b'\x00\xa1\xcf$\x01\xa0\x84=\x00\xa4\xcf$\x01\x9f\x9a\x0c\x00\x02\x00\x82\xea0\x01\x01\x00\x84\xea0\x01\xa8\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        self.payload += clientAvatar
        self.offset += len(clientAvatar)

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
    def reflectJSON(self, receiver):
        reflected = LogicJSONOutReflector({}) # Start off with base data

        reflected.reflectObject("shop")
        # Shop
        reflected.reflectInt(0, "id", 0)

        if reflected.reflectArray(0, "special") != 0:
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "i") != 0:
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "e") != 0:
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "s") != 0:
            reflected.reflectExitArray()

        reflected.reflectObject("t")
        reflected.reflectInt(1000, "t", 0)
        reflected.reflectBool(False, "p", False)
        reflected.reflectExitObject()

        reflected.reflectExitObject()
        # Shop

        # EventManager
        reflected.reflectObject("eventManager")
        reflected.reflectObject("purchaseCounts")
        reflected.reflectExitObject()
        reflected.reflectExitObject()
        # EventManager

        reflected.reflectInt(33517122184, "tick", 0)
        reflected.reflectInt(33517115968, "globalTick", 0)
        reflected.reflectRandom(LogicRandom(random.randint(0, 10000)), "rnd")

        if reflected.reflectArray(0, "skins") != 0:
            reflected.reflectExitArray()

        # LABEL_30
        if reflected.reflectArray(0, "emos") != 0:
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "newEmos") != 0:
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "selEmos") != 0:
            reflected.reflectExitArray()

        if reflected.reflectArray(0, "milestones") != 0:
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
        LogicCharacterEntry.reflect(reflected, receiver["Player"])
        reflected.reflectExitObject()

        # Quests
        reflected.reflectObject("quests")
        reflected.reflectArray(1, "questProgress")
        reflected.reflectExitArray()
        reflected.reflectExitObject()

        # Tutorials
        reflected.reflectObject("tutorials")
        reflected.reflectArray(1, "tut")
        for tut in []: # 5000001,5000002,5000003,5000004,5000005,5000006,5000007,5000008,5000009,5000018
            reflected.reflectNextInt(tut)
        reflected.reflectExitArray()
        reflected.reflectExitObject()

        return json.dumps(reflected.jsonData, ensure_ascii=False)