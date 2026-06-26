from universidade import Universidade
from universidade_ead import UniversidadeEaD
from universidade_fisica import UniversidadeFisica

class Main:

    listaDeUniversidades = [UniversidadeFisica("UFRA", "Belém"),
                            UniversidadeEaD("UNAMA", "www.unama.com.br"),
                            UniversidadeFisica("UFPA", "Ananindeua"),
                            UniversidadeEaD("Estácio", "www.estacio.com.br")]

    for objeto in listaDeUniversidades:
        print(objeto.getNome())
        objeto.aplicarAvaliacao()
        print()