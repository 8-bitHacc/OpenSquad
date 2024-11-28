import zlib
from typing import Union

from Classes.Utilities.Debugger import Debugger

class LogicCompressedString:
    def __init__(self, string = None, stringLength: int = -1):
        if not isinstance(string, bytes) and string is not None: string = zlib.compress(string)
        self.string: bytes = string
        self.stringLength: int = stringLength

    def destruct(self):
        self.string = None
        self.stringLength = -1

    def decode(self, byteStream, returnDecompressed: bool = False) -> Union[bytes, str]:
        """Decodes the string in the ByteStream instance's payload and returns it.

        Parameters:
            byteStream (ByteStream): The ByteStream instance.
            returnDecompressed (bool): Whether to return it as bytes or decompressed (string)
        """
        self.string = byteStream.readBytes(byteStream.readBytesLength())
        self.stringLength = len(self.string)
        return self.string if not returnDecompressed else zlib.decompress(self.string)

    def encode(self, byteStream):
        """Writes the compressed string to the payload of the ByteStream instance provided."""
        byteStream.writeBytes(self.string, self.stringLength)

    def hashCode(self):
        Debugger.error("LogicCompressedString::hashCode is not implemented")

    def hasString(self) -> bool:
        """Returns true if there's a string."""
        return self.stringLength >= 0

    def clear(self):
        """Clears the instance's string to its original state, aka null"""
        self.string = None
        self.stringLength = -1