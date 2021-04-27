'''
    developed by Karen Lorhana 
'''

matriz = []
qtdLinha = int(input())
qtdColuna = int(input())

for lin in range(qtdLinha):
    linha = []
    for col in range(qtdColuna):
        numeros = int(input())
        linha.append(numeros)
    matriz.append(linha)

if qtdLinha != qtdColuna:
    print("A matriz nao possui traco")
else:
    somaPrincial = 0
    somaSecundaria = 0

    #diagonal principal
    for i in range(qtdLinha):
        somaPrincial += matriz[i][i] 
    #diagonal secundária
    for i in range(qtdLinha):
        somaSecundaria += matriz[i][-1 -i]
    print(somaPrincial)
    print(somaSecundaria)

for x in matriz:
    print(*x)