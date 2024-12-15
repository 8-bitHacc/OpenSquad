from Classes.Logic.Reflector.LogicReflector import LogicReflector
from Classes.ByteStream import ByteStream
from Classes.Logic.LogicLong import LogicLong
from Classes.Logic.LogicRandom import LogicRandom


class LogicRawOutReflector(LogicReflector):
    def __init__(self, byteStream: ByteStream):
        self.byteStream: ByteStream = byteStream

    def destruct(self):
        self.byteStream = None

    def reflectObject(self, objectName: str):
        # NOTE: Everdale doesn't write enterObject in raw
        #self.byteStream.writeInt8(102)
        pass

    def reflectObjectOptional(self, objectName: str, a3: bool):
        self.byteStream.writeBoolean(a3)
        if a3: self.reflectObject(objectName)

    def reflectExitObject(self):
        # NOTE: for Everdale exitObject is not written??
        # self.byteStream.writeInt8(103)
        pass

    def reflectInt(self, value: int, objectName: str, a4: int):
        if value == a4:
            self.byteStream.writeBoolean(False)
        else:
            self.byteStream.writeBoolean(True)
            self.byteStream.writeVInt(value)

    def reflectBool(self, value: bool, objectName: str):
        self.byteStream.writeBoolean(value)

    def reflectLong(self, a2, highInt: int, lowInt: int, objectName: str, a6: int):
        if LogicLong.toLong(highInt, lowInt) == a6:
            self.byteStream.writeBoolean(False)
        else:
            self.byteStream.writeBoolean(True)
            self.byteStream.writeLongLong(highInt, LogicLong.toLong(highInt, lowInt))

    def reflectString(self, value: str, objectName: str, a5: str):
        if value == a5:
            self.byteStream.writeBoolean(False)
        else:
            self.byteStream.writeBoolean(True)
            self.byteStream.writeString(value)

    def reflectStringPtr(self, value: str, objectName: str):
        self.byteStream.writeString(value)

    def reflectRandom(self, rnd: LogicRandom, objectName: str):
        self.byteStream.writeInt(rnd.seed)

    def reflectIntArray(self, values: list, objectName: str):
        self.byteStream.writeVInt(len(values))
        count: int = len(values)
        if count >= 1:
            for i in range(count):
                self.byteStream.writeVInt(values[i])

    def reflectArray(self, length: int, objectName: str):
        # NOTE: Everdale doesn't write enterArray in raw
        #self.byteStream.writeInt8(104)
        return

    def reflectExitArray(self):
        # NOTE: Everdale doesn't write exitArray in raw
        #self.byteStream.writeInt8(105)
        pass

    def reflectNextObject(self):
        #self.byteStream.writeInt8(102)
        pass

    def reflectNextInt(self, value: int):
        self.byteStream.writeVInt(value)

    def reflectNextBool(self, value: bool):
        self.byteStream.writeBoolean(value)

    def reflectReflectablePointerBase(self, objectName: str, value: int = 0):
        self.byteStream.writeVInt(value) # :gene: