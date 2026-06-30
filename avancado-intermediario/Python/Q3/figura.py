class Figura:

    def __init__(self,x:float,y:float):
        print("Criando figura")
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, novo_x:float):
        self.__x = novo_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, novo_y:float):
        self.__y = novo_y
    
    def desenhar(self):
        print(f"Desenhando uma figura na posição ({self.__x}, {self.__y})")

    def __str__(self) -> str:
        return f"Figura na posição ({self.__x}, {self.__y})"