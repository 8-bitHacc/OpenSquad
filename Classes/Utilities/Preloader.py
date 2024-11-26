import json

class Preloader:
    ConfigurationData = None

    @classmethod
    def preloadAll(cls):
        cls.ConfigurationData = json.loads(open("Classes/StaticData/Configuration.json", "r").read())

    @classmethod
    def preloadItem(cls, itemName=None):
        try:
            if itemName == "Configuration":
                cls.ConfigurationData = json.loads(open("Classes/StaticData/Configuration.json", "r").read())
            else:
                raise FileNotFoundError

        except FileNotFoundError:
            print(f"Item {itemName} is not a valid Item")

    @classmethod
    def deleteItemData(cls, itemName=None):
        try:
            if itemName == "Configuration":
                cls.ConfigurationData = None
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print(f"Item {itemName} is not a valid Item")
    
    @classmethod
    def getItemData(cls, itemName):
        try:
            if itemName == "Configuration": return cls.ConfigurationData
            else: raise FileNotFoundError

        except FileNotFoundError:
            print(f"Item {itemName} is not a valid Item")

    @classmethod
    def getItemDataByType(cls, type, item, value):
        data = cls.getItemData(type)
        for x in data:
            if x[item] == value:
                return x
        
        return {}
    
    @classmethod
    def preloadFile(cls, path: str):
        valid = {
            "Classes/StaticData/Configuration.json": "ConfigurationData",
        }

        if path not in valid:
            return
        
        name = valid.get(path)
        data = json.loads(open(path, "r").read())
        setattr(cls, name, data)