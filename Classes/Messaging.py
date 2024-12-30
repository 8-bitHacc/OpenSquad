import traceback
from Classes.Utilities.ClientManager import ClientManager
from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Networking.PepperEncrypter import PepperEncrypter, PepperState
from threading import Lock

class Messaging:
    def __init__(self):
        self.PepperCrypto: PepperEncrypter = PepperEncrypter()
        self.Mutex: Lock = Lock()

    def readHeader(self, payloadBytes) -> tuple:
        return int.from_bytes(payloadBytes[:2], 'big', signed=True), int.from_bytes(payloadBytes[2:5], 'big', signed=True)

    def writeHeader(self, packet: PiranhaMessage):
        header = (packet.getMessageType().to_bytes(2, 'big', signed=True)) + (len(packet.payload).to_bytes(3, 'big', signed=True)) + (packet.packetVersion.to_bytes(2, 'big', signed=True))
        return header

    def send(self, receiver=None, packet: PiranhaMessage = PiranhaMessage(b''), SpecificUsersID = None):
        """
        Sends a packet to the client\n
            receiver -> Dict[Connection, PlayerInstance]\n
            packets -> PiranhaMessage or a child of it
        """
        if packet.payload != b"":
            packet.clear()

        messageID = packet.getMessageType()

        if packet.isClientToServerMessage():
            # execute deadly weapons.. (would like to send CryptoErrorMessage for mega troll)
            print("[Messaging::send] You can't send client packets!")
            return

        if receiver is not None and self.PepperCrypto.state == PepperState.PEPPER_AUTH:
            if messageID not in [20100, 20103]:
                receiver["ClientConnection"].disconnect()
                return

        try:
            if SpecificUsersID is None:
                if receiver is not None:
                    packet.encode(receiver)
                else:
                    print("RECEIVER NULL")

                with self.Mutex:
                    packet.payload = self.PepperCrypto.encrypt(messageID, packet.payload)
                    try:
                        receiver["ClientConnection"].client.send(self.writeHeader(packet) + packet.payload)
                    except BrokenPipeError:
                        receiver["ClientConnection"].isAlive = False
                        ClientManager.removeClient(receiver["ClientConnection"].player.SessionKey)
            else:      
                Sessions = []
                if not isinstance(SpecificUsersID[0], int):
                    for player in SpecificUsersID[0]:
                        try:
                            SessionData = ClientManager.checkForSession(player[SpecificUsersID[1]])[1]
                        except:
                            SessionData = ClientManager.checkForSession(getattr(player, SpecificUsersID[1]))[1]
                                
                        Sessions.append(SessionData)
                else:
                    SessionData = ClientManager.checkForSession(SpecificUsersID)[1]
                    Sessions.append(SessionData)
                
                for sessiondata in Sessions:
                    if sessiondata is not None:
                        packet.clear()
                        userReceiver = {"ClientConnection": sessiondata["Connection"], "Player": sessiondata["Connection"].player}
                        packet.encode(userReceiver)

                        userConn = sessiondata["Connection"]
                        with userConn.messaging.Mutex:
                            packet.payload = userConn.messaging.PepperCrypto.encrypt(messageID, packet.payload)
                            try:
                                userConn.client.send(self.writeHeader(packet) + packet.payload)
                            except BrokenPipeError:
                                ClientManager.removeClient(sessiondata["SessionKey"])
                                userConn.isAlive = False

            print(f"MessageID: {messageID}, {packet.__class__.__name__} sent")

        except:
            traceback.print_exc()

    def getPepperCrypto(self) -> PepperEncrypter:
        return self.PepperCrypto
    
    def getMutex(self) -> Lock:
        return self.Mutex