from Classes.Protocol.Messages.Server.BattleEventsMessage import BattleEventsMessage
from Classes.Protocol.PiranhaMessage import PiranhaMessage

class ClientInputMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)
        self.frameID: int = 0

    def decode(self, receiver):
        self.frameID = self.readInt()
        print(self.readBoolean())

    def execute(self, receiver):
        b = BattleEventsMessage()
        b.setFrameID(self.frameID)
        #receiver["ClientConnection"].messaging.send(receiver, b)

    def getMessageType(self):
        return 18853