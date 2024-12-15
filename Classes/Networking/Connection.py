import socket, time, traceback, os
from threading import Thread
from typing import Union
from Classes.Messaging import Messaging

from Classes.Instances.PlayerInstance import PlayerInstance
from Classes.Messaging import Messaging
from Classes.Protocol.LogicLaserMessageFactory import LogicLaserMessageFactory
from Classes.Utilities.ClientManager import ClientManager
from Classes.MessageManager import MessageManager

class Connection(Thread):
    def __init__(self, serverSocket: socket, address, server):
        super().__init__()
        self.client: socket = serverSocket
        self.address = address
        self.player: PlayerInstance = PlayerInstance()
        self.PacketTimeout: float = time.time()
        self.messaging: Messaging = Messaging()
        self.isAlive: bool = True
        self.serverSession = server
        self.messageManager: MessageManager = MessageManager(self)

    def recv(self, n) -> Union[bytes, bytearray]:
        data = bytearray()
        while len(data) < n:
            packet = self.client.recv(n - len(data))
            if not packet: return b''
            data.extend(packet)
        return data

    def dumpMessage(self, messageID: int, payload: bytes):
        index = sum(1 for file in os.listdir("Classes/DumpedMessages/") if str(messageID) in file)
        file = open(f"Classes/DumpedMessages/{messageID}-{index}.bin", "wb+")
        file.seek(0)
        file.write(payload)
        print(f"Dumped {messageID} into {file.name}")
        file.close()

    def run(self):
        try:
            while self.isAlive:
                PacketHeader = self.client.recv(7)
                if len(PacketHeader) >= 7:
                    Header = self.messaging.readHeader(PacketHeader)
                    self.PacketTimeout = time.time()

                    PacketID: int = Header[0]

                    PacketLength: int = Header[1]
                    PacketPayload: Union[bytes, bytearray] = self.messaging.PepperCrypto.decrypt(PacketID, bytes(self.recv(PacketLength)))

                    #if PacketID == 16543: self.dumpMessage(PacketID, PacketPayload)
                            
                    self.messageManager.receiveMessage(PacketID, PacketPayload)

                if (time.time() - self.PacketTimeout) > 7:
                    self.disconnect()
        
        except ConnectionResetError as e:
            print(e)
            self.disconnect()
        
        except ConnectionAbortedError as e:
            print(e)
            self.disconnect()
        
        except ConnectionRefusedError as e:
            print(e)
            self.disconnect()

        except ConnectionError as e:
            print(e)
            self.disconnect()

        except OSError as e:
            print(e)
            self.disconnect()

        except Exception as e:
            print(e)
            print(traceback.format_exc())

    def disconnect(self):
        self.isAlive = False
        print(f"Client disconnected! IP: {self.address[0]}")
        ClientManager.removeClient(self.player.SessionKey)
        self.client.close()