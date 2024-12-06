from Classes.ByteStream.ByteStream import ByteStream
from Classes.Logic.Reflector.LogicRawInReflector import LogicRawInReflector


class LogicCommand(ByteStream):
    def __init__(self, payload):
        super().__init__(payload)
        self.tick = 0
        self.executionTick = 0
        self.accountID = [0, 0]

    def decode(self, byteStream):
        self.reflect(byteStream)

    def encode(self, receiver):
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeLogicLong(*receiver["Player"].getPlayerID())
    
    def getCommandType(self):
        return 0
    
    def clear(self):
        '''Clears the command's payload'''
        self.payload = b""
        self.messageLength = 0
        self.offset = 0
        self.bitoffset = 0

    def reflect(self, byteStream):
        rawIn = LogicRawInReflector(byteStream)
        self.tick = rawIn.reflectInt(0, "t", 0)
        self.executionTick = rawIn.reflectInt(0, "g", 0)
        self.accountID = rawIn.reflectLong(0, 0, 1, "aid", 0)
        print(self.tick, self.executionTick, self.accountID)