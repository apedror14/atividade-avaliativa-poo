import random

from veiculo import Veiculo
from arvore import Arvore
from personagem import Personagem

class Main:
    listaDeObjetosDoJogo = [Arvore(10), Arvore(20), Veiculo("Azul"), Veiculo("Verde"), Personagem("knight"),
                            Personagem("Hornet")]

    for objeto in listaDeObjetosDoJogo:
        print(objeto)
        print()

    listaDeMovimento = [Personagem("Sans"), Veiculo("Verde"), Personagem("Papyrus")]

    for objeto in listaDeMovimento:
        objeto.mover(round(random.uniform(0.0, 10.0)), round(random.uniform(0.0, 10.0)))
        print(objeto)
        print()

