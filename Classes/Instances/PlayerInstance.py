

class PlayerInstance:
    # Main Player Stats
    ID: list = [0, 1]
    AuthenticationToken: str | None = ""
    SessionKey: str = ""

    # Main Player Items
    Name: str | None = "8Hacc"
    registrationState: int = 3
    expTokens: int = 199999999
    trophies: int = 0
    resources: list[dict[str, int]] = [
        {
            "val": 10
        },
        {
            "id": 1,
            "val": 10000
        },
    ]
    UnlockedCharacters: list[dict[str, int]] = [
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
    emoteData: list[dict[str, int]] = [
        {"id": 0, "idx": 0},
        {"id": 1, "idx": 1},
        {"id": 2, "idx": 2},
        {"id": 2, "idx": 2}
    ]
    Quests: list[dict[str, int]] = [{
        "id": 1,
        "progress": 4
    }]

    def createDataEntry(self) -> dict:
        return {"PlayerID": self.ID, "AuthenticationToken": self.AuthenticationToken} # TODO: Implement

    def loadInstance(self, data: dict):
        self.ID = data["PlayerID"]
        self.Name = data.get("Name", None)
        self.registrationState = data.get("regState", -1)
        self.expTokens = data.get("expTokens", 0)
        self.trophies = data.get("trophies", 0)
        self.resources = data.get("resources", self.resources)
        self.UnlockedCharacters = data.get("unlockedCharacters", self.UnlockedCharacters)
        self.UnlockedSkins = data.get("unlockedSkins", [])
        self.emoteData = data.get("emoteData", self.emoteData)
        self.Quests = data.get("quests", [])