lista = []

for i in range(3):
    numero = int(input("valor: "))
    lista.append(numero)

if lista[0] > lista[1] and lista[0] > lista[2]:
    if lista[1] > lista[2]:
        print(lista[1])
    else:
        print(lista[2])

elif lista[1] > lista[0] and lista[1] > lista[2]:
    if lista[0] > lista[2]:
        print(lista[0])
    else:
        print(lista[2])
    
else:
    if lista[0] > lista[1]:
        print(lista[0])
    else:
        print(lista[1])