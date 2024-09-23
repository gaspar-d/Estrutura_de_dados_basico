# ===============================================================================
# 1. Encontrar Números Pares em uma Lista
# Escreva uma função que receba uma lista de inteiros como entrada
# e retorne uma nova lista contendo apenas os números pares.
def encontrar_pares(numeros: list[int]):
    for numero in numeros:
        if numero % 2 == 0:
            print(numero)
    print("=" * 20)


encontrar_pares([1, 2, 3, 4, 5, 6])
# Exemplo de uso:
# Entrada: [1, 2, 3, 4, 5, 6]
# Saída esperada: [2, 4, 6]


# ===============================================================================
# 2. Soma dos Elementos de uma Lista
# Escreva uma função que receba uma lista de inteiros
# e retorne a soma de todos os elementos.
def soma_elementos(numeros: list[int]):
    total: int = 0
    for numero in numeros:
        total += numero
    print(total)
    print("=" * 20)


soma_elementos([10, 20, 30])
# Exemplo de uso:
# Entrada: [10, 20, 30]
# Saída esperada: 60


# ===============================================================================
# 3. Remover Duplicatas de uma Lista
# Escreva uma função que receba uma lista de inteiros
# e retorne uma nova lista sem duplicatas.
def remover_duplicatas(numeros: list[int]):
    result = set(numeros)

    print(result)
    print("=" * 20)


remover_duplicatas([1, 2, 2, 3, 4, 4, 5])

# Exemplo de uso:
# Entrada: [1, 2, 2, 3, 4, 4, 5]
# Saída esperada: [1, 2, 3, 4, 5]
