import traceback

from Classes.Protocol import PiranhaMessage
from Classes.Protocol.LogicLaserMessageFactory import LogicLaserMessageFactory

class MessageManager:
    def __init__(self, connection):
        self.connection = connection
        self.receiverDict = {"ClientConnection": connection, "Player": connection.player, "ClientSocket": connection.client}

    def receiveMessage(self, messageID: int, messagePayload):
        packet: PiranhaMessage = LogicLaserMessageFactory.createMessageByType(messageID, messagePayload)

        if packet is not None:
            try:
                if packet.isServerToClientMessage():  # Check if it is a Server Packet
                    self.connection.disconnect()

                elif packet.isClientToServerMessage():
                    try:
                        packet.decode(self.receiverDict)
                    except:
                        self.connection.disconnect()
                        traceback.print_exc()
                        return

                    packet.execute(self.receiverDict)

            except:
                traceback.print_exc()
    
    def getReceiverDict(self) -> dict:
        return self.receiverDict