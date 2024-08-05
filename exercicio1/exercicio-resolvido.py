# Desafio 4 - Exercicio 1

# Definindo a função 
def soma_tres_numeros(a, b, c):
    return a + b + c

# Solicitando três números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Chamando a função e exibindo o resultado
resultado = soma_tres_numeros(numero1, numero2, numero3)
print(f"A soma dos três números é: {resultado}")
