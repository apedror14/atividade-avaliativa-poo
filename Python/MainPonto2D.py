from Ponto2D import Ponto2D


def main():

    # Criando dois pontos no plano cartesiano
    ponto1 = Ponto2D(3.0, 4.0)
    ponto2 = Ponto2D(-1.5, 7.5)

    print("Pontos criados:")
    print(f"  Ponto 1: {ponto1}")
    print(f"  Ponto 2: {ponto2}")

    # Exibindo as coordenadas separadamente usando os getters
    print("\nCoordenadas do Ponto 1:")
    print(f"  X = {ponto1.getAbcissa()}")
    print(f"  Y = {ponto1.getOrdenada()}")

    print("\nCoordenadas do Ponto 2:")
    print(f"  X = {ponto2.getAbcissa()}")
    print(f"  Y = {ponto2.getOrdenada()}")

    # Calculando a distância entre os dois pontos
    distancia = ponto1.calcularDistancia(ponto2)
    print(f"\nDistância entre os dois pontos: {distancia:.2f}")

    # Clonando o ponto 1 e movendo o clone
    pontoClone = ponto1.clonar()
    print(f"\nClone do Ponto 1 criado na posição {pontoClone}")

    pontoClone.mover(10.0, -5.0)
    print(f"Clone movido para: {pontoClone}")

    print(f"Ponto 1 continua em: {ponto1}")

    # Usando os setters para mover o ponto 2 até a origem
    print("\nMovendo o Ponto 2 para a origem...")
    ponto2.setAbcissa(0.0)
    ponto2.setOrdenada(0.0)
    print(f"Ponto 2 agora está em: {ponto2}")

    distanciaOrigem = ponto1.calcularDistancia(ponto2)
    print(f"Distância do Ponto 1 até a origem: {distanciaOrigem:.2f}")


if __name__ == "__main__":
    main()
