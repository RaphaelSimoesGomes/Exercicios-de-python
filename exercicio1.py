import os
def clear():{
    os.system('cls||clear')
}
clear()
nota = float(input("Digite a sua nota (Obs: você deverá inserir um numero entre 0 e 10)\n>>>"))
    
while True:
        if nota>= 7 and nota <=10:
            clear()
            print("Você está aprovado\n")
            break
        if nota <= 6 and nota >=0:
            clear()
            print("Você está de prova final\n")
            break
        else:
            clear()
            print("Perdâo, não consegui entender a sua nota\n")
        nota = float(input("Digite a sua nota (Obs: você deverá inserir um numero entre 0 e 10)\n>>>"))