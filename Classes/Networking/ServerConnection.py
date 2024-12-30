import socket
from Classes.DataBase.SQLiteManager import SQLiteManager
from Classes.Networking.Connection import Connection
from Classes.Protocol.LogicLaserMessageFactory import LogicLaserMessageFactory
from Classes.Protocol.LogicCommandManager import LogicCommandManager

class ServerConnection:
    def __init__(self, bindAddress):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.db = SQLiteManager()
        print(f"[SQLiteManager::] Database is ready")

        count = LogicLaserMessageFactory.loadAllMessages()
        print(f"[LogicLaserMessageFactory::] {count} messages loaded")

        count = LogicCommandManager.loadAllCommands()
        print(f"[LogicCommandManager::] {count} commands loaded")

        self.setup(bindAddress)

    def setup(self, bindAddress):
        self.server.bind(bindAddress)

        self.server.listen()
        print(f"Listening for new Connections at {bindAddress[0]} and Port {bindAddress[1]}...")
        while True:
            serverSocket, clientAddress = self.server.accept()

            if clientAddress[0] != "20.81.184.218":
                print("New Connection from a Client!")
                Connection(serverSocket, clientAddress, self).start()