'''2 - Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.
** Instale o modulo requests - pip install requests **
URL da API que retorna um usuário aleatório no formato JSON
    url = "https://randomuser.me/api/"'''

import requests
url = 'https://randomuser.me/api/'
def gerar_usuario():
    resposta = requests.get(url)
    dados = resposta.json()
    usuario = dados["results"][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']
    print("Usuário gerado aleatoriamente")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"País: {pais}")
if __name__ == "__main__":
    gerar_usuario()