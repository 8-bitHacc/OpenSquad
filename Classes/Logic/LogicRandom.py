class LogicRandom:
    def __init__(self, randomSeed: int = 0):
        self.seed = randomSeed

    def encode(self, byteStream):
        byteStream.writeInt(self.seed)

    def decode(self, byteStream):
        self.seed = byteStream.readInt()
        return self.seed

    def getIteratedRandomSeed(self) -> int:
        return self.seed

    def rand(self, a2: int) -> int:
        if a2 < 1:
            return 0
        v3 = self.seed
        if not self.seed:
            v3 = -1
        v4 = v3 ^ (v3 << 13) ^ ((v3 ^ (v3 << 13)) >> 17)
        v5 = v4 ^ (32 * v4)
        self.seed = v5
        v6 = v5 % a2
        result = v6
        if v5 < 0:
            return -v6
        return result

    def iterateRandomSeed(self, a2: int) -> int:
        if a2 is None:
            a2 = -1
        v2 = a2 ^ (a2 << 13) ^ ((a2 ^ (a2 << 13)) >> 17)
        return v2 ^ (32 * v2)

    def setIteratedRandomSeed(self, a2: int):
        self.seed = a2