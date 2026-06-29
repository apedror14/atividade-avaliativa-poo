from pais import Pais

# Programa Principal

#   - Região Sul:         Argentina, Paraguai, Uruguai
#   - Região Centro-Oeste: Bolívia, Paraguai, Peru (indiretamente), Argentina
#     (os diretamente limítrofes são: Bolívia, Paraguai, Argentina)
def main():
    brasil = Pais('BRA', 'Brasil', 8_515_767.049)
    brasil.setPopulacao(213_000_000)

    # Argentina
    argentina = Pais('ARG', 'Argentina', 2_780_400.0)
    argentina.setPopulacao(45_610_000)

    # Paraguai
    paraguai = Pais('PRY', 'Paraguai', 406_752.0)
    paraguai.setPopulacao(7_360_000)

    # Uruguai
    uruguai = Pais('URY', 'Uruguai', 176_215.0)
    uruguai.setPopulacao(3_530_000)

    # Bolívia
    bolivia = Pais('BOL', 'Bolívia', 1_098_581.0)
    bolivia.setPopulacao(12_080_000)

    # Peru
    peru = Pais('PER', 'Peru', 1_285_216.0)
    peru.setPopulacao(33_000_000)

    # Chile
    chile = Pais('CHL', 'Chile', 756_102.0)
    chile.setPopulacao(19_500_000)

    # Configuração das fronteiras
    brasil.adicionarFronteira(argentina)
    brasil.adicionarFronteira(paraguai)
    brasil.adicionarFronteira(uruguai)
    brasil.adicionarFronteira(bolivia)

    argentina.adicionarFronteira(brasil)
    argentina.adicionarFronteira(paraguai)
    argentina.adicionarFronteira(uruguai)
    argentina.adicionarFronteira(bolivia)
    argentina.adicionarFronteira(chile)

    paraguai.adicionarFronteira(brasil)
    paraguai.adicionarFronteira(argentina)
    paraguai.adicionarFronteira(bolivia)

    uruguai.adicionarFronteira(brasil)
    uruguai.adicionarFronteira(argentina)

    bolivia.adicionarFronteira(brasil)
    bolivia.adicionarFronteira(argentina)
    bolivia.adicionarFronteira(paraguai)
    bolivia.adicionarFronteira(peru)
    bolivia.adicionarFronteira(chile)

    peru.adicionarFronteira(bolivia)
    peru.adicionarFronteira(chile)

    chile.adicionarFronteira(argentina)
    chile.adicionarFronteira(bolivia)
    chile.adicionarFronteira(peru)

    # Países de fronteira com o Sul e Centro-Oeste do Brasil
    paisesFronteiraBrasil = [argentina, paraguai, uruguai, bolivia]

    # Percorre imprimindo nome e densidade
    print('=' * 60)
    print('  FRONTEIRAS COM O SUL E CENTRO-OESTE DO BRASIL')
    print('=' * 60)
    for pais in paisesFronteiraBrasil:
        print(f'\nNome               : {pais.getNome()}')
        print(f'Densidade Popul.   : {pais.getDensidadePopulacional():.2f} hab./km²')

    print('\n  DEMONSTRAÇÕES ADICIONAIS')

    # Igualdade semântica
    brasil2 = Pais('BRA', 'Brazil', 8_515_767.049)
    print(f'\n[Igualdade semântica]')
    print(f'  brasil.equals(brasil2)  {brasil.equals(brasil2)}')    # True (mesmo ISO)
    print(f'  brasil.equals(peru)     {brasil.equals(peru)}')       # False

    # Limítrofe
    print(f'\n[Limítrofe]')
    print(f'  Brasil faz fronteira com Argentina?  {brasil.ehLimitrofe(argentina)}')
    print(f'  Brasil faz fronteira com Peru?       {brasil.ehLimitrofe(peru)}')

    # Vizinhos comuns
    print(f'\n[Vizinhos comuns: Brasil x Argentina]')
    vizinhosComuns = brasil.getVizinhosComuns(argentina)
    if vizinhosComuns:
        for v in vizinhosComuns:
            print(f'  - {v.getNome()}')
    else:
        print('  Nenhum vizinho em comum.')

    # __str__ de um país
    print(f'\n[Representação em string — Bolívia]')
    print(bolivia)



if __name__ == '__main__':
    main()