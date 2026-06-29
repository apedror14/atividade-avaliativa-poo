class Pessoa:
    def __init__(self,nome, pai=None, mae=None):
        self.__nome = nome
        self.__mae = mae
        self.__pai = pai

    def getNome(self):
        return self.__nome

    def getPai(self):
        return self.__pai

    def getMae(self):
        return self.__mae

    def igualdadeSemantica(self, outraPessoa):
        if outraPessoa is None:
            return False
        return (outraPessoa.getNome() == self.__nome and
                outraPessoa.getPai() == self.__pai and
                outraPessoa.getMae() == self.__mae)




    def saoIrmas(self, outraPessoa):
        if self.igualdadeSemantica(outraPessoa):
            return False

        if (self.__pai != None and self.__pai == outraPessoa.getPai()):
            return True
        else:
            if (self.__mae != None and self.__mae == outraPessoa.getMae()):
                return True
            else:
                return False



    def eAncestral(self, outraPessoa):
        if outraPessoa is None:
            return False

        paiDaOutra = outraPessoa.getPai()
        maeDaOutra = outraPessoa.getMae()

        if (paiDaOutra is not None and self == paiDaOutra) or \
           (maeDaOutra is not None and self == maeDaOutra):
            return True

        if paiDaOutra is not None:
            if self.eAncestral(paiDaOutra):
                return True

        if maeDaOutra is not None:
            if self.eAncestral(maeDaOutra):
                return True

        return False

    def __str__(self):
        return "Nome: " + self.__nome

    def __eq__(self, outraPessoa):
        if outraPessoa is None or not isinstance(outraPessoa, Pessoa):
            return False
        return (self.__nome == outraPessoa.getNome() and
                self.__pai == outraPessoa.getPai() and
                self.__mae == outraPessoa.getMae())
