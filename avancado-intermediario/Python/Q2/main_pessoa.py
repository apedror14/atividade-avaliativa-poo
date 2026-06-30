from pessoa import Pessoa

def main():
    joaquim = Pessoa("Joaquim")
    ana = Pessoa("Ana")
    jaco = Pessoa("Jacó")

    maria = Pessoa("Maria", joaquim, ana)
    jose = Pessoa("José", jaco, None)

    jesus = Pessoa("Jesus Cristo", jose, maria)

    print("Instanciação usando diferentes tipos de construtor:")
    print(joaquim)
    print(maria)
    print(jesus)
    print()

    print("Testando ancestrais:")
    print("Joaquim é ancestral de Jesus Cristo?", jesus.verificarAncestralidade(joaquim))
    print("Ana é ancestral de Jesus Cristo?", jesus.verificarAncestralidade(ana))
    print("Jacó é ancestral de Jesus Cristo?", jesus.verificarAncestralidade(jaco))
    print("Maria é ancestral de Jesus Cristo?", jesus.verificarAncestralidade(maria))
    print("José é ancestral de Jesus Cristo?", jesus.verificarAncestralidade(jose))
    print()

    print("Testando irmãos:")
    print("Joaquim é irmão de Jacó?", joaquim.verificarIrmandade(jaco))
    print("Jesus é irmão de Maria?", jesus.verificarIrmandade(maria))

if __name__ == '__main__':
    main()
