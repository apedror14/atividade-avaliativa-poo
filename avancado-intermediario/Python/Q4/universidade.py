from abc import ABC, abstractmethod
class Universidade(ABC):

    def __init__(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    @abstractmethod
    def aplicarAvaliacao(self):
        pass

    def __str__(self) -> str:
        return f"Universidade: {self.getNome()}"