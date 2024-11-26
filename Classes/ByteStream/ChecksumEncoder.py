from Classes.Utilities.Debugger import Debugger
from Classes.ByteStream.LogicStringUtil import LogicStringUtil
from Classes.Logic.Defs import Defs
from Classes.Logic.LogicLong import LogicLong

class ChecksumEncoder:
    def __init__(self):
        self.result = None
        self.result8 = 0
        self.result12 = 0
        self.result4 = True

    def destruct(self):
        self.result8 = 0 # *(_DWORD *)(result + 8) = 0;
        self.result12 = 0 # *(_DWORD *)(result + 12) = 0;
        self.result4 = True # *(_BYTE *)(result + 4) = 1;
    
    def isCheckSumOnlyMode(self):
        return True # return 1;
    
    def writeStringReference(self, a2):
        self.result = LogicStringUtil.getByteLength(a2) + Defs.__ROR4__(self, self.result8, 31) + 38
        self.result8 = self.result
        return self.result

    def writeFilteredStringReference(self):
        return Debugger.log("error", "Function not implemented")
    
    def writeFilteredString(self):
        return self.writeFilteredStringReference()
    
    def writeString(self, string):
        v3 = Defs.__ROR4__(self, self.result8, 31)
        if string:
            result = v3 + LogicStringUtil.getByteLength(string) + 28
            self.result8 = result
        else:
            result = v3 + 27
            self.result8 = v3 + 27
        return result
    
    def writeBoolean(self, a2):
        v2 = 7
        if a2:
            v2 = 13
        self.result8 = v2 + Defs.__ROR4__(self, self.result8, 31)
        return a2

    
    def writeInt(self, value):
        self.result8 = value + Defs.__ROR4__(self, self.result8, 31) + 9
        return self.result8
    
    def writeInt8(self, value):
        v3 = value
        if value + 0x80 > 0x100:
            Debugger.log("error", "Error occured at ChecksumEncoder::writeInt8")
        result = Defs.__ROR4__(self, self.result8, 31) + v3 + 11
        self.result8 = result
        return self.result
    
    def writeInt16(self, value):
        v3 = value
        if value + 0x8000 > 0x10000:
            Debugger.log("error", "Error occured at ChecksumEncoder::writeInt16")
        result = Defs.__ROR4__(self, self.result8, 31) + v3 + 19
        self.result8 = result
        return result
    
    def writeInt24(self, value):
        if value + 0x800000 > 0x1000000:
            Debugger.log("error", "Error occured at ChecksumEncoder::writeInt24")
        result = (value & 0xFFFFFF) + Defs.__ROR4__(self, self.result8, 31) + 21
        self.result8 = result
        return result

    def writeBytes(self, a2, a3):
        if a2: integer = a3 + 38
        else: integer = 37
        self.result8 = Defs.__ROR4__(self, self.result8, 31)
        return self.result8
    
    def writeByte(self, a2):
        self.result8 = Defs.__ROR4__(self, self.result8, 31) + a2 + 11
        return self.result8
    
    def writeShort(self, a2):
        self.result8 = Defs.__ROR4__(self, self.result8, 31) + a2 + 19
        return self.result8
    
    def writeVInt(self, a2):
        self.result8 = a2 + Defs.__ROR4__(self, self.result8, 31) + 33
        return self.result8
    
    def writeLongLong(self, a2, a3):
        v6 = LogicLong.getHigherInt(self, a2)
        result = LogicLong.getLowerInt(self, a3) + Defs.__ROR4__(self, v6 + Defs.__ROR4__(self, self.result8, 31) + 67, 31) + 91
        self.result8 = result
        return result
    
    def writeLong(self, a2):
        LogicLong.encode(a2, self)


    # Last function
    def isByteStream(self):
        return False # return 0;
    
    def enableChecksum(self, a2):
        if not self.result4 or a2:
            if not self.result4:
                if a2:
                    self.result8 = self.result12
            self.result4 = a2
        else:
            self.result12 = self.result8
            self.result4 = False
    
    def equals(self, a2):
        if not a2:
            return False
        
        v3 = self.result8 # self.result8 (which is 0) or just 8?
        v4 = self.result8 # same for this
        
        if not a2.result4 == True:
            v4 = a2.result12

        if not self.result4 == True:
            v3 = self.result12
        
        return v3 == v4

    def hashCode(self):
        Debugger.log("warning", "str_1_c5d0ab59_de2c_446f_a430_563f8653b1ef_12802")
        return 42
    
    def getChecksum(self):
        # v1 = self.result8

        if not self.result4 == True:
            v1 = self.result12
        
        return v1
    
    def resetChecksum(self): # self as result
        result = self.result8 = 0
        return result
        
