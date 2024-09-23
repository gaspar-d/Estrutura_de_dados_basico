# ===============================================================================
# 1. Contagem de Frequência
# Escreva uma função que receba uma lista de palavras
# e retorne um dicionário onde as chaves são as palavras
# e os valores são o número de vezes que cada palavra aparece na lista.
def contagem_palavras(palavras: list[str]):
    counter: dict[str, int] = {}

    for palavra in palavras:
        if palavra in counter:
            counter[palavra] += 1
        else:
            counter[palavra] = 1

    print(counter)
    print("=" * 30)


contagem_palavras(["maçã", "banana", "maçã", "laranja", "banana", "banana"])

# Exemplo de uso:
# Entrada: ["maçã", "banana", "maçã", "laranja", "banana", "banana"]
# Saída esperada: {"maçã": 2, "banana": 3, "laranja": 1}


# ===============================================================================
# 2. Atualizar Valores de um Dicionário
# Escreva uma função que receba um dicionário com valores inteiros
# e duplique cada valor.
def duplicar_valores(meu_dict: dict[str, int]):
    dict_atualizado: dict[str, int] = {}

    for key, value in meu_dict.items():
        dict_atualizado[key] = value * 2

    print(dict_atualizado)
    print("=" * 30)


duplicar_valores({"a": 10, "b": 20, "c": 30})
# Exemplo de uso:
# Entrada: {"a": 10, "b": 20, "c": 30}
# Saída esperada: {"a": 20, "b": 40, "c": 60}


# ===============================================================================
# 3. Mesclar Dois Dicionários
# Escreva uma função que receba dois dicionários
# e os mescle em um novo dicionário.
# Se houver conflito de chaves, o valor do segundo dicionário deve sobrescrever o do primeiro.
def mesclar_dicionarios(dict1: dict[str, int], dict2: dict[str, int]):
    dict1.update(dict2)
    print(dict1)
    print("=" * 30)

mesclar_dicionarios({"a": 1, "b": 2}, {"b": 3, "c": 4})
# Exemplo de uso:
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# Saída esperada: {"a": 1, "b": 3, "c": 4}
