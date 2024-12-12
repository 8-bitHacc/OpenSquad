import time
from Classes.Protocol.PiranhaMessage import PiranhaMessage

class LoginOkMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)
        self.packetVersion = 1

    def encode(self, receiver):
        self.writeLong(0, 1)  # AccountID
        self.writeLong(0, 1)  # AccountID
        self.writeString("SquadBusters")  # AccountToken
        self.writeString()  # Facebook ID in String format
        self.writeString()  # GameCenter Account Token
        self.writeInt(1)  # Server Major
        self.writeInt(145)  # Server Minor
        self.writeInt(516)  # Server Build
        self.writeInt(11)  # Unknown
        self.writeString("dev")  # Server Environment
        self.writeInt(0)  # Session Count
        self.writeInt(0)  # Play Time in Seconds
        self.writeInt(0)  # Days since Account Creation in Seconds
        self.writeString()  # Facebook AppID
        self.writeString(str(time.time()))  # Server Time
        self.writeString("1714237625000")  # Account Creation Date
        self.writeInt(0)  # Startup Cooldown in Seconds
        self.writeString()  # Google ServiceID (Google Play?)
        self.writeString("GR")  # Login Country
        self.writeString()  # KunlunID
        self.writeInt(3)
        self.writeString("https://event-assets.squadbustersgame.com")  # Event Assets URL
        self.writeString("https://game-assets.squadbustersgame.com")
        self.writeString()
        self.writeCompressedString(b'')  # Supercell ID Token
        self.writeBoolean(True)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeStringReference()

    def getMessageType(self):
        return 29125