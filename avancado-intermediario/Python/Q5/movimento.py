from abc import ABC, abstractmethod

class Movimento(ABC):

    @abstractmethod
    def mover(self, x, y):
        pass