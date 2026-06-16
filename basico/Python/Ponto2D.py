import math


class Ponto2D:

    def __init__(self, abcissa=0.0, ordenada=0.0):
        self.__abcissa = abcissa
        self.__ordenada = ordenada

    def getAbcissa(self):
        return self.__abcissa

    def setAbcissa(self, abcissa):
        self.__abcissa = abcissa

    def getOrdenada(self):
        return self.__ordenada

    def setOrdenada(self, ordenada):
        self.__ordenada = ordenada

    def mover(self, abcissa, ordenada):
        self.__abcissa = abcissa
        self.__ordenada = ordenada

    def calcularDistancia(self, outroPonto):
        deltaX = self.__abcissa - outroPonto.getAbcissa()
        deltaY = self.__ordenada - outroPonto.getOrdenada()
        return math.sqrt(deltaX ** 2 + deltaY ** 2)

    def clonar(self):
        return Ponto2D(self.__abcissa, self.__ordenada)

    def __str__(self):
        return f"({self.__abcissa}, {self.__ordenada})"
