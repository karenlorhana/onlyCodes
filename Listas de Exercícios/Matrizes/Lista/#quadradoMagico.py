# -----------------------------
matriz = []

for lin in range(3):
    linha = []
    for col in range(3):
        numeros = int(input())
        linha.append(numeros)
    matriz.append(linha)

#diagonal principal
magico =  0
for i in range(3):
    magico += matriz[i][i]

#diagonal secundaria

j = 3-1
soma =0
for i in range(3):
    soma += matriz[i][j]
    j -= 1
    
if soma != magico:
    print("-- não é mágico --")
    exit()

#linhas
for i in range(3):
    soma = 0
    for j in range(3):
        soma += matriz[i][j]
    if soma != magico:
        print(" ** nao é mágico **")
        exit()

#colunas

for j in range(3):
    soma = 0
    for i in range(3):
        soma += matriz[i][j]
    if soma != magico:
        print(" == nao é mágico ==")
        exit()
print("é mágico!")