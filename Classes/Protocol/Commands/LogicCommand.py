from Classes.ByteStream.ByteStream import ByteStream

class LogicCommand(ByteStream):
    def __init__(self, payload):
        super().__init__(payload)
        self.tick = 0
        self.executionTick = 0
        self.accountID = [0, 0]

    def decode(self, byteStream):
        self.tick = byteStream.readVInt()
        self.executionTick = byteStream.readVInt()
        self.accountID = byteStream.readLogicLong()

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
    
    def setOffset(self, off: int):
        '''
        Sets the offset of the command's ByteStream instance to the specified value.
    
        Parameters:
            off (int): The new offset value to be set.
        '''
        self.offset = off
    
    def setBitoffset(self, bit: int):
        '''
        Sets the bitoffset of the command's ByteStream instance to the specified value.
    
        Parameters:
            bit (int): The new bitoffset value to be set.
        '''
        self.bitoffset = bit
    
    def setData(self, off: int, bit: int):
        '''
        Sets the offset and bitoffset of the command's ByteStream instance to the specified values.
    
        Parameters:
            off (int): The new offset value to be set.
            bit (int): The new bitoffset value to be set.
        '''
        self.offset = off
        self.bitoffset = bit