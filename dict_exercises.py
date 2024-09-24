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


# ===============================================================================
# 4. Acessar valores de um dicionário aninhado (nested)
# Dado um dicionário aninhado, retorne o valor associado a uma chave no dicionário interno
# lembre-se que dicionários são key: value
def acessar_valor_dicionario(dicionario, chave_externa, chave_interna):
    print(dicionario[chave_externa].get(chave_interna))
    print("=" * 30)


acessar_valor_dicionario(
    {
        "pessoa1": {"nome": "Ana", "idade": 25},
        "pessoa2": {"nome": "Carlos", "idade": 30},
    },
    "pessoa1",
    "nome",
)

# Exemplo de uso:
# dicionario = {
#    "pessoa1": {"nome": "Ana", "idade": 25},
#    "pessoa2": {"nome": "Carlos", "idade": 30}
# }
# acessar_valor_dicionario(dicionario, "pessoa1", "nome") deve retornar "Ana"


# ===============================================================================
# 5. Modifique um valor
# Modifique um valor em um dicionário aninhado nas chaves especificadas
def modificar_dicionario(dicionario, chave_externa, chave_interna, novo_valor):
    dicionario[chave_externa].update({chave_interna: novo_valor})
    print(dicionario)
    print("=" * 30)


modificar_dicionario(
    {
        "produto1": {"nome": "Notebook", "preco": 2000},
        "produto2": {"nome": "Mouse", "preco": 50},
    },
    "produto2",
    "preco",
    60,
)

# Exemplo de uso:
# dicionario = {
#    "produto1": {"nome": "Notebook", "preco": 2000},
#    "produto2": {"nome": "Mouse", "preco": 50}
# }
# modificar_dicionario(dicionario, "produto2", "preco", 60)
# dicionario deve se tornar: {
#    "produto1": {"nome": "Notebook", "preco": 2000},
#    "produto2": {"nome": "Mouse", "preco": 60}
# }


# ===============================================================================
# 6. Some todos os valores numéricos (int)
# Dado um dicionário aninhado, some todos os valores numéricos
def soma_valores_dicionario(dicionario):
    total: int = 0

    for notas in dicionario.values():
        total += sum(notas.values())

    print(total)
    print("=" * 30)


soma_valores_dicionario(
    {"aluno1": {"nota1": 8, "nota2": 9}, "aluno2": {"nota1": 7, "nota2": 10}}
)

# Exemplo de uso:
# dicionario = {
#    "aluno1": {"nota1": 8, "nota2": 9},
#    "aluno2": {"nota1": 7, "nota2": 10}
# }
# soma_valores_dicionario(dicionario) deve retornar 34 (8 + 9 + 7 + 10)
