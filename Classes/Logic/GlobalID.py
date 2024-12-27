
class GlobalID:

    @staticmethod
    def createGlobalID(a1: int, a2: int):
        return a2 % 1000000 + 1000000 * a1
    
    @staticmethod   
    def getInstanceID(a1: int) -> int:
        return a1 % 100000
    
    @staticmethod
    def getClassID(a1: int) -> int:
        return int(a1 / 100000)