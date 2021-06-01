matriz = []
direcao = str(input()).lower() #acima ou abaixo
limiarSoma = int(input())
qtdElementos = int(input())
soma = 0 

for l in range(qtdElementos):
        numeros = input().split()
        lista = list(map(int, numeros))
        matriz.append(lista)

if direcao == "acima":
    for l in range(qtdElementos):
        for c in range(qtdElementos):
            if l+c > l+l:
                soma += matriz[l][c]

if direcao == "abaixo":
    for l in range(qtdElementos):
        for c in range(qtdElementos):
            if l+c < l+l:
                soma += matriz[l][c]

if soma > limiar:
    print(True)
else:
    print(False)


