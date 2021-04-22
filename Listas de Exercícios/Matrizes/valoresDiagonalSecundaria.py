''''
    developed by Karen Lorhana
'''
matriz = []

'''
matriz usada como exemplo:
    [1, 11, 111], 
    [2, 22, 222],
    [3, 33, 333]
'''
for lin in range(1, 3+1):
    linha = []
    for col in range(1, 3+1):
        numero = int(input())
        linha.append(numero)
    matriz.append(linha)

#forma 1 de se fazer:


print(matriz[0][2], matriz[1][1], matriz[2][0]) #diagonal secundaria

#forma 2 de se fazer:

for i in range(2,-1,-1): #diagonal secundaria
    matriz.reverse()
    print(matriz[i][i], end=" ")
