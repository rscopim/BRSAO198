'''3 - Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.'''

# Programa: Verificador de senha forte

def senha_forte(senha):
    return len(senha) >= 8 and any(char.isdigit() for char in senha)

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == "sair":
        break
    if senha_forte(senha):
        print("Senha forte! Cadastro concluído.")
        break
    else:
        print("Senha fraca. Deve ter pelo menos 8 caracteres e 1 número.")
