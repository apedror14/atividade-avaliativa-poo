class NumeroComplexo:

    def __init__(self, parteReal, parteImaginaria):
        self.__parteReal = parteReal
        self.__parteImaginaria = parteImaginaria

    def somar(self, outroComplexo):
        self.__parteReal += outroComplexo.getParteReal()
        self.__parteImaginaria += outroComplexo.getParteImaginaria()

    def subtrair(self, outroComplexo):
        self.__parteReal -= outroComplexo.getParteReal()
        self.__parteImaginaria -= outroComplexo.getParteImaginaria()

    def imprimir(self):
        if self.__parteImaginaria >= 0:
            print(f"{self.__parteReal} + i{self.__parteImaginaria}")
        else:
            print(f"{self.__parteReal} - i{abs(self.__parteImaginaria)}")



    def getParteReal(self):
        return self.__parteReal

    def setParteReal(self, parteReal):
        self.__parteReal = parteReal

    def getParteImaginaria(self):
        return self.__parteImaginaria

    def setParteImaginaria(self, parteImaginaria):
        self.__parteImaginaria = parteImaginaria

