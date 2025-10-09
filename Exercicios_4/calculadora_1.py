'''1 - Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.
As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
Trate os seguintes erros:
Entrada inválida (não numérica) para os números
Divisão por zero
Operação inválida
Use try/except para capturar e tratar os erros apropriadamente.
Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa'''
# Programa: Calculadora com tratamento de erros

def calculadora():
    while True:
        try:
            # Solicita os números
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            # Solicita a operação
            operacao = input("Digite a operação (+, -, *, /): ")

            # Verifica qual operação será realizada
            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Não é possível dividir por zero.")
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida.")

            print("Resultado:", resultado)
            break  # Sai do loop após sucesso

        except ValueError as e:
            print("Erro:", e, "Tente novamente.")
        except ZeroDivisionError as e:
            print("Erro:", e, "Tente novamente.")

# Chama a função principal
calculadora()
