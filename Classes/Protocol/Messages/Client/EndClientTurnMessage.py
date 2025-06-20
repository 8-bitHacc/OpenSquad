from Classes.Logic.LogicCompressedString import LogicCompressedString
from Classes.Protocol.Commands.LogicCommand import LogicCommand
from Classes.Protocol.LogicCommandManager import LogicCommandManager
from Classes.Protocol.PiranhaMessage import PiranhaMessage
from Classes.Utilities.Debugger import Debugger

class EndClientTurnMessage(PiranhaMessage):
    def __init__(self, payload):
        super().__init__(payload)
        self.compressed: bytes = b""
        self.accountID: list = [0, 0]
        self.checksum: int = 0
        self.commandsCount: int = 0
        self.commands: list = []

    def decode(self, receiver):
        self.readCompressedString()
        self.accountID = self.readLongLong()
        self.checksum = self.readInt()

        self.commandsCount = self.readVInt()
        if self.commandsCount > 512:
            Debugger.error("EndClientTurn::decode() command count is too high! (%d)".format(self.commandsCount))
            return

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
                LogicCommand(self.payload).decode(self)
                commandsLeft = self.commandsCount - (command + 1)
                print(
                    f"[EndClientTurnMessage::] Skipped unimplemented command with type: {commandID} {''.join(f'(next {commandsLeft} command(s) might have trouble being decoded)' if commandsLeft != 0 else '')}")

    def execute(self, receiver):
        for command in self.commands:
            if "instance" not in command: continue

            command["instance"].execute(receiver)


    def getMessageType(self):
        return 16543