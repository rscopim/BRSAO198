'''3 - Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
** Instale o modulo requests - pip install requests **
URL da API ViaCEP, passando o CEP informado
    url = f"https://viacep.com.br/ws/{cep}/json/"'''

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    dados = resposta.json()
    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print("CEP encontrado.")
        print(f"Logradouro: {dados["logradouro"]}")
        print(f"Bairro: {dados["bairro"]}")
        print(f"Cidade: {dados["localidade"]}")
        print(f"Estado: {dados["uf"]}")
if __name__ == "__main__":
    cep_usuario = input("Informe o CEP (Apenas números): ")
    consultar_cep(cep_usuario)