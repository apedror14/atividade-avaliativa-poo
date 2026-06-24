from objeto import Objeto

class Arvore(Objeto):

    def __init__(self, altura, x = 0.0, y = 0.0):
        super().__init__(x, y)
        self.__altura = altura

    def getAltura(self):
        return self.__altura

    def __str__(self):
        return (f"{super().__str__()}"
                f"Altura = {self.getAltura()}")