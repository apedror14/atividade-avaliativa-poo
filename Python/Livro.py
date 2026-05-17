class Livro:
    def __init__(self, titulo, autor, anoDePublicacao, numeroDePaginas, peso, volume):
        self.__titulo = titulo
        self.__autor = autor
        self.__anoDePublicacao = anoDePublicacao
        self.__numeroDePaginas = numeroDePaginas
        self.__peso = peso
        self.__volume = volume

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getAnoDePublicacao(self):
        return self.__anoDePublicacao

    def getNumeroDePaginas(self):
        return self.__numeroDePaginas

    def getPeso(self):
        return self.__peso

    def getVolume(self):
        return self.__volume

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setAutor(self, autor):
        self.__autor = autor

    def setAnoDePublicacao(self, anoDePublicacao):
        self.__anoDePublicacao = anoDePublicacao

    def setNumeroDePaginas(self, numeroDePaginas):
        self.__numeroDePaginas = numeroDePaginas

    def setPeso(self, peso):
        self.__peso = peso

    def setVolume(self, volume):
        self.__volume = volume

    def marcarPagina(self, numero):
        if numero >= 1 and numero <= self.__numeroDePaginas:
            print("Livro marcado na página " + str(numero))
        else:
            print("Página inválida!")
