from Classes.Protocol.Commands.LogicCommand import LogicCommand

class LogicUnlockCharacterCommand(LogicCommand):
    def __init__(self, payload):
        super().__init__(payload)
        self.character: int = 0

    def decode(self, byteStream):
        raw = super().decode(byteStream)
        self.character = raw.reflectReflectablePointerBase("character", 0)
        raw.destruct()

    def execute(self, receiver):
        receiver["Player"].UnlockedCharacters.append({"id": self.character})

    def getCommandType(self):
        return 531