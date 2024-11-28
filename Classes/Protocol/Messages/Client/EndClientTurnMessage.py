from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Protocol.Messages.Server.ServerHelloMessage import ServerHelloMessage

class EndClientTurnMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)

    def decode(self, receiver):
        pass


    def execute(self, receiver):
        serverHello = ServerHelloMessage()
        receiver["ClientConnection"].messaging.send(receiver, serverHello)

    def getMessageType(self):
        return 10100
