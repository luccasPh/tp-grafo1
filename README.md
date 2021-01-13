<dl>
<p><strong>
UNIVERSIDADE ESTADUAL DO PIAUÍ<br>
CENTRO DE TECNOLOGIA E URBANISMO<br>
CIÊNCIA DA COMPUTAÇÃO<br>
TEORIA DOS GRAFOS<br>
Prof. Marcus Vinicius<br>

<p>2018-2</p>
</strong></p>
</dl>

### TRABALHO PRATICO I – BUSCA EM LARGURA

**por Lucas Pinheiro de Oliveira**

---

#### 1. DESCRIÇÃO

Ajude um rato a encontrar um pedaço de queijo num labirinto como o do
desenho abaixo:

![](mazebfs/image/ilustracao.png)

Um labirinto desses pode ser representado por uma matriz retangular ![](mazebfs/image/math2.png),
cujo elemento ![](mazebfs/image/math1.png) vale 0 ou −1 conforme a casa correspondente do labirinto
seja uma passagem livre ou uma parede, respectivamente.
O labirinto (de tamanho ![](mazebfs/image/math3.png)) deve ser criado dinamicamente por meio
da leitura de um arquivo texto. O arquivo deve conter exatamente ![](mazebfs/image/math4.png) linhas por
![](mazebfs/image/math5.png) colunas de números inteiros, com valor 0 ou −1 para indicar espaço livre ou
não (respectivamente) no labirinto.
O objetivo do trabalho é desenvolver um programa, baseado na Busca
em Largura, para, a partir de um ponto inicial, encontrar o menor caminho que
o rato deve seguir até alcançar o queijo.

### 2. FUNCIONALIDADES

- a. O programa deve permitir que o usuário possa carregar um novo
  arquivo de configuração de labirinto antes de executar a busca;

- b. O programa deve solicitar a definição da posição inicial do rato, bem
  como da localização do queijo.

### 3. REQUISITOS NÃO FUNCIONAIS

- a. Além da implementação do algoritmo de busca, o programa deverá
  conter um módulo de interface com o usuário, para exibir uma
  animação correspondente à solução encontrada. Existem boas
  bibliotecas disponíveis para a maioria das linguagens, como a
  PyGame (Python), Allegro (C/C++), JMonkeyEngine (Java), Unity
  (C#), dentre outros.

No casso desta aplicação foi utilizado Python com PyQt4

### 4. COMO RODA ESTA APLICAÇÃO

```sh
    # Clone o repositório
    $ git clone https://github.com/luccasPh/tp-grafo1.git && cd tp-grafo1

    # Instale o virtualenv
    $ pip install virtualenv

    # Crie uma nova virtualenv
    $ virtualenv nome_da_virtualenv

    # Ative a nova virtualenv
    $ source nome_da_virtualenv/bin/activate

    # Instale as dependência
    $ pip install -r requirements.txt

    # executar a aplicação
    $ python main.py
```
