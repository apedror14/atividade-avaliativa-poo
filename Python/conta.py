class Conta:
       
    def get_banco(self):
        return self.banco
    def set_banco(self, banco):
        self.banco = banco

    def get_numero(self):
        return self.numero
    def set_numero(self, numero):
        self.numero = numero

    def __init__(self, banco, numero):
        self.banco = banco
        self.numero = numero


    def transferir(self, valor, banco_ou_conta, numero):
        if numero == None:
            print(f"Transferindo R${valor} para o banco {banco_ou_conta.get_banco()} com número de conta {banco_ou_conta.get_numero()}")
        else:
            print(f"Transferindo R${valor} para o banco {banco_ou_conta} com número de conta {numero}")

