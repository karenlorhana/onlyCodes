matrizUm = []
matrizDois = []

qtd = input().split()
qtdLinha = int(qtd[0])
qtdColuna = int(qtd[1])

for i in range(qtdLinha):
    linha = input().split()
    linha = list(map(int,linha))
    matrizUm.append(linha)

for i in range(qtdColuna):
    linha = []
    for j in range(qtdLinha):
        linha.append(matriz[j][i])
    matrizDois.append(linha)

for i in range(qtdColuna):
    for j in range(qtdLinha):
        print(matriz2[i][j], end = ' ')
    print()