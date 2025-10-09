'''4 - Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.'''

# Programa: Registro de notas de uma turma

def registrar_notas():
    notas = []

    while True:
        entrada = input("Digite a nota (0 a 10) ou 'fim' para encerrar: ")

        if entrada.lower() == "fim":
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    if notas:
        media = sum(notas) / len(notas)
        print("Média da turma:", round(media, 2))
    else:
        print("Nenhuma nota válida registrada.")

registrar_notas()
