'''
    developed by Karen Lorhana
'''

matriz1 = []
matriz2 = []
resultado = []

for i in range(3):
    numeros = input().split()
    numeros = list(map(int, numeros))
    matriz1.append(numeros)

for i in range(3):
    numeros2 = input().split()
    numeros2 = list(map(int, numeros2))
    matriz2.append(numeros2)

for i in range(3):
    aux = []
    for j in range(3):
        if matriz1[i][j] == matriz2[i][j]:
            aux.append(matriz2[i][j])
        else:
            aux.append(0)
    resultado.append(aux)

for lin in range(3):
    for col in range(3):
        print(resultado[lin][col], end=' ')
    print()
