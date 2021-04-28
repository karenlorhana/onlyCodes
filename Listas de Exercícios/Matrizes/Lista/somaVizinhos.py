# ?????

matriz =    [[ 1, 2, 3],
            [8, 10, 12],
            [21, 24, 27]]
soma = 0

i = int(input())
j = int(input())

if i <=len(matriz) and j <=len(matriz[0]):
    soma += matriz[i][j]
    if j - 1 >= 0:
        soma += matriz[i][j-1]
    if j + 1 < len(matriz[i]):
        soma += matriz[i][j+1]
    if i - 1 >= 0:
        soma += matriz[i-1][j]
    if i + 1 < 0:
        soma += matriz[i+1][j]
    print(soma)
else:
    print("Digite posições válidas")