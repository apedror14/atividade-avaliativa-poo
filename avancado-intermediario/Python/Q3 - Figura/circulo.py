from figura import Figura
class Circulo(Figura):

    def __init__(self,x:float,y:float,raio:float):
        super().__init__(x,y)
        print("Criando círculo...")
        self.__raio = raio
        
    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, novo_raio:float):
        self.__raio = novo_raio
        
    def desenhar(self):
        print(f"Desenhando um círculo na posição [{self.x},{self.y}] com raio de {self.__raio}")