from Classes.Logic.Reflectable.LogicTimeObject import LogicTimeObject
from Classes.Utilities.Preloader import Preloader
from Classes.Logic.Reflector.LogicJSONOutReflector import LogicJSONOutReflector

class LogicShopEntry:

    @classmethod
    def reflect(cls, reflector: LogicJSONOutReflector) -> None:
        reflector.reflectObject("shop")

        offers = Preloader.offers
        reflector.reflectInt(len(offers), "id", 0)

        if reflector.reflectArray(len(offers.get("special", [])), "special", False) != 0:
            for offer in offers["special"]: cls.reflectOffer(reflector, offer)
            reflector.reflectExitArray()

        if reflector.reflectArray(len(offers.get("i", [])), "i", False) != 0:
            for offer in offers["i"]: cls.reflectOffer(reflector, offer)
            reflector.reflectExitArray()

        if reflector.reflectArray(len(offers.get("e", [])), "e", False) != 0:
            for offer in offers["e"]: cls.reflectOffer(reflector, offer)
            reflector.reflectExitArray()

        if reflector.reflectArray(len(offers.get("s", [])), "s", False) != 0:
            for offer in offers["s"]: cls.reflectOffer(reflector, offer)
            reflector.reflectExitArray()

        LogicTimeObject.reflect(reflector, 1000)

        reflector.reflectExitObject()

    @classmethod
    def reflectOffer(cls, reflector: LogicJSONOutReflector, offer: dict) -> None:
        # TODO: Test
        reflector.reflectInt(offer["id"], "id", 0)
        reflector.reflectInt(offer.get("cost", 0), "c", 0)
        reflector.reflectInt(offer.get("amount", 0), "a", 0)
        reflector.reflectBool(offer.get("bLimit", False), "bLimit", False)
        reflector.reflectInt(offer.get("dd", 0), "dd", 0)
        reflector.reflectInt(offer.get("d", 0), "d", 0)
        reflector.reflectInt(offer.get("cr", 3000000), "cr", 3000000)
        reflector.currentArrayIndex += 1