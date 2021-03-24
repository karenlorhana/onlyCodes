menorNumero = []
qtdArray = int(input())
cont, posicao, x = 0, 0, 0

numero = str(input()).split()
lista = [int (k) for k in numero]
for i in range(qtdArray):
    cont += 1
    if x == 0:
        menorNumero = lista[0]
        x += 1
    elif menorNumero > lista[i]:
        menorNumero = lista[i]
        posicao = cont

print("Menor valor:", menorNumero)
if posicao != 0:
    print("Posicao:", posicao-1)
else:
    print("Posicao:", posicao)