# ===============================================================================
# 1. Encontrar Números Pares em uma Lista
# Escreva uma função que receba uma lista de inteiros como entrada
# e retorne uma nova lista contendo apenas os números pares.
def encontrar_pares(numeros: list[int]):
    for numero in numeros:
        if numero % 2 == 0:
            print(numero)
    print("=" * 20)


# encontrar_pares([1, 2, 3, 4, 5, 6])

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


# soma_elementos([10, 20, 30])

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


# remover_duplicatas([1, 2, 2, 3, 4, 4, 5])

# Exemplo de uso:
# Entrada: [1, 2, 2, 3, 4, 4, 5]
# Saída esperada: [1, 2, 3, 4, 5]


# ===============================================================================
# 4. Acesse elementos em uma lista 2D (matriz)
# Dada uma lista 2D (matriz), retorne o valor na posição linha e coluna
def acessar_elemento_matriz(matriz, linha, coluna):
    print(matriz[linha][coluna])


# acessar_elemento_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 2)

# Exemplo de uso:
# matriz = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9]
# ]
# acessar_elemento_matriz(matriz, 1, 2) deve retornar 6


# ===============================================================================
# 5. Some TODOS elementos da lista 2D
# Dada uma lista 2D (matriz), retorne a soma de todos os elementos
def soma_matriz(matriz):
    # Esse primeiro modo é só para visualizar o acesso,
    # o total2 é modo correto pois não importa o tamanho das listas ele vai somar usando o mesmo código
    total = matriz[0][0] + matriz[0][1] + matriz[1][0] + matriz[1][1]

    total2 = 0
    for linha in matriz:
        for coluna in linha:
            total2 += coluna

    print(total2)


# soma_matriz([[1, 2], [3, 4, 5]])
# Exemplo de uso:
# matriz = [
#    [1, 2],
#    [3, 4]
# ]
# soma_matriz(matriz) deve retornar 10 (1 + 2 + 3 + 4)


# ===============================================================================
# 6. Modifique elementos na lista 2D
# Modifique o elemento em uma lista 2D (matriz) na posição dada pela linha e coluna
def modificar_matriz(matriz, linha, coluna, novo_valor):
    matriz[linha][coluna] = novo_valor

    print(matriz)


modificar_matriz([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1, 100)

# Exemplo de uso:
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# modificar_matriz(matriz, 1, 1, 100) modifica o 5 para 100
# matriz deve se tornar: [
#    [1, 2, 3],
#    [4, 100, 6],
#    [7, 8, 9]
# ]
