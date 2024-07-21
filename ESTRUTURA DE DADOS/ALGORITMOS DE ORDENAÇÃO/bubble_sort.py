# Algoritmo Bubble Sort
import random

def bubble_sort(v):
    # Define o fim inicial como o comprimento do vetor
    fim = len(v)
    # Continua até que o fim seja maior que 0
    while fim > 0:
        i = 0
        # Percorre o vetor do início até o fim menos um
        while i < fim - 1:
            # Se o elemento atual é maior que o próximo elemento
            if v[i] > v[i + 1]:
                # Troca os elementos de posição
                tempo = v[i]
                v[i] = v[i + 1]
                v[i + 1] = tempo
            
            i += 1 # Incrementa o índice

        fim -= 1 # Decrementa o fim

# Cria um vetor com valores de 0 até 19
vetor = list(range(0, 20))

random.shuffle(vetor) # Embaralha o vetor para desordená-lo

# Chama a função de ordenação
bubble_sort(vetor)

# Testando
print(vetor)
# Saída esperada: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]