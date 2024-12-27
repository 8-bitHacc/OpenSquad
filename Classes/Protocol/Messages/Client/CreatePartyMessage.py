from Classes.Protocol.Messages.Server.PartyMemberJoinedMessage import PartyMemberJoinedMessage
from Classes.Protocol.PiranhaMessage import PiranhaMessage

class CreatePartyMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)

    def execute(self, receiver):
        c = PartyMemberJoinedMessage()
        receiver["ClientConnection"].messaging.send(receiver, c)

    def getMessageType(self) -> int:
        return 14718