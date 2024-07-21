# Algoritmo Insertion Sort
import random

def insertion_sort(v):
    # Inicia a ordenação a partir do segundo elemento (índice 1)
    i = 1
    while i < len(v):
        # Armazena o valor atual em uma variável temporária
        tempo = v[i]
        trocou = False
        # Inicia a comparação com o elemento anterior
        j = i - 1
        # Move os elementos maiores que o valor atual para a direita
        while j >= 0 and v[j] > tempo:
            v[j + 1] = v[j]
            trocou = True
            j -= 1
        # Insere o valor temporário na posição correta
        if trocou:
            v[j + 1] = tempo
        # Passa para o próximo elemento
        i += 1

# Cria um vetor com valores de 0 até 9
vetor = list(range(0, 10))

# Embaralha o vetor para desordená-lo
random.shuffle(vetor)

# Chama a função de ordenação
insertion_sort(vetor)

# Testando
print(vetor)
# Saída: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
