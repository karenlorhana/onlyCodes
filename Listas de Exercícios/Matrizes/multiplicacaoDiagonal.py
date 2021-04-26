# -----------------

n = int(input())
while n!= 0:
    matriz = [[],[],[],[]]
    for j in range(4):
        for i in range(4):
            if j == i:
                matriz[i].append(int(input())*n)
            else:
                matriz[i].append(int(input()))
    for i in range(4):
        for j in range(4):
            print(matriz[i][j], end=' ')
        print()
    n = int(input())