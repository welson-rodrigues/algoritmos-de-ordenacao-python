import random
import time

def merge_sort(v, p, r):
    # Condição de parada (condição de existência)
    if p < r:
        q = (p + r) // 2 # Posição do elemento meio
        merge_sort(v, p, q) # Quebrando o vetor em um sub-vetor 1 (metade na esquerda)
        merge_sort(v, q + 1, r) # Quebrando o vetor em um sub-vetor 2 (metade da direita)
        intercalar(v, p, q, r)

def intercalar(v, p, q, r):
    tempo = v.copy() # Cópia do vetor real
    i = p # Contador do sub-vetor 1
    j = q + 1 # Contador do sub-vetor 2
    k = p # Contador do vetor real

    # Momento em que a intercalação será realizada
    while k <= r:
        if i > q:
            # Entra quando não tiver elementos no sub-vetor 1
            v[k] = tempo[j]
            j += 1
        elif j > r:
            # Entra quando não tiver mais elementos no sub-vetor 2
            v[k] = tempo[i]
            i += 1
        elif tempo[i] <= tempo[j]:
            # Nesse caso, retirar o elemento do sub-vetor 1
            v[k] = tempo[i]
            i += 1
        else:
            # Nesse caso, retirar o elemento do sub-vetor 1
            v[k] = tempo[j]
            j += 1
        k += 1

vetor = list(range(0, 10000))
random.shuffle(vetor)

# Teste
antes = time.time()
merge_sort(vetor, 0, len(vetor) - 1)
depois = time.time()
total = (depois - antes) * 1000
""" print(vetor) """
print(f"A ordenação do Merge Sort demorou {total: 0.2f} milissegundos")