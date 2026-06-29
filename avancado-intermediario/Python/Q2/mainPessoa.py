from pessoa import Pessoa

# Construtores sobrecarregados - teste com diferentes parâmetros

# Sem ancestrais
joaquim = Pessoa("Joaquim")
ana = Pessoa("Ana")
jaco = Pessoa("Jaco")

# Com ancestrais
maria = Pessoa("Maria", joaquim, ana)
jose = Pessoa("Jose", jaco, None)

# Com ancestrais (pai e mãe)
jesus = Pessoa("Jesus Cristo", jose, maria)

# Teste de instanciação
print("Instanciação usando diferentes tipos de construtor:")
print(joaquim)
print(maria)
print(jesus)
print()

# Testes de ancestral
print("Testando ancestrais:")
print("Joaquim é ancestral de Jesus Cristo?", joaquim.eAncestral(jesus))
print("Ana é ancestral de Jesus Cristo?", ana.eAncestral(jesus))
print("Jacó é ancestral de Jesus Cristo?", jaco.eAncestral(jesus))
print("Maria é ancestral de Jesus Cristo?", maria.eAncestral(jesus))
print("José é ancestral de Jesus Cristo?", jose.eAncestral(jesus))
print()

# Testes de irmãos
print("Testando irmãos:")
print("Joaquim é irmão de Jacó?", jaco.saoIrmas(joaquim))
print("Jesus é irmão de Maria?", maria.saoIrmas(jesus))