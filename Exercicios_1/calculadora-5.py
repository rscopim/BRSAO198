'''5 - Crie um programa em Python que peça dois números e uma operação matemática (+, -, * ou /), e mostre o resultado de acordo com a operação escolhida.'''

num1 = float(input("Digite o primero número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")
if operacao == "+":
    print("Resultado: ", num1 + num2)
elif operacao == "-":
    print("Resultado: ", num1 - num2)
elif operacao == "*":
    print("Resultado: ", num1 * num2)
elif operacao == "/":
     if num2 != 0:    
        print("Resultado: ", num1 / num2)
     else:
         print("Erro, não é possível dividir por ZERO!")
else:
    print("Operação inválida!")

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
operacao = input("Escolha uma operacao (+, -, * ou /): ")

match operacao:
    case "+":
        print(f"Resultado da conta: {n1 + n2}")
    case "-":
        print(f"Resultado da conta: {n1 - n2}")
    case "*":
        print(f"Resultado da conta: {n1 * n2}")
    case "/":
        print(f"Resultado da conta: {n1 / n2}")
    case _:
        print("Operação Inválida!")

from operator import add, mul, sub, truediv

def calculator(num_a, num_b, operator):
    operations = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": truediv
    }

    operation = operations[operator]
    return operation(num_a, num_b)

print(calculator(2, 2, "+"))
print(calculator(2, 2, "-"))
print(calculator(2, 2, "*"))
print(calculator(2, 2, "/"))

n1 = int(input('um valor'))
n2 = int(input('outro valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, e a divisao é {:.2f}'.format(s, m, d), end=' ')
print('Divisao inteira {} e a potencia {}'.format(di, e))
