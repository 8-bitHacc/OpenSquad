from Classes.Protocol.Commands.LogicCommand import LogicCommand

class LogicTutorialStepsPassedCommand(LogicCommand):
    def __init__(self, payload):
        super().__init__(payload)
        self.tutorialStep: int = 0

    def decode(self, byteStream):
        raw = super().decode(byteStream)
        self.tutorialStep = raw.reflectReflectablePointerBase("data", 0)
        print(f"passed tutorial step: {self.tutorialStep}")
        raw.destruct()

    def execute(self, receiver):
        pass

    def getCommandType(self):
        return 520