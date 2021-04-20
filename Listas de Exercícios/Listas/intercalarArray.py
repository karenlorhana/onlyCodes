numero= int(input())
lista1 = []
lista2 = []
lista3 = []

for i in range(numero):
    lista1.append(int(input()))

for i  in range(numero):
    lista2.append(int(input()))

for i in range(numero):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

for i in range(len(lista3)):
    print(lista3[i])