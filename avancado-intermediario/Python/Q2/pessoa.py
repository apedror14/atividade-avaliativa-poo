class Pessoa:
    def __init__(self, nome: str, pai: 'Pessoa' = None, mae: 'Pessoa' = None):
        self.__nome = nome
        self.__pai = pai
        self.__mae = mae

    def getNome(self) -> str:
        return self.__nome

    def getPai(self) -> 'Pessoa':
        return self.__pai

    def getMae(self) -> 'Pessoa':
        return self.__mae

    def verificarIgualdadeSemantica(self, outraPessoa: 'Pessoa') -> bool:
        if outraPessoa is None:
            return False
        mesmoNome = self.__nome == outraPessoa.getNome()
        mesmoPai = self.__pai is outraPessoa.getPai()
        mesmaMae = self.__mae is outraPessoa.getMae()
        return mesmoNome and mesmoPai and mesmaMae

    def verificarIrmandade(self, outraPessoa: 'Pessoa') -> bool:
        if outraPessoa is None or self.verificarIgualdadeSemantica(outraPessoa):
            return False
        
        mesmoPai = self.__pai is not None and self.__pai.verificarIgualdadeSemantica(outraPessoa.getPai())
        mesmaMae = self.__mae is not None and self.__mae.verificarIgualdadeSemantica(outraPessoa.getMae())
        
        return mesmoPai or mesmaMae

    def verificarAncestralidade(self, possivelAncestral: 'Pessoa') -> bool:
        if possivelAncestral is None:
            return False

        if (self.__pai is not None and self.__pai.verificarIgualdadeSemantica(possivelAncestral)) or \
           (self.__mae is not None and self.__mae.verificarIgualdadeSemantica(possivelAncestral)):
            return True

        ancestralPeloPai = self.__pai is not None and self.__pai.verificarAncestralidade(possivelAncestral)
        ancestralPelaMae = self.__mae is not None and self.__mae.verificarAncestralidade(possivelAncestral)

        return ancestralPeloPai or ancestralPelaMae

    def __str__(self) -> str:
        nomePai = self.__pai.getNome() if self.__pai is not None else "desconhecido(a)"
        nomeMae = self.__mae.getNome() if self.__mae is not None else "desconhecido(a)"
        return "Nome: " + self.__nome + ", Pai: " + nomePai + ", Mãe: " + nomeMae

