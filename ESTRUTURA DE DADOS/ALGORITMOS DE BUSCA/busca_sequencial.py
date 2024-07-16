import time

def busca_sequencial(v, x):
    i = 0

    # Percorrendo o vetor
    while i < len(v):
        if v[i] == x:
            return i
        
        i += 1

    return - 1

vetor = list(range(100, 200))

# print(vetor)

elemento = 150
antes = time.time()
posicao = busca_sequencial(vetor, elemento)
depois = time.time()
total = (depois - antes) * 1000

# Teste
if posicao >= 0:
    print(f"O elemento {elemento} foi encontrado na posição {posicao}")
else:
    print("O elemento NÃO foi encontrado.")

print(f"Tempo total foi: {total:0.2f} milissegundos")