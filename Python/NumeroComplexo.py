class NumeroComplexo:

    def __init__(self, parteReal, parteImaginaria):
        self.__parteReal = parteReal
        self.__parteImaginaria = parteImaginaria

    def somar(self, outroComplexo):
        novoReal = self.__parteReal + outroComplexo.getParteReal()
        novoImaginario = self.__parteImaginaria + outroComplexo.getParteImaginaria()
        return NumeroComplexo(novoReal, novoImaginario)

    def subtrair(self, outroComplexo):
        novoReal = self.__parteReal - outroComplexo.getParteReal()
        novoImaginario = self.__parteImaginaria - outroComplexo.getParteImaginaria()
        return NumeroComplexo(novoReal, novoImaginario)

    def imprimir(self):
        if self.__parteImaginaria >= 0:
            print(f"{self.__parteReal} + {self.__parteImaginaria}i")
        else:
            print(f"{self.__parteReal}  {self.__parteImaginaria}i")



    def getParteReal(self):
        return self.__parteReal

    def setParteReal(self, parteReal):
        self.__parteReal = parteReal

    def getParteImaginaria(self):
        return self.__parteImaginaria

    def setParteImaginaria(self, parteImaginaria):
        self.__parteImaginaria = parteImaginaria

