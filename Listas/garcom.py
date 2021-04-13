lista = []
qtdQuebrados = 0
bandeijas = oint(input())

for i in range(bandeijas):
    lista = input().split(" ")
    
    if(int(lista[0]) > int(lista[1])):
        qtdQuebrados += int(lista[1])

print(qtdQuebrados)