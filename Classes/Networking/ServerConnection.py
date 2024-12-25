import socket
from Classes.Networking.Connection import Connection
from Classes.Protocol.LogicLaserMessageFactory import LogicLaserMessageFactory
from Classes.Protocol.LogicCommandManager import LogicCommandManager
from Classes.Streams.StreamEntryFactory import StreamEntryFactory

class ServerConnection:
    def __init__(self, bindAddress):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        count = LogicLaserMessageFactory.loadAllMessages()
        print(f"[LogicLaserMessageFactory::] {count} messages loaded")

        count = LogicCommandManager.loadAllCommands()
        print(f"[LogicCommandManager::] {count} commands loaded")

        count = StreamEntryFactory.loadAllEntries()
        print(f"[StreamEntryFactory::] {count} streams loaded")

        self.setup(bindAddress)

    def setup(self, bindAddress):
        self.server.bind(bindAddress)

        self.server.listen()
        print(f"Listening for new Connections at {bindAddress[0]} and Port {bindAddress[1]}...")
        while True:
            serverSocket, clientAddress = self.server.accept()
            print('grrrr')

            if clientAddress[0] != "20.81.184.218":
                print("New Connection from a Client!")
                Connection(serverSocket, clientAddress, self).start()