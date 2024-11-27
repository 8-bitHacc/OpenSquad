import unittest
from Classes.Logic.Reflector.LogicJSONInReflector import LogicJSONInReflector


class JSONInReflectorTest(unittest.TestCase):

    def testCreation(self):
        testJson: dict = {"cool": True, "test": [1, 2, 5], "n": 10, "entries": {"bug": True}, "nec": "HACCY"}
        reflector: LogicJSONInReflector = LogicJSONInReflector(testJson)
        self.assertTrue(reflector.jsonData, testJson)
        self.assertIsNotNone(reflector.currentObject)

    def testReflectObjectEnter(self):
        testJson: dict = {"cool": True, "test": [1, 2, 5], "n": 10, "entries": {"bug": True}, "nec": "HACCY"}
        reflector: LogicJSONInReflector = LogicJSONInReflector(testJson)
        self.assertTrue(reflector.reflectObject("entries"))

    def testReflectObjectEnterAndReflectBool(self):
        testJson: dict = {"cool": True, "test": [1, 2, 5], "n": 10, "entries": {"bug": True}, "nec": "HACCY"}
        reflector: LogicJSONInReflector = LogicJSONInReflector(testJson)
        self.assertTrue(reflector.reflectObject("entries"))
        self.assertTrue(reflector.reflectBool("bug", False))

    def testReflectObjectExitAndReflectArray(self):
        testJson: dict = {"cool": True, "test": [1, 2, 5], "n": 10, "entries": {"bug": True}, "nec": "HACCY"}
        reflector: LogicJSONInReflector = LogicJSONInReflector(testJson)
        self.assertTrue(reflector.reflectObject("entries"))
        reflector.reflectExitObject()
        self.assertEqual(reflector.reflectArray(0, "test"), 3)

    def testReflectInt(self):
        testJson: dict = {"cool": True, "test": [1, 2, 5], "n": 10, "entries": {"bug": True}, "nec": "HACCY"}
        reflector: LogicJSONInReflector = LogicJSONInReflector(testJson)
        self.assertEqual(reflector.reflectInt("n", -1), 10)

    def testReflectString(self):
        testJson: dict = {"cool": True, "test": [1, 2, 5], "n": 10, "entries": {"bug": True}, "nec": "HACCY"}
        reflector: LogicJSONInReflector = LogicJSONInReflector(testJson)
        self.assertEqual(reflector.reflectString("nec"), "HACCY")

    def testReflectIntArray(self):
        testJson: dict = {"cool": True, "test": [1, 2, 5], "n": 10, "entries": {"bug": True}, "nec": "HACCY"}
        reflector: LogicJSONInReflector = LogicJSONInReflector(testJson)
        intArray: list = reflector.reflectIntArray("test")
        self.assertEqual(intArray, [1, 2, 5])
