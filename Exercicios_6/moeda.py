'''4 - Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
** Instale o modulo requests - pip install requests **
URL da API com base na moeda informada
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"'''

import requests

def consultar_moeda(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    dados = resposta.json()
    chave = f"{moeda}BRL"
    if chave not in dados:
        print("Moeda não encontrada.")
        return
    else:
        cotacao = dados[chave]
        print("Cotação {moeda}/BRL: ")
        print(f"Valor atual: {cotacao["bid"]}")
        print(f"Máximo do dia: {cotacao["high"]}")
        print(f"Mínimo do dia: {cotacao["low"]}")
        print(f"Data/Hora atualização: {cotacao["create_date"]}")
if __name__ == "__main__":
    moeda_usuario = input("Informe o código da moeda desejada (ex: USD, EUR, GBP): ").upper()
    consultar_moeda(moeda_usuario)
