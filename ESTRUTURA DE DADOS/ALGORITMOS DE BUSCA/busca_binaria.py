# Algoritmo de Busca Binária
def busca_binaria(v, p, r, x):
    # v: vetor onde a busca será realizada
    # p: vetor inicial
    # r: vetor final
    # x: elemento a ser buscado

    # Condição de parada: verifica se ainda há elementos no intervalo [p, r]
    if p <= r:
        # Calcula o índice do meio do intervalo
        q = (p + r) // 2
        
        # Se o elemento procurado é maior que o elemento no meio, busca na metade direita
        if x > v[q]:
            return busca_binaria(v, q + 1, r, x)
        # Se o elemento procurado é menor que o elemento no meio, busca na metade esquerda
        elif x < v[q]:
            return busca_binaria(v, p, q - 1, x)
        else:
            # Se o elemento procurado é igual ao elemento no meio, retorna o índice q
            return q
        
    # Se o intervalo [p, r] não contém elementos, retorna -1
    return -1

# Cria um vetor com valores de 50 até 999
vetor = list(range(50, 1000))
# Define o elemento que queremos buscar
elemento = 98
# Chama a função de busca binária passando o vetor, os índices inicial e final, e o elemento
posicao = busca_binaria(vetor, 0, len(vetor) - 1, elemento)

# Testando
if posicao >= 0:
    print(f"O elemento {elemento} foi encontrado na posição {posicao}")
else:
    print("O elemento NÃO foi encontrado.")

# Saída: O elemento 98 foi encontrado na posição 48.