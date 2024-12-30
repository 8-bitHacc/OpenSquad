
from Classes.Protocol.Messages.Server.TitanDisconnectedMessage import TitanDisconnectedMessage

class ClientManager:
    clients = {}

    @classmethod
    def insertClient(cls, sessionKey: str, connection, playerid: list):
        try:
            if cls.checkForSession(playerid)[0] is not None:
                if playerid == [0, 0]: return
                data = cls.checkForSession(playerid)
                c = TitanDisconnectedMessage()
                data[1]["Connection"].messaging.send({}, c)
                cls.removeClient(data[0])
            cls.clients[sessionKey] = {"Connection": connection, "PlayerID": playerid, "PlayerInstance": connection.player, "SessionKey": sessionKey}
        except Exception:
            pass

    @classmethod
    def removeClient(cls, sessionID):
        try:
            if sessionID != "": cls.clients.pop(sessionID)
        except KeyError:
            print(f"[ClientManager::] Failed to remove SessionID {sessionID}")

    @classmethod
    def getAllClients(cls) -> int:
        return len(cls.clients)

    @classmethod
    def checkForSession(cls, SpecificUserID: list) -> tuple[str, dict] | tuple[None, None]:
        try:
            for SessionKey, SessionData in cls.clients.items():
                if SessionData["PlayerID"] == SpecificUserID:
                    return SessionKey, SessionData  # Return the data
            return None, None  # If session is not found, return None
        except:
            print("Error at checkingSession")
            return None, None  # Handle any exceptions and return None

    @classmethod
    def getAllClientConnections(cls, type: str = None) -> list:
        try:
            Sessions = []
            for SessionKey, SessionData in cls.clients.items():
                if type == "Player":
                    Sessions.append(SessionData["Connection"].player)
                else:
                    Sessions.append(SessionData["Connection"])

            return Sessions
        except:
            print("error at getAllClientConnections")
            return []