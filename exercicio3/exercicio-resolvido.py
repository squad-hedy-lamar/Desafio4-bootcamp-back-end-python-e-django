"""
3. Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
cada opção, crie uma função.
Extra: Crie uma terceira, que é um menu para o usuário escolher a
opção desejada, onde esse menu chama a função de conversão
correta.


"""
#função para converter celsius para fahrenheit
def celsiusToFahrenheit():
    userinput = float(input("Digite quantos graus Celsius você deseja converter para Fahrenheit?"))
    numberconvert = (userinput * 9/5) + 32
    print(f"O {int(userinput)} Celsius é {int(numberconvert)} Fahrenheit")
    return numberconvert

#função para converter fahrenheit para celsius
def fahrenheitToCelsius():
    userinput = float(input("Digite quantos graus Fahrenheit você deseja converter para Celsius?"))
    numberconvert = (userinput - 32) *5/9
    print(f"{int(userinput)} Fahrenheit é {int(numberconvert)} Celsius")
    return numberconvert
#Menu para o usuario escolher a função correspondente 
def menu():
    print("Ola, Digite o numero correspondente para a função:")
    functionumber = int(input("Digite 1 para \n #converter Celsius em Fahrenheit? \n Digite 2 para \n #converter Fahrenheit em Celsius?\n"))
    if functionumber == 1:
        celsiusToFahrenheit()
    elif functionumber == 2:
        fahrenheitToCelsius()
    else:
        print("error")

menu()