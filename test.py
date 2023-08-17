CMA = CMB = CMG = CMM = None
AMA = AMB = PMG = PMM = soma_alturas = soma_pesos = count = 0

while True:
    codigo = int(input("Digite o código do cliente (ou 0 para sair): "))
    
    if codigo == 0:
        break
    
    altura = float(input("Digite a altura do cliente em metros: "))
    peso = float(input("Digite o peso do cliente em quilogramas: "))
    
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

print("\nCliente mais alto:")
print("Código:", CMA)
print("Altura:", AMA)

print("\nCliente mais baixo:")
print("Código:", CMB)
print("Altura:", AMB)

print("\nCliente mais gordo:")
print("Código:", CMG)
print("Peso:", PMG)

print("\nCliente mais magro:")
print("Código:", CMM)
print("Peso:", PMM)

print("\nMédia das alturas:", media_alturas)
print("Média dos pesos:", media_pesos)