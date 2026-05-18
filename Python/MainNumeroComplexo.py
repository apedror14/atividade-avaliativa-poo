import NumeroComplexo

nc1 = NumeroComplexo.NumeroComplexo(5, 3)
nc2 = NumeroComplexo.NumeroComplexo(2, 4)
nc1.imprimir()
nc2.imprimir()

resultadoSoma = nc1.somar(nc2)
print("Resultado da Soma: ")
resultadoSoma.imprimir()

resultadoSubtracao = nc1.subtrair(nc2)
print("Resultado da Subtração: ")
resultadoSubtracao.imprimir()


