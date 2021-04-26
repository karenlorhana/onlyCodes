# ---------------------

matriz = []
n = int(input())

for i in range(n):
    cont = 1
    linha = []
    for j in range(n):
        linha.append(cont)
        cont += 1
    matriz.append(linha)

cont =-1 
for i in range(n):
    for j in range(n):
        if j == n-1 and j>cont:
            print(matriz[i][j])
        elif j > cont:
            print(matriz[i][j], end=' ')
        else:
            print("  ", end=' ')
    cont +=1