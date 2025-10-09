'''2 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
A função deve receber dois parâmetros:
valor_conta (float): O valor total da conta
porcentagem_gorjeta (float): A porcentagem da gorjeta (por exemplo, 10 para 10%)'''

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

valor = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta (%): "))
gorjeta = calcular_gorjeta(valor, porcentagem)

print(f"Gorjeta: R$ {gorjeta:.2f}")
print(f"Total a pagar: R$ {valor + gorjeta:.2f}")
