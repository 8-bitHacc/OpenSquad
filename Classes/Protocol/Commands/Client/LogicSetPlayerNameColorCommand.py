from Classes.Protocol.Commands.LogicCommand import LogicCommand

class LogicSetPlayerNameColorCommand(LogicCommand):
    def __init__(self, payload):
        super().__init__(payload)

    def decode(self, receiver):
        super().decode(receiver)

    def execute(self, receiver):
        pass
    
    def getCommandType(self):
        return 527
