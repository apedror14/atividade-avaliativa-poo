# IMPORTANTE!!
```
Ao terminarem suas questões, adicionem às pastas JAVA e PYTHON apenas o arquivo referente à CLASSE e sua MAIN.
```

# Apresentação

Os exercícios apresentados a seguir fazem parte dos instrumentos de avaliação da disciplina de Programação Orientada a Objetos para o NAP I (Nota de Avaliação Parcial I). No caso, referem-se ao critério de avaliação denominado “exercícios em sala em dupla” e correspondem a 30% da nota final. No entanto, em razão do contexto atual de infraestrutura, o mesmo será aplicado em grupo, como tarefa do SIGAA.

Os exercícios devem ser respondidos em duas linguagens de programação, Python e Java. Cada solução corresponderá a um visto, certo ou errado. Então a nota final desse critério de avaliação corresponderá à proporção do número de acertos. Por exemplo:

* considerando que até o final do NAP I dez exercícios sejam aplicados
* então das 20 respostas esperadas, dez em Java e dez em Python, 18 respostas estejam corretas
* a nota final no critério “exercícios em sala em dupla” será 9 (nove)
* considerando que esse critério corresponde a 30% da nota final
* essa nota corresponderá a 2,7 pontos na nota final do NAP I
 
## Orientações de Submissão da Resposta

A submissão da solução será através de uma tarefa do SIGAA, que pode ser acessada a partir do menu “Atividades >> Tarefas”. Nessa operação, a equipe deve submeter um único arquivo, com limite de tamanho de 10Mb, conforme restrições da plataforma.

Assim, antes de submeter a tarefa, cada equipe precisará seguir as orientações
abaixo:

* Reunir todos os arquivos em Java produzidos para cada exercício, ou seja, classe da solução e mais a classe principal que manipula os objetos da solução
* Reunir todos os arquivos em Python produzidos para cada exercício, ou seja, arquivo da classe da solução e mais arquivo do programa principal que manipula os objetos da solução
* Compactar os arquivos é um único arquivo em formato ZIP, RAR ou 7z

### Exercício 1

Criar a classe `Ponto2D` que representa um ponto no plano cartesiano. Além dos atributos encapsulados por você identificados, a classe deve oferecer os seguintes métodos:
 
*   **Construtor** que permitam a inicialização do ponto, num local indicado por dois parâmetros do tipo `double`, indicando o valor de abcissa e ordenada do ponto que está sendo criado;
*   **Métodos de acesso (getter/setter)** dos atributos do ponto por você identificado;
*   **Métodos sobrecarregados de movimentação** do ponto com os mesmos parâmetros indicados para os construtores, ou seja, o ponto “sai” de uma localização e “vai” para a localização nova;
*   **Método que permita calcular a distância** do ponto que recebe a mensagem, para um outro ponto (objeto) informado;
*   **Método que permita a criação de um novo ponto** no mesmo local do ponto que recebeu a mensagem (clonar).
 
Considere implementar uma classe/programa principal que instancia/crie dois distintos e imprima as coordenadas dos pontos instanciados, bem como:

*   imprima a distância entre os pontos
*   clone um do pontos e movimente o ponto clonado para uma localização distinta

**Atenção aos padrões de nomenclatura da classe e de seus atributos e métodos, que devem considerar o padrão CamelCase.**
 
### Exercício 2

Criar a classe `Livro` abaixo com os seguintes atributos encapsulados:

*   `Título` como texto
*   `Autor` como texto
*   `Ano de publicação` como inteiro
*   `Número de páginas` como inteiro
*   `Peso` como real
*   `Volume` como real
 
Adicionar na classe:

*   método **construtor** que inicializa todos os atributos
*   métodos **acessores (getter e setter)**
*   método `marcarPagina(numero)`, cujo comportamento imprima a mensagem:
    *   `"Livro marcado na página " + numero`
        *   quando o número da página existir no livro
    *   `"Página inválida!"`
        *   quando o número da página não existir no livro

Considere implementar uma classe/programa principal que instancia/crie dois livros e imprima o título e ano de publicação dos livros instanciados/criados, bem como marque uma página de cada livro criado.

**Atenção aos padrões de nomenclatura da classe e de seus atributos e métodos, que devem considerar o padrão CamelCase.**

### Exercício 3

Criar a classe `NumeroComplexo`, que representa um número complexo. Além dos atributos encapsulados por você identificados, a classe deve fornecer as seguintes operações:
 
*   **Construtor** com valores das partes imaginária e real;
*   **Métodos getter/setter** para os atributos da parte inteira e parte imaginária;
*   **Método `somar`**, que recebe outro número complexo e o adiciona ao número complexo que recebeu a mensagem. `(a+bi)+(c+di) = (a+c)+(b+d)i`;
*   **Método `subtrair`**, que recebe outro número complexo e o subtrai do número complexo que recebeu a mensagem. `(a+bi)−(c+di) =(a−c)+(b−d)i`;
*   **Um método que imprima** uma representação do número complexo, ou seja: `a + ib`, onde `a` é a parte real e `b` é a parte imaginária.
 
Considere implementar uma classe/programa principal que instancia/crie dois número complexos e imprima a representação dos números instanciados/criados, bem como:

*   some os números e imprima o resultado dessa soma
*   subtraia os números e imprima o resultado dessa subtração

**Atenção aos padrões de nomenclatura da classe e de seus atributos e métodos, que devem considerar o padrão CamelCase.**
 
 
### Exercício 4

Criar a classe `Conta` com os seguintes atributos encapsulados (privados) e seus respectivos métodos acessores (getter e setter públicos):

*   `Banco` como inteiro
*   `Número` como texto
 
Adicionar na classe:

*   método **construtor** que inicializa todos os atributos dessa classe
*   criar os **métodos sobrecarregados** a seguir, que imprimam a mensagem:
    *   `"Transferindo " + <VALOR> + " para conta " + <CONTA>`
        *   `<VALOR>` é o valor informado para transferência
        *   `<CONTA>` são os dados da conta: banco e número
 
Métodos sobrecarregados:

*   `transferir(banco, número, valor)`
    *   Dados da conta (banco e número)
*   `transferir(conta, valor)`
    *   Um outro objeto conta
 
Considere implementar uma classe/programa principal que instancia/crie duas contas e imprima os dados de cada conta, bem como simule o uso de cada método “transferir” sobrecarregado, ou seja:

*   transferir um valor usando um objeto conta como destinatário da transferência
*   transferir um valor usando os dados (banco e número) da conta destinatária na transferência
 
 
### Exercício 5

Criar a classe `Circulo` que representa um círculo no plano cartesiano. Para tanto, além dos atributos encapsulados por você identificados, considere adicionar na classe os seguintes métodos:
 
*   Um **construtor** que receba o raio e as coordenadas do centro do círculo.
*   **Método de acesso (getter)** para:
    *   raio do círculo (`double`)
    *   centro do círculo (`texto`)
*   Métodos `inflar` e `desinflar`, que, respectivamente, aumentam e diminuem o raio do círculo de um valor informado.
    *   Obs.: o centro do círculo permanece inalterado.
*   **Métodos sobrecarregados** para `inflar` e `desinflar`, que respectivamente, aumentam e diminuem o raio do círculo de uma unidade.
    *   Obs.: o centro do círculo permanece inalterado.
*   **Métodos sobrecarregados para mover** o círculo, que:
    *   por padrão (sem parâmetros) levam o centro do círculo para a origem do espaço 2D.
    *   movem o círculo para um local indicado por dois parâmetros do tipo `double`, indicando o valor de abcissa e ordenada do ponto, do centro do círculo, para onde se move.
    *   Obs: o raio permanece inalterado ao mover o círculo.
*   Método que retorna a **área do círculo**.
 
Considere implementar uma classe/programa principal que instancia/crie dois círculos e imprima os dados de cada círculo (raio, centro e área), bem como:

*   infle cada um dos círculos usando os métodos sobrecarregados criados
*   imprima os dados dos círculos após inflá-los
*   desinfle cada um dos círculos usando os métodos sobrecarregados criados
*   imprima os dados dos círculos após desinflá-los
