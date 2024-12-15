from Classes.Logic.Reflector.LogicReflector import LogicReflector
from Classes.ByteStream import ByteStream
from Classes.Logic.LogicRandom import LogicRandom
from Classes.Utilities.Debugger import Debugger

class LogicRawInReflector(LogicReflector):
    def __init__(self, byteStream: ByteStream):
        self.byteStream: ByteStream = byteStream

    def destruct(self):
        self.byteStream = None

    def reflectObject(self, objectName: str) -> bool:
        # Squad has it as return 1;
        return True

    def reflectObjectOptional(self, objectName: str, a3: bool):
        if self.byteStream.readBoolean():
            self.reflectObject(objectName)

    def reflectExitObject(self) -> bool:
        # NOTE: for Everdale (Squad too) exitObject is not read, it's a blank sub (nullsub)??
        # return self.byteStream.readInt8() == 103
        pass

    def reflectInt(self, value: int, objectName: str, a4: int) -> int:
        if self.byteStream.readBoolean():
            return self.byteStream.readVInt()
        else: return a4

    def reflectBool(self, value: bool, objectName: str) -> bool:
        return self.byteStream.readBoolean()

    def reflectLong(self, a2, highInt: int, lowInt: int, objectName: str, a6: int) -> int:
        if self.byteStream.readBoolean():
            return self.byteStream.readLongLong()
        else: return a6

    def reflectString(self, value: str, objectName: str, a5: str) -> str:
        if self.byteStream.readBoolean():
            return self.byteStream.readString()
        else: return a5

    def reflectRandom(self, rnd: LogicRandom, objectName: str):
        rnd.setIteratedRandomSeed(self.byteStream.readInt())

    def reflectIntArray(self, values: list, objectName: str) -> list:
        intArray: list = []
        count: int = self.byteStream.readVInt()
        if count >= 0xFFFFFF: Debugger.error("LogicRawInReflector::reflectIntArray invalid count")
        if count >= 1:
            for i in range(count):
                intArray.append(self.byteStream.readVInt())

    def reflectArray(self, length: int, objectName: str) -> int:
        return 1

    def reflectExitArray(self) -> bool:
        # NOTE: Everdale doesn't read exitArray in raw
        # return self.byteStream.readInt8() == 105
        pass

    def reflectNextObject(self) -> bool:
        return self.byteStream.readInt8() == 102

    def reflectNextInt(self, value: int) -> int:
        return self.byteStream.readVInt()

    def reflectNextBool(self, value: bool) -> bool:
        return self.byteStream.readBoolean()

    def reflectNextReflectable(self, reflectable, reflectableType: int):
        v6: int = self.byteStream.readInt8()
        if v6 == 113:
            if reflectableType == -1:
                reflectableType = self.byteStream.readVInt()
            print(f"reflectableType {reflectableType}")
            if self.byteStream.readInt8() == 114:
                return 1
        if v6 == 112:
            return 0

    def reflectReflectablePointerBase(self, objectName: str, value: int):
        return self.byteStream.readVInt() # LogicRawInReflector + 8 init value = LogicReflector::sm_pDefaultReflectableIdMap