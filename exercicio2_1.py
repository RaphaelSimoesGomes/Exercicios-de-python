import re

while True:
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")

    if password == username:
        print("Erro: A senha não pode ser igual ao nome de usuário. Tente novamente.")
    elif len(password) < 8:
        print("Erro: A senha deve ter no mínimo 8 caracteres. Tente novamente.")
    elif not re.search(r"\d", password) or not re.search(r"[A-Za-z]", password) or not any(char in "!@#$%^&*()-=_+[]{}|;:',.<>/?\\" for char in password):
        print("Erro: A senha deve conter pelo menos uma letra, um número e um caractere especial. Tente novamente.")
    else:
        break

print("Nome de usuário:", username)
print("Senha:", password)