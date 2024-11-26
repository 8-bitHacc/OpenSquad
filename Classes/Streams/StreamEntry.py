
class StreamEntry:
    def __init__(self, streamData):
        self.stream = streamData

    def encode(self, bytestream):
        pass
    
    def getStreamEntryType(self):
        return 0