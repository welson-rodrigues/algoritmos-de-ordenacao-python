# Algoritmo de Busca Sequencial
def busca_sequencial(v, x):
    # Inicializa o índice na primeira posição do vetor
    i = 0

    # Percorrendo o vetor
    while i < len(v):
        # Verifica se o elemento na posição atual é igual ao elemento procurado
        if v[i] == x:
            # Retorna o índice da posição do elemento
            return i
        
        # Incrementa
        i += 1

    # Se não for encontrado retorna -1
    return -1

# Cria um vetor com valores de 100 até 199
vetor = list(range(100, 200))

# Define o elemento procurado
elemento = 150

# Chama a função de busca sequencial passando o vetor e o elemento
posicao = busca_sequencial(vetor, elemento)

# Testando
if posicao >= 0:
    print(f"O elemento {elemento} foi encontrado na posição {posicao}")
else:
    print("O elemento NÃO foi encontrado.")

# Saída: O elemento 150 foi encontrado na posição 50
