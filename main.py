from collections import deque
import numpy as np
import time
import tracemalloc 

# variaveis do algoritmo
duracao = ["0","0", "0", "0", "0"] # apenas inicializando a lista de duração
averageTimeDFS = 0
averageTimeBFS = 0
memoryUsageDFS = 0
memoryUsageBFS = 0
sampleArray = np.array(duracao) 
convertedArray = sampleArray.astype(float) 

# Representação do labirinto como um grafo
grafo_labirinto = {
    (4, 0): [(4, 1), (3, 0)],          # U 
    (4, 1): [(4, 0), (3, 1), (4 ,2)],  # V 
    (4, 2): [(4, 1), (4, 3)],          # X 
    (4, 3): [(4, 2), (4, 4)],          # Y 
    (4, 4): [(3, 4), (4, 3)],          # Z 

    (3, 0): [(4, 0), (2, 0)],           # P 
    (3, 1): [(4, 1), (2, 1)],           # Q 
    (3, 2): [(3, 3), (2, 2)],           # R 
    (3, 3): [(3, 2), (3, 4)],           # S 
    (3, 4): [(4, 4), (3, 3)],           # T 

    (2, 0): [(3, 0)],                   # K 
    (2, 1): [(3, 1), (2, 2)],           # L 
    (2, 2): [(2, 1), (3, 2), (2, 3)],   # M 
    (2, 3): [(1, 3), (2, 2), (2, 4)],   # N 
    (2, 4): [(2, 3)],                   # O 

    (1, 0): [(0, 0), (1, 1)],           # F 
    (1, 1): [(1, 0), (1, 2)],           # G 
    (1, 2): [(0, 2), (1, 1), (1, 3)],   # H 
    (1, 3): [(2, 3), (1, 2)],           # I 
    (1, 4): [(0, 4)],                   # J 

    (0, 0): [(1, 0), (0, 1)],           # A 
    (0, 1): [(0, 0)],                   # B 
    (0, 2): [(1, 2), (0, 3)],           # C 
    (0, 3): [(0, 2), (0, 4)],           # D 
    (0, 4): [(1, 4), (0, 3)]            # E (fim) 
}

inicio = (4, 0)  # posição inicial no labirinto
fim = (0, 4)     # objetivo final

def medir_consumo_memoria(func, *args, **kwargs):
    #Mede o consumo de memória 
    tracemalloc.start()
    resultado = func(*args, **kwargs)
    mem_atual, mem_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return resultado, mem_pico /1024  # Conversão para KB

# Daqui em diante está a implementação dos algoritmos BFS e DFS

def BFS(inicio, fim, grafo):
    tempo_inicial = time.perf_counter()  # registra o tempo inicial

    fila_de_pesquisa = deque([(inicio, [inicio])])  # inicializa uma tupla com a posição inicial e o caminho
    verificados = set()  # armazena posições já verificadas

    while fila_de_pesquisa:
        atual, caminho_atual = fila_de_pesquisa.popleft()  # retira a posição atual e armazena o caminho

        # verifica se a posição atual é o destino
        if atual == fim:
            tempo_final = time.perf_counter()
            duracao = tempo_final - tempo_inicial
            return caminho_atual, duracao

        verificados.add(atual)  # adiciona a posição atual ao conjunto de verificados

        # checa os vizinhos da posição atual
        for vizinho in grafo.get(atual, []):
            if vizinho not in verificados:
                fila_de_pesquisa.append((vizinho, caminho_atual + [vizinho]))

    tempo_final = time.perf_counter()
    duracao = tempo_final - tempo_inicial

    return None, duracao

for i in range(5):
    (caminho, duracao), mem_bfs = medir_consumo_memoria(BFS, inicio, fim, grafo_labirinto)
    convertedArray[i] = duracao
    averageTimeBFS += duracao
    memoryUsageBFS += mem_bfs

print("-" * 150)
print(f"Duração média do BFS: {averageTimeBFS/5}\nConsumo médio de memória: {memoryUsageBFS/5:.2f} KB\nCaminho: {caminho}")

print("-" * 150)

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

for i in range(5):
    (caminho, duracao), mem_dfs = medir_consumo_memoria(DFS, inicio, fim, grafo_labirinto)
    convertedArray[i] = duracao
    averageTimeDFS += duracao
    memoryUsageDFS += mem_dfs

print("-" * 150)
print(f"Duração média do DFS: {averageTimeDFS/5}\nConsumo médio de memória: {memoryUsageDFS/5:.2f} KB\nCaminho: {caminho}")

print("-" * 150)
