

class PlayerInstance:
    # Main Player Stats
    HighID = 0
    LowID = 1
    AuthenticationToken = ""
    Region = "GR"
    SessionKey = ""

    # Main Player Items
    Name = "8Hacc"
    Registered = False
    UnlockedCharacters = [
        {
            "id": 0,
        },
        {
            "id": 2,
        },
        {
            "id": 4,
        }
    ]
    UnlockedSkins = []
    Quests = [{
        "id": 1,
        "progress": 4
    }]

    def getPlayerID(self) -> list:
        return [self.HighID, self.LowID]