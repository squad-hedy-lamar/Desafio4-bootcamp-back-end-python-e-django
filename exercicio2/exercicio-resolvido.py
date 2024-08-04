# 4 - Desafio: exercicio 2
# 2. Reverso do número. Faça uma função que retorne o reverso de um
# número inteiro informado. Por exemplo: 127-> 721.


def reverso_numero(numero):
    numero_reverso = int(str(numero)[::-1])
    return numero_reverso


numero_informado = 127
numero_reverso = reverso_numero(numero_informado)
print(f"O reverso do número {numero_informado} é {numero_reverso}")
