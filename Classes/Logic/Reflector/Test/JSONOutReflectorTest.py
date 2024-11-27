import unittest
from Classes.Logic.Reflector.LogicJSONOutReflector import LogicJSONOutReflector

class JSONOutReflectorTest(unittest.TestCase):

    def testReflectWriteObject(self):
        reflector: LogicJSONOutReflector = LogicJSONOutReflector({})
        reflector.reflectObject("test")
        reflector.reflectExitObject()
        self.assertEqual(reflector.jsonData, {'test': {}})

    def testReflectWriteInt(self):
        reflector: LogicJSONOutReflector = LogicJSONOutReflector({})
        reflector.reflectInt(69, "n", -1)
        self.assertEqual(reflector.jsonData, {'n': 69})

    def testReflectComplex(self):
        # {"cool": True, "test": [1, 2, 5], "n": 10, "entries": {"bug": True}, "nec": "HACCY"}
        reflector: LogicJSONOutReflector = LogicJSONOutReflector({})
        reflector.reflectBool(True, "cool", False)
        reflector.reflectIntArray([1, 2, 5], "test")
        reflector.reflectInt(10, "n", -1)
        reflector.reflectObject("entries")
        reflector.reflectBool(True, "bug", False)
        reflector.reflectExitObject()
        reflector.reflectString("HACCY", "nec", "")
        self.assertEqual(reflector.jsonData, {"cool": True, "test": [1, 2, 5], "n": 10, "entries": {"bug": True}, "nec": "HACCY"})

