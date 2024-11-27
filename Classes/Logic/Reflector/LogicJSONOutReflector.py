from Classes.Logic.Reflector.LogicReflector import LogicReflector
from Classes.Logic.LogicRandom import LogicRandom
from Classes.Utilities.Debugger import Debugger
from Classes.Logic.LogicLong import LogicLong


class LogicJSONOutReflector(LogicReflector):
    def __init__(self, data: any):
        """
        Create a new LogicJSONOutReflector instance
        """
        self.jsonData: any = data  # + 36
        self.stack: list = []
        self.stackCount: int = 0
        if type(data) is dict:
            self.currentObject: dict = data
            self.currentArray: list = None
        elif type(data) is list:
            self.currentObject: dict = None  # + 28
            self.currentArray: list = data  # + 32
        self.currentArrayIndex: int = 0  # + 40
        self.indexStack: list = []
        self.indexStackCount: int = 0

    def destruct(self):
        self.jsonData = None
        self.stack = None
        self.stackCount = 0
        self.indexStack = None
        self.indexStackCount = 0
        self.currentArray = None
        self.currentObject = None
        self.currentArrayIndex = 0

    def reflectObject(self, objectName: str) -> bool:
        self.beginObject(objectName)
        return True

    def reflectExitObject(self):
        self.endObject()

    def reflectInt(self, value: int, objectName: str, a4: int):
        if self.currentObject is None:
            Debugger.error("LogicJSONOutReflector: no object exists")
            if value == a4: return
        if value != a4:
            self.currentObject[objectName] = value

    def reflectBool(self, value: bool, objectName: str, a4: bool):
        if self.currentObject is None: Debugger.error("LogicJSONOutReflector: no object exists")
        if value ^ a4:
            self.currentObject[objectName] = value

    def reflectLong(self, highInt: int, lowInt: int, objectName: str, a7: int, a8: int):
        longValue: int = LogicLong.toLong(highInt, lowInt)
        defaultValue: int = LogicLong.toLong(a7, a8)
        if self.currentObject is None:
            Debugger.error("LogicJSONOutReflector: no object exists")
        if longValue != defaultValue:
            self.currentObject[objectName] = longValue

    def reflectString(self, value: str, objectName: str, a5: str):
        self.setString(objectName, value, a5)

    def reflectRandom(self, rnd: LogicRandom, objectName: str):
        seed: int = rnd.seed
        if self.currentObject is None: Debugger.error("LogicJSONOutReflector: no object exists")
        if seed == 0: return
        self.currentObject[objectName] = seed

    def reflectIntArray(self, values: list, objectName: str):
        self.beginArray(objectName)
        for value in values:
            self.reflectNextInt(value)
        self.endArray()

    def reflectArray(self, length: int, objectName: str) -> int:
        if length >= 1:
            self.beginArray(objectName)
        return length

    def reflectExitArray(self):
        self.endArray()

    def reflectNextInt(self, value: int):
        if self.currentArray is None: Debugger.error("LogicJSONOutReflector: no object exists")
        self.currentArray.append(value)

    def reflectNextBool(self, value: bool):
        if self.currentArray is None: Debugger.error("LogicJSONOutReflector: no object exists")
        self.currentArray.append(value)

    def beginObject(self, objectName: str):
        jsonObject: dict = {}
        if self.currentObject is not None:
            self.currentObject[objectName] = jsonObject
        else:
            self.currentArray.append(jsonObject)
        self.pushStack()
        self.currentObject = jsonObject

    def endObject(self):
        if self.currentObject is None: Debugger.error("endObject called while no current object exists")
        if self.stackCount <= 0: Debugger.error("Mismatched begin/end or enter/exits in LogicJSONOutReflector")
        if self.indexStackCount <= 0: Debugger.error("Mismatched begin/end or enter/exits in LogicJSONOutReflector")

        jsonObject: any = self.stack[self.stackCount - 1]
        self.stackCount -= 1
        self.stack.pop()

        self.currentArrayIndex = self.indexStack[self.indexStackCount - 1]
        self.indexStackCount -= 1
        self.indexStack.pop()

        self.currentObject = None
        self.currentArray = None

        if type(jsonObject) is dict:
            self.currentObject = jsonObject
        elif type(jsonObject) is list:
            self.currentArray = jsonObject
        else:
            Debugger.error("LogicJSONOutReflector - Unsupported object type in stack")

    def beginArray(self, objectName: str):
        jsonArray: list = []
        if self.currentObject is not None:
            self.currentObject[objectName] = jsonArray
        else:
            self.currentArray.append(jsonArray)
        self.pushStack()
        self.currentArray = jsonArray

    def endArray(self):
        if self.currentArray is None: Debugger.error("endArray called while no current array exists")
        if self.stackCount <= 0: Debugger.error("Mismatched begin/end or enter/exits in LogicJSONOutReflector")
        if self.indexStackCount <= 0: Debugger.error("Mismatched begin/end or enter/exits in LogicJSONOutReflector")
        jsonObject: any = self.stack[self.stackCount - 1]
        self.stackCount -= 1
        self.stack.pop()

        self.currentArrayIndex = self.indexStack[self.indexStackCount - 1]
        self.indexStackCount -= 1
        self.indexStack.pop()

        self.currentObject = None
        self.currentArray = None

        if type(jsonObject) is dict:
            self.currentObject = jsonObject
        elif type(jsonObject) is list:
            self.currentArray = jsonObject
        else:
            Debugger.error("LogicJSONOutReflector - Unsupported object type in stack")

    def setString(self, objectName: str, value: str, a4: str):
        if self.currentObject is None:
            Debugger.error("LogicJSONOutReflector: no object exists")
        if value != a4:
            self.currentObject[objectName] = value

    def pushStack(self):
        jsonRoot: any = self.currentObject
        if jsonRoot is not None:
            # Push object to stack
            self.stack.append(jsonRoot)
            self.stackCount += 1
        else:
            jsonRoot = self.currentArray
            # Push array to stack
            self.stack.append(jsonRoot)
            self.stackCount += 1

        # Push current index to stack
        self.indexStack.append(self.currentArrayIndex)
        self.indexStackCount += 1

        # Reset current variables
        self.currentObject = None
        self.currentArray = None
        self.currentArrayIndex = 0
