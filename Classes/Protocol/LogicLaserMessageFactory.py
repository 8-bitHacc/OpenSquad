from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Utilities.Utility import Utility

class LogicLaserMessageFactory:
    PacketIDs = {
        24124: "TeamMessage",
        27475: "EndClientTurnHandledMessage",
        13493: "GoHomeMessage",
        29125: "LoginOkMessage",
        24758: "ApiTokenMessage",
        14359: "TeamChatMessage",
        14351: "TeamJoinMessage",
        14352: "TeamKickMessage",
        24125: "TeamLeftMessage",
        10502: "AddFriendMessage",
        23456: "BattleEndMessage",
        23458: "BattleLogMessage",
        10108: "KeepAliveMessage",
        23457: "LobbyInfoMessage",
        24104: "OutOfSyncMessage",
        14177: "PlayAgainMessage",
        14867: "SetRegionMessage",
        14103: "StartGameMessage",
        24129: "TeamErrorMessage",
        14353: "TeamLeaveMessage",
        10177: "ClientInfoMessage",
        10401: "CreateGameMessage",
        20105: "FriendListMessage",
        22202: "MapPreviewMessage",
        24399: "MyAllianceMessage",
        22102: "PlayerMapsMessage",
        10117: "ReportUserMessage",
        12998: "SetCountryMessage",
        14350: "TeamCreateMessage",
        14365: "TeamInviteMessage",
        14360: "TeamPostAdMessage",
        24131: "TeamStreamMessage",
        10101: "LoginMessage",
        16939: "AllianceWarMessage",
        30000: "AttributionMessage",
        10100: "ClientHelloMessage",
        18856: "ClientInputMessage",
        29997: "CryptoErrorMessage",
        24403: "LeaderboardMessage",
        24101: "OwnHomeDataMessage",
        20100: "ServerHelloMessage",
        10501: "AcceptFriendMessage",
        24301: "AllianceDataMessage",
        24310: "AllianceListMessage",
        24411: "AvatarStreamMessage",
        14178: "DebugMessageMessage",
        25892: "DisconnectedMessage",
        14305: "JoinAllianceMessage",
        20801: "NotificationMessage",
        14366: "PlayerStatusMessage",
        10506: "RemoveFriendMessage",
        10116: "ResetAccountMessage",
        20559: "StartLoadingMessage",
        14107: "StopSpectateMessage",
        14362: "TeamSetEventMessage",
        14358: "TeamSpectateMessage",
        24109: "VisionUpdateMessage",
        17338: "AdjustPackageMessage",
        24364: "AllianceTeamsMessage",
        10110: "AnalyticEventMessage",
        10103: "CreateAccountMessage",
        16543: "EndClientTurnMessage",
        12102: "GetPlayerMapsMessage",
        14308: "LeaveAllianceMessage",
        23774: "PlayerJWTokenMessage",
        24113: "PlayerProfileMessage",
        24123: "SeasonRewardsMessage",
        20000: "SetEncryptionMessage",
        14104: "StartSpectateMessage",
        24106: "StopHomeLogicMessage",
        10121: "UnlockAccountMessage",
        20107: "AddableFriendsMessage",
        24308: "AllianceMemberMessage",
        24311: "AllianceStreamMessage",
        14301: "CreateAllianceMessage",
        12107: "EnterMapEditorMessage",
        20110: "FriendLoggedInMesssage",
        14403: "GetLeaderboardMessage",
        15793: "GetTokenFriendMessage",
        24715: "GlobalChatLineMessage",
        10113: "SetDeviceTokenMessage",
        24105: "SpectateFailedMessage",
        24589: "TeamInvitationMessage",
        14364: "TeamReportChatMessage",
        17337: "UnbotifyReportMessage",
        10118: "AccountSwitchedMessage",
        20112: "AddFriendFailedMessage",
        14110: "AskForBattleEndMessage",
        14203: "BindLineAccountMessage",
        12100: "CreatePlayerMapMessage",
        12101: "DeletePlayerMapMessage",
        20111: "FriendLoggedOutMessage",
        20108: "KeepAliveServerMessage",
        24108: "MatchmakeFailedMessage",
        24777: "PlayAgainStatusMessage",
        12125: "ReportPlayerMapMessage",
        10636: "SCIDBindAccountMessage",
        14324: "SearchAlliancesMessage",
        20161: "ShutdownStartedMessage",
        12104: "SumbitPlayerMapMessage",
        14367: "TeamClearInviteMessage",
        14369: "TeamPremadeChatMessage",
        14881: "TeamRequestJoinMessage",
        14363: "TeamSetLocationMessage",
        20132: "UnlockAccountOkMessage",
        12103: "UpdatePlayerMapMessage",
        10507: "AddFriendByEmailMessage",
        24333: "AllianceResponseMessage",
        10504: "AskForFriendListMessage",
        10055: "AskPlayerJWTokenMessage",
        10321: "AttributionEventMessage",
        14202: "BindKakaoAccountMessage",
        10212: "ChangeAvatarNameMessage",
        14166: "ChronosEventSeenMessage",
        20402: "CreateGameFailedMessage",
        20106: "FriendListUpdateMessage",
        14113: "GetPlayerProfileMessage",
        14277: "GetSeasonRewardsMessage",
        14114: "HomeBattleReplayMessage",
        14105: "HomeLogicStoppedMessage",
        24206: "LineAccountBoundMessage",
        14103: "MatchmakeRequestMessage",
        12105: "PublishPlayerMapMessage",
        20117: "ReportUserStatusMessage",
        25165: "SCIDAccountBoundMessage",
        14330: "SendAllianceMailMessage",
        14778: "SetTeamChatMutedMessage",
        12111: "SignoffPlayerMapMessage",
        24130: "TeamGameStartingMessage",
        24582: "TeamInviteStatusMessage",
        14361: "TeamMemberStatusMessage",
        12110: "TeamSetPlayerMapMessage",
        20103: "LoginFailedMessage",
        13922: "AcceptTokenFriendMessage",
        24412: "AvatarStreamEntryMessage",
        14106: "CancelMatchmakingMessage",
        10099: "ClientCryptoErrorMessage",
        20199: "FriendSuggestionsMessage",
        24203: "KakaoAccountBoundMessage",
        19001: "LatencyTestResultMessage",
        29003: "LatencyTestStatusMessage",
        10102: "LoginUsingSessionMessage",
        20405: "MatchMakingStatusMessage",
        14777: "SetInvitesBlockedMessage",
        24177: "SetRegionResponseMessage",
        24112: "UpdConnectionInfoMessage",
        14214: "UnbindLineAccountMessage",
        20501: "AcceptFriendFailedMessage",
        10111: "AccountIdentifiersMessage",
        14302: "AskForAllianceDataMessage",
        14405: "AskForAvatarStreamMessage",
        20206: "AvatarOnlineStatusUpdated",
        24413: "BattleReportStreamMessage",
        14266: "BindTencentAccountMessage",
        24700: "BrawlTvChannelListMessage",
        10107: "ClientCapabilitiesMessage",
        20109: "FriendOnlineStatusMessage",
        14108: "GoHomeFromSpectateMessage",
        14307: "KickAllianceMemberMessage",
        24216: "LineAccountUnboundMessage",
        12152: "RankedMatchBanHeroMessage",
        22150: "RankedMatchStartedMessage",
        14117: "RequestMatchCancelMessage",
        14715: "SendGlobalChatLineMessage",
        14299: "SetAllianceCountryMessage",
        24178: "SetCountryResponseMessage",
        14373: "TeamBotSlotDisableMessage",
        14368: "TeamInviteResponseMessage",
        14355: "TeamSetMemberReadyMessage",
        14356: "TeamTogglePractiseMessage",
        14372: "TeamToggleSettingsMessage",
        14268: "TencentCheckCanPayMessage",
        14701: "TuneBrawlTvChannelMessage",
        10109: "UdpCheckConnectionMessage",
        14213: "UnbindKakaoAccountMessage",
        24312: "AllianceStreamEntryMessage",
        24365: "AllianceTeamRemovedMessage",
        10150: "AppleBillingRequestMessage",
        10112: "AuthenticationCheckMessage",
        14115: "BattleLogViewReplayMessage",
        14201: "BindFacebookAccountMessage",
        12106: "ChangePlayerMapNameMessage",
        12108: "GoHomeFromMapEditorMessage",
        24215: "KakaoAccountUnboundMessage",
        14700: "ListBrawlTvChannelsMessage",
        26007: "LogicDeviceLinkDoneMessage",
        22153: "RankedMatchBanEndedMessage",
        12155: "RankedMatchPickHeroMessage",
        14317: "RequestJoinAllianceMessage",
        18686: "SetSupportedCreatorMessage",
        24220: "TencentAccountBoundMessage",
        20113: "UnlockAccountFailedMessage",
        10503: "AskForAddableFriendsMessage",
        14304: "AskForAllianceStreamMessage",
        20121: "BillingRequestFailedMessage",
        24701: "BrawlTvChannelNextUpMessage",
        20118: "ChatAccountBanStatusMessage",
        14315: "ChatToAllianceStreamMessage",
        24201: "FacebookAccountBoundMessage",
        22089: "GetTokenFriendResultMessage",
        10151: "GoogleBillingRequestMessage",
        24114: "HomeBattleReplayDataMessage",
        24304: "JoinableAllianceListMessage",
        10159: "KunlunBillingRequestMessage",
        26008: "LogicDeviceLinkErrorMessage",
        20406: "MatchMakingCancelledMessage",
        20171: "PersonalBreakStartedMessage",
        22107: "PlayerMapInfoUpdatedMessage",
        10119: "ReportAllianceStreamMessage",
        11736: "SCIDLogoutAllDevicesMessage",
        14371: "TeamJoinOrCreateRoomMessage",
        14357: "TeamToggleMemberSideMessage",
        14116: "ViewReplayByStringIdMessage",
        10523: "YoozooBillingRequestMessage",
        20523: "YoozooOrderAvailableMessage",
        24309: "AllianceMemberRemovedMessage",
        14212: "BindGamecenterAccountMessage",
        22111: "PlayerMapGreenlightedMessage",
        22151: "RankedMatchBanStartedMessage",
        22156: "RankedMatchHeroPickedMessage",
        22159: "RankedMatchTerminatedMessage",
        14880: "TeamRequestJoinCancelMessage",
        10152: "TencentBillingRequestMessage",
        20101: "UdpBigMessageFragmentMessage",
        19002: "UdpLatencyTestRequestMessage",
        14211: "UnbindFacebookAccountMessage",
        24111: "AvailableServerMessageMessage",
        20205: "AvatarNameChangeFailedMessage",
        14600: "AvatarNameCheckRequestMessage",
        14316: "ChangeAllianceSettingsMessage",
        24214: "FacebookAccountUnboundMessage",
        26085: "GamecenterAccountBoundMessage",
        10309: "GetAllianceInviteTokenMessage",
        24116: "HomeBattleReplayFailedMessage",
        24117: "HomeBattleReplayViewedMessage",
        17190: "JoinAllianceUsingTokenMessage",
        14199: "LookForGameRoomRequestMessage",
        22154: "RankedMatchPickStartedMessage",
        14322: "SendAllianceInvitationMessage",
        10576: "SetBlockFriendRequestsMessage",
        14479: "TeamInvitationResponseMessage",
        14882: "TeamRequestJoinApproveMessage",
        24319: "TeamStreamEntryRemovedMessage",
        29002: "UdpLatencyTestResponseMessage",
        40000: "AdUpdateConversionValueMessage",
        10559: "AskForFriendSuggestionsMessage",
        20300: "AvatarNameCheckResponseMessage",
        22100: "CreatePlayerMapResponseMessage",
        22101: "DeletePlayerMapResponseMessage",
        24555: "FriendOnlineStatusEntryMessage",
        24205: "LineAccountAlreadyBoundMessage",
        26005: "LogicDeviceLinkResponseMessage",
        14418: "RemoveAvatarStreamEntryMessage",
        22125: "ReportPlayerMapResponseMessage",
        28689: "SCIDAccountAlreadyBoundMessage",
        29001: "StartLatencyTestRequestMessage",
        22104: "SumbitPlayerMapResponseMessage",
        29900: "SupercellIdNotificationMessage",
        19003: "TriggerStartLatencyTestMessage",
        22103: "UpdatePlayerMapResponseMessage",
        20931: "AntiAddictionDataUpdatedMessage",
        14406: "AskForBattleReplayStreamMessage",
        10516: "AskForPlayingLineFriendsMessage",
        24418: "AvatarStreamEntryRemovedMessage",
        23459: "BattleLogReplayAvailableMessage",
        10160: "BillingCancelledByClientMessage",
        14262: "BindGoogleServiceAccountMessage",
        10153: "CafeBazaarBillingRequestMessage",
        14306: "ChangeAllianceMemberRoleMessage",
        24313: "ChangeAllianceSettingsOkMessage",
        24204: "KakaoAccountAlreadyBoundMessage",
        16002: "LogicDeviceLinkEnterCodeMessage",
        22105: "PublishPlayerMapResponseMessage",
        22957: "PvpMatchmakingNotificationMessage",
        19004: "RequestLatencyTestStatusMessage",
        14118: "SinglePlayerMatchRequestMessage",
        14370: "TeamAllianceMemberInviteMessage",
        14354: "TeamChangeMemberSettingsMessage",
        10514: "AskForPlayingKakaoFriendsMessage",
        14109: "GoHomeFromOfflinePractiseMessage",
        22377: "GoogleServiceAccountBoundMessage",
        16003: "LogicDeviceLinkConfirmYesMessage",
        16001: "LogicDeviceLinkMenuClosedMessage",
        22155: "RankedMatchPickHeroFailedMessage",
        12157: "RankedMatchUpdateHeroDataMessage",
        20545: "YoozooOrderDeliveryFailedMessage",
        24318: "AllianceStreamEntryRemovedMessage",
        12905: "GetCurrentBattleReplayDataMessage",
        16000: "LogicDeviceLinkCodeRequestMessage",
        22152: "RankedMatchBanHeroResponseMessage",
        22157: "RankedMatchHeroDataUpdatedMessage",
        23067: "SCIDLogoutAllDevicesResultMessage",
        24221: "TencentAccountAlreadyBoundMessage",
        24223: "TencentCheckCanPayResponseMessage",
        20207: "AllianceOnlineStatusUpdatedMessage",
        14303: "AskForJoinableAlliancesListMessage",
        10515: "AskForPlayingTencentFriendsMessage",
        22106: "ChangePlayerMapNameResponseMessage",
        24202: "FacebookAccountAlreadyBoundMessage",
        14323: "JoinAllianceUsingInvitationMessage",
        26002: "LogicDeviceLinkCodeResponseMessage",
        28686: "SetSupportedCreatorResponseMessage",
        10509: "AddFriendByAvatarNameAndCodeMessage",
        24321: "AllianceInvitationSendFailedMessage",
        10513: "AskForPlayingFacebookFriendsMessage",
        28363: "BuyBundleBillingPackResponseMessage",
        23302: "GetAllianceInviteTokenResultMessage",
        14321: "RespondToAllianceJoinRequestMessage",
        20151: "AppleBillingProcessedByServerMessage",
        10517: "AskForPlayingSupercellFriendsMessage",
        22687: "GamecenterAccountAlreadyBoundMessage",
        10512: "AskForPlayingGamecenterFriendsMessage",
        20152: "GoogleBllingProcessedByServerMessage",
        20156: "KunlunBillingProcessedByServerMessage",
        26004: "LogicDeviceLinkCodeDeactivatedMessage",
        26003: "LogicDeviceLinkNewDeviceLinkedMessage",
        14326: "SendAllianceInvitationToFriendMessage",
        20173: "YoozooBillingProcessedByServerMessage",
        17000: "LogicAccountTransferCodeRequestMessage",
        24222: "TencentAntiAddictionInstructionMessage",
        20153: "TencentBillingProcessedByServerMessage",
        23494: "GoogleServiceAccountAlreadyBoundMessage",
        27002: "LogicAccountTransferCodeResponseMessage",
        20154: "CafeBazaarBillingProcessedByServerMessage",
        22158: "RankedMatchFinalPreparationStartedMessage",
        22109: "DebugPlayerMapReviewResultOverrideSetMessage",
        14267: "TencentAntiAddictionInstructionExecutedMessage",
    }

    UseLogic = {} # Packets that import a Logic class
    UseStreams = {} # Packets that import a Stream class

    @classmethod
    def loadMessage(cls, path: str):

        usesLogic = {}
        usesStreams = {}
        checkType = True

        for module, name, variable in Utility.getVariables(path):
            if checkType:
                moduleName = module.__name__
                packetType = "1" if moduleName.startswith("Classes.Protocol.Messages.Client") else "2"
                checkType = False

            source = Utility.getSource(variable)

            if source and "Classes/Logic" in source:
                if source not in usesLogic:
                    usesLogic[name] = source

            if source and "Classes/Streams" in source:
                if source not in usesStreams:
                    usesStreams[name] = source

            if isinstance(variable, type):
                if issubclass(variable, PiranhaMessage):

                    if hasattr(variable, "getMessageType"):

                        if path.split("/")[-1].removesuffix(".py").endswith(variable.__name__):
                            try:

                                messageID = variable.getMessageType(...)

                                if str(messageID)[0] != packetType:
                                    continue
                                
                                cls.PacketIDs[messageID] = variable
                                variable.path = path # The message's source path
                                variable.module = module # Corresponding module for packet

                                for name, path in usesLogic.items():

                                    existing: list = cls.UseLogic.get(path, [])

                                    for x in existing:
                                        if x.__name__ == variable.__name__:
                                            existing.remove(x)

                                    existing.append(variable)
                                    setattr(module, name, Utility.loadLogic(path)) # Update with latest
                                    cls.UseLogic[path] = existing

                                for name, path in usesStreams.items():

                                    existing: list = cls.UseStreams.get(path, [])

                                    for x in existing:
                                        if x.__name__ == variable.__name__:
                                            existing.remove(x)

                                    existing.append(variable)
                                    setattr(module, name, Utility.loadLogic(path))
                                    cls.UseStreams[path] = existing
                                
                                return variable

                            except:
                                print("error")

    @staticmethod
    def reloadMessage(message=None, path=None):

        source = path

        if path is None:
            source = getattr(message, "path", None)

        if source:

            new = LogicLaserMessageFactory.loadMessage(source)
            
            # Gets messages imported in this message

            for required in LogicLaserMessageFactory.PacketIDs.values():
                if not isinstance(required, str):
                    if hasattr(required, "module"):
                        if required.getMessageType(...) != new.getMessageType(...):
                            module = required.module
                            for name in dir(module):
                                value = getattr(required.module, name)
                                if isinstance(value, type):
                                    if value.__name__ == new.__name__:
                                        setattr(required.module, name, new)

            return new

    @staticmethod
    def loadAllMessages():

        for item in Utility.items("Classes/Protocol/Messages/Client") + Utility.items("Classes/Protocol/Messages/Server"):
            if item.endswith(".py"):
                LogicLaserMessageFactory.loadMessage(item)

        return len([y for x, y in LogicLaserMessageFactory.PacketIDs.items() if not isinstance(y, str)])

    @staticmethod
    def getMessageName(messageID: int):
        try:
            message = LogicLaserMessageFactory.PacketIDs[messageID]
        except KeyError:
            message = str(messageID)

        if type(message) == str:
            return message
        else:
            return message.__name__

    @staticmethod
    def MessageExists(messageID: int):
        return messageID in LogicLaserMessageFactory.PacketIDs.keys()

    @staticmethod
    def createMessageByType(messageType: int, messagePayload=b'') -> PiranhaMessage:
        messagesList = LogicLaserMessageFactory.PacketIDs
        if LogicLaserMessageFactory.MessageExists(messageType):
            if type(messagesList[messageType]) is not str:
                print(f"MessageID: {messageType}, {LogicLaserMessageFactory.getMessageName(messageType)} created")
                return messagesList[messageType](messagePayload)
            else:
                print(f"MessageID: {messageType}, {LogicLaserMessageFactory.getMessageName(messageType)} skipped")
        else:
            print(messageType, "skipped")
            return PiranhaMessage(b"")