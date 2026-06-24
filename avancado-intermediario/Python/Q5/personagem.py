from objeto import Objeto
from movimento import Movimento

class Personagem(Objeto, Movimento):

    def __init__(self, nome, x = 0.0, y = 0.0):
        super().__init__(x, y)
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def mover(self, x, y):
        self.setX(x)
        self.setY(y)

    def __str__(self):
        return (f"{super().__str__()}"
                f"Nome = {self.getNome()}")
