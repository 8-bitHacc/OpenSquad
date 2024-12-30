from Classes.Protocol.PiranhaMessage import PiranhaMessage

class LeaderboardMessage(PiranhaMessage):
    def __init__(self, payload=b''):
        super().__init__(payload)

    def encode(self, receiver):
        self.writeVInt(0) # Players Count

    def getMessageType(self) -> int:
        return 21264