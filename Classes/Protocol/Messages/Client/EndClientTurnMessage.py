from Classes.Logic.LogicCompressedString import LogicCompressedString
from Classes.Logic.Reflector.LogicRawInReflector import LogicRawInReflector
from Classes.Protocol.LogicCommandManager import LogicCommandManager
from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Utilities.Debugger import Debugger

class EndClientTurnMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)
        self.compressed: bytes = None
        self.accountID: list = [0, 0]
        self.checksum: int = 0
        self.commandsCount: int = 0
        self.commands: list = []

    def decode(self, receiver):
        compressedString = LogicCompressedString()
        self.compressed = compressedString.decode(self)
        self.accountID = self.readLongLong()
        self.checksum = self.readInt()

        self.commandsCount = self.readVInt()
        if self.commandsCount > 512:
            Debugger.error("EndClientTurn::decode() command count is too high! (%d)".format(self.commandsCount))

        for command in range(self.commandsCount):
            commandID = self.readVInt()
            if LogicCommandManager.isServerToClient(commandID): continue

            self.commands.append({"id": commandID})

            if LogicCommandManager.commandExists(commandID):
                commandInstance = LogicCommandManager.createCommand(commandID)
                if commandInstance is not None:
                    print(f"[EndClientTurnMessage::] Created command with type: {commandID}, {LogicCommandManager.getCommandName(commandID)}")
                    commandInstance.decode(self)
                    self.commands[command]["instance"] = commandInstance
                else:
                    print(
                        f"[EndClientTurnMessage::] Skipped unimplemented command with type: {commandID}, {LogicCommandManager.getCommandName(commandID)}")
            else:
                commandsLeft = (command + 1) - self.commandsCount
                print(
                    f"[EndClientTurnMessage::] Skipped unimplemented command with type: {commandID} {''.join(f'(next {commandsLeft} command(s) might have trouble being decoded)' if commandsLeft != 0 else '')}")


    def getMessageType(self):
        return 16543