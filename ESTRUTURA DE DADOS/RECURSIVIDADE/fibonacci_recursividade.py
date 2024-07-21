# Função Recursiva com Fibonacci

def fibonacci(n, anterior=0, proxima=1):
    # Verifica se n é 0, caso sim, retorna uma lista vazia
    if n == 0:
        return []
        
    # Verifica se n é 1, caso sim, retorna uma lista com o primeiro elemento da sequência
    if n == 1:
        return [anterior]

    # Concatena o valor atual com o resultado da chamada recursiva
    # Reduz o valor de n e atualiza os valores de 'anterior' e 'proxima'
    return [anterior] + fibonacci(n - 1, proxima, anterior + proxima)

# Testando a função
n = 10 # Define o número de elementos a serem gerados na sequência de Fibonacci
resultado = fibonacci(n)
# Converte cada número da lista para string e junta com '-' como separador
print('-'.join(map(str, resultado)))

# Resultado esperado: 0-1-1-2-3-5-8-13-21-34