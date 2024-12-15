from Classes.Utilities.Utility import Utility
from Classes.Protocol.Commands.LogicCommand import LogicCommand

class LogicCommandManager:

    CommandIDs = {
        503: "LogicQuestsSeenCommand",
        520: "LogicTutorialStepsPassedCommand"
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
    def loadAllCommands(cls) -> int:
        for item in Utility.items("Classes/Protocol/Commands/Client") + Utility.items("Classes/Protocol/Commands/Server"):
            if item.endswith(".py"):
                cls.loadCommand(item)

        return len([y for x, y in cls.CommandIDs.items() if not isinstance(y, str)])

    @classmethod
    def commandExists(cls, messageid: int) -> bool:
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
    def isServerToClient(commandID: int) -> bool:
        if 200 <= commandID < 500:
            return True
        
        return False