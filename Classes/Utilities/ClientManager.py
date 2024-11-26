import traceback


class ClientManager:
    clients = {}

    @classmethod
    def insertClient(cls, sessionKey, connection, playerid):
        try:
            if cls.checkForSession(playerid)[0] is not None:
                if playerid == [0, 0]: return
                data = cls.checkForSession(playerid)
                cls.removeClient(data[0])
            cls.clients[sessionKey] = {"Connection": connection, "PlayerID": playerid, "SessionKey": sessionKey}
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
    def checkForSession(cls, SpecificUserID):
        try:
            for SessionKey, SessionData in cls.clients.items():
                if SessionData["PlayerID"] == SpecificUserID:
                    return SessionKey, SessionData  # Return the data
            return None, None  # If session is not found, return None
        except:
            print(traceback.format_exc())
            return None, None  # Handle any exceptions and return None

    @classmethod
    def getAllClientSessionData(cls):
        try:
            Sessions = []
            for SessionKey, SessionData in cls.clients.items():
                Sessions.append(SessionData["Connection"])

            return Sessions  # sorry for lazyness
        except:
            print(traceback.format_exc())

    @classmethod
    def getAllClientConnections(cls, type=None):
        try:
            Sessions = []
            for SessionKey, SessionData in cls.clients.items():
                if type == "Player":
                    Sessions.append(SessionData["Connection"].player)
                else:
                    Sessions.append(SessionData["Connection"])

            return Sessions
        except:
            print(traceback.format_exc())
