from Conta import Conta

def main():
    conta1 = Conta(123, "456789-0")
    conta2 = Conta(456, "987654-3")

    print(f"Conta 1: Banco {conta1.getBanco()}, Número {conta1.getNumero()}")
    print(f"Conta 2: Banco {conta2.getBanco()}, Número {conta2.getNumero()}")

    conta1.transferir(conta2, 200.0)
    conta1.transferir(456, "987654-3", 100.0)

if __name__ == "__main__":
    main()
