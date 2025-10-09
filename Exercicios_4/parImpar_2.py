'''2 - Crie um programa que solicite ao usuário que insira números inteiros. O programa deve continuar solicitando números até que o usuário digite 'fim'. Para cada número inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, o programa deve informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos.'''
# Programa: Identificador de par ou ímpar

def verificar_par_ou_impar():
    pares = 0
    impares = 0

    while True:
        numero = input("Digite um número inteiro ou 'fim' para encerrar: ")

        if numero.lower() == "fim":
            break  # Sai do loop

        try:
            numero = int(numero)
            if numero % 2 == 0:
                print(numero, "é PAR")
                pares += 1
            else:
                print(numero, "é ÍMPAR")
                impares += 1
        except ValueError:
            print("Erro: entrada inválida. Digite um número inteiro.")

    print("Total de pares:", pares)
    print("Total de ímpares:", impares)

verificar_par_ou_impar()
