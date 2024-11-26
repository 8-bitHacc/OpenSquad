from Classes.Protocol.PiranhaMessage import PiranhaMessage


class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)
        self.packetVersion = 0

    def encode(self, receiver):
        base = b'\x00\x00\x00\x00\x00\x00;t\x00\x00\x00\x00\x00\x00;tSe\xd95\x02\xe7\x11\x89\xd4a\x92\xd4a\x95\xd4a\x96\xd4a\xae\xd4a\x80\xd4a\x81\xd4a\x82\xd4a\x83\xd4a\x84\xd4a\x87\xd4a\x90\xd4a\x93\xd4a\xa0\xd4a\x86\xd4a\x88\xd4a\xa6\xd4a\x04\xa9\xcb\xc9\x02\xa2\xcb\xc9\x02\xa0\xcb\xc9\x02\xa6\xcb\xc9\x02\x00\x00\x00\x17ds2_ExpLeagueGrasslands\x8a\xbe\x92\x01\xbf\xa7\xd6\xb9\x07\xa0\xeem\x11\x89\xd4a\x92\xd4a\x95\xd4a\x96\xd4a\xae\xd4a\x80\xd4a\x81\xd4a\x82\xd4a\x83\xd4a\x84\xd4a\x87\xd4a\x90\xd4a\x93\xd4a\xa0\xd4a\x86\xd4a\x88\xd4a\xa6\xd4a\x04\xa2\xcb\xc9\x02\xa6\xcb\xc9\x02\xa9\xcb\xc9\x02\xa0\xcb\xc9\x02\x00\x00\x00\x1ads1Duo_ExpLeagueGrasslands\x8e\xbe\x92\x01\xf0\xca\xd3\xdc\t\xa0\xeem\x00'
        self.payload += base
        self.offset += base.__len__()

        json = self.getJSON()
        # self.writeInt(json.__len__()) # relfected json length!!
        self.writeString(json)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(59)
        self.writeVInt(-12)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString("8Hacc")
        self.writeVInt(0)  # name set
        self.writeInt(0)
        self.writeInt(0)
        self.writeVInt(100)
        self.writeVInt(0)  # battle pass tokens
        self.writeInt(0)
        self.writeVInt(0)  # gems
        self.writeVInt(99998)
        self.writeVInt(0)
        self.writeVInt(99997)  # Squad League
        self.writeVInt(3)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeVInt(300001)
        self.writeVInt(1)  # wtfff
        self.writeVInt(500000)  # Coins
        self.writeVInt(0)
        self.writeVInt(300004)
        self.writeVInt(1)
        self.writeVInt(99999)
        self.writeVInt(0)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeVInt(400002)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(400004)
        self.writeVInt(5)
        self.writeVInt(1000)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

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
        "a": 1337,
        "bLimit": true,
        "dd": 5200003,
        "d": 800002
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
        "c": 1000,
        "a": 1,
        "bLimit": true,
        "dd": 5200024,
        "d": 4500000,
        "cr": 300012
      },
      {
        "id": 10,
        "c": 1500,
        "a": 1,
        "bLimit": true,
        "dd": 5200019,
        "d": 5500004,
        "cr": 300012
      },
      {
        "id": 9,
        "c": 1500,
        "a": 1,
        "bLimit": true,
        "dd": 5200019,
        "d": 5500067,
        "cr": 300012
      }
    ],
    "t": {
      "t": 33518015982
    }
  },
  "eventManager": {
    "purchaseCounts": {}
  },
  "tick": 33517122184,
  "global_t": 33517115968,
  "rnd": 1399183669,
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
  "ver": 5,
  "gemRew": [
    6200000,
    6200002,
    6200000,
    6200002,
    6200002,
    6200000,
    6200008,
    6200000,
    6200008,
    6200001,
    6200003,
    6200001,
    6200003,
    6200001,
    6200003,
    6200001
  ],
  "gemT": {
    "t": 10
  },
  "lootLimitT": {
    "t": 10
  },
  "lootLimitUnused": 20000,
  "plazaRewardT": {
    "t": 20
  },
  "plazaChestT": {
    "t": 20
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
      5000012
    ]
  },
  "pProg": 1,
  "sEvent": 2
}'''