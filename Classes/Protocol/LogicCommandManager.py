from Classes.Utilities.Utility import Utility
from Classes.Protocol.Commands.LogicCommand import LogicCommand

class LogicCommandManager:

    CommandIDs = {
       217: "LogicProLeagueSeasonChangedCommand",
       504: "LogicSendAllianceMailCommand",
       221: "LogicTeamChatMuteStateChangedCommand",
       215: "LogicSetSupportedCreatorCommand",
       519: "LogicPurchaseOfferCommand",
       539: "LogicBrawlPassAutoCollectWarningSeenCommand",
       541: "LogicClearESportsHubNotificationCommand",
       211: "LogicOffersChangedCommand",
       209: "LogicKeyPoolChangedCommand",
       202: "LogicDiamondsAddedCommand",
       527: "LogicSetPlayerNameColorCommand",
       517: "LogicClaimRankUpRewardCommand",
       218: "LogicBrawlPassSeasonChangedCommand",
       528: "LogicViewInboxNotificationCommand",
       536: "LogicPurchaseBrawlPassProgressCommand",
       205: "LogicDecreaseHeroScoreCommand",
       507: "LogicUnlockSkinCommand",
       542: "LogicSelectGroupSkinCommand",
       534: "LogicPurchaseBrawlPassCommand",
       204: "LogicDayChangedCommand",
       526: "LogicUnlockFreeSkinsCommand",
       525: "LogicSelectCharacterCommand",
       531: "LogicCancelPurchaseOfferCommand",
       524: "LogicVideoStartedCommand",
       522: "LogicHeroSeenCommand",
       214: "LogicGemNameChangeStateChangedCommand",
       206: "LogicAddNotificationCommand",
       515: "LogicClearShopTickersCommand",
       535: "LogicClaimTailRewardCommand",
       538: "LogicSelectEmoteCommand",
       533: "LogicQuestsSeenCommand",
       512: "LogicToggleInGameHintsCommand",
       203: "LogicGiveDeliveryItemsCommand",
       523: "LogicClaimAdRewardCommand",
       224: "LogicSetESportsHubNotificationCommand",
       505: "LogicSetPlayerThumbnailCommand",
       210: "LogicIAPChangedCommand",
       208: "LogicTransactionsRevokedCommand",
       201: "LogicChangeAvatarNameCommand",
       511: "LogicHelpOpenedCommand",
       521: "LogicPurchaseHeroLvlUpMaterialCommand",
       506: "LogicSelectSkinCommand",
       520: "LogicLevelUpCommand",
       508: "LogicChangeControlModeCommand",
       514: "LogicDeleteNotificationCommand",
       212: "LogicPlayerDataChangedCommand",
       216: "LogicCooldownExpiredCommand",
       540: "LogicPurchaseChallengeLivesCommand",
       213: "LogicInviteBlockingChangedCommand",
       529: "LogicSelectStarPowerCommand",
       503: "LogicClaimDailyRewardCommand",
       509: "LogicPurchaseDoubleCoinsCommand",
       537: "LogicVanityItemSeenCommand",
       219: "LogicBrawlPassUnlockedCommand",
       532: "LogicItemSeenCommand",
       530: "LogicSetPlayerAgeCommand",
       207: "LogicChangeResourcesCommand",
       1000: "LogicDebugCommand",
       500: "LogicGatchaCommand",
       220: "LogicHeroWinQuestsChangedCommand",
       222: "LogicRankedSeasonChangedCommand",
       223: "LogicCooldownAddedCommand",
    }

    UseLogic = {} # Commands that import a Logic class
    UseStreams = {} # Commands that import a Stream class

    @classmethod
    def getCommandName(cls, messageid):
        try:
            message = cls.CommandIDs[messageid]
        except KeyError:
            message = str(messageid)
        
        if type(message) == str:
            return message
        else:
            return message.__name__
        
    @classmethod
    def loadCommand(cls, path: str):

        usesLogic = {}
        usesStreams = {}

        for module, name, variable in Utility.getVariables(path):

            source = Utility.getSource(variable)

            if source and "Classes/Logic" in source:
                if source not in usesLogic:
                    usesLogic[name] = source

            if source and "Classes/Streams" in source:
                if source not in usesStreams:
                    usesStreams[name] = source

            if isinstance(variable, type):

                if hasattr(variable, "getCommandType"):

                    if path.split("/")[-1].removesuffix(".py").endswith(variable.__name__):

                        try:

                            commandID = variable.getCommandType(...)
                            cls.CommandIDs[commandID] = variable

                            variable.path = path # The command's source path
                            variable.module = module # Corresponding module for command

                            for name, path in usesLogic.items():

                                existing: list = cls.UseLogic.get(path, [])

                                for x in existing:
                                    if x.__name__ == variable.__name__:
                                        existing.remove(x)

                                existing.append(variable)
                                setattr(module, name, Utility.loadLogic(path))
                                cls.UseLogic[path] = existing

                            for name, path in usesStreams.items():

                                existing: list = cls.UseStreams.get(path, [])

                                for x in existing:
                                    if x.__name__ == variable.__name__:
                                        existing.remove(x)

                                existing.append(variable)
                                setattr(module, name, Utility.loadStream(path))
                                cls.UseStreams[path] = existing
                            
                            return variable

                        except:
                            print("error")

    @classmethod
    def loadAllCommands(cls):

        for item in Utility.items("Classes/Protocol/Commands/Client") + Utility.items("Classes/Protocol/Commands/Server"):
            if item.endswith(".py"):
                cls.loadCommand(item)

        return len([y for x, y in cls.CommandIDs.items() if not isinstance(y, str)])

    @classmethod
    def commandExists(cls, messageid: int):
        return messageid in cls.CommandIDs.keys()

    @classmethod
    def createCommand(cls, commandType: int, messagePayload=b'') -> LogicCommand:
        commandIDs = cls.CommandIDs
        if cls.commandExists(commandType):
            if type(commandIDs[commandType]) != str:
                return commandIDs[commandType](messagePayload)
            else:
                return LogicCommand(b"")
        else:
            return LogicCommand(b"")
    
    @staticmethod
    def isServerToClient(commandID: int):
        if 200 <= commandID < 500:
            return True
        elif 500 <= commandID:
            return False
        
        return False