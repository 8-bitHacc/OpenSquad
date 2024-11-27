import unittest
from Classes.Logic.Reflector.LogicRawInReflector import LogicRawInReflector
from Classes.ByteStream.ByteStream import ByteStream


class RawInReflectorTest(unittest.TestCase):
    def testReadComplex(self):
        payload = bytes.fromhex("00 00 00 07 FE 53 FA C4 00 00 00 04 00 0A 13 41 04 E2 6A B8 68 01 71 68 0C 00 01 02 04 05 08 "
                      "23 2C 8B 01 07 A0 01 8B 04 69 02 00 00 00 22 45 78 70 4C 65 61 67 75 65 47 72 61 73 73 6C 61 "
                      "6E 64 73 5F 73 6F 6C 6F 5F 33 39 38 31 39 36 37 36 39 01 00 00 00 07 FE 53 FC 2C 00 A1 EE 6D "
                      "72 69 01 66 68 00 67 00")
        bytestream: ByteStream = ByteStream(payload)
        reflector: LogicRawInReflector = LogicRawInReflector(bytestream)

        unk1: int = bytestream.readLongLong()
        unk2: int = bytestream.readLongLong()
        unk3: int = bytestream.readInt()
        print(f"unk1 {unk1}, unk2 {unk2}, unk3 {unk3}")

        wArrayLen: int = reflector.reflectArray(-1, "w")
        print(f"w Array, len {wArrayLen}")
        for i in range(wArrayLen):
            print("reflectNextReflectable")
            if bytestream.readInt8() == 113:
                unkArrayLen: int = reflector.reflectArray(-1, "unk")
                print(f"unkArrayLen {unkArrayLen}")
                # skip
                bytestream.offset += 0xF
                if reflector.reflectExitArray(): print("exit unk Array")
                # ends at offset 0x5D
                bytestream.offset += 0x34
                if bytestream.readInt8() == 114:
                    print("exit Reflectable")
                    break
        if reflector.reflectExitArray(): print("Exit w Array")

        # offset 0x60
        print("dm Array")
        reflector.reflectObjectOptional("dm", True)






