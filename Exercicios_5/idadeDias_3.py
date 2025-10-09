'''3 - Crie uma função que calcule a idade de uma pessoa em dias, com base no ano de nascimento informado pelo usuário.
O programa deve considerar o ano atual como base para o cálculo.
Use try/except para tratar erros de entrada e valide que o ano não pode ser maior que o ano atual.'''

from datetime import datetime

def idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    if ano_nascimento > ano_atual:
        raise ValueError("Ano de nascimento não pode ser maior que o ano atual.")
    idade = ano_atual - ano_nascimento
    return idade * 365

try:
    ano = int(input("Digite seu ano de nascimento: "))
    dias = idade_em_dias(ano)
    print(f"Você já viveu aproximadamente {dias} dias.")
except ValueError as e:
    print("Erro:", e)
