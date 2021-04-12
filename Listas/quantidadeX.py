'''
    developed by Karen Lorhana
'''
numeros = []
cont = 0

for i in range (10):
    numero = int(input())
    numeros.append(numero)

x = int(input())

for j in range(len(numeros)):
    if numeros[j] == x :
        cont += 1

print(cont)
