# MANUAL DO DESENVOLVEDOR - Guilda 4 (O Conselho de Missões)

*Atenção: Salve este documento como PDF antes de enviar.*

## 1. Identificação
**Grupo:** Guilda 4 — O Conselho de Missões
**Módulo:** Algoritmos de Busca e Ordenação
**Integrantes:** [Nomes dos Integrantes]

## 2. Introdução e Cenário
No mundo de Brasilândia, o Conselho de Missões gerencia um quadro de ameaças. Estas ameaças (missões) possuem diferentes atributos, como nível de dificuldade, recompensa em ouro e urgência. O objetivo deste sistema é organizar esse mural de missões e permitir que o conselho localize missões específicas rapidamente por meio de algoritmos de ordenação e busca implementados sem o uso de bibliotecas de ordenação prontas.

## 3. Especificação do Tipo Abstrato de Dados (TAD)
Para modelar o problema, criamos a classe **Missao** contendo os seguintes atributos lógicos:
- `codigo`: Inteiro que identifica unicamente a missão.
- `titulo`: Texto descritivo da missão.
- `grau_dificuldade`: Inteiro representando a dificuldade.
- `recompensa_ouro`: Inteiro com o valor em ouro da missão.
- `urgencia`: Inteiro indicando a prioridade da ameaça.

**Implementação adotada:** 
Foi adotada uma estrutura de **Vetor/Array** para armazenar as instâncias de Missão. Vetores são ideais para a Guilda 4, pois permitem acesso direto à memória (indexação em $O(1)$) que é o principal pré-requisito técnico para a execução eficiente de uma **Busca Binária**.

## 4. Explicação das Operações e Principais Trechos de Código
- **Ordenação Elementar (Selection Sort):** Percorre a lista, encontra o menor/maior elemento do subarray não ordenado e faz a troca com a posição atual. O código possui dois laços (loops) aninhados e utiliza variáveis para rastrear "comparações" e "movimentações".
- **Ordenação Eficiente (Quick Sort):** Usa a estratégia Divisão e Conquista. Um pivô é escolhido e o vetor é particionado de modo que os menores fiquem à esquerda e os maiores à direita. A função recursiva se chama nas sublistas resultantes. Contadores globais/referenciados foram utilizados para computar as operações.
- **Busca Linear:** Percorre sequencialmente do índice `0` ao `N-1`. Interrompe ao achar o código. Funciona em arrays desordenados.
- **Busca Binária:** Com o array obrigatoriamente ordenado pelo campo de busca (Código), a busca divide o espaço de procura ao meio a cada iteração, verificando se o código buscado é maior ou menor que o item no meio do vetor.

## 5. Análise de Eficiência, Complexidade e Comparativo

### Quadro Comparativo de Algoritmos (Selecionados e Não Selecionados)

| Algoritmo | Ideia Geral | Melhor Caso | Caso Médio | Pior Caso | Estabilidade | Uso de Memória (Adicional) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Selection Sort** (Escolhido) | Encontra repetidamente o mínimo da parte não ordenada e o coloca no final da parte ordenada. | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | Não Estável | $O(1)$ |
| **Quick Sort** (Escolhido) | Divisão e Conquista usando um pivô. Particiona a lista em "menores" e "maiores" que o pivô. | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | Não Estável | $O(\log n)$ a $O(n)$ (pilha) |
| **Bubble Sort** (Não Selecionado) | Troca elementos adjacentes repetidas vezes se estiverem na ordem errada, flutuando o maior. | $O(n)$ | $O(n^2)$ | $O(n^2)$ | Estável | $O(1)$ |
| **Insertion Sort** (Não Selecionado) | Constrói a lista ordenada elemento a elemento, inserindo cada novo item na posição correta. | $O(n)$ | $O(n^2)$ | $O(n^2)$ | Estável | $O(1)$ |
| **Shell Sort** (Não Selecionado) | Variante do Insertion que permite a troca de elementos distantes, reduzindo o "gap" com o tempo. | $O(n \log n)$ | Depende do gap | $O(n^2)$ | Não Estável | $O(1)$ |
| **Merge Sort** (Não Selecionado) | Divisão e Conquista. Divide o vetor em metades, ordena recursivamente e depois mescla (*merge*). | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | Estável | $O(n)$ (Arrays auxiliares) |
| **Heap Sort** (Não Selecionado) | Transforma o vetor numa árvore binária completa (Heap) e extrai repetidamente a raiz. | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | Não Estável | $O(1)$ |

*Nota sobre a implementação dos selecionados:*
O Selection Sort é $O(n^2)$ em todos os cenários pois sempre executa as comparações completas do resto da lista, independentemente da entrada estar previamente ordenada. O Quick Sort é extremamente veloz na média ($O(n \log n)$), mas em um vetor já ordenado (dependendo do particionamento e escolha do pivô) pode degradar para $O(n^2)$. 

## 6. Resultados do Laboratório e Casos de Teste (Exemplo Prático)
Executando os testes em `laboratorio.py`, os seguintes resultados ilustram o comportamento discutido:

**Para N = 100:**
- Selection Sort: ~4950 Comparações | ~99 Movimentações (Média)
- Quick Sort: ~650 Comparações | ~300 Movimentações (Média)
**Para N = 5000:**
- Selection Sort: ~12.497.500 Comparações | Tempo notavelmente maior.
- Quick Sort: ~70.000 Comparações | Termina em milissegundos.

*(Obs: Os valores podem variar dependendo da distribuição randômica da entrada, porém a discrepância cresce substancialmente provando a diferença entre uma curva $n^2$ e $n \log n$).*

## 7. Decisões de Projeto, Vantagens e Limitações
- **Uso de deepcopy():** Em nosso desafio lúdico, ao executar a ordenação, utilizamos `copy.deepcopy()` para garantir que ambos os algoritmos estavam lidando com arranjos puramente idênticos. Avaliar o Selection Sort primeiro alteraria o vetor original (passagem por referência), destruindo a premissa de testar o Quick Sort com o exato mesmo cenário de desordem.
- **Por que Quick Sort?** Escolhemos o Quick Sort devido ao fato de não exigir cópias adicionais do array ($O(n)$ de memória extra), como ocorre no Merge Sort, poupando a alocação de novos vetores a cada chamada. Sua desvantagem/limitação é a instabilidade e o possível pior caso se o particionamento cair em divisões de N-1 seguidas.
- **Busca Binária:** Implementamos a lógica entendendo que ela necessita dos dados *pré-ordenados* no campo-chave que será consultado. Não podemos realizar Busca Binária "por código" se o mural foi acabado de ser ordenado "por urgência". Por isso, a busca binária só ocorre após o passo onde geramos um array ordenado por código.

## 8. Defesa Oral: Guia de Respostas para a Equipe (Roteiro de Estudo)

- **Por que os algoritmos devem receber cópias idênticas dos dados?**
  Para que a comparação de performance (comparações/tempo) seja justa. Se o algoritmo B rodar num array que já foi ordenado pelo algoritmo A, os cenários não são equivalentes (podem ocorrer resultados viciados no melhor ou pior caso).
- **Qual é a complexidade dos algoritmos implementados?**
  Selection Sort = sempre $O(n^2)$. Quick Sort = Médio $O(n \log n)$ / Pior caso $O(n^2)$. Busca Linear = $O(n)$. Busca Binária = $O(\log n)$.
- **Por que um algoritmo O(n²) pode ser aceitável para conjuntos pequenos?**
  A constante matemática embutida e a simplicidade das operações (nenhuma chamada recursiva na memória, arrays pequenos ficam inteiros no Cache L1 do processador) fazem com que algoritmos O(n²) como Insertion/Selection sejam mais rápidos que o Quick Sort para `N < 15` (motivo pelo qual muitas implementações modernas de linguagens misturam Quick com Insertion para os fragmentos pequenos - *IntroSort/TimSort*).
- **Por que a busca binária exige dados ordenados pelo atributo pesquisado?**
  A lógica da busca binária depende de descartar metade da lista com certeza matemática. Se o item do meio for "50", e estamos buscando "30", sabemos com certeza que o 30 está na metade da esquerda. Se estivesse desordenado, não haveria como garantir essa exclusão.
- **Por que a busca binária é mais adequada a vetores do que a listas encadeadas?**
  Para encontrar o "meio", precisamos saltar diretamente para um índice (ex: `indice = tamanho / 2`). Vetores permitem "Acesso Aleatório" (Random Access) de complexidade O(1). Listas Encadeadas exigiriam percorrer nó por nó até chegar no meio O(n), o que destruiria a eficiência da Busca Binária (tornando ela pior que a Linear).
- **O algoritmo implementado é estável? Como isso pode afetar elementos empatados?**
  Tanto o Selection Sort quanto o Quick Sort implementados **NÃO** são estáveis. Isso significa que, se duas missões possuírem a exata mesma urgência, a ordem relativa entre elas no vetor original pode ser trocada/embaralhada.
- **Por que o tempo medido pode variar entre diferentes execuções?**
  O processador executa tarefas em concorrência com o Sistema Operacional e outros programas no computador (escalonamento de threads). Além disso, dependendo do estado do Gerenciador de Memória e L1/L2/L3 Cache, os tempos oscilam, embora a grandeza seja similar. A métrica real de complexidade assintótica são as "comparações matemáticas", não o "relógio de parede".
