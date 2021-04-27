'''
    developed by Karen Lorhana
'''

matriz = []
qtd = input().split()
qtdLinha = int(qtd[0])
qtdColuna = int(qtd[1])
menor = 0
maior = 0

for lin in range(qtdLinha):
    linha = []
    for col in range(qtdColuna):
        numeros = int(input("digite os numeros: "))
        linha.append(numeros)
        if numeros < 0:
            menor += 1
        else:
            maior += 1
    matriz.append(linha)


print("Matriz formada:")
for i in range(qtdLinha):
    for j in range(qtdColuna):
        if j == qtdColuna-1:
            print(matriz[i][j])
        else:
            print(matriz[i][j], end = ' ')

if qtdLinha != qtdColuna:
    print("A diagonal principal e secundaria nao pode ser obtida.")
else:
    diagonalPrincipal = 0
    diagonalSecundaria = 0
    for i in range(qtdLinha): #diagonal principal
        diagonalPrincipal += matriz[i][i]
    for i in range(qtdLinha): #diagonal secundaria
        matriz.reverse()
        diagonalSecundaria += matriz[i][i]
    print("A diagonal principal e secundaria tem valor(es) %i e %i respectivamente."%(diagonalPrincipal,diagonalSecundaria))
print("A matriz possui %i numero(s) menor(es) que zero."%menor)
print("A matriz possui %i numero(s) maior(es) que zero."%maior)