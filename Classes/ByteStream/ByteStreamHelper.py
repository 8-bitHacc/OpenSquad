from Classes.Logic.LogicLong import LogicLong
from Classes.Logic.GlobalID import GlobalID
import zlib


class ByteStreamHelper:

    # TODO: Decompress
    @staticmethod
    def decompress(byteStream):
        length = byteStream.readInt()
        if length != 4294967295:
            byteStream.readIntLittleEndian()
            return zlib.decompress(byteStream.readBytes(length - 4))
    
    @staticmethod
    def encodeLogicLong(bytestream, high: int = -1, low: int = 0):
        logiclong = LogicLong(high, low)
        bytestream.writeVInt(logiclong.getHigherInt())
        bytestream.writeVInt(logiclong.getLowerInt())
    
    @staticmethod
    def encodeLogicLongList(bytestream, longList: list):
        bytestream.writeVInt(len(longList))
        for long in longList:
            logicLong = LogicLong(*long)
            bytestream.writeVInt(logicLong.getHigherInt())
            bytestream.writeVInt(logicLong.getLowerInt())
    
    @staticmethod
    def decodeLogicLong(bytestream):
        highID = bytestream.readVInt()
        lowID = bytestream.readVInt()
        return [highID, lowID]
    
    @staticmethod
    def decodeLogicLongList(bytestream):
        longList = []
        length = bytestream.readVInt()
        if length == -1:
            return []
        
        for x in range(length):
            longList.append({"h": bytestream.readVInt(), "l": bytestream.readVInt()})
        
        return longList

    @staticmethod
    def compress(byteStream, compressedString: bytes):
        compressed = zlib.compress(compressedString)
        byteStream.writeInt(len(compressed) + 4)
        byteStream.writeIntLittleEndian(len(compressedString))
        return compressed

    # TODO: ByteStreamHelper::writeGlobalID
    @staticmethod
    def writeGlobalID(byteStream, high = 0, low = 0):
        if (low == 0 and high == 0):
            byteStream.writeVInt(0)
            return
        if (high != 0 and low == 0):
            ClassID = GlobalID.getClassID(high)
            InstanceID = GlobalID.getInstanceID(high)
            byteStream.writeVInt(ClassID)
            byteStream.writeVInt(InstanceID)
        else:
            byteStream.writeVInt(high)
            byteStream.writeVInt(low)

    @staticmethod
    def decodeIntList(byteStream):
        length = byteStream.readVInt()
        # if intlist[1] >= Length:
        intList = []
        for i in range(length):
            intList.append(byteStream.readVInt())
        return intList

    @staticmethod
    def writeDataReference(byteStream, id=0, id1=0):
        byteStream.writeVInt(id)
        if id > 0:
            byteStream.writeVInt(id1)

    @staticmethod
    def readDataReference(self):
        high = self.readVInt()

        if high > 0:
            low = self.readVInt()
        else:
            return [high, 0]
        
        return [high, low]

    @staticmethod
    def encodeIntList(byteStream, arrayData: list = []):
        byteStream.writeVInt(len(arrayData))
        for integer in arrayData:
            byteStream.writeVInt(integer)

    # TODO: LogicBattlePlayerMap::encode
    @staticmethod
    def writeBattlePlayerMap(byteStream, mapData = []):
        if byteStream.writeBoolean(mapData != []):
            raise NotImplementedError("LogicBattlePlayerMap::encode is not implemented!")
