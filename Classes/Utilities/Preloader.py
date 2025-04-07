import json

class Preloader:
    configuration: dict = None
    offers: dict = None

    @classmethod
    def preloadAll(cls):
        cls.configuration = json.loads(open("Classes/StaticData/configuration.json", "r").read())
        cls.offers = json.loads(open("Classes/StaticData/offers.json", "r").read())

    @classmethod
    def preloadItem(cls, itemName=None):
        try:
            if itemName == "Configuration":
                cls.configuration = json.loads(open("Classes/StaticData/configuration.json", "r").read())
            elif itemName == "Shop":
                cls.offers = json.loads(open("Classes/StaticData/offers.json", "r").read())
            else:
                raise FileNotFoundError

        except FileNotFoundError:
            print(f"Item {itemName} is not a valid Item")

    @classmethod
    def deleteItemData(cls, itemName=None):
        try:
            if itemName == "Configuration":
                cls.configuration = None
            elif itemName == "Shop":
                cls.offers = None
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print(f"Item {itemName} is not a valid Item")
    
    @classmethod
    def getItemData(cls, itemName):
        try:
            if itemName == "Configuration": return cls.configuration
            elif itemName == "Shop": return cls.offers
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
            "Classes/StaticData/configuration.json": "configuration",
            "Classes/StaticData/offers.json": "offers",
        }

        if path not in valid:
            return
        
        name = valid.get(path)
        data = json.loads(open(path, "r").read())
        setattr(cls, name, data)