from universidade import Universidade

class UniversidadeEaD(Universidade):

    def __init__(self, nome, urlPlataforma):
        super().__init__(nome)
        self.__urlPlataforma = urlPlataforma

    def getUrlPlataforma(self):
        return self.__urlPlataforma

    def setUrlPlataforma(self, urlPlataforma):
        self.__urlPlataforma = urlPlataforma

    def aplicarAvaliacao(self):
        print(f"Avaliações Online na {self.getUrlPlataforma()}")

