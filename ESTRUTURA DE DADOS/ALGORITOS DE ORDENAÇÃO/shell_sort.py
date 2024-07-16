import time
import random

def shell_sort(v):

    h = len(v) // 2 # distância
    while h > 0:
        i = h
        while i < len(v):
            tempo = v[i]
            trocou = False
            j = i - h
            while j >= 0 and v[j] > tempo:
                v[j + h] = v[j]
                trocou = True
                j -= h

            if trocou:
                v[j + h] = tempo

            i += 1

        h = h // 2

vetor = list(range(0, 100000))
random.shuffle(vetor)
antes = time.time()

shell_sort(vetor)
depois = time.time()
total = (depois - antes) * 1000

print(vetor)
print(f"A ordenação do Shell Sort demorou: {total: 0.2f} milissegundos")