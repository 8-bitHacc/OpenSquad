from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Protocol.Messages.Server.LeaderboardMessage import LeaderboardMessage

class GetGlobalLeaderboardMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)

    def execute(self, receiver):
        lb = LeaderboardMessage()
        receiver["ClientConnection"].messaging.send(receiver, lb)

    def getMessageType(self) -> int:
        return 12184