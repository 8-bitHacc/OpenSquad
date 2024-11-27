from abc import ABC, abstractmethod


class LogicReflector(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def destruct(self):
        pass
