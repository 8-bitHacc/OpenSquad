from Classes.ByteStream.ByteStream import ByteStream


class PiranhaMessage(ByteStream):
    def __init__(self, payload = b""):
        """Initializes the Packet's default data"""
        super().__init__(payload)
        self.packetVersion = 0

    def decode(self, receiverDict: dict): #Dict[Connection, PlayerInstance]):
        """
        Data sent by a ClientMessage, to read the data, provide the structure

        Parameters:
            receiverDict (dict): A dict containing data about the client connection
        """
        pass

    def encode(self, receiverDict): #Dict[Connection, PlayerInstance]):
        """Encoding of a Message/Packet, data must be provided by User"""
        pass

    def execute(self, receiverDict): #Dict[Connection, PlayerInstance]):
        """Executes the Message actions provided by the User"""
        pass

    def getMessageType(self) -> int:
        """ Returns the MessageID """
        return 0

    def isServerToClientMessage(self):
        MessageID = self.getMessageType()
        if 20000 < MessageID < 30000 or MessageID == 40000:
            return True

    def isClientToServerMessage(self):
        """Checks if the Message is from Client sending to Server"""
        MessageID = self.getMessageType()
        if 10000 < MessageID < 20000 or MessageID == 30000:
            return True
    
    def getMessageTypeName(self):
        """Gets the Message's Name"""
        return self.__class__.__name__
    
    def setMessageVersion(self):
        """Sets the Message's Version Number"""
        return self.packetVersion
    
    def clear(self, **kwargs):
        """Clears the Message Buffer"""
        self.payload = b''
        self.packetVersion = 0
        self.offset = 0
        self.bitoffset = 0

    def reflect(self, reflector, receiver):
        """Encodes the message's payload using Reflector"""
        pass