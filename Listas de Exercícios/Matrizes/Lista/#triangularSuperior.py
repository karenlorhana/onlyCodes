#-------------
 
matriz = []

for i in range(3):
    linha = input().split()
    linha = [int(x) for x in linha]
    matriz.append(linha)

achou_nao_zero = False

for i in range(1, len(matriz)):
    for j in range(0, i):
        if matriz[i][j] != 0:
            achou_nao_zero = True
            break

    if achou_nao_zero:
        break

if achou_nao_zero:
  print("A matriz não é uma matriz triangular superior.")
else:
  print("A matriz é uma matriz triangular superior.")