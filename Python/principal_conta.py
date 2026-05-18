from conta import Conta

conta1 = Conta("001", "12345-6")
conta2 = Conta("002", "98765-4")

print(f"Conta 1: Banco {conta1.get_banco()}, Número {conta1.get_numero()}")
print(f"Conta 2: Banco {conta2.get_banco()}, Número {conta2.get_numero()}")

conta2.transferir(100, conta1, None)

conta2.transferir(50, "002", "98765-4")

