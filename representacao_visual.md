# Representação Visual - O Conselho de Missões (Guilda 4)

Você pode copiar e colar os diagramas abaixo diretamente no seu arquivo `Manual_do_Desenvolvedor.md` (o GitHub e muitos conversores de PDF suportam a linguagem "Mermaid"). Você também pode tirar *prints* da visualização para colocar nos seus Slides!

---

## 1. Representação Lógica do TAD (Modelagem e Memória)

Este diagrama mostra o relacionamento das classes e como os dados ficam dispostos fisicamente em blocos contíguos de memória (Vetor/Array), garantindo o acesso rápido $O(1)$ por índice.

```mermaid
classDiagram
    class MuralMissoes {
        +Array vetor[Missao]
        +int capacidade
    }
    
    class Missao {
        +int codigo
        +String titulo
        +int grau_dificuldade
        +int recompensa_ouro
        +int urgencia
    }
    
    MuralMissoes "1" *-- "*" Missao : contém N instâncias
```

**Visão do Vetor na Memória:**
```mermaid

graph LR
    subgraph Estrutura do Array na Memória
        direction LR
        0["Índice 0<br/>[Cod: 101]"] --- 1["Índice 1<br/>[Cod: 102]"]
        1 --- 2["Índice 2<br/>[Cod: 103]"]
        2 --- 3["..."]
        3 --- N["Índice N-1<br/>[Cod: 199]"]
    end
    
    style 0 fill:#2d3748,stroke:#4a5568,color:#fff
    style 1 fill:#2d3748,stroke:#4a5568,color:#fff
    style 2 fill:#2d3748,stroke:#4a5568,color:#fff
    style N fill:#2d3748,stroke:#4a5568,color:#fff
```

---

## 2. Representação do Algoritmo: Busca Binária

Este fluxograma ilustra o princípio da divisão e conquista da Busca Binária ao procurar a Missão de Código **110**. Note que a pré-condição é que o vetor já esteja ordenado.

```mermaid
graph TD
    subgraph iter1["1. Primeira Iteração"]
    A1[Cod: 101] --- A2[Cod: 102] --- A3[Cod: 105] --- A4((Meio<br/>Cod: 108)) --- A5[Cod: 110] --- A6[Cod: 112] --- A7[Cod: 120]
    end
    
    subgraph iter2["2. Segunda Iteração (Descartando a metade esquerda)"]
    B1((Meio<br/>Cod: 110)) --- B2[Cod: 112] --- B3[Cod: 120]
    end
    
    subgraph sucesso["3. Sucesso"]
    C1(((Cod: 110 Encontrado!)))
    end
    
    iter1 -->|Alvo 110 é maior que o Meio 108| iter2
    iter2 -->|Alvo 110 é igual ao Meio| sucesso
    
    style A4 fill:#ecc94b,stroke:#b7791f,color:#000
    style B1 fill:#ecc94b,stroke:#b7791f,color:#000
    style C1 fill:#48bb78,stroke:#2f855a,color:#fff
```

---

## 3. Representação do Algoritmo: Quick Sort

Este diagrama explica a estratégia de partição do algoritmo mais eficiente escolhido pelo grupo, utilizando um Pivô.

```mermaid
graph TD
    A["Vetor Desordenado<br>[ 9, 2, 5, 1, 7, 3, 4 ]<br/><b>Pivô Escolhido: 4</b>"]
    
    A -->|Menores ou iguais a 4| B["Sub-vetor Esquerda<br>[ 2, 1, 3 ]"]
    A -->|Posição Final do Pivô| C["[ 4 ]"]
    A -->|Maiores que 4| D["Sub-vetor Direita<br>[ 9, 5, 7 ]"]
    
    B --> E["Ordenação Recursiva..."]
    D --> F["Ordenação Recursiva..."]
    
    E -.-> G["[ 1, 2, 3 ]"]
    F -.-> H["[ 5, 7, 9 ]"]
    
    G --> I["Vetor Final Ordenado<br>[ 1, 2, 3, 4, 5, 7, 9 ]"]
    C --> I
    H --> I
    
    style A fill:#4a5568,color:#fff
    style C fill:#ecc94b,color:#000
    style I fill:#48bb78,color:#fff
```
