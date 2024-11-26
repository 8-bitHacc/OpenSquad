from Classes.Utilities.Utility import Utility

class StreamEntryFactory:

    StreamTypes = {
        2: "ChatStreamEntry",
        4: "AllianceEventStreamEntry",
        8: "QuickChatStreamEntry",
        3: "JoinRequestAllianceStreamEntry"
    }

    @staticmethod
    def createStreamEntryByType(byteStream, stream):
        StreamType = stream.streamType
        if StreamType in StreamEntryFactory.StreamTypes:
            StreamEntryFactory.StreamTypes[StreamType](stream).encode(byteStream)
        else:
            raise NotImplementedError(f"[StreamEntryFactory::] StreamType {StreamType} is not implemented")

    @classmethod
    def loadEntry(cls, path: str):

        entry = Utility.loadStream(path)
        
        if entry:
            streamType = entry.getStreamEntryType(entry)
            cls.StreamTypes[streamType] = entry
            return entry

    @classmethod
    def loadAllEntries(cls):

        for stream in Utility.items("Classes/Streams"):
            if stream != "StreamEntryFactory":
                cls.loadEntry(stream)
        
        return len(cls.StreamTypes)