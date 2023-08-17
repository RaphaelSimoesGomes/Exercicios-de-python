import os
def clear():{
    os.system('cls||clear')
}
clear()
CMA = CMB = CMG = CMM = None
AMA = AMB = PMG = PMM = soma_alturas = soma_pesos = count = 0

while True:
    codigo = int(input("Digite o código do cliente (ou 0 para sair):\n>>> "))
    
    if codigo == 0:
        break
    clear()
    altura = float(input("Digite a altura do cliente em metros:\n>>> "))
    peso = float(input("Digite o peso do cliente:\n>>> "))
    clear()
    
    if CMA is None or altura > AMA:
        CMA, AMA = codigo, altura
    
    if CMB is None or altura < AMB:
        CMB, AMB = codigo, altura
    
    if CMG is None or peso > PMG:
        CMG, PMG = codigo, peso
    
    if CMM is None or peso < PMM:
        CMM, PMM = codigo, peso
    
    soma_alturas += altura
    soma_pesos += peso
    count += 1

media_alturas = soma_alturas / count
media_pesos = soma_pesos / count
clear()
print('================================================================')
print("Cliente mais alto:\n")
print("Código:", CMA)
print("Altura:", AMA)
print('================================================================')
print("Cliente mais baixo:\n")
print("Código:", CMB)
print("Altura:", AMB)
print('================================================================')
print("Cliente mais gordo:\n")
print("Código:", CMG)
print("Peso:", PMG)
print('================================================================')
print("Cliente mais magro:\n")
print("Código:", CMM)
print("Peso:", PMM)
print('================================================================')
print("Média entre todas as pessoas da academia")
print("\nMédia das alturas:", media_alturas)
print("Média dos pesos:", media_pesos,"\n")