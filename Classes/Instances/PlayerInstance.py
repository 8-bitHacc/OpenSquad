

class PlayerInstance:
    # Main Player Stats
    accountID: list[int] = []
    accountToken: str | None = None
    sessionKey: str = None

    # Main Player Items
    name: str | None = None
    registrationState: int = -1
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
    members: list[dict[str, int]] = [
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
    skins: list = []
    emotes: list[dict[str, int]] = [
        {"id": 0, "idx": 0},
        {"id": 1, "idx": 1},
        {"id": 2, "idx": 2},
        {"id": 2, "idx": 2}
    ]
    quests: list[dict[str, int]] = [{
        "id": 94,
        "progress": 4
    }]

    def createDataEntry(self) -> dict:
        return {"id": self.accountID, "token": self.accountToken, "name": self.name, "regState": self.registrationState}

    def loadInstance(self, data: dict):
        self.accountID = data["id"]
        self.name = data.get("name", None)
        self.registrationState = data.get("regState", -1)
        self.expTokens = data.get("expTokens", 0)
        self.trophies = data.get("trophies", 0)
        self.resources = data.get("resources", self.resources)
        self.members = data.get("members", self.members)
        self.skins = data.get("skins", [])
        self.emotes = data.get("emotes", self.emotes)
        self.quests = data.get("quests", [])