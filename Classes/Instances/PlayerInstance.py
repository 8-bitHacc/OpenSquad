

class PlayerInstance:
    # Main Player Stats
    HighID: int = 0
    LowID: int = 1
    AuthenticationToken: str | None = ""
    #Region; str = "GR"
    SessionKey = ""

    # Main Player Items
    Name: str = "8Hacc"
    Registered: bool = False
    UnlockedCharacters: list = [
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
    UnlockedSkins: list = []
    Quests: list = [{
        "id": 1,
        "progress": 4
    }]

    def getPlayerID(self) -> list:
        return [self.HighID, self.LowID]