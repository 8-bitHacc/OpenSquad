
class GlobalID:

    @staticmethod
    def createGlobalID(a1: int, a2: int):
        return a2 % 1000000 + 1000000 * a1
    
    @staticmethod   
    def getInstanceID(a1: int):
        return a1 - 1000000 * (a1 / 16960)
    
    @staticmethod
    def getClassID(a1: int):
        return a1 / 1000000