from pais import Pais

def main():
    brasil = Pais('BRA', 'Brasil', 8_515_767.049)
    brasil.setPopulacao(213_000_000)

    argentina = Pais('ARG', 'Argentina', 2_780_400.0)
    argentina.setPopulacao(45_610_000)

    paraguai = Pais('PRY', 'Paraguai', 406_752.0)
    paraguai.setPopulacao(7_360_000)

    uruguai = Pais('URY', 'Uruguai', 176_215.0)
    uruguai.setPopulacao(3_530_000)

    bolivia = Pais('BOL', 'Bolívia', 1_098_581.0)
    bolivia.setPopulacao(12_080_000)

    peru = Pais('PER', 'Peru', 1_285_216.0)
    peru.setPopulacao(33_000_000)

    chile = Pais('CHL', 'Chile', 756_102.0)
    chile.setPopulacao(19_500_000)

    brasil.adicionarFronteira(argentina)
    brasil.adicionarFronteira(paraguai)
    brasil.adicionarFronteira(uruguai)
    brasil.adicionarFronteira(bolivia)
    brasil.adicionarFronteira(peru)

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

    paisesFronteiraBrasil = [argentina, paraguai, uruguai, bolivia, peru]

    print('=' * 60)
    print('  FRONTEIRAS COM O SUL E CENTRO-OESTE DO BRASIL')
    print('=' * 60)
    for pais in paisesFronteiraBrasil:
        print(f'\nNome               : {pais.getNome()}')
        print(f'Densidade Popul.   : {pais.getDensidadePopulacional():.2f} hab./km²')

    print('\n  DEMONSTRAÇÕES ADICIONAIS')

    brasil2 = Pais('BRA', 'Brazil', 8_515_767.049)
    print(f'\n[Igualdade semântica]')
    print(f'  brasil.equals(brasil2)  {brasil.equals(brasil2)}')    
    print(f'  brasil.equals(peru)     {brasil.equals(peru)}')       

    print(f'\n[Limítrofe]')
    print(f'  Brasil faz fronteira com Argentina?  {brasil.ehLimitrofe(argentina)}')
    print(f'  Brasil faz fronteira com Peru?       {brasil.ehLimitrofe(peru)}')

    print(f'\n[Vizinhos comuns: Brasil x Argentina]')
    vizinhosComuns = brasil.getVizinhosComuns(argentina)
    if vizinhosComuns:
        for v in vizinhosComuns:
            print(f'  - {v.getNome()}')
    else:
        print('  Nenhum vizinho em comum.')

    print(f'\n[Representação em string — Bolívia]')
    print(bolivia)



if __name__ == '__main__':
    main()
