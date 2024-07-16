# FUNÇÃO RECURSIVA COM FIBONACCI

def fibonacci(n, anterior = 0, proxima = 1):
    if n == 0:
        return []
    if n == 1:
        return [anterior]
    return [anterior] + fibonacci(n - 1, proxima, anterior + proxima)

# Teste
n = 10 # Gera n números na sequência de Fibonacci
resultado = fibonacci(n)
print('-'.join(map(str, resultado)))

# Resultado: 0-1-1-2-3-5-8-13-21-34