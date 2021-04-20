maiorPalavra = ''

while True:
    lista = input()
    if lista == "0":
        break
    else:
        lista = lista.split()
        for i in range(len(lista)):
            if len(lista[i]) >= len(maiorPalavra):
                maiorPalavra = lista[i]
            if i == len(lista)-1:
                print(len(lista[i]))
            else:
                print(len(lista[i]),end = "-")
print("Maior palavra:",maiorPalavra)