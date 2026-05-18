import NumeroComplexo

nc1 = NumeroComplexo.NumeroComplexo(5, 3)
nc2 = NumeroComplexo.NumeroComplexo(2, 4)

print("Números originais:")
nc1.imprimir()
nc2.imprimir()

nc1.somar(nc2)
print("Resultado da Soma: ")
nc1.imprimir()

nc1.setParteReal(5)
nc1.setParteImaginaria(3)

nc1.subtrair(nc2)
print("Resultado da Subtração: ")
nc1.imprimir()
