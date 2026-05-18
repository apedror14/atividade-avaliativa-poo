class Circulo:

    PI = 3.14159

    def __init__(self, raio, centroX, centroY):
        self.__raio = float(raio)
        self.__centroX = float(centroX)
        self.__centroY = float(centroY)

    def inflar(self, valor=None):
        if valor is None:
            self.__raio += 1.0
        else:
            self.__raio += float(valor)

    def desinflar(self, valor=None):
        if valor is None:
            self.__raio -= 1.0
        else:
            self.__raio -= float(valor)
        if self.__raio < 0:
            self.__raio = 0.0

    def mover(self, x=None, y=None):
        if x is None and y is None:
            self.__centroX = 0.0
            self.__centroY = 0.0
        else:
            self.__centroX = float(x)
            self.__centroY = float(y)

    def calcularArea(self):
        return self.PI * (self.__raio ** 2)

    def imprimirDados(self, nome):
        print(f"[{nome}] Raio: {self.getRaio()} | Centro: {self.getCentro()} | Área: {self.calcularArea():.2f}")





    def getRaio(self):
        return self.__raio

    def setRaio(self, raio):
        if raio >= 0:
            self.__raio = float(raio)
        else:
            print("Erro: O raio não pode ser negativo!")

    def getCentro(self):
        return f"({self.__centroX}, {self.__centroY})"

    def setCentro(self, centroX, centroY):
        self.__centroX = float(centroX)
        self.__centroY = float(centroY)