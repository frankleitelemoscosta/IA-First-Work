> Status finished :heavy_check_mark:

# Trabalho IA: Comparação entre Algoritmos de Busca Não Informada
## Objetivo 🎯

<body>
    <p>Implementar e comparar dois diferentes algoritmos de busca não informada aplicados a um problema
clássico de busca - o problema do labirinto.</p>
</body>

![image](https://github.com/user-attachments/assets/2e14cd4d-104b-4404-91f8-9f3fe3a1916b)


## Descrição 📜 

<body>
    <p> O código foi projetado na linguagem python, implementa e compara os algoritmos de busca BFS (Busca em Largura) e DFS (Busca em Profundidade) para encontrar um caminho em um labirinto representado como um grafo. Ele mede o tempo médio de execução de cada algoritmo em 5 execuções e exibe o caminho encontrado para o destino.</p>
</body>

## Estrutura do Projeto 🏗️
- **Linguagem:** Python.
- **Bibliotecas utilizadas:**
  - `collections.deque`: para implementar a fila de pesquisa no BFS.
  - `numpy`: para manipulação e conversão de arrays.
  - `time`: para medir o tempo de execução.
  - `tracemalloc `: para medir o consumo de memória.

## Representação do Labirinto ➡️
O labirinto é representado como um grafo, onde cada posição é um nó, e os caminhos possíveis entre as posições são arestas. A representação do grafo é feita usando um dicionário Python:

```python
grafo_labirinto = {
    (4, 0): [(4, 1), (3, 0)],          
    (4, 1): [(4, 0), (3, 1), (4 ,2)],
    ...
}
```
<p>Cada chave é uma coordenada (linha, coluna).</p>
<p>Cada valor é uma lista de coordenadas vizinhas acessíveis.<p>

## Ánalise dos Algoritmos Implementados 🔍
### BFS (Busca em Largura)
 - **Descrição**: Explora todos os vizinhos de um nó antes de passar para o próximo nível.
 - **Medidas de Desempenho**:
    - **Tempo de Execução**: Geralmente rápido em grafos rasos.
    - **Consumo de Memória**: Alto, pois mantém todos os nós do nível atual em memória.
    - **Completude**: Sempre encontra a solução se ela existir.
    - **Optimalidade**: Garante a solução mais curta em grafos não ponderados.

 ### DFS (Busca em Profundidade)
 - **Descrição**: Explora um caminho até o máximo possível antes de retroceder.
 - **Medidas de Desempenho**:
    - **Tempo de Execução**: Pode ser rápido, mas varia dependendo da estrutura do grafo.
    - **Consumo de Memória**: Menor que BFS, pois utiliza uma pilha para gerenciar os nós.
    - **Completude**: Não é garantido encontrar a solução em todos os casos, especialmente em grafos com ciclos.
    - **Optimalidade**:  Não garante a solução mais curta.

## Exemplo de Saída 💻

### BFS

```

Duração média do BFS: 6.967999506741762e-05
Consumo médio de memória: 3.64 KB
Caminho: [(4, 0), (4, 1), (3, 1), (2, 1), (2, 2), (2, 3), (1, 3), (1, 2), (0, 2), (0, 3), (0, 4)]

```
---
### DFS
```
Duração média do DFS: 3.651999868452549e-05
Consumo médio de memória: 3.07 KB
Caminho: [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4), (3, 3), (3, 2), (2, 2), (2, 3), (1, 3), (1, 2), (0, 2), (0, 3), (0, 4)]
```
## Considerações Finais 📝

- **BFS** é ideal para encontrar o menor caminho em grafos não ponderados, mas pode consumir muita memória.
- **DFS** pode ser mais eficiente em termos de memória, mas não garante a solução mais curta.
 - Os resultados podem variar dependendo do tamanho e da estrutura do grafo utilizado.

## Compilação e Execução ⚙️
1. Certifique-se de que o Python 3.x está instalado no sistema.
2. Instale a biblioteca numpy, se necessário:
 - ````  pip install numpy ````
3. Salve o código em um arquivo .py e execute no terminal:
- ````python nome_do_arquivo.py ````