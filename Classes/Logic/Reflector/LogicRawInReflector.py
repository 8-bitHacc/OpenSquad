from Classes.Logic.Reflectable.LogicReflectable import LogicReflectable
from Classes.Logic.Reflectable.LogicReflectableFactory import LogicReflectableFactory
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
        # NOTE: Everdale doesn't read exitArray in raw, empty in squad too
        # return self.byteStream.readInt8() == 105
        pass

    def reflectNextObject(self) -> bool:
        return self.byteStream.readInt8() == 102

    def reflectNextInt(self, value: int) -> int:
        return self.byteStream.readVInt()

    def reflectNextBool(self, value: bool) -> bool:
        return self.byteStream.readBoolean()

    def reflectNextReflectable(self, reflectableType: int):
        hasReflectable: bool = self.byteStream.readBoolean()
        if hasReflectable:
            reflectableId: int = self.byteStream.readVInt()

            if reflectableId != reflectableType:
                Debugger.error("LogicRawInReflector::reflectNextReflectablePointer(): required type mismatch")
            else:
                ref: LogicReflectable = LogicReflectableFactory.createReflectable(reflectableType)
        else:
            pass

    # TODO: Pss, do this! hm why


    def reflectReflectablePointerBase(self, objectName: str, value: int):
        return self.byteStream.readVInt() # LogicRawInReflector + 8 init value = LogicReflector::sm_pDefaultReflectableIdMap