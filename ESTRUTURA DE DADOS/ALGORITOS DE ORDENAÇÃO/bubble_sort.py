import time
import random

def bubble_sort(v):
    fim = len(v)
    while fim > 0:
        i = 0
        # Percorrendo o vetor de 0 até o fim
        while i < fim - 1:
            if v[i] > v[i + 1]:
                # realizando a troca da posição atual pela próxima
                tempo = v[i]
                v[i] = v[i + 1]
                v[i + 1] = tempo
            i += 1
        fim -= 1

vetor = list(range(0, 100)) # Vetor gerado de forma automatica
random.shuffle(vetor) # Embaralhando os números gerados

antes = time.time()
bubble_sort(vetor) # Ordenando o vetor
depois = time.time()
# print(vetor) # Vetor desordenado
total = (depois - antes) * 1000
print(f"A ordenação do Bubble Sort demorou {total: 0.2f} milissegundos")