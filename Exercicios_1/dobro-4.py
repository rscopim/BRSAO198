'''4 - Crie uma função em Python que receba um número como parâmetro e retorne o dobro desse número. Depois, chame essa função com um número fornecido pelo usuário.'''

def dobro(numero):
    return numero * 2
valor = int(input("Digite um número: "))
resultado = dobro(valor)
print("O dobro do valor digitado é: ", resultado)