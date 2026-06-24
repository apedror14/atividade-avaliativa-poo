from abc import ABC, abstractmethod

class Objeto(ABC):

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    @abstractmethod
    def __str__(self):
        return (f"Posição X = {self.getX()} \n"
                f"Posição Y = {self.getY()} \n")
