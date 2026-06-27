from figura import Figura
class Retangulo(Figura):

    def __init__(self,x:float,y:float,base:float,altura:float):
        super().__init__(x,y)
        print("Criando Retângulo...")
        self.__base = base
        self.__altura = altura

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, nova_base: float):
        self.__base = nova_base

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, nova_altura: float):
        self.__altura = nova_altura
    def desenhar(self):
        print(f"Desenhando um Retângulo na posição [{self.x},{self.y}] com base {self.__base} e altura {self.__altura}")