from universidade import Universidade

class UniversidadeFisica(Universidade):

    def __init__(self, nome, campus):
        super().__init__(nome)
        self.__campus = campus

    def getCampus(self):
        return self.__campus

    def setCampus(self, campus):
        self.__campus = campus

    def aplicarAvaliacao(self):
        print(f"Avaliações presenciais no campus {self.getCampus()}")