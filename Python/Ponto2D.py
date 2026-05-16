import math


class Ponto2D:

    # O construtor recebe as coordenadas x e y do ponto
    def __init__(self, abcissa=0.0, ordenada=0.0):
        self.__abcissa = abcissa
        self.__ordenada = ordenada

    # Retorna o valor de x
    def getAbcissa(self):
        return self.__abcissa

    # Atualiza o valor de x
    def setAbcissa(self, abcissa):
        self.__abcissa = abcissa

    # Retorna o valor de y
    def getOrdenada(self):
        return self.__ordenada

    # Atualiza o valor de y
    def setOrdenada(self, ordenada):
        self.__ordenada = ordenada

    # Move o ponto para uma nova posição 
    def mover(self, abcissa, ordenada):
        self.__abcissa = abcissa
        self.__ordenada = ordenada

    # Calcula a distância
    def calcularDistancia(self, outroPonto):
        deltaX = self.__abcissa - outroPonto.getAbcissa()
        deltaY = self.__ordenada - outroPonto.getOrdenada()
        return math.sqrt(deltaX ** 2 + deltaY ** 2)

    # Cria um novo ponto 
    def clonar(self):
        return Ponto2D(self.__abcissa, self.__ordenada)

    def __str__(self):
        return f"({self.__abcissa}, {self.__ordenada})"
