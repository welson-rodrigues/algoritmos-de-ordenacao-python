# Algoritmo Shell Sort
import random

def shell_sort(v):
    # Inicializa a distância de comparação, começando com a metade do tamanho da lista
    h = len(v) // 2
    
    # Continua até a distância ser reduzida a 0
    while h > 0:
        # Itera sobre os elementos da lista começando na posição h
        i = h
        while i < len(v):
            tempo = v[i]  # Armazena o valor atual
            trocou = False
            j = i - h
            # Move os elementos que são maiores que tempo para a direita
            while j >= 0 and v[j] > tempo:
                v[j + h] = v[j]
                trocou = True
                j -= h
            
            # Coloca o valor de tempo na posição correta
            if trocou:
                v[j + h] = tempo
            
            i += 1
        
        # Distância na metade
        h = h // 2

# Cria uma lista com números de 0 a 9 e embaralha
vetor = list(range(0, 10))
random.shuffle(vetor)

# Ordena a lista usando o algoritmo Shell Sort
shell_sort(vetor)

# Testando
print(vetor)  # Saída esperada: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
