

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
    emoteData: list[dict] = [
        {"id": 0, "idx": 0},
        {"id": 1, "idx": 1},
        {"id": 2, "idx": 2},
        {"id": 2, "idx": 2}
    ]
    Quests: list[dict] = [{
        "id": 1,
        "progress": 4
    }]

    def getPlayerID(self) -> list:
        return [self.HighID, self.LowID]