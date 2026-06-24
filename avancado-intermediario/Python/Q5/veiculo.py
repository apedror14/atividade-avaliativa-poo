from objeto import Objeto
from movimento import Movimento

class Veiculo(Objeto, Movimento):

    def __init__(self, cor, x = 0.0, y = 0.0):
        super().__init__(x, y)
        self.__cor = cor

    def getCor(self):
        return self.__cor

    def mover(self, x, y):
        self.setX(x)
        self.setY(y)

    def __str__(self):
        return (f"{super().__str__()}"
                f"Cor = {self.getCor()}")