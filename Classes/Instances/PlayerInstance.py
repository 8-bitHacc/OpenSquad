

class PlayerInstance:
    # Main Player Stats
    HighID = 0
    LowID = 1
    AuthenticationToken = ""
    Region = "GR"
    SessionKey = ""

    # Main Player Items
    Name = "Brawler"
    Registered = False
    Trophies = 0
    HighTrophies = 0
    ProfileIcon = 0
    NameColor = 0
    TrophyRewardsClaimed = 1
    ExperiencePoints = 0

    def getPlayerID(self) -> list:
        return [self.HighID, self.LowID]