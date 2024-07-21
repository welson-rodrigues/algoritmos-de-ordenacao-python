# Algoritmo Selection Sort
import random

def selection_sort(v):
    i = 0
    while i < len(v) - 1: # Equando o i for menor do que o tamanho do vetor menos 1
        menor = i
        j = i + 1 # o j sempre está uma posição na frente do i (vai até a penultima casa)
        # Em busca do menor elemento
        while j < len(v): # j vai até o final do vetor (vai até a última)
            if v[j] < v[menor]:
                menor = j

            j += 1

        # Verifica se precisa realizar a troca
        if menor != i:
            tempo = v[i]
            v[i] = v[menor]
            v[menor] = tempo

        i += 1


vetor = list(range(0, 10)) # Vetor ordenado
random.shuffle(vetor) # Embaralhando o vetor

selection_sort(vetor)

# Testando
print(vetor) # Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]