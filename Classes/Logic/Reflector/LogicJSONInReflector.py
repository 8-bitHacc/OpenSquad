from Classes.Reflect.LogicReflector import LogicReflector
from Classes.LogicRandom import LogicRandom
from Classes.Debugger import Debugger
from Classes.ListUtils import getFromArray


class LogicJSONInReflector(LogicReflector):
    def __init__(self, data: any):
        """
        Create a new JSONInReflector
        """
        #  self.jsonData: dict = json.load(data)
        self.jsonData: dict = data
        self.stack: list = []
        self.stackCount: int = 0
        if type(data) is dict:
            self.currentObject: dict = data
            self.currentArray: list = None
        elif type(data) is list:
            self.currentObject: dict = None  # + [20]
            self.currentArray: list = data  # + [21]
        self.currentArrayIndex: int = 0  # + [22]
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
        if self.currentObject is not None:
            jsonObject: dict = self.currentObject.get(objectName)
            if jsonObject is not None:
                self.pushStack()
                self.currentObject = jsonObject
                return True
        else:
            jsonObject: dict = getFromArray(self.currentArray, self.currentArrayIndex)
            if jsonObject is not None:
                self.pushStack()
                self.currentObject = jsonObject
                return True
        return False

    def reflectExitObject(self):
        self.exitObject()

    def reflectInt(self, objectName: str, a4: int) -> int:
        jsonNumber: any = self.currentObject.get(objectName)
        if jsonNumber is not None:
            if type(jsonNumber) is int:
                return jsonNumber
            else: Debugger.warning(f"JSONNumber type is {type(jsonNumber)}, key {objectName}")
        else: Debugger.error("LogicJSONInReflector: no current object exists")
        return a4

    def reflectBool(self, objectName: str, a4: bool) -> bool:
        jsonBoolean: any = self.currentObject.get(objectName)
        if jsonBoolean is not None:
            if type(jsonBoolean) is bool:
                return jsonBoolean
            else: Debugger.warning(f"JSONBoolean type is {type(jsonBoolean)}, key {objectName}")
        else: Debugger.error("LogicJSONInReflector: no current object exists")
        return a4

    def reflectLong(self, objectName: str, a6: int) -> int:
        jsonNumber: any = self.currentObject.get(objectName)
        if jsonNumber is not None:
            if type(jsonNumber) is int:
                return jsonNumber
            else: Debugger.warning(f"JSONNumber type is {type(jsonNumber)}, key {objectName}")
        else: Debugger.error("LogicJSONInReflector: no current object exists")
        return a6

    def reflectString(self, objectName: str, a5: str = "") -> str:
        return self.getString(objectName, a5)

    def reflectRandom(self, rnd: LogicRandom, objectName: str):
        jsonNumber: any = self.currentObject.get(objectName)
        if jsonNumber is not None:
            if type(jsonNumber) is int:
                rnd.setIteratedRandomSeed(jsonNumber)
            else: Debugger.warning(f"JSONNumber type is {type(jsonNumber)}, key {objectName}")
        else: Debugger.error("LogicJSONInReflector: no current object exists")

    def reflectIntArray(self, objectName: str) -> list:
        result: list = []
        if self.enterArray(objectName):
            if self.currentArray is None: Debugger.error("LogicJSONInReflector: no current array exists")
            currentArraySize: int = len(self.currentArray)
            for i in range(currentArraySize):
                result.append(self.reflectNextInt())
            self.exitArray()
        return result

    def reflectArray(self, length: int, objectName: str) -> int:
        if not self.enterArray(objectName): return -1
        if self.currentArray is None: Debugger.error("LogicJSONInReflector: no current array exists")
        return len(self.currentArray)

    def reflectExitArray(self):
        self.exitArray()

    def reflectNextObject(self):
        pass

    def reflectNextInt(self, value: int = 0) -> int:
        if self.currentArray is None: Debugger.error("LogicJSONInReflector: no current array exists")
        jsonNumber: any = getFromArray(self.currentArray, self.currentArrayIndex)
        self.currentArrayIndex += 1
        if jsonNumber is not None:
            if type(jsonNumber) is int:
                return jsonNumber
            else:
                Debugger.warning(f"JSONNumber wrong type {type(jsonNumber)}, index {self.currentArrayIndex - 1}")
        return 0

    def reflectNextBool(self, value: bool = False) -> bool:
        if self.currentArray is None: Debugger.error("LogicJSONInReflector: no current array exists")
        jsonBoolean: any = getFromArray(self.currentArray, self.currentArrayIndex)
        self.currentArrayIndex += 1
        if jsonBoolean is not None:
            if type(jsonBoolean) is bool:
                return jsonBoolean
            else: Debugger.warning(f"JSONBoolean wrong type {type(jsonBoolean)}, index {self.currentArrayIndex - 1}")
        return False

    def exitObject(self):
        if self.currentObject is None: Debugger.error("exitObject called while no current object exists")
        if self.stackCount <= 0: Debugger.error("Mismatched begin/end or enter/exits in LogicJSONInReflector")
        if self.indexStackCount <= 0: Debugger.error("Mismatched begin/end or enter/exits in LogicJSONInReflector")

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
            Debugger.error("LogicJSONInReflector - Unsupported object type in stack")

    def exitArray(self):
        if self.currentArray is None: Debugger.error("exitArray called while no current array exists")
        if self.stackCount <= 0: Debugger.error("Mismatched begin/end or enter/exits in LogicJSONInReflector")
        if self.indexStackCount <= 0: Debugger.error("Mismatched begin/end or enter/exits in LogicJSONInReflector")

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
            Debugger.error("LogicJSONInReflector - Unsupported object type in stack")

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

    def getString(self, objectName: str, a4: str) -> str:
        jsonString: any = self.currentObject.get(objectName)
        if jsonString is not None:
            if type(jsonString) is str:
                return str(jsonString)
            else:
                Debugger.warning(f"JSONString type is {type(jsonString)}, key {objectName}")
        else:
            Debugger.error("LogicJSONInReflector: no current object exists")
        return a4

    def enterArray(self, objectName: str) -> bool:
        jsonObject = self.currentObject
        jsonArray: list = None
        if jsonObject is not None:
            jsonArray = self.currentObject.get(objectName)
            if type(jsonArray) is not list:
                Debugger.warning(f"JSONArray type is {type(jsonArray)}, key {objectName}")
                jsonArray = None
        else:
            jsonArray = getFromArray(self.currentArray, self.currentArrayIndex)
            if type(jsonArray) is not list:
                Debugger.warning(f"JSONArray wrong type {type(jsonArray)}, index {self.currentArrayIndex}")
                jsonArray = None
            self.currentArrayIndex += 1
        if jsonArray is not None and len(jsonArray) != 0:
            self.pushStack()
            self.currentArray = jsonArray
            return True
        return False
