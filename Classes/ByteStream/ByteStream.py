from Classes.ByteStream.LogicStringUtil import LogicStringUtil
from Classes.Utilities.Debugger import Debugger
from Classes.ByteStream.ByteStreamHelper import ByteStreamHelper
from Classes.Logic.LogicLong import LogicLong


class ByteStream:
    def __init__(self, payload):
        self.payload = payload  # 4, Buffer
        self.messageLength = len(self.payload)  # 20, Length
        self.offset = 0  # 16, Offset
        self.bitoffset = 0  # 6, Bitoffset

    def destruct(self):
        self.payload = None
        self.messageLength = 0
        self.offset = 0
        self.bitoffset = 0

    def isCheckSumOnlyMode(self):
        return False  # return 0;

    def writeHexa(self, data):
        if data:
            if data.startswith('0x'):
                data = data[2:]
            base = bytes.fromhex(''.join(data.split()).replace(' ', ''))
            print(base)
            self.payload += base
            self.offset += len(base)

    # WIP TODO: writeStringReference
    def writeStringReference(self, string=""):
        # super().writeStringReference(string)
        self.bitoffset = 0
        v4 = LogicStringUtil.getBytes(string)
        v6 = LogicStringUtil.getByteLength(v4)
        if v6 < 900001:
            self.writeIntToByteArray(v6)
            self.payload += v4
            self.offset += v6
        else:
            Debugger.log("warn", "ByteStream::writeStringReference invalid string length %d".format(v6))
            self.writeIntToByteArray(-1)

    # TODO: writeString
    def writeString(self, string=None):
        # super().writeString(string)
        if string is not None:
            v4 = LogicStringUtil.getBytes(string)
            v6 = LogicStringUtil.getByteLength(v4)
            if v6 > 900001:
                Debugger.log("warning", "ByteStream::writeString invalid string length %d".format(v6))
                ByteStream.writeIntToByteArray(self, -1)
            else:
                ByteStream.writeIntToByteArray(self, v6)
                self.payload += v4
                self.offset += v6
        else:
            ByteStream.writeIntToByteArray(self, -1)

            # TODO: writeBoolean

    def writeBoolean(self, value: bool) -> bool:
        payload = list(self.payload)
        if self.bitoffset == 0:
            self.offset += 1
            payload.append(0)
        if (value & 1) != 0:
            payload[self.offset - 1] = payload[self.offset - 1] | 1 << (self.bitoffset & 31)
        self.bitoffset = self.bitoffset + 1 & 7
        self.payload = bytes(payload)
        return value

    # TODO: writeInt
    def writeInt(self, value):
        # super().writeInt(value)
        self.writeIntToByteArray(value)

    # TODO: writeInt8
    def writeInt8(self, value):
        self.bitoffset = 0
        payload = list(self.payload)
        payload.append(value & 0xFF)
        self.payload = bytes(payload)
        self.offset += 1

    # TODO: writeInt16
    def writeInt16(self, value):
        self.bitoffset = 0
        payload = list(self.payload)
        payload.append(value >> 8 & 0xFF)
        payload.append(value & 0xFF)
        self.payload = bytes(payload)
        self.offset += 2

    # TODO: writeInt24
    def writeInt24(self, value):
        self.bitoffset = 0
        payload = list(self.payload)
        payload.append(value >> 16 & 0xFF)
        payload.append(value >> 8 & 0xFF)
        payload.append(value & 0xFF)
        self.payload = bytes(payload)
        self.offset += 3

    def writeIntLittleEndian(self, value):
        self.bitoffset = 0
        payload = list(self.payload)
        payload.append(value >> 24 & 0xFF)
        payload.append(value >> 16 & 0xFF)
        payload.append(value >> 8 & 0xFF)
        payload.append(value & 0xFF)
        self.payload = bytes(payload)
        self.offset += 4

    # TODO: writeBytes
    def writeBytes(self, values, length):
        self.bitoffset = 0
        if values != 0:
            self.writeIntToByteArray(length)
            # a4 = payload?
            self.payload += values
            self.offset += length
        else:
            self.writeIntToByteArray(-1)

    # TODO: writeByte
    def writeByte(self, value):
        self.bitoffset = 0
        payload = list(self.payload)
        payload.append(value & 0xFF)
        self.payload = bytes(payload)
        self.offset += 1

    # TODO: writeShort
    def writeShort(self, short):
        self.bitoffset = 0  # a1[6] = 0; a1 refers to the ByteStream class
        newBuffer = list(self.payload)
        newBuffer.append(short >> 8 & 0xFF)
        newBuffer.append(short & 0xFF)
        self.payload = bytes(newBuffer)
        self.offset += 2

    # TODO: writeVInt
    def writeVInt(self, value):
        # super().writeVInt(value)
        v2 = value
        self.bitoffset = 0
        data = b''

        if (v2 & 2147483648) != 0:
            if v2 >= -63:
                data += (v2 & 0x3F | 0x40).to_bytes(1, 'big', signed=False)
                self.offset += 1
            elif v2 > -8192:
                data += (v2 & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 2
            elif v2 > -1048576:
                data += (v2 & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 16) | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 3
            elif v2 > -134217727:
                data += (v2 & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 20) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 4
            else:
                data += (v2 & 0x3F | 0xC0).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 20) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 27) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 5

        else:
            if v2 <= 63:
                data += (v2 & 0x3F).to_bytes(1, 'big', signed=False)
                self.offset += 1
            elif v2 <= 0x2000:
                data += (v2 & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 2
            elif v2 <= 0x100000:
                data += (v2 & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 3
            elif v2 <= 0x7FFFFFF:
                data += (v2 & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 20) & 0x7F).to_bytes(1, 'big', signed=False)
                self.offset += 4
            else:
                data += (v2 & 0x3F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 6) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 13) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 20) & 0x7F | 0x80).to_bytes(1, 'big', signed=False)
                data += ((v2 >> 27) & 0xF).to_bytes(1, 'big', signed=False)
                self.offset += 5

        self.payload += data

    # TODO: writeVLong
    def writeVLong(self, high, low):
        raise DeprecationWarning("ByteStream::writeVLong is deprecated, use ByteStream::writeLogicLong instead.")
        # self.writeVInt(high)
        # self.writeVInt(low)
        # gay

    # TODO: writeLongLong
    def writeLongLong(self, high, low):
        # super().writeLongLong(high, low)
        logicLong = LogicLong(high, low)

        self.writeIntToByteArray(logicLong.getHigherInt())
        self.writeIntToByteArray(logicLong.getLowerInt())

    def writeLogicLong(self, high, low):
        ByteStreamHelper.encodeLogicLong(self, high, low)

    def readLogicLong(self) -> list:
        return ByteStreamHelper.decodeLogicLong(self)

    def isByteStream(self) -> bool:
        return True  # return 1;

    def getLength(self) -> int:
        if self.offset < self.messageLength:
            return self.messageLength

        return self.offset

    def getOffset(self) -> int:
        return self.offset  # return *(_DWORD *)(a1 + 16);

    def isAtEnd(self) -> bool:
        return self.offset > self.messageLength

    def clear(self, a2):
        self.offset = 0
        self.bitoffset = 0
        self.messageLength = 0
        self.payload = 0
        self.messageLength = a2
        self.payload = a2

    def writeIntToByteArray(self, value):
        self.bitoffset = 0
        payload = list(self.payload)
        payload.append(value >> 24 & 0xFF)
        payload.append(value >> 16 & 0xFF)
        payload.append(value >> 8 & 0xFF)
        payload.append(value & 0xFF)
        self.payload = bytes(payload)
        self.offset += 4

    def readVInt(self) -> int:
        self.bitoffset = 0
        b = self.payload[self.offset]
        self.offset += 1
        r = b & 0x3F
        if (b & 0x40) != 0:
            if (b & 0x80) != 0:
                b2 = self.payload[self.offset]
                self.offset += 1
                r2 = (b2 << 6) & 0x1FC0 | r
                if (b2 & 0x80) != 0:
                    b3 = self.payload[self.offset]
                    self.offset += 1
                    r3 = r2 | (b3 << 0xD) & 0xFE000
                    if (b3 & 0x80) != 0:
                        b4 = self.payload[self.offset]
                        self.offset += 1
                        r4 = r3 | (b4 << 0x14) & 0x7F00000
                        if (b4 & 0x80) != 0:
                            b5 = self.payload[self.offset]
                            self.offset += 1
                            return r4 | (b5 << 0x1B) | 0x80000000
                        else:
                            return r4 | 0xF8000000
                    else:
                        return r3 | 0xFFF00000
                else:
                    return r2 | 0xFFFFE000
            else:
                return b | 0xFFFFFFC0
        elif (b & 0x80) != 0:
            b2_ = self.payload[self.offset]
            self.offset += 1
            r |= (b2_ << 6) & 0x1FC0
            if (b2_ & 0x80) != 0:
                b3_ = self.payload[self.offset]
                self.offset += 1
                r |= (b3_ << 0xD) & 0xFE000
                if (b3_ & 0x80) != 0:
                    b4_ = self.payload[self.offset]
                    self.offset += 1
                    r |= (b4_ << 0x14) & 0x7F00000
                    if (b4_ & 0x80) != 0:
                        b5_ = self.payload[self.offset]
                        self.offset += 1
                        return r | (b5_ << 0x1B)
        return r

    def readVIntb(self):
        offset = self.offset
        self.bitoffset = 0
        v4 = offset + 1
        self.offset = offset + 1
        result = self.payload[offset] & 0x3F
        if (self.payload[offset] & 0x40) != 0:
            if (self.payload[offset] & 0x80) != 0:
                self.offset = offset + 2
                v7 = self.payload[v4]
                v8 = result & 0xFFFFE03F | ((v7 & 0x7F) << 6)
                if (v7 & 0x80) != 0:
                    self.offset = offset + 3
                    v9 = v8 & 0xFFF01FFF | ((self.payload[offset + 2] & 0x7F) << 13)
                    if (self.payload[offset + 2] & 0x80) != 0:
                        self.offset = offset + 4
                        v10 = v9 & 0xF80FFFFF | ((self.payload[offset + 3] & 0x7F) << 20)
                        if (self.payload[offset + 3] & 0x80) != 0:
                            self.offset = offset + 5
                            return v10 & 0x7FFFFFF | (self.payload[offset + 4] << 27) | 0x80000000
                        else:
                            return v10 | 0xF8000000
                    else:
                        return v9 | 0xFFF00000
                else:
                    return v8 | 0xFFFFE000
            else:
                return self.payload[offset] | 0xFFFFFFC0
        elif (self.payload[offset] & 0x80) != 0:
            self.offset = offset + 2
            v6 = self.payload[v4]
            result = result & 0xFFFFE03F | ((v6 & 0x7F) << 6)
            if (v6 & 0x80) != 0:
                self.offset = offset + 3
                result = result & 0xFFF01FFF | ((self.payload[offset + 2] & 0x7F) << 13)
                if (self.payload[offset + 2] & 0x80) != 0:
                    self.offset = offset + 4
                    result = result & 0xF80FFFFF | ((self.payload[offset + 3] & 0x7F) << 20)
                    if (self.payload[offset + 3] & 0x80) != 0:
                        self.offset = offset + 5
                        return result & 0x7FFFFFF | (self.payload[offset + 4] << 27)

        return result

    def readInt(self) -> int:
        self.bitoffset = 0
        result = (self.payload[self.offset] << 24)
        result += (self.payload[self.offset + 1] << 16)
        result += (self.payload[self.offset + 2] << 8)
        result += (self.payload[self.offset + 3])
        self.offset += 4
        return result

    def readInt8(self) -> int:
        return self.readInt()

    def readIntLittleEndian(self) -> int:
        self.bitoffset = 0
        result = (self.payload[self.offset])
        result += (self.payload[self.offset + 1] << 8)
        result += (self.payload[self.offset + 2] << 16)
        result += (self.payload[self.offset + 3] << 24)
        self.offset += 4
        return result

    def readString(self, maxLength=900000) -> str:
        self.bitoffset = 0
        length = self.readInt()
        if length <= -1:
            if length != -1:
                Debugger.log("warning", "Negative String length encountered.")
            return ''
        elif length > maxLength:
            if length == 4294967295: return ''
            Debugger.log("warning", f"Too long String encountered, length {length}, max {maxLength}")
            return ''
        result = bytes(self.payload[self.offset:self.offset + length]).decode('utf-8')
        self.offset += length
        return result

    def writeDataReference(self, High, Low=0):
        ByteStreamHelper.writeDataReference(self, High, Low)

    def readDataReference(self) -> list:
        return ByteStreamHelper.readDataReference(self)

    def readBoolean(self) -> bool:
        v1 = self.bitoffset
        v3 = self.offset + ((8 - v1) >> 3)
        self.offset = v3
        self.bitoffset = (v1 + 1) & 7
        return (1 & (1 << v1) & self.payload[self.offset - 1]) != 0

    def readBytes(self, length, max=99999) -> bytes:
        self.bitoffset = 0
        if (length & 0x80000000) != 0:
            if length != -1:
                pass
                # Debugger.log("warning", "Negative readBytes length encountered.")
        elif length <= max:
            result = self.payload[self.offset:self.offset + length]
            self.offset += length
            return bytes(result)
        else:
            Debugger.log("warning", f"readBytes too long array, max {max}")
        return b''

    def writeLong(self, long: int, long1: int):
        logicLong = LogicLong(long, long1)
        logicLong.encode(self)

    def readLong(self) -> list:
        return [self.readInt(), self.readInt()]  # High and Low

    def writeCompressedString(self, string=None):
        self.bitoffset = 0
        compressed = ByteStreamHelper.compress(self, string)
        self.payload += compressed

    def readCompressedString(self) -> str:
        return ByteStreamHelper.decompress(self)

    def readStringReference(self, max=900000) -> str:
        self.bitoffset = 0
        length = (self.payload[self.offset] << 24)
        length += (self.payload[self.offset + 1] << 16)
        length += (self.payload[self.offset + 2] << 8)
        length += (self.payload[self.offset + 3])
        self.offset += 4
        if length <= -1:
            if length != -1:
                Debugger.log("warning", "Negative String length encountered.")
            return ""
        elif length > max:
            Debugger.log("warning", f"Too long String encountered, length {length}, max {max}")
            return ""
        result = bytes(self.payload[self.offset:self.offset + length]).decode('utf-8')
        self.offset += length
        return result

    def readLongLong(self) -> list:
        self.bitoffset = 0
        high = (self.payload[self.offset] << 24)
        high += (self.payload[self.offset + 1] << 16)
        high += (self.payload[self.offset + 2] << 8)
        high += (self.payload[self.offset + 3])
        self.offset += 4
        low = (self.payload[self.offset] << 24)
        low += (self.payload[self.offset + 1] << 16)
        low += (self.payload[self.offset + 2] << 8)
        low += (self.payload[self.offset + 3])
        self.offset += 4
        return [high, low]

    def writeBattlePlayerMap(self, playerMap):
        ByteStreamHelper.writeBattlePlayerMap(self, playerMap)

    def readVLong(self):
        raise DeprecationWarning("ByteStream::readVLong is deprecated, use ByteStream::readLogicLong instead.")
        # data = {}
        # data["High"] = self.readVInt()
        # data["Low"] = self.readVInt()
        # return [data["High"], data["Low"]]

    def readBytesLength(self) -> int:
        self.bitoffset = 0
        result = (self.payload[self.offset] << 24)
        result += (self.payload[self.offset + 1] << 16)
        result += (self.payload[self.offset + 2] << 8)
        result += (self.payload[self.offset + 3])
        self.offset += 4
        return result