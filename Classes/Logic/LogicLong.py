class LogicLong:
    def __init__(self, high: int = 0, low: int = 0):
        self.highID = high
        self.lowID = low

    def decode(self, bytestream):
        self.highID = bytestream.readInt()
        self.lowID = bytestream.readInt()

    def encode(self, bytestream):
        bytestream.writeInt(self.highID)
        bytestream.writeInt(self.lowID)

    def getHigherInt(self) -> int:
        return self.highID

    def getLowerInt(self) -> int:
        return self.lowID

    def getLong(self):
        result = self.lowID
        if result >> 31 == -1:
            return result | 0x80000000
        return result

    def greaterThan(self, high, low):
        result = False
        if high and low:
            result = True
            if self.highID <= high:
                result = False
                if self.highID == high:
                    return self.lowID > low
                
        return result

    def hashCode(self):
        return 31 * self.highID + self.lowID

    def isZero(self):
        if not self.lowID: return self.highID == 0
        else: return False