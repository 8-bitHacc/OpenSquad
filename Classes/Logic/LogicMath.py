class LogicMath:
    SIN_TABLE = [0x0000, 0x0012, 0x0024, 0x0036, 0x0047, 0x0059, 0x006B, 0x007D,
            0x008F, 0x00A0, 0x00B2, 0x00C3, 0x00D5, 0x00E6, 0x00F8, 0x0109,
            0x011A, 0x012B, 0x013C, 0x014D, 0x015E, 0x016F, 0x0180, 0x0190,
            0x01A0, 0x01B1, 0x01C1, 0x01D1, 0x01E1, 0x01F0, 0x0200, 0x020F,
            0x021F, 0x022E, 0x023D, 0x024B, 0x025A, 0x0268, 0x0276, 0x0284,
            0x0292, 0x02A0, 0x02AD, 0x02BA, 0x02C7, 0x02D4, 0x02E1, 0x02ED,
            0x02F9, 0x0305, 0x0310, 0x031C, 0x0327, 0x0332, 0x033C, 0x0347,
            0x0351, 0x035B, 0x0364, 0x036E, 0x0377, 0x0380, 0x0388, 0x0390,
            0x0398, 0x03A0, 0x03A7, 0x03AF, 0x03B5, 0x03BC, 0x03C2, 0x03C8,
            0x03CE, 0x03D3, 0x03D8, 0x03DD, 0x03E2, 0x03E6, 0x03EA, 0x03ED,
            0x03F0, 0x03F3, 0x03F6, 0x03F8, 0x03FA, 0x03FC, 0x03FE, 0x03FF,
            0x03FF, 0x0400, 0x0400]
    SQRT_TABLE = [0x00, 0x10, 0x16, 0x1B, 0x20, 0x23, 0x27, 0x2A, 0x2D,
            0x30, 0x32, 0x35, 0x37, 0x39, 0x3B, 0x3D, 0x40, 0x41,
            0x43, 0x45, 0x47, 0x49, 0x4B, 0x4C, 0x4E, 0x50, 0x51,
            0x53, 0x54, 0x56, 0x57, 0x59, 0x5A, 0x5B, 0x5D, 0x5E,
            0x60, 0x61, 0x62, 0x63, 0x65, 0x66, 0x67, 0x68, 0x6A,
            0x6B, 0x6C, 0x6D, 0x6E, 0x70, 0x71, 0x72, 0x73, 0x74,
            0x75, 0x76, 0x77, 0x78, 0x79, 0x7A, 0x7B, 0x7C, 0x7D,
            0x7E, 0x80, 0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86,
            0x87, 0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F,
            0x90, 0x90, 0x91, 0x92, 0x93, 0x94, 0x95, 0x96, 0x96,
            0x97, 0x98, 0x99, 0x9A, 0x9B, 0x9B, 0x9C, 0x9D, 0x9E,
            0x9F, 0xA0, 0xA0, 0xA1, 0xA2, 0xA3, 0xA3, 0xA4, 0xA5,
            0xA6, 0xA7, 0xA7, 0xA8, 0xA9, 0xAA, 0xAA, 0xAB, 0xAC,
            0xAD, 0xAD, 0xAE, 0xAF, 0xB0, 0xB0, 0xB1, 0xB2, 0xB2,
            0xB3, 0xB4, 0xB5, 0xB5, 0xB6, 0xB7, 0xB7, 0xB8, 0xB9,
            0xB9, 0xBA, 0xBB, 0xBB, 0xBC, 0xBD, 0xBD, 0xBE, 0xBF,
            0xC0, 0xC0, 0xC1, 0xC1, 0xC2, 0xC3, 0xC3, 0xC4, 0xC5,
            0xC5, 0xC6, 0xC7, 0xC7, 0xC8, 0xC9, 0xC9, 0xCA, 0xCB,
            0xCB, 0xCC, 0xCC, 0xCD, 0xCE, 0xCE, 0xCF, 0xD0, 0xD0,
            0xD1, 0xD1, 0xD2, 0xD3, 0xD3, 0xD4, 0xD4, 0xD5, 0xD6,
            0xD6, 0xD7, 0xD7, 0xD8, 0xD9, 0xD9, 0xDA, 0xDA, 0xDB,
            0xDB, 0xDC, 0xDD, 0xDD, 0xDE, 0xDE, 0xDF, 0xE0, 0xE0,
            0xE1, 0xE1, 0xE2, 0xE2, 0xE3, 0xE3, 0xE4, 0xE5, 0xE5,
            0xE6, 0xE6, 0xE7, 0xE7, 0xE8, 0xE8, 0xE9, 0xEA, 0xEA,
            0xEB, 0xEB, 0xEC, 0xEC, 0xED, 0xED, 0xEE, 0xEE, 0xEF,
            0xF0, 0xF0, 0xF1, 0xF1, 0xF2, 0xF2, 0xF3, 0xF3, 0xF4,
            0xF4, 0xF5, 0xF5, 0xF6, 0xF6, 0xF7, 0xF7, 0xF8, 0xF8,
            0xF9, 0xF9, 0xFA, 0xFA, 0xFB, 0xFB, 0xFC, 0xFC, 0xFD,
            0xFD, 0xFE, 0xFE, 0xFF]
    ATAN_TABLE = [0x00, 0x00, 0x01, 0x01, 0x02, 0x02, 0x03, 0x03, 0x04,
            0x04, 0x04, 0x05, 0x05, 0x06, 0x06, 0x07, 0x07, 0x08,
            0x08, 0x08, 0x09, 0x09, 0x0A, 0x0A, 0x0B, 0x0B, 0x0B,
            0x0C, 0x0C, 0x0D, 0x0D, 0x0E, 0x0E, 0x0E, 0x0F, 0x0F,
            0x10, 0x10, 0x11, 0x11, 0x11, 0x12, 0x12, 0x13, 0x13,
            0x13, 0x14, 0x14, 0x15, 0x15, 0x15, 0x16, 0x16, 0x16,
            0x17, 0x17, 0x18, 0x18, 0x18, 0x19, 0x19, 0x19, 0x1A,
            0x1A, 0x1B, 0x1B, 0x1B, 0x1C, 0x1C, 0x1C, 0x1D, 0x1D,
            0x1D, 0x1E, 0x1E, 0x1E, 0x1F, 0x1F, 0x1F, 0x20, 0x20,
            0x20, 0x21, 0x21, 0x21, 0x22, 0x22, 0x22, 0x23, 0x23,
            0x23, 0x23, 0x24, 0x24, 0x24, 0x25, 0x25, 0x25, 0x25,
            0x26, 0x26, 0x26, 0x27, 0x27, 0x27, 0x27, 0x28, 0x28,
            0x28, 0x28, 0x29, 0x29, 0x29, 0x29, 0x2A, 0x2A, 0x2A,
            0x2A, 0x2B, 0x2B, 0x2B, 0x2B, 0x2C, 0x2C, 0x2C, 0x2C,
            0x2D, 0x2D, 0x2D]

    @staticmethod
    def clamp(value: int, a2: int, a3: int):
        if (value < a3):
            a3 = value
        
        if (value <= a2):
            return a2
        
        return a3
    
    @staticmethod
    def abs(result: int):
        if (result < 0):
            return -result
        
        return result
    
    @staticmethod
    def sign(a1: int):
        v1 = a1 >> 31

        if (a1 > 0):
            return 1
        
        return v1

    @staticmethod
    def sqrtApproximate(a1: int, a2: int):
        if (a1 < 0):
            a1 = -a1
        
        if (a2 < 0):
            a2 = -a2
        
        v2 = a1 < a2
        v3 = a2

        if (a1 > a2):
            a2 = a1
        
        if a2:
            v3 = a1
        
        return a2 + ((53 * v3) >> 7)
    
    @staticmethod
    def pow(a1: int, a2: int) -> int:
        if not a2:
            return 1
        
        result = 1
        v5 = False

        while not v5:
            v4 = a1 * a1

            if ((a1 & 1) == 0):
                a1 = 1
            
            result *= a1
            v5 = a2 >> 1 == 0
            a2 >>= 1
            a1 = v4
        
        return result
    
    @staticmethod
    def normalizeAngle180(a1: int):
        result = a1 % 360 + (0x168 if a1 % 360 < 0 else 0)

        if (result > 179):
            result -= 360
        
        return result
    
    @staticmethod
    def max(result: int, a2: int):
        if (result <= a2):
            return a2
        
        return result

    @staticmethod
    def cos(a1: int):
        v1 = (a1 + 90) % 360 + (0x168 if (a1 + 90) % 360 < 0 else 0)
        if v1 > 179:
            v3 = v1 - 180
            if v1 - 180 > 90:
                v3 = 360 - v1
            return LogicMath.SQRT_TABLE[v3]
        else:
            if v1 > 90:
                v1 = 180 - v1
            return LogicMath.SIN_TABLE[v1]

    @staticmethod
    def sin(a1: int):
        v1 = (a1 + 90) % 360 + (360 if (a1 + 90) % 360 < 0 else 0)
        if v1 > 179:
            v3 = v1 - 180
            if v1 - 180 > 90:
                v3 = 360 - v1
            return LogicMath.SQRT_TABLE[v3]
        else:
            if v1 > 90:
                v1 = 180 - v1
            return LogicMath.SIN_TABLE[v1]

    @staticmethod
    def sqrt(a1: int):
        if a1 < 65536:
            if a1 < 256:
                if a1 < 0:
                    return -1
                else:
                    return LogicMath.SQRT_TABLE[a1] >> 4
            else:
                if a1 < 4096:
                    if a1 < 1024:
                        v5 = (LogicMath.SQRT_TABLE + (a1 & 0xFFFFFFFC)) >> 3
                    else:
                        v5 = (LogicMath.SQRT_TABLE + ((a1 >> 2) & 0xFFFFFFFC)) >> 2
                elif a1 < 16384:
                    v5 = LogicMath.SQRT_TABLE[a1 >> 6] >> 1
                else:
                    v5 = LogicMath.SQRT_TABLE[a1 >> 8]

                result = v5 + 1
                if result * result > a1:
                    return v5
        else:
            if a1 < 268435456:
                if a1 <= 1048575:
                    v6 = 1
                    v7 = 10
                    if a1 > 262143:
                        v6 = 2
                        v7 = 12
                else:
                    v6 = 3
                    v7 = 14
                    if a1 > 4194303:
                        v6 = 4
                        v7 = 16

                v8 = ((LogicMath.SQRT_TABLE[a1 >> v7] << v6) | 1) + a1 / (LogicMath.SQRT_TABLE[a1 >> v7] << v6)
            else:
                if a1 < 268435456:
                    v3 = 5
                    v7 = 14
                    if a1 > 4194303:
                        v3 = 6
                        v4 = 20
                elif a1 < 1073741824:
                    v3 = 7
                    v4 = 22
                else:
                    result = 0xFFFF
                    if a1 == 0x7FFFFFFF: return result
                    v3 = 8
                    v4 = 24
                v9 = ((LogicMath.SQRT_TABLE[a1 >> v4] << v3) | 1) + a1 / (LogicMath.SQRT_TABLE[a1 >> v4] << v3)
                v8 = a1 / (v9 >> 1) + (v9 >> 1) + 1

            result = v8 >> 1
            if result * result > a1:
                return (v8 >> 1) - 1

        return result

    @staticmethod
    def getRotatedX(a1: int, a2: int, a3: int):
        v3 = (a3 + 90) % 360 + (0x168 if (a3 + 90) % 360 < 0 else 0)
        if v3 > 179:
            v5 = v3 - 180
            if v3 - 180 > 90:
                v5 = 360 - v3

            v4 = -LogicMath.SIN_TABLE[v5]
        else:
            if v3 > 90:
                v3 = 180 - v3

            v4 = LogicMath.SIN_TABLE[v3]

        v6 = v4 * a1
        v7 = a3 % 360 + (0x168 if a3 % 360 < 0 else 0)
        if v7 > 179:
            v9 = v7 - 180
            if v7 - 180 > 90:
                v9 = 360 - v7
            v8 = -LogicMath.SIN_TABLE[v9]
        else:
            if v7 > 90:
                v7 = 180 - v7
            v8 = LogicMath.SIN_TABLE[v7]

        return (v6 - v8 * a2) / 1024

    @staticmethod
    def getRotatedY(a1: int, a2: int, a3: int):
        v3 = a3 % 360 + (0x168 if a3 % 360 < 0 else 0)
        if v3 > 179:
            v5 = v3 - 180
            if v5 > 90:
                v5 = 360 - v3
            v4 = -LogicMath.SIN_TABLE[v5]
        else:
            if v3 > 90:
                v3 = 180 - v3
            v4 = LogicMath.SIN_TABLE[v3]
        v6 = v4 * a1
        v7 = (a3 + 90) % 360 + (0x168 if (a3 + 90) % 360 < 0 else 0)
        if v7 > 179:
            v9 = v7 - 180
            if v9 > 90:
                v9 = 360 - v7
            v8 = -LogicMath.SIN_TABLE[v9]
        else:
            if v7 > 90:
                v7 = 180 - v7
            v8 = LogicMath.SIN_TABLE[v7]
        return (v6 + v8 * a2) / 1024

    @staticmethod
    def normalizeAngle360(a1: int):
        return a1 % 360 + (0x168 if a1 % 360 < 0 else 0)