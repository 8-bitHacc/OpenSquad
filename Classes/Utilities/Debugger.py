class Debugger:
    RED = "\033[31m"
    RESET = "\033[0m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"

    @classmethod
    def log(cls, logtype="info", text=None):
        colorCode = "\033[37m"
        if logtype.lower() == "warning": colorCode = cls.YELLOW
        elif logtype.lower() == "error": colorCode = cls.RED
        elif logtype.lower() == "info": colorCode = cls.CYAN
        print(f"{colorCode}[{logtype.upper()}] {text}{cls.RESET}")

    @classmethod
    def error(cls, text: str):
        print(f"{cls.RED}[ERROR] {text}{cls.RESET}")

    @classmethod
    def warn(cls, text: str):
        print(f"{cls.RED}[ERROR] {text}{cls.RESET}")