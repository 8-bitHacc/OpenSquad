from Classes.ByteStream.ByteStream import ByteStream
from Classes.Logic.Reflector.LogicRawInReflector import LogicRawInReflector
from Classes.Logic.Reflector.LogicRawOutReflector import LogicRawOutReflector


class LogicCommand(ByteStream):
    def __init__(self, payload):
        super().__init__(payload)
        self.tick: list = [0, 0]
        self.executionTick: list = [0, 0]
        self.accountID: list = [0, 0]

    def decode(self, byteStream: ByteStream) -> LogicRawInReflector:
        rawIn = LogicRawInReflector(byteStream)
        self.tick = rawIn.reflectLong(0, 0, 0, "t", 0) # Command Tick
        self.executionTick = rawIn.reflectLong(0, 0, 0, "g", 0)  # Execution Tick
        self.accountID = rawIn.reflectLong(0, 0, 0, "aid", 0) # AccountID
        return rawIn

    def encode(self, receiver: dict)  -> None:
        """Encodes the command header. (Squad uses reflection for it)"""
        rawOut = LogicRawOutReflector(self)
        rawOut.reflectLong(0, self.tick[0], self.tick[1], "t", 0)
        rawOut.reflectLong(0, self.executionTick[0], self.executionTick[1], "g", 0)
        rawOut.reflectLong(0, self.accountID[0], self.accountID[1], "aid", 0)
        rawOut.destruct()
    
    def getCommandType(self) -> int:
        return 0
    
    def clear(self) -> None:
        """Clears the command's payload"""
        self.payload = b""
        self.messageLength = 0
        self.offset = 0
        self.bitoffset = 0

    def reflect(self, reflector: LogicRawOutReflector | LogicRawInReflector, receiver: dict) -> None:
        """Encodes additional data useful to the client using reflection functions."""
        pass