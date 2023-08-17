import os
def clear():{
    os.system('cls||clear')
}
clear()
while True:
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    if password == username:
        clear()
        print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.\n")
    else:
        break
clear()
print("Nome de usuário:", username)
print("Senha:", password)