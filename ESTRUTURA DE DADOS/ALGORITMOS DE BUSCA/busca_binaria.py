import time

def busca_binaria(v, p, r, x):
    # Condição de parada (ou condição de existência)
    if p <= r:
        q = (p + r) // 2 # O índice do meio do vetor
        if x > v[q]:
            return busca_binaria(v, q + 1, r, x)
        elif x < v[q]:
            return busca_binaria(v, p, q - 1, x)
        else:
            return q # Encontramos o elemento
        
    return - 1 # Não encontramos o elemento

vetor = list(range(0, 100))
elemento = 98
antes = time.time()
posicao = busca_binaria(vetor, 0, len(vetor) - 1, elemento)
depois = time.time()
total = (depois - antes) * 1000
# print(vetor)

# Teste
if posicao >= 0:
    print(f"O elemento {elemento} foi encontrado na posição {posicao}")
else:
    print("O elemento NÃO foi encontrado.")
print(f"O tempo foi: {total:0.2f} milissegundos")