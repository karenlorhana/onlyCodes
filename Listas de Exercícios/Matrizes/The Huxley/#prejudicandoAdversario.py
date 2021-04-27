matriz = []
qtd = int(input())

for lin in range(qtd):
    numero = input().split()
    lista = list(map(int,numero))
    matriz.append(lista)

transposta = []
for i in range(qtd):
    linha = []
    for j in range(qtd):
        linha.append(matriz[j][i])
    transposta.append(linha)

for i in range(qtd):
    for j in range(qtd):
        if transposta[i][j]<0:
            transposta[i][j]*=2
 
for i in range(qtd):
    for j in range(qtd):
        if j == qtd-1:
            print(transposta[i][j])
        else:
            print(transposta[i][j], end = ' ')