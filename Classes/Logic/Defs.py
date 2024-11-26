
class Defs:
    # Translated from IDA's defs.h file
    def __ROL__(self, value, count):
        nbits = value.__sizeof__() * 8

        if count > 0:
            count %= nbits
            high = value >> (nbits - count)
            if (high - 1) < 0:
                high & ~(high(-1) << count)
            value <<= count
            value |= high
        else:
            count = -count % nbits
            low = value << (nbits - count)
            value >>= count
            value |= low

        return value
    
    def __ROL1__(self, value, count):
        return Defs.__ROL__(self, value, count)
    
    def __ROL2__(self, value, count):
        return Defs.__ROL__(self, value, count)
    
    def __ROL4__(self, value, count):
        return Defs.__ROL__(self, value, count)
    
    def __ROL8__(self, value, count):
        return Defs.__ROL__(self, value, count)
    
    def __ROR1__(self, value, count):
        return Defs.__ROL__(self, value, -count)

    def __ROR2__(self, value, count):
        return Defs.__ROL__(self, value, -count)
    
    def __ROR4__(self, value, count):
        return Defs.__ROL__(self, value, -count)

    def __ROR8__(self, value, count):
        return Defs.__ROL__(self, value, -count)