'''5 - Crie um programa com uma função que cadastre alunos e suas respectivas notas.
O sistema deve:
Solicitar o nome do aluno.
Solicitar 3 notas válidas (entre 0 e 10).
Armazenar os dados em um dicionário, onde a chave é o nome e o valor é uma lista de notas.
Permitir o cadastro de vários alunos até que o usuário digite "fim".
Exibir ao final:
A lista de alunos e suas médias.
O aluno com a maior média.
Use def para as funcionalidades e try/except para tratar entradas inválidas.'''

def cadastrar_alunos():
    alunos = {}
    while True:
        nome = input("Digite o nome do aluno (ou 'fim' para encerrar): ")
        if nome.lower() == "fim":
            break
        notas = []
        for i in range(3):
            while True:
                try:
                    nota = float(input(f"Digite a {i+1}ª nota: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota inválida, digite entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida, digite um número.")
        alunos[nome] = notas
    return alunos

def mostrar_resultados(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    maior_media = 0
    melhor_aluno = ""
    for nome, notas in alunos.items():
        media = sum(notas) / len(notas)
        print(f"Aluno: {nome} - Média: {media:.2f}")
        if media > maior_media:
            maior_media = media
            melhor_aluno = nome
    print(f"\nAluno com maior média: {melhor_aluno} ({maior_media:.2f})")

alunos = cadastrar_alunos()
mostrar_resultados(alunos)
