'''2 - Crie um programa em Python que solicite um número do usuário e informe se ele é par ou ímpar. '''

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número", numero, "é par.")
else:
    print("O número", numero, "é ímpar.")