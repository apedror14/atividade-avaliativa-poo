class Conta:
    def __init__(self, banco, numero):
        self.__banco = int(banco)
        self.__numero = str(numero)

    def getBanco(self):
        return self.__banco

    def setBanco(self, banco):
        self.__banco = int(banco)

    def getNumero(self):
        return self.__numero

    def setNumero(self, numero):
        self.__numero = str(numero)

    def transferir(self, arg1, arg2, arg3=None):
        if arg3 is not None:
            banco = arg1
            numero = arg2
            valor = arg3
            print(f"Transferindo {valor} para conta Banco: {banco}, Numero: {numero}")
        else:
            conta_destino = arg1
            valor = arg2
            print(f"Transferindo {valor} para conta Banco: {conta_destino.getBanco()}, Numero: {conta_destino.getNumero()}")
