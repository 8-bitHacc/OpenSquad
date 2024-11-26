from Classes.Logic.LogicMath import LogicMath
from Classes.Logic.GlobalID import GlobalID

class BitStream:
    def __init__(self):
        self.bits = b''
        self.bitIndex: int = 0
        self.bitLength = len(self.bits)
        self.bitoffset = 0
    
    def writePositiveInt(self, a2: int, a3: int):
        v6 = LogicMath.clamp(a2, 0, ~(-1 << a3))

        if (v6 != a2):
            red = "\033[31m"
            reset = "\033[0m"
            print(red + f"Write to BitStream out of range! (a2: {a2}, a3: {a3})" + reset)
            return
        
        # BitStream::ensureCapacity is not needed in Python
        self.writeBits(v6, a3)
    
    def writeBits(self, a2: int, a3: int):
        if (a3 >= 1):
            for i in range(a3):
                pass