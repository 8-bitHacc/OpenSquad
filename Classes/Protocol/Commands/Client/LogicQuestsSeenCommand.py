from Classes.Protocol.Commands.LogicCommand import LogicCommand

class LogicQuestsSeenCommand(LogicCommand):
    def __init__(self, payload):
        super().__init__(payload)
        self.questID: int = 0

    def decode(self, byteStream):
        super().decode(byteStream)
        self.questID = byteStream.readVInt()
        print(f"Quest seen: {self.questID}")

    def execute(self, receiver):
        pass

    def getCommandType(self):
        return 523