from collections import deque
import numpy as np
import time
import tracemalloc  # Para medir o consumo de memória

# Variáveis do algoritmo
duracao = ["0", "0", "0", "0", "0"]  # Inicializando a lista de duração
averageTimeDFS = 0
averageTimeBFS = 0
memoryUsageDFS = 0
memoryUsageBFS = 0
sampleArray = np.array(duracao)
convertedArray = sampleArray.astype(float)

# Representação do labirinto como um grafo
grafo_labirinto = {
    (4, 0): [(4, 1), (3, 0)],          
    (4, 1): [(4, 0), (3, 1), (4, 2)],  
    (4, 2): [(4, 1), (4, 3)],          
    (4, 3): [(4, 2), (4, 4)],          
    (4, 4): [(3, 4), (4, 3)],          

    (3, 0): [(4, 0), (2, 0)],           
    (3, 1): [(4, 1), (2, 1)],           
    (3, 2): [(3, 3), (2, 2)],           
    (3, 3): [(3, 2), (3, 4)],           
    (3, 4): [(4, 4), (3, 3)],           

    (2, 0): [(3, 0)],                   
    (2, 1): [(3, 1), (2, 2)],           
    (2, 2): [(2, 1), (3, 2), (2, 3)],   
    (2, 3): [(1, 3), (2, 2), (2, 4)],   
    (2, 4): [(2, 3)],                   

    (1, 0): [(0, 0), (1, 1)],           
    (1, 1): [(1, 0), (1, 2)],           
    (1, 2): [(0, 2), (1, 1), (1, 3)],   
    (1, 3): [(2, 3), (1, 2)],           
    (1, 4): [(0, 4)],                   

    (0, 0): [(1, 0), (0, 1)],           
    (0, 1): [(0, 0)],                   
    (0, 2): [(1, 2), (0, 3)],           
    (0, 3): [(0, 2), (0, 4)],           
    (0, 4): [(1, 4), (0, 3)]            
}

inicio = (4, 0)  # Posição inicial no labirinto
fim = (0, 4)     # Objetivo final


def medir_consumo_memoria(func, *args, **kwargs):
    """Mede o consumo de memória ao executar a função."""
    tracemalloc.start()
    resultado = func(*args, **kwargs)
    mem_atual, mem_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return resultado, mem_pico / 1024  # Conversão para KB


def BFS(inicio, fim, grafo):
    tempo_inicial = time.perf_counter()
    fila_de_pesquisa = deque([(inicio, [inicio])])
    verificados = set()

    while fila_de_pesquisa:
        atual, caminho_atual = fila_de_pesquisa.popleft()

        if atual == fim:
            tempo_final = time.perf_counter()
            duracao = tempo_final - tempo_inicial
            return caminho_atual, duracao

        verificados.add(atual)

        for vizinho in grafo.get(atual, []):
            if vizinho not in verificados:
                fila_de_pesquisa.append((vizinho, caminho_atual + [vizinho]))

    tempo_final = time.perf_counter()
    duracao = tempo_final - tempo_inicial
    return None, duracao


def DFS(inicio, fim, grafo):
    tempo_inicial = time.perf_counter()
    pilha_de_pesquisa = [(inicio, [inicio])]
    verificados = set()

    while pilha_de_pesquisa:
        atual, caminho_atual = pilha_de_pesquisa.pop()

        if atual == fim:
            tempo_final = time.perf_counter()
            duracao = tempo_final - tempo_inicial
            return caminho_atual, duracao

        verificados.add(atual)

        for vizinho in grafo.get(atual, []):
            if vizinho not in verificados:
                pilha_de_pesquisa.append((vizinho, caminho_atual + [vizinho]))

    tempo_final = time.perf_counter()
    duracao = tempo_final - tempo_inicial
    return None, duracao


# Execução dos algoritmos com medições
for i in range(5):
    (caminho, duracao), mem_bfs = medir_consumo_memoria(BFS, inicio, fim, grafo_labirinto)
    convertedArray[i] = duracao
    averageTimeBFS += duracao
    memoryUsageBFS += mem_bfs

print("-" * 150)
print("BFS:")
print(f"Duração média: {averageTimeBFS/5} segundos")
print(f"Consumo médio de memória: {memoryUsageBFS/5:.2f} KB")
print(f"Caminho encontrado: {caminho}")
print("Completude: Sempre encontra a solução (se existir)")
print("Optimalidade: Garante o menor caminho")
print("-" * 150)

for i in range(5):
    (caminho, duracao), mem_dfs = medir_consumo_memoria(DFS, inicio, fim, grafo_labirinto)
    convertedArray[i] = duracao
    averageTimeDFS += duracao
    memoryUsageDFS += mem_dfs

print("DFS:")
print(f"Duração média: {averageTimeDFS/5} segundos")
print(f"Consumo médio de memória: {memoryUsageDFS/5:.2f} KB")
print(f"Caminho encontrado: {caminho}")
print("Completude: Pode não encontrar a solução em grafos com ciclos")
print("Optimalidade: Não garante o menor caminho")
print("-" * 150)
