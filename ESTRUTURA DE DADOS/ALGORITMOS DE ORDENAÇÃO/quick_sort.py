# Algoritmo Quick Sort
import random

def quick_sort(v, p, r):
    # Condição de parada (ou condição de existência)
    if p < r:
        q = particionar(v, p, r)
        quick_sort(v, p, q - 1) # Pivotar a esquerda (ordenar os elementos menores do que o pivô)
        quick_sort(v, q + 1, r) # Pivotar a direita (ordenar os elementos maiores do que o pivô)

def particionar(v, p, r):
    x = v[p] # Escolhendo o pivô (é o primeiro elemento da esquerda)
    i = p # Destino do pivô
    j = p + 1 # Contador para percorrer o restante do vetor

    # Percorrer o vetor
    while j <= r:
        if v[j] < x:
            i += 1
            trocar(v, i, j) # Detectou-se um elemento menor que o pivô, incrementa o i
        j += 1 # Passa para o próximo elemento

    trocar(v, p, i)

    return i

def trocar(v, n, m):
    tempo = v[n]
    v[n] = v[m]
    v[m] = tempo

vetor = list(range(0, 10)) # Cria um vetor ordenado de 0 a 9
random.shuffle(vetor) # Deixe o vetor desordenado
quick_sort(vetor, 0, len(vetor) - 1)

# Testando
print(vetor) # Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]