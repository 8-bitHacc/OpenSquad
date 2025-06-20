from Classes.Logic.String import String

class LogicStringUtil:

    @staticmethod
    def getByteLength(a2: str):
        return len(a2)

    @staticmethod
    def getBytes(a2: str):
        if not isinstance(a2, str): return b""
        return a2.encode()