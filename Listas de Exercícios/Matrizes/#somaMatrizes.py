'''
    developed by Karen Lorhana
'''
# -------------

matrizUm = []
matrizDois = []

for qtdLinha in range(1, 2+1):
    linha = []
    for qtdCol in range(1, 3+1):
        print("Digite o número", qtdCol, " da linha", qtdLinha)
        numero = int(input())
        linha.append(numero)
    matrizUm.append(linha)

for qtdLinha in range(1, 2+1):
    linha = []
    for qtdCol in range(1, 3+1):
        print("Digite o número", qtdCol, " da linha", qtdLinha)
        numero = int(input())
        linha.append(numero)
    matrizDois.append(linha)

for i in range(len(matrizUm)):
    linha = []
    for x in range(len(matrizUm[0])):
        linha.append(matrizUm[i][x] + matrizDois[i][x])
    print(linha)
