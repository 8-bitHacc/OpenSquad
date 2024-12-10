from Classes.Logic.LogicCompressedString import LogicCompressedString
from Classes.Logic.Reflector.LogicRawInReflector import LogicRawInReflector
from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Utilities.Debugger import Debugger

class EndClientTurnMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)
        self.compressed: bytes = None
        self.accountID: list = [0, 0]
        self.checksum: int = 0
        self.commandsCount: int = 0

    def decode(self, receiver):
        compressedString = LogicCompressedString()
        self.compressed = compressedString.decode(self)
        self.accountID = self.readLongLong()
        self.checksum = self.readInt()

        self.commandsCount = self.readVInt()
        if self.commandsCount > 512:
            Debugger.error("EndClientTurn::decode() command count is too high! (%d)".format(self.commandsCount))

        for x in range(self.commandsCount):
            print(f"received commandId: {self.readVInt()}")
            commandDecode = LogicRawInReflector(self)
            print(commandDecode.reflectLong(0, 0, 0, "t", 0))
            print(commandDecode.reflectLong(0, 0, 0,"g", 0))
            print(commandDecode.reflectLong(0, 0, 0, "aid", 0))

    def getMessageType(self):
        return 16543