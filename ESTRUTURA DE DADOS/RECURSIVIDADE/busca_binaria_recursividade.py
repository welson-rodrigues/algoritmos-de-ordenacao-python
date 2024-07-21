# Função Recursiva com Busca Binária

def busca_binaria(lista, elemento, inicio, fim):
    # Caso base: Se a parte da lista estiver vazia
    if inicio > fim:
        return - 1  # Elemento não encontrado

    # Calcula o índice do meio
    meio = (inicio + fim) // 2

    # Se o elemento do meio for igual ao elemento buscado
    if lista[meio] == elemento:
        return meio  # Elemento encontrado

    # Se o elemento do meio for maior que o elemento buscado
    elif lista[meio] > elemento:
        # Continua a busca na metade esquerda da lista
        return busca_binaria(lista, elemento, inicio, meio - 1)
    
    # Se o elemento do meio for menor que o elemento buscado
    else:
        # Continua a busca na metade direita da lista
        return busca_binaria(lista, elemento, meio + 1, fim)

# Testando
lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_procurado = 7 # Deve aparecer no índice 6

resultado = busca_binaria(lista_ordenada, elemento_procurado, 0, len(lista_ordenada) - 1)

if resultado != -1:
    print(lista_ordenada)
    print(f"Elemento encontrado no índice: {resultado}")
else:
    print("Elemento não encontrado")

"""

A saída será essa:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Elemento encontrado no índice: 6

"""