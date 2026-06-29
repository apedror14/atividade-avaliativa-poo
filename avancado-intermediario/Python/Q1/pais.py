class Pais:
    def __init__(self, codigoIso: str, nome: str, dimensaoKm2: float):
        """código ISO, o nome e a dimensão do país.
        população começa com 0 e a lista de fronteiras começa vazia.
        """
        self.__codigoIso = codigoIso
        self.__nome = nome
        self.__dimensaoKm2 = dimensaoKm2
        self.__populacao = 0
        self.__paisesFronteira = []


    # Getters e Setters
    def getCodigoIso(self) -> str:
        return self.__codigoIso

    def setCodigoIso(self, codigoIso: str):
        self.__codigoIso = codigoIso

    def getNome(self) -> str:
        return self.__nome

    def setNome(self, nome: str):
        self.__nome = nome

    def getPopulacao(self) -> int:
        return self.__populacao

    def setPopulacao(self, populacao: int):
        self.__populacao = populacao

    def getDimensaoKm2(self) -> float:
        return self.__dimensaoKm2

    def setDimensaoKm2(self, dimensaoKm2: float):
        self.__dimensaoKm2 = dimensaoKm2

    # Igualdade semântica

    def equals(self, outroPais: 'Pais') -> bool:
        if not isinstance(outroPais, Pais):
            return False
        return self.__codigoIso == outroPais.__codigoIso

    # Adiciona um país à lista de fronteiras

    def adicionarFronteira(self, pais: 'Pais'):
        for p in self.__paisesFronteira:
            if p.equals(pais):
                return  # Evita duplicatas
        self.__paisesFronteira.append(pais)

    # Verifica se um país é limítrofe

    def ehLimitrofe(self, pais: 'Pais') -> bool:
        for p in self.__paisesFronteira:
            if p.equals(pais):
                return True
        return False

    # Densidade populacional

    def getDensidadePopulacional(self) -> float:
        if self.__dimensaoKm2 == 0:
            return 0.0
        return self.__populacao / self.__dimensaoKm2

    # Vizinhos comuns entre dois países

    def getVizinhosComuns(self, outroPais: 'Pais') -> list:
        vizinhosComuns = []
        for p in self.__paisesFronteira:
            if outroPais.ehLimitrofe(p):
                vizinhosComuns.append(p)
        return vizinhosComuns

    # Representação em string

    def __str__(self) -> str:
        fronteiras = ", ".join(p.getNome() for p in self.__paisesFronteira) if self.__paisesFronteira else 'Nenhuma'
        return (
            f'País: {self.__nome} ({self.__codigoIso})\n'       
            f'  População   : {self.__populacao:,} hab.\n'
            f'  Dimensão    : {self.__dimensaoKm2:,.3f} km²\n'
            f'  Densidade   : {self.getDensidadePopulacional():.2f} hab./km²\n'
            f'  Fronteiras  : {fronteiras}'
        )