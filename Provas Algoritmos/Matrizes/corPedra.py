matriz = []
qtd = int(input())
aux = 0
for l in range(qtd):
        numeros = input().split()
        lista = list(map(int, numeros))
        matriz.append(lista)

for i in range(1,qtd):
    for c in range(1,qtd):
        aux = int(matriz[i][j-1]) + int(matriz[i - 1][ j - 1]) + int(matriz[i - 1][j]) 
        if (aux == 0 or aux == 1):
            matriz[i][j] = 1
        elif (aux == 2 or aux == 3):
            matriz[i][j] == 0

print(matriz[n][n])