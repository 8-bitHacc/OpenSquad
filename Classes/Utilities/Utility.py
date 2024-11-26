import random, string, json, os, inspect
from types import ModuleType

from Classes.Streams.StreamEntry import StreamEntry
from importlib.util import spec_from_file_location, module_from_spec
from typing import Any

class Utility:

    @staticmethod
    def loadModule(path: str):
        dirname = path.replace("/", ".").removesuffix(".py")
        spec = spec_from_file_location(dirname, path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    
    @staticmethod
    def getVariables(path: str) -> list[tuple[ModuleType, str, Any]] | list[Any]:
        try:
            module = Utility.loadModule(path)
            return [(module, x, getattr(module, x)) for x in dir(module)]
        except:
            return []
    
    @staticmethod
    def loadLogic(path: str):
        for module, name, attr in Utility.getVariables(path):
            if path.removesuffix(".py").endswith(name):
                if isinstance(attr, type):
                    return attr

    @staticmethod          
    def loadStream(path: str):
        for module, name, attr in Utility.getVariables(path):
            if path.removesuffix(".py").endswith(name):
                if isinstance(attr, type):
                    if issubclass(attr, StreamEntry):
                        if hasattr(attr, "getStreamEntryType"):
                            return attr
    
    @staticmethod
    def getSource(attribute):
        
        try:
            return inspect.getsourcefile(attribute).replace("\\", "/")
        except:
            return None
    
    @staticmethod
    def items(folder: str):

        try:
            return [f"{folder}/{x}" for x in os.listdir(folder)]
        except:
            return []

    @staticmethod
    def createRandomToken(length: int = 40):
        Token = "".join(random.choice(string.ascii_letters + string.digits) for i in range(length))
        return Token

    @staticmethod
    def createRandomLongID():
        HighID = int("".join([str(random.randint(0, 9)) for _ in range(1)]))
        LowID = int("".join([str(random.randint(0, 9)) for _ in range(9)]))
        return [HighID, LowID]
    
    @staticmethod
    def updateJSONFile(filepath, data):
        try:
            jsonString = json.dumps(data, indent=4)

            with open(filepath, "w") as file:
                file.write(jsonString)

        except (TypeError, ValueError) as e:
            print(f"Invalid JSON data: {e}")
        except Exception as e:
            print(f"Failed to update JSON File `{filepath}`: {e}")